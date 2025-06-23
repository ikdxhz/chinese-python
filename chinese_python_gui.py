#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 更新日志
"""
更新日志:
2023-09-09: 初始版本发布
2024-05-18: 
- 修复正则表达式转义序列错误
- 移除30秒执行时间限制
- 增加实时输出功能
- 增加停止执行功能
- 改进UI交互体验
"""

import os
import sys
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import subprocess
from pathlib import Path
import re
import threading
import time

# 导入中文Python解释器模块
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import chinese_python
# 从mapping模块导入翻译函数
import mapping

class PythonHighlighter:
    """Python代码语法高亮器"""
    
    def __init__(self, text_widget):
        self.text_widget = text_widget
        
        # 配置标签
        self.text_widget.tag_configure("keyword", foreground="#0000FF")  # 关键字：蓝色
        self.text_widget.tag_configure("string", foreground="#008000")   # 字符串：绿色
        self.text_widget.tag_configure("comment", foreground="#808080")  # 注释：灰色
        self.text_widget.tag_configure("function", foreground="#800080") # 函数：紫色
        self.text_widget.tag_configure("number", foreground="#FF8000")   # 数字：橙色
        self.text_widget.tag_configure("decorator", foreground="#CC0000")# 装饰器：红色
        
        # Python关键字列表
        self.keywords = [
            "False", "None", "True", "and", "as", "assert", "async", "await", "break", 
            "class", "continue", "def", "del", "elif", "else", "except", "finally", 
            "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", 
            "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"
        ]
        
        # 内置函数列表
        self.builtins = [
            "abs", "all", "any", "bin", "bool", "bytearray", "bytes", "callable", "chr", 
            "classmethod", "compile", "complex", "delattr", "dict", "dir", "divmod", "enumerate", 
            "eval", "exec", "filter", "float", "format", "frozenset", "getattr", "globals", 
            "hasattr", "hash", "help", "hex", "id", "input", "int", "isinstance", "issubclass", 
            "iter", "len", "list", "locals", "map", "max", "memoryview", "min", "next", "object", 
            "oct", "open", "ord", "pow", "print", "property", "range", "repr", "reversed", "round", 
            "set", "setattr", "slice", "sorted", "staticmethod", "str", "sum", "super", "tuple", 
            "type", "vars", "zip", "__import__"
        ]
    
    def highlight_code(self, code):
        """对代码进行语法高亮"""
        # 清除所有现有标签
        for tag in ["keyword", "string", "comment", "function", "number", "decorator"]:
            self.text_widget.tag_remove(tag, "1.0", tk.END)
        
        # 获取文本内容
        content = self.text_widget.get("1.0", tk.END)
        
        # 简单的行处理方式
        lines = content.split('\n')
        for i, line in enumerate(lines):
            line_num = i + 1
            
            # 高亮注释
            if '#' in line:
                comment_start = line.find('#')
                self.text_widget.tag_add("comment", f"{line_num}.{comment_start}", f"{line_num}.end")
            
            # 高亮关键字
            for keyword in self.keywords:
                start = 0
                while True:
                    start = line.find(keyword, start)
                    if start == -1:
                        break
                    
                    # 确保是独立的单词
                    end = start + len(keyword)
                    if (start == 0 or not line[start-1].isalnum()) and (end >= len(line) or not line[end].isalnum()):
                        self.text_widget.tag_add("keyword", f"{line_num}.{start}", f"{line_num}.{end}")
                    
                    start = end
            
            # 高亮内置函数
            for func in self.builtins:
                start = 0
                while True:
                    start = line.find(func, start)
                    if start == -1:
                        break
                    
                    # 确保是独立的单词
                    end = start + len(func)
                    if (start == 0 or not line[start-1].isalnum()) and (end >= len(line) or not line[end].isalnum()):
                        self.text_widget.tag_add("function", f"{line_num}.{start}", f"{line_num}.{end}")
                    
                    start = end
            
            # 高亮字符串
            self._highlight_strings_in_line(line, line_num)
    
    def _highlight_pattern(self, pattern, tag):
        """使用正则表达式查找并应用标签"""
        # 设置文本小部件为正常状态以进行编辑
        current_state = self.text_widget.cget("state")
        self.text_widget.config(state="normal")
        
        try:
            start = "1.0"
            while True:
                try:
                    # 查找模式
                    pos = self.text_widget.search(pattern, start, tk.END, regexp=True)
                    if not pos:
                        break
                    
                    # 计算匹配的结束位置
                    line, col = pos.split('.')
                    line, col = int(line), int(col)
                    
                    # 获取匹配的文本
                    line_text = self.text_widget.get(f"{line}.0", f"{line}.end")
                    
                    try:
                        match = re.search(pattern, line_text[col:])
                        if not match:
                            start = f"{line+1}.0"
                            continue
                            
                        match_length = len(match.group(0))
                        end = f"{line}.{col + match_length}"
                        
                        # 应用标签
                        self.text_widget.tag_add(tag, pos, end)
                        
                        # 移动到下一个位置
                        start = end
                    except re.error:
                        # 如果正则表达式搜索出错，跳过当前行
                        start = f"{line+1}.0"
                        
                except Exception as e:
                    # 如果处理某一匹配项出错，继续处理下一个
                    print(f"高亮错误: {e}")
                    break
        except Exception as e:
            # 如果整个高亮过程出错，打印错误但不中断程序
            print(f"语法高亮错误: {e}")
        
        # 恢复文本小部件的原始状态
        self.text_widget.config(state=current_state)

    def _highlight_strings_in_line(self, line, line_num):
        """在单行中高亮字符串"""
        # 高亮双引号字符串
        in_string = False
        start_pos = -1
        i = 0
        
        while i < len(line):
            if line[i] == '"' and (i == 0 or line[i-1] != '\\'):
                if not in_string:  # 字符串开始
                    in_string = True
                    start_pos = i
                else:  # 字符串结束
                    in_string = False
                    self.text_widget.tag_add("string", f"{line_num}.{start_pos}", f"{line_num}.{i+1}")
            i += 1
            
        # 高亮单引号字符串
        in_string = False
        start_pos = -1
        i = 0
        
        while i < len(line):
            if line[i] == "'" and (i == 0 or line[i-1] != '\\'):
                if not in_string:  # 字符串开始
                    in_string = True
                    start_pos = i
                else:  # 字符串结束
                    in_string = False
                    self.text_widget.tag_add("string", f"{line_num}.{start_pos}", f"{line_num}.{i+1}")
            i += 1

