import os
import importlib
import time
import sys
from io import StringIO
from typing import Dict, Any, List
import pandas as pd
import json
from datetime import datetime

def discover_api_files(api_dir: str = None) -> list:
    """发现所有API脚本文件"""
    if api_dir is None:
        # 获取当前文件所在目录的父目录中的apis目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        api_dir = os.path.join(os.path.dirname(current_dir), "apis")
    
    api_files = []
    for root, _, files in os.walk(api_dir):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                api_files.append(os.path.join(root, file))
    return api_files

class APITestResult:
    """API测试结果类"""
    def __init__(self, module_name: str):
        self.module_name = module_name
        self.passed = False
        self.output = ""
        self.error = None
        self.execution_time = 0.0
        self.data_validation = {}
        
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典格式"""
        return {
            "module": self.module_name,
            "passed": self.passed,
            "output": self.output,
            "error": self.error,
            "execution_time": self.execution_time,
            "data_validation": self.data_validation,
            "timestamp": datetime.now().isoformat()
        }

def test_api_module(module_path: str) -> APITestResult:
    """测试单个API模块"""
    # 初始化测试结果
    module_name = os.path.splitext(os.path.basename(module_path))[0]
    result = APITestResult(module_name)
    
    # 动态导入模块
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    
    # 捕获输出
    output = StringIO()
    sys.stdout = output
    
    try:
        start_time = time.time()
        
        # 执行测试
        if hasattr(module, "test"):
            try:
                result_data = module.test()
                
                # 数据验证
                if isinstance(result_data, list):
                    result.data_validation = {
                        "is_list": True,
                        "not_empty": len(result_data) > 0,
                        "is_dict_items": all(isinstance(item, dict) for item in result_data) if result_data else False,
                        "failure_reason": None if (len(result_data) > 0 and all(isinstance(item, dict) for item in result_data)) 
                                          else "返回空列表" if len(result_data) == 0 
                                          else "列表元素不是字典格式"
                    }
                    result.passed = result.data_validation["is_list"] and result.data_validation["not_empty"] and result.data_validation["is_dict_items"]
                elif isinstance(result_data, pd.DataFrame):
                    result.data_validation = {
                        "is_dataframe": True,
                        "not_empty": not result_data.empty,
                        "columns": list(result_data.columns),
                        "failure_reason": None if not result_data.empty else "返回空DataFrame"
                    }
                    result.passed = result.data_validation["is_dataframe"] and result.data_validation["not_empty"]
                else:
                    result.data_validation = {
                        "valid_type": False,
                        "failure_reason": f"无效返回类型: {type(result_data)}"
                    }
                    result.passed = False
                    
            except Exception as e:
                result.passed = False
                result.error = str(e)
                result.data_validation = {
                    "failure_reason": f"测试执行异常: {str(e)}"
                }
                
        result.execution_time = time.time() - start_time
    except Exception as e:
        result.passed = False
        result.error = str(e)
        result.data_validation = {
            "failure_reason": f"测试框架异常: {str(e)}"
        }
    finally:
        result.output = output.getvalue()
        sys.stdout = sys.__stdout__
    
    return result

def run_all_tests() -> List[Dict[str, Any]]:
    """运行所有测试并生成报告"""
    api_files = discover_api_files()
    results = []
    
    for api_file in api_files:
        result = test_api_module(api_file)
        results.append(result.to_dict())
        
        status = "✓" if result.passed else "✗"
        print(f"{status} {result.module_name} ({result.execution_time:.2f}s)")
        if result.error:
            print(f"    Error: {result.error}")
    
    # 生成测试报告
    generate_test_report(results)
    return results

def generate_test_report(results: List[Dict[str, Any]]):
    """生成测试报告文件"""
    # 将失败用例前置
    sorted_results = sorted(results, key=lambda x: x["passed"])
    
    report = {
        "summary": {
            "total": len(sorted_results),
            "passed": sum(1 for r in sorted_results if r["passed"]),
            "failed": sum(1 for r in sorted_results if not r["passed"]),
            "success_rate": sum(1 for r in sorted_results if r["passed"]) / len(sorted_results) * 100 if len(sorted_results) > 0 else 0
        },
        "details": sorted_results
    }
    
    # 修改报告目录为test/reports
    reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    
    # 生成新报告
    report_path = os.path.join(reports_dir, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    
    # 保留最近5个报告
    report_files = sorted(
        [f for f in os.listdir(reports_dir) if f.startswith("api_test_report_") and f.endswith(".json")],
        key=lambda x: os.path.getmtime(os.path.join(reports_dir, x)),
        reverse=True
    )
    for old_report in report_files[5:]:
        os.remove(os.path.join(reports_dir, old_report))
    
    print(f"\n测试报告已生成: {report_path}")

if __name__ == "__main__":
    # 修复事件循环嵌套问题
    run_all_tests()