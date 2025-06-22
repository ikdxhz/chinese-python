#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 中文Python关键词映射

# 关键词映射
PY_MAPPING = {
    # 控制流 - 多种表达方式
    # if 系列
    "如果": "if",
    "若": "if",
    "若是": "if",
    "假如": "if",
    "倘若": "if",
    
    # elif 系列
    "否则如果": "elif",
    "或者如果": "elif",
    "不然如果": "elif",
    "要不然如果": "elif",
    
    # else 系列
    "否则": "else",
    "不然": "else",
    "要不然": "else",
    "反之": "else",
    
    # for 系列
    "对于": "for",
    "遍历": "for",
    "循环": "for",
    "迭代": "for",
    
    # in 系列
    "在": "in",
    "属于": "in",
    "存在于": "in",
    "里面": "in",
    
    # while 系列
    "当": "while",
    "当循环": "while",
    "只要": "while",
    "循环当": "while",
    
    # continue, break 系列
    "跳过": "continue",
    "继续": "continue",
    "略过": "continue",
    "下一个": "continue",
    
    "中断": "break",
    "跳出": "break",
    "终止": "break",
    "停止": "break",
    
    # return 系列
    "返回": "return",
    "回传": "return",
    "输出": "return",
    
    # 异常处理
    "尝试": "try",
    "试着": "try",
    "测试": "try",
    
    "捕获": "except",
    "异常": "except",
    "例外": "except",
    "错误": "except",
    
    "最后": "finally",
    "善后": "finally",
    "无论如何": "finally",
    
    # 函数与类
    "定义": "def",
    "函数": "def",
    "方法": "def",
    
    "类": "class",
    "对象类": "class",
    "模型": "class",
    
    # 逻辑运算符
    # and 系列
    "且": "and",
    "并且": "and",
    "同时": "and",
    "与": "and",
    
    # or 系列
    "或": "or",
    "或者": "or",
    "亦或": "or",
    "或是": "or",
    
    # not 系列
    "非": "not",
    "不": "not",
    "不是": "not",
    "取反": "not",
    
    # is 系列
    "是": "is",
    "为": "is",
    "等于": "is",
    
    # is not 系列
    "不是": "is not",
    "不等于": "is not",
    "不为": "is not",
    
    # 比较运算符
    "大于": ">",
    "小于": "<",
    "大于等于": ">=",
    "小于等于": "<=",
    "等于": "==",
    "不等于": "!=",
    
    # 内置函数
    # 基础输入输出
    "打印": "print",
    "输出": "print",
    "显示": "print",
    "写出": "print",
    
    "输入": "input",
    "读取": "input",
    "接收": "input",
    "获取输入": "input",
    
    # 内置函数 - 类型相关
    "类型": "type",
    "获取类型": "type",
    "判断类型": "type",
    
    # 数据结构和序列
    "范围": "range",
    "区间": "range",
    "序列": "range",
    "数列": "range",
    
    "长度": "len",
    "计数": "len",
    "数量": "len",
    "个数": "len",
    
    "枚举": "enumerate",
    "索引序列": "enumerate",
    "带序号": "enumerate",
    
    "映射": "map",
    "遍历映射": "map",
    "变换": "map",
    
    "过滤": "filter",
    "筛选": "filter",
    
    "压缩": "zip",
    "配对": "zip",
    "合并序列": "zip",
    
    "排序": "sorted",
    "排列": "sorted",
    "排序列表": "sorted",
    
    "反转": "reversed",
    "倒序": "reversed",
    "逆序": "reversed",
    
    # 类型转换
    "整数": "int",
    "转整数": "int",
    "取整": "int",
    
    "浮点": "float",
    "小数": "float",
    "浮点数": "float",
    
    "字符串": "str",
    "文本": "str",
    "字符列": "str",
    
    "列表": "list",
    "表": "list",
    "数组": "list",
    
    "字典": "dict",
    "映射表": "dict",
    "键值对": "dict",
    
    "集合": "set",
    "无序集": "set",
    "不重复集": "set",
    
    "元组": "tuple",
    "不可变序列": "tuple",
    "固定序列": "tuple",
    
    "布尔": "bool",
    "真假": "bool",
    "逻辑值": "bool",
    
    # 数学函数
    "绝对值": "abs",
    "取绝对值": "abs",
    
    "最大值": "max",
    "最大": "max",
    "取最大": "max",
    
    "最小值": "min",
    "最小": "min",
    "取最小": "min",
    
    "求和": "sum",
    "合计": "sum",
    "总和": "sum",
    
    "四舍五入": "round",
    "舍入": "round",
    
    # 其他
    # 模块和包
    "导入": "import",
    "引入": "import",
    "加载": "import",
    "引用": "import",
    
    "从": "from",
    "来自": "from",
    "自": "from",
    
    "作为": "as",
    "别名": "as",
    "命名为": "as",
    
    # 布尔值与空值
    "真": "True",
    "是的": "True",
    "对": "True",
    "正确": "True",
    
    "假": "False",
    "否": "False",
    "错": "False",
    "错误": "False",
    
    "空": "None",
    "无": "None",
    "空值": "None",
    "未定义": "None",
    
    # 作用域与流程控制
    "全局": "global",
    "全局变量": "global",
    "全局作用域": "global",
    
    "局部": "local",
    "局部变量": "local",
    
    "断言": "assert",
    "检查": "assert",
    "确认": "assert",
    
    "生成": "yield",
    "产出": "yield",
    "让出": "yield",
    
    "通过": "pass",
    "跳过语句": "pass",
    "空语句": "pass",
    
    "删除": "del",
    "移除": "del",
    "去除": "del",
    
    "抛出": "raise",
    "抛出异常": "raise",
    "引发": "raise",
    
    # 运算符与特殊符号
    "加": "+",
    "减": "-",
    "乘": "*",
    "除": "/",
    "取整除": "//",
    "整除": "//",
    "取模": "%",
    "取余": "%",
    "求余": "%",
    "幂": "**",
    "指数": "**",
    "次方": "**",
    
    # print参数
    "结束": "end",
    
    # 装饰器
    "装饰器": "@",
    "修饰器": "@",
    
    # 文件操作
    "打开": "open",
    "与": "with",
    "作为": "as",
    
    # 特殊方法
    "初始化": "__init__",
    "构造": "__init__",
    "字符表示": "__str__",
    "表示": "__repr__",
    "长度": "__len__",
    "调用": "__call__",
    "迭代器": "__iter__",
    "超类": "super",
    
    # 特殊属性
    "自身": "self",
    "本身": "self",
    "自己": "self",
    
    # 列表方法
    "添加": "append",
    "追加": "append",
    "增加": "append",
}