class ChinesePythonGUI:
    """
    中文Python解释器的图形用户界面
    """
    def __init__(self, root):
        self.root = root
        self.root.title("中文Python编辑器")
        self.root.geometry("1000x700")
        
        # 设置图标和主题
        self.setup_appearance()
        
        # 当前打开的文件路径
        self.current_file = None
        
        # 创建线程控制变量
        self.stop_execution = threading.Event()
        self.execution_thread = None
        
        # 创建界面组件
        self.create_widgets()
        
        # 绑定快捷键
        self.bind_shortcuts()
        
    def setup_appearance(self):
        """设置界面外观"""
        # 尝试设置一个更好看的主题
        try:
            self.root.tk.call("source", "azure.tcl")
            self.root.tk.call("set_theme", "light")
        except tk.TclError:
            # 如果没有azure主题，使用默认主题
            pass
            
        # 设置窗口图标
        try:
            self.root.iconbitmap("python_icon.ico")
        except tk.TclError:
            # 如果没有图标文件，忽略
            pass
    
    def create_widgets(self):
        """创建界面组件"""
        # 创建主框架
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 创建菜单栏
        self.create_menu()
        
        # 创建工具栏
        self.create_toolbar()
        
        # 创建编辑器区域
        self.create_editor_area()
        
        # 创建输出区域
        self.create_output_area()
        
        # 创建状态栏
        self.create_status_bar()
        
    def create_menu(self):
        """创建菜单栏"""
        self.menu_bar = tk.Menu(self.root)
        
        # 文件菜单
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="新建", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="打开", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="保存", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_command(label="另存为", command=self.save_file_as, accelerator="Ctrl+Shift+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="退出", command=self.exit_app, accelerator="Alt+F4")
        self.menu_bar.add_cascade(label="文件", menu=self.file_menu)
        
        # 编辑菜单
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="撤销", command=lambda: self.editor.event_generate("<<Undo>>"), accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="重做", command=lambda: self.editor.event_generate("<<Redo>>"), accelerator="Ctrl+Y")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="剪切", command=lambda: self.editor.event_generate("<<Cut>>"), accelerator="Ctrl+X")
        self.edit_menu.add_command(label="复制", command=lambda: self.editor.event_generate("<<Copy>>"), accelerator="Ctrl+C")
        self.edit_menu.add_command(label="粘贴", command=lambda: self.editor.event_generate("<<Paste>>"), accelerator="Ctrl+V")
        self.menu_bar.add_cascade(label="编辑", menu=self.edit_menu)
        
        # 运行菜单
        self.run_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.run_menu.add_command(label="运行", command=self.run_code, accelerator="F5")
        self.run_menu.add_command(label="停止", command=self.stop_code, accelerator="F12")
        self.run_menu.add_command(label="清空输出", command=self.clear_output, accelerator="F6")
        self.menu_bar.add_cascade(label="运行", menu=self.run_menu)
        
        # 帮助菜单
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="关于", command=self.show_about)
        self.help_menu.add_command(label="帮助", command=self.show_help)
        self.menu_bar.add_cascade(label="帮助", menu=self.help_menu)
        
        # 设置菜单栏
        self.root.config(menu=self.menu_bar)
        
    def create_toolbar(self):
        """创建工具栏"""
        self.toolbar = ttk.Frame(self.main_frame)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # 新建按钮
        self.new_button = ttk.Button(self.toolbar, text="新建", command=self.new_file)
        self.new_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        # 打开按钮
        self.open_button = ttk.Button(self.toolbar, text="打开", command=self.open_file)
        self.open_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        # 保存按钮
        self.save_button = ttk.Button(self.toolbar, text="保存", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        # 运行按钮
        self.run_button = ttk.Button(self.toolbar, text="运行", command=self.run_code)
        self.run_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        # 停止按钮
        self.stop_button = ttk.Button(self.toolbar, text="停止", command=self.stop_code, state="disabled")
        self.stop_button.pack(side=tk.LEFT, padx=2, pady=2)
        
        # 清空输出按钮
        self.clear_button = ttk.Button(self.toolbar, text="清空输出", command=self.clear_output)
        self.clear_button.pack(side=tk.LEFT, padx=2, pady=2)
        
    def create_editor_area(self):
        """创建编辑器区域"""
        # 创建编辑器框架
        self.editor_frame = ttk.LabelFrame(self.main_frame, text="代码编辑器")
        self.editor_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 创建编辑器
        self.editor = scrolledtext.ScrolledText(
            self.editor_frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=("Consolas", 12)
        )
        self.editor.pack(fill=tk.BOTH, expand=True)
        
        # 设置编辑器的Tab行为
        self.editor.bind("<Tab>", self.handle_tab)
        
        # 设置语法高亮（简单实现）
        self.setup_syntax_highlighting()
        
    def create_output_area(self):
        """创建输出区域"""
        # 创建输出框架
        self.output_container = ttk.Frame(self.main_frame)
        self.output_container.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 创建转换后代码框架
        self.converted_frame = ttk.LabelFrame(self.output_container, text="转换后的Python代码")
        self.converted_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=5)
        
        # 创建转换后代码文本框
        self.converted_code = scrolledtext.ScrolledText(
            self.converted_frame,
            wrap=tk.WORD,
            width=40,
            height=10,
            font=("Consolas", 10),
            bg="#f8f8f8",
            state="disabled"  # 初始状态为禁用，防止用户编辑
        )
        self.converted_code.pack(fill=tk.BOTH, expand=True)
        
        # 为转换后的Python代码添加语法高亮
        self.python_highlighter = PythonHighlighter(self.converted_code)
        
        # 创建执行结果框架
        self.output_frame = ttk.LabelFrame(self.output_container, text="执行结果")
        self.output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=2, pady=5)
        
        # 创建执行结果文本框
        self.output = scrolledtext.ScrolledText(
            self.output_frame,
            wrap=tk.WORD,
            width=40,
            height=10,
            font=("Consolas", 10),
            bg="#f0f0f0",
            state="disabled"  # 初始状态为禁用，防止用户编辑
        )
        self.output.pack(fill=tk.BOTH, expand=True)
        
        # 配置输出区域的文本标签
        self.output.tag_configure("normal", foreground="#000000")  # 普通输出：黑色
        self.output.tag_configure("error", foreground="#FF0000")   # 错误输出：红色
        self.output.tag_configure("warning", foreground="#FFA500") # 警告输出：橙色
        self.output.tag_configure("success", foreground="#008000") # 成功输出：绿色
        self.output.tag_configure("info", foreground="#0000FF")    # 信息输出：蓝色
        
    def create_status_bar(self):
        """创建状态栏"""
        self.status_bar = ttk.Label(self.root, text="就绪", anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def setup_syntax_highlighting(self):
        """设置简单的语法高亮"""
        # 这里只是一个简单的实现，实际上需要更复杂的逻辑
        # 可以考虑使用第三方库如pygments来实现完整的语法高亮
        self.editor.tag_configure("keyword", foreground="blue")
        self.editor.tag_configure("string", foreground="green")
        self.editor.tag_configure("comment", foreground="gray")
        
        # 绑定按键事件以触发语法高亮
        self.editor.bind("<KeyRelease>", self.highlight_syntax)
        
    def bind_shortcuts(self):
        """绑定快捷键"""
        # 文件操作快捷键
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda e: self.save_file_as())
        
        # 运行快捷键
        self.root.bind("<F5>", lambda e: self.run_code())
        self.root.bind("<F6>", lambda e: self.clear_output())
        self.root.bind("<F12>", lambda e: self.stop_code())
        
        # Tab键处理
        self.editor.bind("<Tab>", self.handle_tab)
        
    def handle_tab(self, event):
        """处理Tab键，插入4个空格而不是制表符"""
        # 插入4个空格
        self.editor.insert(tk.INSERT, "    ")
        # 阻止默认的Tab行为
        return "break"
        
    def new_file(self):
        """创建新文件"""
        # 如果当前文件已修改，提示保存
        if self.is_modified():
            if not self.confirm_save():
                return  # 用户取消了操作
                
        # 清空编辑器
        self.editor.delete(1.0, tk.END)
        # 重置当前文件路径
        self.current_file = None
        # 更新状态栏
        self.update_status("新建文件")
        
    def open_file(self):
        """打开文件"""
        # 如果当前文件已修改，提示保存
        if self.is_modified():
            if not self.confirm_save():
                return  # 用户取消了操作
                
        # 打开文件对话框
        file_path = filedialog.askopenfilename(
            defaultextension=".cnpy",
            filetypes=[("中文Python文件", "*.cnpy"), ("所有文件", "*.*")]
        )
        
        if file_path:
            try:
                # 读取文件内容
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    
                # 清空编辑器并插入文件内容
                self.editor.delete(1.0, tk.END)
                self.editor.insert(tk.END, content)
                
                # 更新当前文件路径
                self.current_file = file_path
                
                # 更新状态栏
                self.update_status(f"已打开: {file_path}")
                
                # 触发语法高亮
                self.highlight_syntax(None)
                
            except Exception as e:
                messagebox.showerror("错误", f"无法打开文件: {e}")
                
    def save_file(self):
        """保存文件"""
        if self.current_file:
            try:
                # 获取编辑器内容
                content = self.editor.get(1.0, tk.END)
                
                # 保存到文件
                with open(self.current_file, "w", encoding="utf-8") as file:
                    file.write(content)
                    
                # 更新状态栏
                self.update_status(f"已保存: {self.current_file}")
                
                return True
                
            except Exception as e:
                messagebox.showerror("错误", f"无法保存文件: {e}")
                return False
        else:
            # 如果没有当前文件路径，执行另存为操作
            return self.save_file_as()
            
    def save_file_as(self):
        """另存为文件"""
        # 打开保存文件对话框
        file_path = filedialog.asksaveasfilename(
            defaultextension=".cnpy",
            filetypes=[("中文Python文件", "*.cnpy"), ("所有文件", "*.*")]
        )
        
        if file_path:
            # 更新当前文件路径
            self.current_file = file_path
            
            # 执行保存操作
            return self.save_file()
            
        return False
        
    def is_modified(self):
        """检查编辑器内容是否已修改"""
        # 这里可以实现更复杂的逻辑，例如与原始文件内容比较
        # 简单起见，我们假设任何非空内容都表示已修改
        return len(self.editor.get(1.0, tk.END).strip()) > 0
        
    def confirm_save(self):
        """确认是否保存修改"""
        response = messagebox.askyesnocancel("保存", "是否保存当前更改?")
        
        if response is None:  # 取消操作
            return False
        elif response:  # 是，保存
            return self.save_file()
        else:  # 否，不保存
            return True
            
    def exit_app(self):
        """退出应用"""
        # 如果当前文件已修改，提示保存
        if self.is_modified():
            if not self.confirm_save():
                return  # 用户取消了操作
                
        # 退出应用
        self.root.quit()
        
    def run_code(self):
        """运行代码"""
        # 获取编辑器内容
        code = self.editor.get(1.0, tk.END)
        
        # 如果代码为空，不执行
        if not code.strip():
            self.update_status("没有代码可执行")
            return
            
        # 如果当前文件已修改，提示保存
        if self.current_file and self.is_modified():
            if messagebox.askyesno("保存", "运行前是否保存当前更改?"):
                if not self.save_file():
                    return  # 保存失败，不执行
        
        # 清空输出区域
        self.clear_output()
        
        # 更新状态栏
        self.update_status("正在执行...")
        
        # 重置停止标志
        self.stop_execution.clear()
        
        # 启用停止按钮
        self.stop_button.config(state="normal")
        
        try:
            # 如果有保存的文件，直接运行该文件
            if self.current_file:
                self.run_file(self.current_file)
            else:
                # 否则，直接执行代码而不保存为文件
                self.execute_code_directly(code)
                    
            self.update_status("执行完成")
            
        except Exception as e:
            self.append_output(f"执行错误: {e}\n", "error")
            self.update_status("执行出错")
        
        # 执行完毕后禁用停止按钮
        self.stop_button.config(state="disabled")
            
    def execute_code_directly(self, code):
        """直接执行中文Python代码"""
        try:
            # 转换中文代码到Python代码
            python_code = mapping.translate_to_python(code)
            
            # 显示转换后的代码到转换代码框
            self.set_converted_code(python_code)
            
            # 清空输出区域
            self.clear_output()
            
            # 显示执行开始信息
            self.append_output("开始执行代码...\n", "info")
            
            # 使用线程执行长时间运行的代码
            self.run_with_timeout(python_code)
                
        except Exception as e:
            self.append_output(f"执行错误: {e}\n", "error")
            
    def run_with_timeout(self, python_code, timeout=3600):
        """使用线程执行代码
        
        参数:
            python_code: 要执行的Python代码
            timeout: 超时时间（秒）, 默认3600秒（1小时）
        """
        # 创建自定义输出流，实现实时输出到GUI
        class OutputRedirector:
            def __init__(self, text_widget, tag="normal"):
                self.text_widget = text_widget
                self.tag = tag
                self.buffer = ""
                
            def write(self, string):
                self.buffer += string
                if "\n" in self.buffer or len(self.buffer) > 80:  # 当有换行或缓冲区超过80字符时更新GUI
                    self.text_widget.config(state="normal")
                    self.text_widget.insert(tk.END, self.buffer, self.tag)
                    self.text_widget.see(tk.END)
                    self.text_widget.config(state="disabled")
                    self.text_widget.update()  # 强制更新GUI
                    self.buffer = ""
                    
            def flush(self):
                if self.buffer:
                    self.text_widget.config(state="normal")
                    self.text_widget.insert(tk.END, self.buffer, self.tag)
                    self.text_widget.see(tk.END)
                    self.text_widget.config(state="disabled")
                    self.text_widget.update()
                    self.buffer = ""
        
        # 重定向标准输出和标准错误
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        
        # 创建自定义输出重定向器
        stdout_redirector = OutputRedirector(self.output, "normal")
        stderr_redirector = OutputRedirector(self.output, "error")
        
        # 创建事件用于通知执行完成
        execution_done = threading.Event()
        execution_result = {"success": False}
        
        # 定义执行线程
        def execution_thread():
            sys.stdout = stdout_redirector
            sys.stderr = stderr_redirector
            
            try:
                # 创建命名空间
                namespace = {
                    'sys': sys,
                    '__builtins__': __builtins__,
                    
                    # 确保关键词映射也可用
                    '类型': type,
                }
                
                exec(python_code, namespace)
                execution_result["success"] = True
                
            except Exception as e:
                stderr_redirector.write(str(e))
            finally:
                # 确保缓冲区内容被刷新
                stdout_redirector.flush()
                stderr_redirector.flush()
                
                # 恢复标准输出和标准错误
                sys.stdout = original_stdout
                sys.stderr = original_stderr
                
                # 通知执行完成
                execution_done.set()
        
        # 创建并启动执行线程
        self.execution_thread = threading.Thread(target=execution_thread)
        self.execution_thread.daemon = True  # 设置为守护线程，这样主程序退出时线程也会退出
        self.execution_thread.start()
        
        # 在UI上显示执行中的提示
        self.update_status("正在执行代码...")
        self.root.update()
        
        # 等待执行完成或超时
        start_time = time.time()
        
        # 创建进度动画字符
        progress_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        char_index = 0
        
        # 实时显示进度
        self.append_output("正在执行代码...\n", "info")
        progress_line = self.output.index("end-1c linestart")
        
        while not execution_done.is_set() and (time.time() - start_time) < timeout:
            # 检查是否要求停止
            if self.stop_execution.is_set():
                self.append_output("\n执行已被用户停止！\n", "warning")
                self.update_status("执行已停止")
                return
                
            # 更新进度动画
            elapsed = time.time() - start_time
            if elapsed % 0.2 < 0.1:  # 每0.2秒更新一次动画
                char_index = (char_index + 1) % len(progress_chars)
                
                # 更新状态栏
                self.update_status(f"正在执行代码... {progress_chars[char_index]} (已用时 {elapsed:.1f} 秒)")
                
                # 更新UI
                self.root.update()
            time.sleep(0.05)
        
        # 检查是否超时
        if not execution_done.is_set():
            self.output.config(state="normal")
            self.output.delete(progress_line, "end-1c")
            self.output.config(state="disabled")
            
            self.append_output("\n⚠️ 代码执行超时！", "warning")
            self.append_output("\n可能原因：\n", "warning")
            self.append_output("1. 代码中存在无限循环\n", "warning")
            self.append_output("2. 计算量过大，需要更长时间\n", "warning")
            self.append_output("3. 存在等待用户输入的代码\n", "warning")
            
            self.update_status("代码执行超时")
            return
        
        # 显示执行结果
        if execution_result["success"]:
            self.update_status("代码执行完成")
            self.append_output("\n代码执行成功！\n", "success")
        else:
            self.update_status("代码执行出错")
            
    def run_file(self, file_path):
        """运行指定的文件"""
        try:
            # 读取文件内容
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()
                
            # 转换中文代码到Python代码
            python_code = mapping.translate_to_python(code)
            
            # 显示转换后的代码到转换代码框
            self.set_converted_code(python_code)
            
            # 清空输出区域
            self.clear_output()
            
            # 显示执行开始信息
            self.append_output(f"开始执行文件: {os.path.basename(file_path)}\n", "info")
            
            # 使用超时机制执行文件
            self.run_file_with_timeout(file_path)
                
        except Exception as e:
            self.append_output(f"运行文件时出错: {e}\n", "error")
            self.update_status("运行文件出错")
            
    def run_file_with_timeout(self, file_path, timeout=3600):
        """使用线程执行文件
        
        参数:
            file_path: 要执行的文件路径
            timeout: 超时时间（秒）, 默认3600秒（1小时）
        """
        # 创建自定义输出流，实现实时输出到GUI
        class OutputRedirector:
            def __init__(self, text_widget, tag="normal"):
                self.text_widget = text_widget
                self.tag = tag
                self.buffer = ""
                
            def write(self, string):
                self.buffer += string
                if "\n" in self.buffer or len(self.buffer) > 80:  # 当有换行或缓冲区超过80字符时更新GUI
                    self.text_widget.config(state="normal")
                    self.text_widget.insert(tk.END, self.buffer, self.tag)
                    self.text_widget.see(tk.END)
                    self.text_widget.config(state="disabled")
                    self.text_widget.update()  # 强制更新GUI
                    self.buffer = ""
                    
            def flush(self):
                if self.buffer:
                    self.text_widget.config(state="normal")
                    self.text_widget.insert(tk.END, self.buffer, self.tag)
                    self.text_widget.see(tk.END)
                    self.text_widget.config(state="disabled")
                    self.text_widget.update()
                    self.buffer = ""
        
        # 重定向标准输出和标准错误
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        
        # 创建自定义输出重定向器
        stdout_redirector = OutputRedirector(self.output, "normal")
        stderr_redirector = OutputRedirector(self.output, "error")
        
        # 创建事件用于通知执行完成
        execution_done = threading.Event()
        execution_result = {"success": False}
        
        # 定义执行线程
        def execution_thread():
            sys.stdout = stdout_redirector
            sys.stderr = stderr_redirector
            
            try:
                # 直接调用chinese_python模块的函数运行文件
                chinese_python.run_cnpy_file(str(file_path))
                execution_result["success"] = True
                
            except Exception as e:
                stderr_redirector.write(str(e))
            finally:
                # 确保缓冲区内容被刷新
                stdout_redirector.flush()
                stderr_redirector.flush()
                
                # 恢复标准输出和标准错误
                sys.stdout = original_stdout
                sys.stderr = original_stderr
                
                # 通知执行完成
                execution_done.set()
                
        # 创建并启动执行线程
        self.execution_thread = threading.Thread(target=execution_thread)
        self.execution_thread.daemon = True  # 设置为守护线程，这样主程序退出时线程也会退出
        self.execution_thread.start()
        
        # 在UI上显示执行中的提示
        self.update_status("正在执行文件...")
        self.root.update()
        
        # 等待执行完成或超时
        start_time = time.time()
        
        # 创建进度动画字符
        progress_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        char_index = 0
        
        # 实时显示进度
        self.append_output(f"正在执行文件: {os.path.basename(file_path)}...\n", "info")
        progress_line = self.output.index("end-1c linestart")
        
        while not execution_done.is_set() and (time.time() - start_time) < timeout:
            # 检查是否要求停止
            if self.stop_execution.is_set():
                self.append_output("\n执行已被用户停止！\n", "warning")
                self.update_status("执行已停止")
                return
                
            # 更新进度动画
            elapsed = time.time() - start_time
            if elapsed % 0.2 < 0.1:  # 每0.2秒更新一次动画
                char_index = (char_index + 1) % len(progress_chars)
                
                # 更新状态栏
                self.update_status(f"正在执行文件... {progress_chars[char_index]} (已用时 {elapsed:.1f} 秒)")
                
                # 更新UI
                self.root.update()
            time.sleep(0.05)
            
        # 检查是否超时
        if not execution_done.is_set():
            self.output.config(state="normal")
            self.output.delete(progress_line, "end-1c")
            self.output.config(state="disabled")
            
            self.append_output("\n⚠️ 文件执行超时！", "warning")
            self.append_output("\n可能原因：\n", "warning")
            self.append_output("1. 代码中存在无限循环\n", "warning")
            self.append_output("2. 计算量过大，需要更长时间\n", "warning")
            self.append_output("3. 存在等待用户输入的代码\n", "warning")
            
            self.update_status("文件执行超时")
            return
        
        # 显示执行结果
        if execution_result["success"]:
            self.update_status("文件执行完成")
            self.append_output("\n文件执行成功！\n", "success")
        else:
            self.update_status("文件执行出错")
            
    def clear_output(self):
        """清空输出区域"""
        # 清空转换后代码框
        self.converted_code.config(state="normal")
        self.converted_code.delete(1.0, tk.END)
        self.converted_code.config(state="disabled")
        
        # 清空执行结果框
        self.output.config(state="normal")
        self.output.delete(1.0, tk.END)
        self.output.config(state="disabled")
        
    def append_output(self, text, tag="normal"):
        """向输出区域添加文本
        
        参数:
            text: 要添加的文本
            tag: 文本标签，可以是 "normal", "error", "warning", "success", "info"
        """
        self.output.config(state="normal")
        self.output.insert(tk.END, text, tag)
        self.output.see(tk.END)  # 滚动到底部
        self.output.config(state="disabled")
        
    def set_converted_code(self, code):
        """设置转换后的Python代码"""
        self.converted_code.config(state="normal")
        self.converted_code.delete(1.0, tk.END)
        
        # 处理长代码显示
        if len(code) > 10000:  # 如果代码超过10000个字符
            # 只显示前5000个字符和后5000个字符
            truncated_code = code[:5000] + "\n\n...... 代码过长，中间部分已省略 ......\n\n" + code[-5000:]
            self.converted_code.insert(tk.END, truncated_code)
            self.append_output("注意：代码过长，转换后代码框中只显示部分内容。\n", "warning")
        else:
            self.converted_code.insert(tk.END, code)
        
        # 应用语法高亮
        self.python_highlighter.highlight_code(self.converted_code.get(1.0, tk.END))
        
        self.converted_code.see(1.0)  # 滚动到顶部
        self.converted_code.config(state="disabled")
        
    def update_status(self, message):
        """更新状态栏消息"""
        self.status_bar.config(text=message)
        
    def highlight_syntax(self, event=None):
        """简单的语法高亮实现"""
        # 先移除所有标签
        for tag in ["keyword", "string", "comment"]:
            self.editor.tag_remove(tag, "1.0", tk.END)
            
        # 获取文本内容
        content = self.editor.get("1.0", tk.END)
        
        # 关键字列表
        keywords = [
            "打印", "如果", "否则", "否则如果", "对于", "在", "当", "尝试", "捕获", "最后",
            "定义", "类", "返回", "跳过", "中断", "继续", "导入", "从", "作为", "真", "假", "空"
        ]
        
        # 高亮关键字
        for keyword in keywords:
            start_index = "1.0"
            while True:
                start_index = self.editor.search(keyword, start_index, stopindex=tk.END)
                if not start_index:
                    break
                    
                end_index = f"{start_index}+{len(keyword)}c"
                self.editor.tag_add("keyword", start_index, end_index)
                start_index = end_index
                
        # 高亮字符串 (简单实现，不处理转义)
        start_index = "1.0"
        while True:
            start_index = self.editor.search('"', start_index, stopindex=tk.END)
            if not start_index:
                break
                
            end_index = self.editor.search('"', f"{start_index}+1c", stopindex=tk.END)
            if not end_index:
                break
                
            end_index = f"{end_index}+1c"
            self.editor.tag_add("string", start_index, end_index)
            start_index = end_index
            
        # 高亮单引号字符串
        start_index = "1.0"
        while True:
            start_index = self.editor.search("'", start_index, stopindex=tk.END)
            if not start_index:
                break
                
            end_index = self.editor.search("'", f"{start_index}+1c", stopindex=tk.END)
            if not end_index:
                break
                
            end_index = f"{end_index}+1c"
            self.editor.tag_add("string", start_index, end_index)
            start_index = end_index
            
        # 高亮注释
        start_index = "1.0"
        while True:
            start_index = self.editor.search("#", start_index, stopindex=tk.END)
            if not start_index:
                break
                
            line = int(float(start_index))
            end_index = f"{line}.end"
            self.editor.tag_add("comment", start_index, end_index)
            start_index = f"{line + 1}.0"
            
    def show_about(self):
        """显示关于对话框"""
        about_text = """中文Python编辑器 v1.1

这是一个用于编写和执行中文Python代码的简单编辑器。

更新日志:
2023-09-09: 初始版本发布
2024-05-18: 
- 修复正则表达式转义序列错误
- 移除30秒执行时间限制
- 增加实时输出功能
- 增加停止执行功能
- 改进UI交互体验

作者: ikdxhz
"""
        messagebox.showinfo("关于中文Python编辑器", about_text)
        
    def show_help(self):
        """显示帮助对话框"""
        help_text = """
中文Python编辑器使用指南:

1. 文件操作:
   - 新建文件: Ctrl+N
   - 打开文件: Ctrl+O
   - 保存文件: Ctrl+S
   - 另存为: Ctrl+Shift+S

2. 编辑操作:
   - 撤销: Ctrl+Z
   - 重做: Ctrl+Y
   - 剪切: Ctrl+X
   - 复制: Ctrl+C
   - 粘贴: Ctrl+V

3. 运行代码:
   - 运行: F5
   - 清空输出: F6

4. 中文Python语法示例:
   打印("你好，世界！")
   
   如果 x > 0:
       打印("x是正数")
   否则如果 x < 0:
       打印("x是负数")
   否则:
       打印("x是零")
       
   对于 i 在 范围(10):
       打印(i)
        """
        messagebox.showinfo("帮助", help_text)

    def stop_code(self):
        """停止当前正在执行的代码"""
        if self.execution_thread and self.execution_thread.is_alive():
            # 设置停止标志
            self.stop_execution.set()
            self.update_status("正在停止执行...")
            self.append_output("\n正在停止执行...\n", "warning")
            
            # 禁用停止按钮，防止重复点击
            self.stop_button.config(state="disabled")


def main():
    """主函数"""
    # 创建主窗口
    root = tk.Tk()
    
    # 创建应用实例
    app = ChinesePythonGUI(root)
    
    # 设置窗口关闭事件
    root.protocol("WM_DELETE_WINDOW", app.exit_app)
    
    # 启动主循环
    root.mainloop()


if __name__ == "__main__":
    main() 