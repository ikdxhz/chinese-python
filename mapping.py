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
    "遍访": "for",
    "历遍": "for",
    "轮询": "for",
    "逐个": "for",
    "逐一": "for",
    "依次": "for",
    "每当": "for",
    "每一个": "for",
    "逐项": "for",
    "取遍": "for",
    "历数": "for",
    "依序": "for",
    "按序": "for",
    
    # in 系列
    "在": "in",
    "属于": "in",
    "存在于": "in",
    "里面": "in",
    "之中": "in",
    "其中": "in",
    "中的": "in",
    "包含于": "in",
    "位于": "in",
    "处于": "in",
    "范围内": "in",
    "集合中": "in",
    "内部": "in",
    
    # while 系列
    "当": "while",
    "当循环": "while",
    "只要": "while",
    "循环当": "while",
    "周而复始": "while",
    "循环往复": "while",
    "不断重复": "while",
    "重复执行": "while",
    "持续": "while",
    "一直": "while",
    "直到": "while",
    "当条件": "while",
    "循环直到": "while",
    "持续循环": "while",
    "不停": "while",
    "连续": "while",
    
    # continue, break 系列
    "跳过": "continue",
    "继续": "continue",
    "略过": "continue",
    "下一个": "continue",
    "略过此节": "continue",
    "略过此轮": "continue",
    "且看下回": "continue",
    "进行下一轮": "continue",
    "忽略剩余": "continue",
    "转入下轮": "continue",
    "跳至下一轮": "continue",
    "忽略本次": "continue",
    "放弃本轮": "continue",
    
    "中断": "break",
    "跳出": "break",
    "终止": "break",
    "停止": "break",
    "中止": "break",
    "点到为止": "break",
    "到此为止": "break",
    "结束循环": "break",
    "跳出循环": "break",
    "跳离循环": "break",
    "脱离循环": "break",
    "离开循环": "break",
    "不再循环": "break",
    
    # return 系列
    "返回": "return",
    "回传": "return",
    "输出": "return",
    
    # lambda 系列
    "匿名函数": "lambda",
    "匿名": "lambda",
    "短函数": "lambda",
    "内联函数": "lambda",
    "简函数": "lambda",
    "快函数": "lambda",
    "微函数": "lambda",
    
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
    "总是执行": "finally",
    "清理": "finally",
    
    # 常见异常类型
    "值错误": "ValueError",
    "类型错误": "TypeError",
    "索引错误": "IndexError",
    "键错误": "KeyError",
    "文件未找到错误": "FileNotFoundError",
    "导入错误": "ImportError",
    "零除错误": "ZeroDivisionError",
    "属性错误": "AttributeError",
    "名称错误": "NameError",
    "语法错误": "SyntaxError",
    "缩进错误": "IndentationError",
    "溢出错误": "OverflowError",
    "运行时错误": "RuntimeError",
    "内存错误": "MemoryError",
    
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
    
    # 数据结构方法
    "添加": "append",
    "追加": "append",
    "增加": "append",
    
    "插入": "insert",
    "插入位置": "insert",
    "置入": "insert",
    
    "扩展": "extend",
    "连接": "extend",
    "合并": "extend",
    
    "移除": "remove",
    "删除元素": "remove",
    "去除": "remove",
    
    "弹出": "pop",
    "取出": "pop",
    "删除并返回": "pop",
    
    "清空": "clear",
    "清除": "clear",
    "全部删除": "clear",
    
    "索引": "index",
    "查找位置": "index",
    "定位": "index",
    
    "计数": "count",
    "统计": "count",
    "出现次数": "count",
    
    "复制": "copy",
    "拷贝": "copy",
    "克隆": "copy",
    
    "获取": "get",
    "获取值": "get",
    "取值": "get",
    
    "键值对": "items",
    "所有项": "items",
    "键值项": "items",
    
    "所有键": "keys",
    "键列表": "keys",
    "获取键": "keys",
    
    "所有值": "values",
    "值列表": "values",
    "获取值列表": "values",
    
    "更新": "update",
    "合并字典": "update",
    "更新字典": "update",
    
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
    
    # nonlocal 系列
    "非局部": "nonlocal",
    "外层变量": "nonlocal",
    "外部变量": "nonlocal",
    "上层作用域": "nonlocal",
    "上层变量": "nonlocal",
    "引用外部": "nonlocal",
    "使用外部": "nonlocal",
    
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
    "使用": "with",
    "借助": "with",
    "利用": "with",
    "伴随": "with",
    "携带": "with",
    "处理上下文": "with",
    "上下文管理": "with",
    "资源管理": "with",
    
    # 文件模式
    "读模式": "r",
    "写模式": "w",
    "追加模式": "a",
    "二进制模式": "b",
    "文本模式": "t",
    "读写模式": "r+",
    
    # 文件方法
    "读取": "read",
    "读一行": "readline",
    "读所有行": "readlines",
    "写入": "write",
    "写入行": "writelines",
    "关闭": "close",
    "刷新": "flush",
    "定位": "seek",
    "获取位置": "tell",
    
    # 网络编程
    "网络": "network",
    "套接字": "socket",
    "服务器": "server",
    "客户端": "client",
    "主机": "host",
    "端口": "port",
    "地址": "address",
    "IP地址": "ip_address",
    "域名": "domain",
    "URL": "url",
    "HTTP": "http",
    "HTTPS": "https",
    "FTP": "ftp",
    "SSH": "ssh",
    "TCP": "tcp",
    "UDP": "udp",
    "请求": "request",
    "响应": "response",
    "GET请求": "get",
    "POST请求": "post",
    "PUT请求": "put",
    "DELETE请求": "delete",
    "头部": "headers",
    "内容类型": "content_type",
    "状态码": "status_code",
    "认证": "authentication",
    "授权": "authorization",
    "Cookie": "cookie",
    "会话": "session",
    "连接": "connection",
    "连接池": "connection_pool",
    "超时": "timeout",
    "重试": "retry",
    "代理": "proxy",
    "网络爬虫": "web_crawler",
    "API": "api",
    "REST": "rest",
    "JSON": "json",
    "XML": "xml",
    "WebSocket": "websocket",
    "异步IO": "asyncio",
    
    # JSON处理
    "解析JSON": "json.loads",
    "转为JSON": "json.dumps",
    "读取JSON文件": "json.load",
    "写入JSON文件": "json.dump",
    
    # 路径操作
    "路径连接": "os.path.join",
    "文件存在": "os.path.exists",
    "是目录": "os.path.isdir",
    "是文件": "os.path.isfile",
    "获取大小": "os.path.getsize",
    "获取修改时间": "os.path.getmtime",
    "获取路径": "os.path.abspath",
    "获取文件名": "os.path.basename",
    "获取目录名": "os.path.dirname",
    
    # 特殊方法
    "初始化": "__init__",
    "构造": "__init__",
    "字符表示": "__str__",
    "表示": "__repr__",
    "长度": "__len__",
    "调用": "__call__",
    "迭代器": "__iter__",
    "超类": "super",
    "父类": "super",
    "基类": "super",
    
    # 特殊属性
    "吾": "self",
    "予": "self",
    "自身": "self",
    "本身": "self",
    "自己": "self",
    "此对象": "self",
    "在下": "self",
    "本实例": "self",
    "本类实例": "self",
    "当前实例": "self",
    "当前对象": "self",
    "我": "self",
    "俺": "self",
    "咱": "self",
    "本尊": "self",
    "吾身": "self",
    "小生": "self",
    "贫道": "self",
    "老衲": "self",
    "老朽": "self",
    "鄙人": "self",
    
    # 面向对象编程
    "继承": "inherit",
    "多态": "polymorphism",
    "封装": "encapsulation",
    "抽象": "abstraction",
    "实例": "instance",
    "对象": "object",
    "属性": "attribute",
    "方法": "method",
    "静态方法": "@staticmethod",
    "类方法": "@classmethod",
    "抽象方法": "@abstractmethod",
    "私有": "private",
    "保护": "protected",
    "公开": "public",
    "构造函数": "__init__",
    "析构函数": "__del__",
    "实现": "implement",
    "接口": "interface",
    
    # 列表方法 (恢复被误删的内容)
    "添加": "append",
    "追加": "append",
    "增加": "append",
    
    # 数据科学
    "数据框": "DataFrame",
    "系列": "Series",
    "读取CSV": "pd.read_csv",
    "读取Excel": "pd.read_excel",
    "分组": "groupby",
    "聚合": "aggregate",
    "透视表": "pivot_table",
    "合并": "merge",
    "连接": "concat",
    "描述统计": "describe",
    "均值": "mean",
    "中位数": "median",
    "标准差": "std",
    "最大值": "max",
    "最小值": "min",
    "求和": "sum",
    "计数": "count",
    "唯一值": "unique",
    "空值": "na",
    "缺失值": "null",
    "填充": "fillna",
    "丢弃": "dropna",
    "替换": "replace",
    "排序": "sort",
    "绘图": "plot",
    "直方图": "hist",
    "散点图": "scatter",
    "折线图": "line",
    "条形图": "bar",
    "箱线图": "box",
    
    # Web开发
    "路由": "route",
    "请求": "request",
    "响应": "response",
    "会话": "session",
    "表单": "form",
    "重定向": "redirect",
    "模板": "template",
    "渲染": "render",
    "视图": "view",
    "控制器": "controller",
    "模型": "model",
    "静态文件": "static",
    "蓝图": "blueprint",
    "中间件": "middleware",
    "认证": "auth",
    "授权": "authorization",
    "登录": "login",
    "注册": "register",
    "登出": "logout",
    "数据库": "database",
    "数据存储": "database",
    "数据仓库": "database",
    "数据管理系统": "database",
    "查询": "query",
    "检索": "query",
    "数据查询": "query",
    "搜索数据": "query",
    "插入": "insert",
    "新增": "insert",
    "添加记录": "insert",
    "增加数据": "insert",
    "录入": "insert",
    "更新": "update",
    "修改": "update",
    "更改": "update",
    "变更数据": "update",
    "删除": "delete",
    "移除": "delete",
    "清除记录": "delete",
    "抹去数据": "delete",
    "选择": "select",
    "筛选": "select",
    "提取": "select",
    "获取字段": "select",
    "从": "from",
    "where子句": "where",
    "分组依据": "group by",
    "排序依据": "order by",
    "连接": "join",
    "左连接": "left join",
    "右连接": "right join",
    "内连接": "inner join",
    "外连接": "outer join",
    
    # 高级Python特性
    "生成器": "generator",
    "迭代器": "iterator",
    "装饰器": "decorator",
    "上下文管理器": "context manager",
    "异步": "async",
    "非同步": "async",
    "并发执行": "async",
    "异步执行": "async",
    "等待": "await",
    "异步等待": "await",
    "等候": "await",
    "暂停等待": "await",
    "挂起等待": "await",
    "并发": "concurrent",
    "协程": "coroutine",
    "并行": "parallel",
    "线程": "thread",
    "进程": "process",
    "锁": "lock",
    "信号量": "semaphore",
    "事件": "event",
    "队列": "queue",
    "通道": "channel",
    "异步IO": "asyncio",
    "异步函数": "async def",
    "异步等待": "await",
    "异步循环": "async for",
    "异步with": "async with",
    "生成器表达式": "generator expression",
    "列表推导式": "list comprehension",
    "字典推导式": "dict comprehension",
    "集合推导式": "set comprehension",
    "元组拆包": "tuple unpacking",
    "星号拆包": "*args",
    "双星号拆包": "**kwargs",
    "类型注解": "type annotation",
    "数据类": "dataclass",
    "属性": "property",
    "描述符": "descriptor",
    "元类": "metaclass",
    "抽象基类": "abc",
    "虚拟环境": "venv",
    "包管理器": "pip",
    "单元测试": "unittest",
    "文档测试": "doctest",
    "性能分析": "profile",
    
    # 常用包
    "数值计算": "numpy",
    "数据分析": "pandas",
    "可视化": "matplotlib",
    "科学计算": "scipy",
    "机器学习": "scikit-learn",
    "深度学习": "tensorflow",
    "神经网络": "pytorch",
    "自然语言处理": "nltk",
    "计算机视觉": "opencv",
    "网络请求": "requests",
    "网络爬虫": "scrapy",
    "网页解析": "beautifulsoup",
    "接口开发": "flask",
    "网站开发": "django",
    "快速开发": "fastapi",
    "GUI开发": "tkinter",
    "游戏开发": "pygame",
    "数据库操作": "sqlalchemy",
    "日期时间": "datetime",
    "正则表达式": "re",
    "日志记录": "logging",
    "配置解析": "configparser",
    "命令行": "argparse",
    "系统操作": "os",
    "路径操作": "pathlib",
    "文件操作": "io",
    "压缩文件": "zipfile",
    "序列化": "pickle",
    
    # 具有中国特色的关键词表达
    # 控制流
    "倘若": "if",
    "设若": "if",
    "诚如": "if",
    "若然": "if",
    "但凡": "if",
    "苟若": "if", 
    "倘使": "if",
    "如若": "if",
    "设使": "if",

    "否则的话": "else",
    "其他情况": "else",
    "退而求其次": "else",
    "否则然": "else",
    "不然者": "else",
    "不尔": "else",
    "不若": "else",
    "若非如此": "else",
    
    "周而复始": "while",
    "循环往复": "while",
    "不断重复": "while",
    
    "遍访": "for",
    "历遍": "for",
    "轮询": "for",
    
    "中止": "break",
    "点到为止": "break",
    "到此为止": "break",
    
    "略过此节": "continue",
    "略过此轮": "continue",
    "且看下回": "continue",
    
    "回馈": "return",
    "奉上": "return",
    "献上": "return",
    
    # 逻辑运算
    "既": "and",
    "亦": "and",
    "并": "and",
    
    "抑或": "or",
    "要么": "or",
    "二选一": "or",
    
    "非也": "not",
    "并非": "not",
    "绝非": "not",
    
    # 函数与类
    "术": "def",
    "法门": "def",
    "招式": "def",
    
    "流派": "class",
    "门派": "class",
    "派系": "class",
    
    # 数据结构
    "清单": "list",
    "簿册": "list",
    "名录": "list",
    
    "字典册": "dict",
    "对照表": "dict",
    "查阅表": "dict",
    
    # 输入输出
    "显示于": "print",
    "呈现": "print",
    "道出": "print",
    
    "询问": "input",
    "请教": "input",
    "求教": "input",
    
    # 异常处理
    "小心行事": "try",
    "且试试": "try",
    "姑且一试": "try",
    
    "倘若有误": "except",
    "若有差池": "except",
    "若有闪失": "except",
    
    "善后事宜": "finally",
    "无论成败": "finally",
    "皆须善后": "finally",
    
    # 文件操作
    "开卷": "open",
    "阅览": "read",
    "誊抄": "write",
    "合卷": "close",
    
    # 变量操作
    "乃是": "=",
    "即为": "=",
    "定为": "=",
    
    # 循环迭代
    "其中每一": "for in",
    "遍览": "for in",
    "历数": "for in",
    
    # 类方法
    "本门方法": "@classmethod",
    "门规": "@classmethod",
    "师门心法": "@classmethod",
    
    # Matplotlib可视化相关
    "图像": "figure",
    "子图": "subplot",
    "绘图": "plot",
    "散点图": "scatter",
    "条形图": "bar",
    "饼图": "pie",
    "直方图": "hist",
    "箱线图": "boxplot",
    "等高线图": "contour",
    "热图": "heatmap",
    "标题": "title",
    "横轴标签": "xlabel",
    "纵轴标签": "ylabel",
    "图例": "legend",
    "网格": "grid",
    "紧凑布局": "tight_layout",
    "保存图像": "savefig",
    "显示": "show",
    "关闭": "close",
    "轴方向": "axis",
    "刻度": "tick",
    "颜色条": "colorbar",
    "注释": "annotate",
    "文本": "text",
    "样式": "style",
    "子图网格": "subplots",
    
    # Pandas和NumPy补充
    "数组": "array",
    "平方": "square",
    "平均值": "mean",
    "中值": "median",
    "标准差": "std",
    "方差": "var",
    "随机数": "random",
    "正态": "normal",
    "均匀分布": "uniform",
    "线性回归": "linregress",
    "相关系数": "corrcoef",
    "协方差": "cov",
    "转置": "transpose",
    "重塑": "reshape",
    "拼接": "concatenate",
    "切片": "slice",
    "最大值索引": "argmax",
    "最小值索引": "argmin",
    "唯一值": "unique",
    "值计数": "value_counts",
    "分组": "groupby",
    "聚合": "agg",
    "排序": "sort_values",
    "升序": "ascending",
    "填充": "fillna",
    "丢弃": "dropna",
    "方法": "method",
    "依据": "by",
    "合并": "merge",
    "连接": "join",
    "透视表": "pivot_table",
    "重置索引": "reset_index",
    "设置索引": "set_index",
    "采样": "sample",
    "重命名": "rename",
    "分箱": "cut",
    "替换": "replace",
    "应用函数": "apply",
    "开方": "sqrt",
    "立方": "cube",
    "立方根": "cbrt",
    "绝对值": "abs",
    "对数": "log",
    "自然对数": "log",
    "以10为底对数": "log10",
    "以2为底对数": "log2",
    "指数": "exp",
    "幂": "pow",
    "正弦": "sin",
    "余弦": "cos",
    "正切": "tan",
    "反正弦": "arcsin",
    "反余弦": "arccos",
    "反正切": "arctan",
    "弧度转角度": "degrees",
    "角度转弧度": "radians",
    "双曲正弦": "sinh",
    "双曲余弦": "cosh",
    "双曲正切": "tanh",
    "阶乘": "factorial",
    "向上取整": "ceil",
    "向下取整": "floor",
    "四舍五入": "round",
    "取整数部分": "trunc",

    # 数据分析
    "数据分析": "data_analysis",
    "数据处理": "data_processing",
    "数据清洗": "data_cleaning",
    "数据可视化": "data_visualization",
    "数据提取": "data_extraction",
    "数据转换": "data_transformation",
    "数据筛选": "data_filtering",
    "数据聚合": "data_aggregation",
    "数据分组": "data_grouping",
    "数据归一化": "data_normalization",
    "数据标准化": "data_standardization",

    # JSON操作
    "解析JSON": "json.loads",
    "转为JSON": "json.dumps",
    "解码JSON": "json.loads",
    "编码JSON": "json.dumps",
    "从文件读取JSON": "json.load",
    "写入JSON到文件": "json.dump",
    "JSON格式化": "json.dumps(indent=4)",
    "JSON排序": "json.dumps(sort_keys=True)",

    # 日期时间
    "当前日期时间": "datetime.now()",
    "今天": "date.today()",
    "时间戳": "timestamp()",
    "格式化日期": "strftime()",
    "解析日期": "strptime()",
    "日期差": "timedelta()",
    "年": "year",
    "月": "month",
    "日": "day",
    "时": "hour",
    "分": "minute",
    "秒": "second",
    "毫秒": "millisecond",
    "微秒": "microsecond",
    "星期": "weekday()",
    "ISO格式": "isoformat()",
    "UTC时间": "utcnow()",

    # 系统操作
    "环境变量": "os.environ",
    "当前目录": "os.getcwd()",
    "改变目录": "os.chdir()",
    "创建目录": "os.mkdir()",
    "递归创建目录": "os.makedirs()",
    "删除目录": "os.rmdir()",
    "递归删除目录": "shutil.rmtree()",
    "列出目录": "os.listdir()",
    "遍历目录": "os.walk()",
    "文件重命名": "os.rename()",
    "文件移动": "shutil.move()",
    "文件复制": "shutil.copy()",
    "目录复制": "shutil.copytree()",
    "执行命令": "os.system()",
    "获取命令输出": "subprocess.check_output()",
    "运行命令": "subprocess.run()",
    "命令管道": "subprocess.Popen()",
    "平台信息": "sys.platform",
    "Python版本": "sys.version",
    "退出程序": "sys.exit()",
    "命令行参数": "sys.argv",
    "标准输入": "sys.stdin",
    "标准输出": "sys.stdout",
    "标准错误": "sys.stderr",
    "临时文件": "tempfile.TemporaryFile()",
    "临时目录": "tempfile.TemporaryDirectory()",

    # 进程与线程
    "创建线程": "threading.Thread()",
    "启动线程": "thread.start()",
    "加入线程": "thread.join()",
    "线程名称": "thread.name",
    "线程标识": "thread.ident",
    "线程锁": "threading.Lock()",
    "线程事件": "threading.Event()",
    "线程池": "concurrent.futures.ThreadPoolExecutor()",
    "创建进程": "multiprocessing.Process()",
    "启动进程": "process.start()",
    "终止进程": "process.terminate()",
    "进程池": "multiprocessing.Pool()",
    "异步执行": "executor.submit()",
    "等待完成": "future.result()",
    "进程队列": "multiprocessing.Queue()",
    "进程管道": "multiprocessing.Pipe()",
    "共享内存": "multiprocessing.shared_memory",

    # GUI编程
    "窗口": "window",
    "根窗口": "root",
    "主窗口": "main_window",
    "标签": "label",
    "按钮": "button",
    "输入框": "entry",
    "文本框": "text",
    "复选框": "checkbox",
    "单选按钮": "radiobutton",
    "下拉菜单": "combobox",
    "列表框": "listbox",
    "滚动条": "scrollbar",
    "菜单": "menu",
    "菜单栏": "menubar",
    "工具栏": "toolbar",
    "状态栏": "statusbar",
    "画布": "canvas",
    "事件": "event",
    "绑定": "bind",
    "点击事件": "click_event",
    "鼠标事件": "mouse_event",
    "键盘事件": "keyboard_event",
    "布局": "layout",
    "网格布局": "grid",
    "水平布局": "horizontal",
    "垂直布局": "vertical",
    "框架": "frame",
    "选项卡": "tab",
    "对话框": "dialog",
    "消息框": "messagebox",
    "文件对话框": "filedialog",
    "颜色选择器": "colorchooser",
    "图像": "image",
    "图标": "icon",
    "字体": "font",
    "样式": "style",
    "主题": "theme",
    "分集合": "splitset",
    "过滤集合": "filterset",
    "映射集合": "mapset",
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
    triple_quote_pattern = r'(""".*?"""|\'{3}.*?\'{3})'
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
    triple_quote_pattern = r'(""".*?"""|\'{3}.*?\'{3})'
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