# 反向映射（用于错误输出转换）
PY_REVERSE_MAPPING = {v: k for k, v in PY_MAPPING.items()}

def translate_to_python(chinese_code):
    """
    将中文Python代码转换为标准Python代码
    
    增强版:
    - 支持多种中文表达方式
    - 确保只替换完整的关键词
    - 保留字符串和注释中的内容不替换
    - 正确处理print函数的括号
    - 避免替换变量名和参数名
    - 将中文标点符号转换为英文标点符号
    """
    import re
    
    # 中文标点符号到英文标点符号的映射
    punctuation_mapping = {
        "，": ",",
        "。": ".",
        "；": ";",
        "：": ":",
        "！": "!",
        "？": "?",
        """: "\"",
        """: "\"",
        "'": "'",
        "'": "'",
        "（": "(",
        "）": ")",
        "【": "[",
        "】": "]",
        "《": "<",
        "》": ">",
        "——": "-",
        "……": "...",
        "、": ",",
        "·": ".",
    }
    
    # 创建一个临时转换字典，确保长词组先替换（如"否则如果"应在"否则"之前替换）
    sorted_keys = sorted(PY_MAPPING.keys(), key=len, reverse=True)
    
    # 先提取所有字符串和注释，避免替换它们内部的内容
    # 存储所有字符串和注释的位置
    placeholders = {}
    
    # 提取三引号字符串
    triple_quote_pattern = r'(""".*?"""|\'\'\'.*?\'\'\')'
    triple_quotes = re.findall(triple_quote_pattern, chinese_code, re.DOTALL)
    for i, quote in enumerate(triple_quotes):
        placeholder = f"__TRIPLE_QUOTE_{i}__"
        placeholders[placeholder] = quote
        chinese_code = chinese_code.replace(quote, placeholder)
    
    # 提取单行字符串
    string_pattern = r'(".*?"|\'.*?\')'
    strings = re.findall(string_pattern, chinese_code)
    for i, string in enumerate(strings):
        placeholder = f"__STRING_{i}__"
        placeholders[placeholder] = string
        chinese_code = chinese_code.replace(string, placeholder)
    
    # 提取注释
    comment_pattern = r'(#.*?)$'
    comments = []
    for line in chinese_code.split('\n'):
        comment_match = re.search(comment_pattern, line)
        if comment_match:
            comments.append(comment_match.group(1))
    for i, comment in enumerate(comments):
        placeholder = f"__COMMENT_{i}__"
        placeholders[placeholder] = comment
        chinese_code = chinese_code.replace(comment, placeholder)
    
    # 提取变量名和参数名，避免被当作关键词替换
    # 这包括函数定义中的参数、变量赋值和循环变量等
    var_placeholders = {}
    
    # 捕获并保护所有变量定义
    var_pattern = r'([^\s\(\)=:,]+)\s*='  # 变量名 = 形式
    for match in re.finditer(var_pattern, chinese_code):
        var_name = match.group(1).strip()
        if var_name and var_name not in var_placeholders:
            placeholder = f"__VAR_{len(var_placeholders)}__"
            var_placeholders[placeholder] = var_name
            # 只替换变量定义的左侧，不替换右侧的使用
            chinese_code = chinese_code.replace(f"{var_name} =", f"{placeholder} =", 1)
    
    # 捕获并保护函数参数名
    func_pattern = r'(?:定义|函数|方法)\s+\w+\(([^\)]*)\)'
    for match in re.finditer(func_pattern, chinese_code):
        params = match.group(1).split(',')
        for i, param in enumerate(params):
            param = param.strip()
            if param and param not in var_placeholders:
                placeholder = f"__VAR_{len(var_placeholders)}__"
                var_placeholders[placeholder] = param
                # 替换对应位置的参数
                params[i] = placeholder
        # 重建函数签名
        func_sig = match.group(0)
        new_params = ", ".join(params)
        new_sig = re.sub(r'\([^\)]*\)', f'({new_params})', func_sig)
        chinese_code = chinese_code.replace(func_sig, new_sig)
    
    # 捕获并保护for循环变量（对于...在...形式）
    for_pattern = r'(?:对于|遍历|循环|迭代)\s+([^\s]+)\s+(?:在|属于|存在于|里面)'
    for match in re.finditer(for_pattern, chinese_code):
        var_name = match.group(1).strip()
        if var_name and var_name not in var_placeholders:
            placeholder = f"__VAR_{len(var_placeholders)}__"
            var_placeholders[placeholder] = var_name
            # 替换for循环变量
            chinese_code = chinese_code.replace(
                f"{match.group(0).split(var_name)[0]}{var_name}",
                f"{match.group(0).split(var_name)[0]}{placeholder}"
            )
    
    # 进行关键词替换
    result = chinese_code
    
    # 先处理特殊情况：print语句需要正确处理括号
    # 查找所有"打印/输出/显示/写出"等打印命令
    print_keywords = ['打印', '输出', '显示', '写出']
    for print_word in print_keywords:
        # 查找没有括号的打印语句（例如：打印 结果）
        pattern = fr'({print_word}\s+[^\(\n]+)'
        for match in re.finditer(pattern, result):
            original = match.group(1)
            # 提取打印命令后面的内容
            content = original.split(' ', 1)[1].strip()
            # 替换为有括号的形式
            result = result.replace(original, f"{print_word}({content})")
    
    # 处理一般关键词替换
    for key in sorted_keys:
        # 确保只替换"词"而不是词的一部分
        # 使用正则表达式以确保我们替换的是完整的关键词
        pattern = r'(?<!\w)' + re.escape(key) + r'(?!\w)'
        result = re.sub(pattern, PY_MAPPING[key], result)
    
    # 恢复所有变量名
    for placeholder, var_name in var_placeholders.items():
        result = result.replace(placeholder, var_name)
    
    # 转换代码中的中文标点符号为英文标点符号（不包括字符串和注释）
    for zh_punct, en_punct in punctuation_mapping.items():
        result = result.replace(zh_punct, en_punct)
    
    # 恢复所有字符串和注释（保留原始的中文标点符号）
    for placeholder, original in placeholders.items():
        result = result.replace(placeholder, original)
    
    return result

