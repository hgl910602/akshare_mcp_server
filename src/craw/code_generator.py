import requests
import configparser
import os
from typing import Dict
from openai import OpenAI
from pathlib import Path

# 全局OpenAI客户端
DEEPSEEK_CLIENT = None

class CodeGenerator:
    """代码生成器，用于调用大模型生成接口实现代码"""
    
    def __init__(self):
        """
        初始化代码生成器
        """
        global DEEPSEEK_CLIENT
        if DEEPSEEK_CLIENT is None:
            # 读取配置文件
            config = configparser.ConfigParser()
            config_path = os.path.join(Path(__file__).parent.parent.parent, 'config.ini')
            config.read(config_path)
            api_key = config.get('deepseek', 'api_key', fallback=os.getenv("DEEPSEEK_API_KEY"))
            DEEPSEEK_CLIENT = OpenAI(
                api_key=api_key,
                base_url="https://api.deepseek.com/v1"
            )

    def generate_implementation(self, data_dict: Dict) -> str:
        """
        根据接口数据生成实现代码
        
        Args:
            data_dict: 包含接口信息的字典，包含以下字段:
                - interface_name: 接口名称
                - category: 分类
                - sub_category: 子分类
                - description: 描述
                - limit_info: 使用限制
                - input_params: 输入参数
                - output_params: 输出参数
                - example: 示例调用
                
        Returns:
            str: 生成的Python代码字符串
        """
        # 构造提示词
        prompt = self._build_prompt(data_dict)
        
        try:
            generated_code = self._call_deepseek_api(prompt)
            return generated_code
        except Exception as e:
            print(f"调用DeepSeek API失败: {str(e)}")
            return self._mock_generate_code(data_dict)

    def _call_deepseek_api(self, prompt: str) -> str:
        """调用DeepSeek API获取生成的代码"""
        try:
            completion = DEEPSEEK_CLIENT.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            return completion.choices[0].message.content.replace("```python", "").replace("```", "").strip()
        except Exception as e:
            print(f"OpenAI兼容调用失败: {str(e)}")
            raise

    def _build_prompt(self, data_dict: Dict) -> str:
        """构造调用大模型的提示词"""
        return f"""
请根据以下接口信息生成基于akshare的Python异步函数实现:

接口名称: {data_dict.get('interface_name', '')}
分类: {data_dict.get('category', '')}-{data_dict.get('sub_category', '')}
描述: {data_dict.get('description', '')}
使用限制: {data_dict.get('limit_info', '无')}
输入参数: {data_dict.get('input_params', '无')}
输出参数: {data_dict.get('output_params', '无')}
示例调用: {data_dict.get('example', '无')}

要求:
* 使用async/await语法
* 请注意不需要自己爬代码，而是使用示例的代码生成可用代码即可
* 包含完整的类型提示
* 添加错误处理
* 返回类型为List[Dict[str, Any]]
* 在文件中加入一个同步的调用方法，起名为test()，这个方法与__main__类似的调用了execute方法，主要是方便其他批量工具自动化测试
* 请注意test方法调用的是你生成的execute方法，而不是akshare的原始方法
* test方法调用execute时，如果出现了异常请异常上抛，不要擅自捕获返回空列表
* 如果execute方法本身带参数，也请在test方法中依据调用示例模拟出参数带上，确保能够真正验证到这个方法
* 如果execute方法是异步的，test方法中请使用asyncio.run，而不是asyncio.get_event_loop()
* 为每个方法添加一个__main__测试块，包含调用示例，__main__中应演示如何调用该函数并打印结果
* 请注意__main__中请不要调用test()方法
* 只返回具体的python代码即可，代码带注释，但不需要额外的文字解释
* 如果原函数本身带参数，也请带在生成方法的接口上带对应的参数
* 内部生成的主方法，请命名为execute，这样方便后续的泛化调用
* 请确保生成的代码是可用的，并且可以直接运行
"""
