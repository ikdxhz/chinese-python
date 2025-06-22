#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os#文件操作
import sys#系统操作
import importlib.util#导入模块
import code#代码执行
from mapping import translate_to_python, translate_from_python#翻译
#读取并执行.cnpy文件
def run_cnpy_file(file_path):# 读取并执行.cnpy文件
    """#读取并执行.cnpy文件
    """ #读取并执行.cnpy文件
    if not os.path.exists(file_path):#如果文件不存在
        print(f"错误：文件 {file_path} 不存在".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))#打印错误信息
        return#返回
    
    if not file_path.endswith('.cnpy'):#如果文件不是.cnpy文件
        print(f"警告：文件 {file_path} 不是.cnpy文件".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            chinese_code = f.read()#读取文件内容
        
        # 转换中文代码到Python代码
        python_code = translate_to_python(chinese_code)#转换中文代码到Python代码
        
        # 输出转换后的代码（调试用）
        print("\n== 转换后的Python代码 ==".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))#打印转换后的Python代码
        print(python_code)
        
        # 创建一个临时模块名
        module_name = os.path.basename(file_path).replace('.cnpy', '')#创建一个临时模块名
        
        # 创建执行环境，包含所有内置函数和常用模块
        exec_globals = {
            # 提供对内置函数的访问
            'type': type,#类型
            'print': print,#打印
            'len': len,#长度
            'range': range,#范围
            'list': list,#列表
            'dict': dict,#字典
            'set': set,#集合
            'tuple': tuple,#元组
            'int': int,#整数
            'float': float,#浮点数
            'str': str,#字符串
            'bool': bool,#布尔值
            'True': True, #真
            'False': False, #假
            'None': None, #空
            'map': map, #映射
            'filter': filter, #过滤
            'enumerate': enumerate, #枚举
            'zip': zip, #压缩
            'sum': sum, #求和
            'min': min, #最小值
            'max': max, #最大值
            'abs': abs, #绝对值
            'round': round, #四舍五入
            'sorted': sorted, #排序
            'reversed': reversed, #反转
            
            # 提供模块访问
            'os': os, #操作系统
            'sys': sys, #系统
            '__builtins__': __builtins__, #内置函数
            
            # 确保关键词映射也可用
            '类型': type,#类型
        }
        
        # 在内存中执行Python代码
        print("== 代码执行结果 ==".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))#打印代码执行结果
        exec(python_code, exec_globals)
        
    except Exception as e:
        print(f"执行错误：{e}".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
        import traceback
        print(traceback.format_exc().encode('utf-8').decode(sys.stdout.encoding, 'ignore'))

def run_interactive_shell():#运行交互式中文Python解释器
    """
    运行交互式中文Python解释器，支持多行代码输入
    输入"执行()"命令时才执行代码块
    """
    banner = """
    中文Python解释器 v0.1
    输入中文Python代码，可多行输入
    输入"执行()"单独一行执行代码块
    输入"清空()"单独一行清空当前代码块
    输入'退出()' 或 'exit()' 退出解释器
    
    支持多种中文表达方式，如:
    - 如果/若/若是/假如（对应if）
    - 且/并且/同时/与（对应and）
    - 打印/输出/显示（对应print）
    """.encode('utf-8').decode(sys.stdout.encoding, 'ignore')#打印帮助信息
    
    print(banner)#打印帮助信息
    
    # 使用单一全局命名空间，确保函数定义和变量在会话期间保持可用
    namespace = {
        # 提供对内置函数的访问
        'type': type,#类型
        'print': print,#打印
        'len': len,#长度
        'range': range,#范围
        'list': list,#列表
        'dict': dict,#字典
        'set': set,#集合
        'tuple': tuple,#元组
        'int': int,#整数
        'float': float,#浮点数
        'str': str,#字符串
        'bool': bool,#布尔值
        'True': True, #真
        'False': False, #假
        'None': None, #空
        'map': map, #映射
        'filter': filter,#过滤
        'enumerate': enumerate,#枚举
        'zip': zip,#压缩
        'sum': sum,#求和
        'min': min,#最小值
        'max': max,#最大值
        'abs': abs,#绝对值
        'round': round,#四舍五入
        'sorted': sorted,#排序
        'reversed': reversed,#反转
        
        # 提供模块访问
        'os': os, #操作系统
        'sys': sys, #系统
        '__builtins__': __builtins__, #内置函数
        
        # 确保关键词映射也可用
        '类型': type,#类型
    }
    
    # 代码缓冲区
    code_buffer = []#代码缓冲区
    
    while True:#循环
        try:#尝试
            # 显示提示符
            if not code_buffer:#如果代码缓冲区为空
                prompt = ">>> " #提示符
            else:
                prompt = "... " #提示符
            
            # 获取用户输入
            line = input(prompt)#获取用户输入
            command = line.strip()#去除空格
            
            # 处理特殊命令
            if not code_buffer and command in ["退出()", "exit()"]:#如果代码缓冲区为空且命令为退出
                print("再见！".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))#打印再见
                break#退出
            elif command == "执行()":#如果命令为执行
                # 执行代码块
                if not code_buffer:
                    print("没有代码可执行".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))#打印没有代码可执行
                    continue#继续
                
                chinese_code = '\n'.join(code_buffer)#将代码缓冲区中的代码连接成一个字符串
                try:
                    # 输出要执行的代码（调试用）
                    print("\n== 要执行的代码 ==".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
                    print(chinese_code)#打印要执行的代码
                    
                    # 将中文代码转换为Python代码
                    python_code = translate_to_python(chinese_code)#将中文代码转换为Python代码
                    print("== 转换后的Python代码 ==".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
                    print(python_code)#打印转换后的Python代码
                    print("== 执行结果 ==".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))#打印执行结果
                    
                    # 直接使用exec执行所有代码
                    # 这样可以确保函数定义等语句能正确执行
                    exec(python_code, namespace)#执行Python代码
                    
                    # 如果代码只是一个表达式，尝试获取其值并打印
                    stripped_code = chinese_code.strip()#去除空格
                    if (not stripped_code.startswith("#") and 
                        "=" not in stripped_code and 
                        "打印" not in stripped_code and
                        "定义" not in stripped_code and
                        "类" not in stripped_code and
                        "如果" not in stripped_code and
                        "对于" not in stripped_code and
                        "当" not in stripped_code):
                        try:
                          result = eval(python_code, namespace)#执行
                        except:
                            pass
                except Exception as e:
                    print(f"执行错误: {e}".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
                    import traceback
                    print(traceback.format_exc().encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
                finally:
                    # 清空代码缓冲区
                    code_buffer = []
                    print() # 额外的换行，美观
            elif command == "清空()":
                # 清空代码缓冲区
                code_buffer = []
                print("代码缓冲区已清空".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
            else:
                # 将行添加到代码缓冲区
                code_buffer.append(line)
                
        except (KeyboardInterrupt, EOFError):
            print("\n再见！".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
            break

def print_help():
    """
    打印帮助信息
    """
    print("中文Python解释器 v0.1".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
    print("用法：".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
    print("  python chinese_python.py              - 启动交互式中文Python解释器".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
    print("  python chinese_python.py <文件名.cnpy> - 执行中文Python文件".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
    print("  python chinese_python.py --help       - 显示此帮助信息".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))

def main():
    """
    主函数
    """
    if len(sys.argv) < 2:
        # 无参数时启动交互模式
        run_interactive_shell()
        return
    
    arg = sys.argv[1]
    
    if arg == '--help':
        print_help()
    elif os.path.exists(arg):
        run_cnpy_file(arg)
    else:
        print(f"错误：无法找到文件 {arg}".encode('utf-8').decode(sys.stdout.encoding, 'ignore'))
        print_help()

if __name__ == "__main__":
    main() 