def translate_from_python(python_code):
    """
    将标准Python代码转换为中文Python代码
    
    参数:
    - python_code: 要翻译的Python代码
    
    返回:
    - 翻译后的中文Python代码，使用默认中文关键词
    """
    import re
    
    # 用于从Python关键词映射回中文关键词的首选项字典
    preferred_chinese = {
        'if': '如果',
        'elif': '否则如果',
        'else': '否则',
        'for': '对于',
        'in': '在',
        'while': '当',
        'continue': '跳过',
        'break': '中断',
        'return': '返回',
        'try': '尝试',
        'except': '捕获',
        'finally': '最后',
        'def': '定义',
        'class': '类',
        'and': '且',
        'or': '或',
        'not': '非',
        'is': '是',
        'is not': '不是',
        'print': '打印',
        'input': '输入',
        'range': '范围',
        'len': '长度',
        'int': '整数',
        'float': '浮点',
        'str': '字符串',
        'list': '列表',
        'dict': '字典',
        'set': '集合',
        'tuple': '元组',
        'import': '导入',
        'from': '从',
        'as': '作为',
        'True': '真',
        'False': '假',
        'None': '空',
        'global': '全局',
        'assert': '断言',
        'yield': '生成',
        'pass': '通过',
        'del': '删除',
        'raise': '抛出',
        '//': '取整除',
        '%': '取模',
    }
    
    # 先提取所有字符串和注释，避免替换它们内部的内容
    placeholders = {}
    
    # 提取三引号字符串
    triple_quote_pattern = r'(""".*?"""|\'\'\'.*?\'\'\')'
    triple_quotes = re.findall(triple_quote_pattern, python_code, re.DOTALL)
    for i, quote in enumerate(triple_quotes):
        placeholder = f"__TRIPLE_QUOTE_{i}__"
        placeholders[placeholder] = quote
        python_code = python_code.replace(quote, placeholder)
    
    # 提取单行字符串
    string_pattern = r'(".*?"|\'.*?\')'
    strings = re.findall(string_pattern, python_code)
    for i, string in enumerate(strings):
        placeholder = f"__STRING_{i}__"
        placeholders[placeholder] = string
        python_code = python_code.replace(string, placeholder)
    
    # 提取注释
    comment_pattern = r'(#.*?)$'
    comments = []
    for line in python_code.split('\n'):
        comment_match = re.search(comment_pattern, line)
        if comment_match:
            comments.append(comment_match.group(1))
    for i, comment in enumerate(comments):
        placeholder = f"__COMMENT_{i}__"
        placeholders[placeholder] = comment
        python_code = python_code.replace(comment, placeholder)
    
    # 创建一个临时转换字典，确保长词组先替换
    sorted_keys = sorted(preferred_chinese.keys(), key=len, reverse=True)
    result = python_code
    
    for key in sorted_keys:
        pattern = r'(?<!\w)' + re.escape(key) + r'(?!\w)'
        chinese_word = preferred_chinese[key]
        result = re.sub(pattern, chinese_word, result)
    
    # 恢复所有字符串和注释
    for placeholder, original in placeholders.items():
        result = result.replace(placeholder, original)
    
    return result