<!--
 * @Author: 崩布猪
 * @Date: 2024-05-28 14:08:30
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-05-30 10:14:53
 * @FilePath: \CS\web\PHP.md
 * @Description: 
 * 
-->
# PHP 

**php是什么**

PHP（全称“PHP: Hypertext Preprocessor”），超文本预处理器的字母缩写）是一种被广泛应用的开放源代码的多用途脚本语言，它可嵌入到 HTML中，尤其适合 web 开发。

它运行在服务端

**PHP能做什么**

主要用于服务端脚本 和 命令行脚本
它能在所有主流操作系统上使用

特征：支持大范围的数据库
      支持多种服务歇息
      高效的文本处理特性

## 基本语法

### PHP标记
PHP 有一个 echo 标记简写 `<?=`， 它是更完整的 `<?php echo` 的简写形式。

PHP代码结构：PHP代码以<?php和?>标记符号包围，并在其中编写PHP代码。

PHP注释：以//或#开头的单行注释，或/*和*/包围的多行注释。

## 数据类型
null
bool
int
float
string

#### **array**
PHP 中的 [array](https://www.php.net/manual/zh/language.types.array.php) 实际上是一个有序映射。映射是一种把 _values_ 关联到 _keys_ 的类型。此类型针对多种不同用途进行了优化； 它可以被视为数组、列表（向量）、哈希表（映射的实现）、字典、集合、堆栈、队列等等。 由于 [array](https://www.php.net/manual/zh/language.types.array.php) 的值可以是其它 [array](https://www.php.net/manual/zh/language.types.array.php) 所以树形结构和多维 [array](https://www.php.net/manual/zh/language.types.array.php) 也是允许的。
##### 定义
```
array(
    key  => value,
    key2 => value2,
    key3 => value3,
    ...
)

// 使用短数组语法  
$array = [  
"foo" => "bar",  
"bar" => "foo",  
];
```
object
resource
never
void
Value

## 变量

变量是存储数据的容器，PHP中使用$符号来声明变量。

规则
$符号开始，后面跟变量名，变量名只能包含字母数字和下划线，且不能以数字开头。
区分大小写，不能包含空格
global关键字：在函数内部使用global关键字声明全局变量，使变量可以在函数外部被访问。
可变变量
```
$a = a
$$a = b

```
  

检测变量的数据类型 is_type() 函数
类型转换 强制转换

## **常量**
命名常量函数 define() 函数
```
<?php
define("CONSTANT", "Hello world.");
echo CONSTANT; // 输出 "Hello world."
echo Constant; // 抛出错误：未定义的常量 "Constant"
               // 在 PHP 8.0.0 之前，输出 "Constant" 并发出一个提示级别错误信息
?>

```

#### 魔术常量

| 名字                     | 说明                                                                                |     |
| ---------------------- | --------------------------------------------------------------------------------- | --- |
| \__LINE__              | 文件中的当前行号。                                                                         |     |
| \__FILE__              | 文件的完整路径和文件名。如果用在被包含文件中，则返回被包含的文件名。                                                |     |
| \__DIR__               | 文件所在的目录。如果用在被包括文件中，则返回被包括的文件所在的目录。它等价于 `dirname(__FILE__)`。除非是根目录，否则目录中名不包括末尾的斜杠。 |     |
| \__FUNCTION__          | 当前函数的名称。匿名函数则为 `{closure}`。                                                       |     |
| \__CLASS__             | 当前类的名称。类名包括其被声明的作用域（例如 `Foo\Bar`）。当用在 trait 方法中时，__CLASS__ 是调用 **trait** 方法的类的名字。     |     |
| \__TRAIT__             | Trait 的名字。Trait 名包括其被声明的作用域（例如 `Foo\Bar`）。                                        |     |
| \__METHOD__            | 类的方法名。                                                                            |     |
| \__NAMESPACE__         | 当前命名空间的名称。                                                                        |     |
| **`ClassName::class`** | 完整的类名。                                                                            |     |
|                        |                                                                                   |     |

## 表达式 和 运算符
PHP 是一种面向表达式的语言，从这一方面来讲几乎一切都是表达式，简单但却最精确的定义表达式的方式就是“任何有值的东西”。

```

+ - *  / % **
++ --
= += -= *= /= ....

```


**运算符**

算术运算符：+ - * / % ++ --
赋值运算符：= += -= *= /= %=
比较运算符：== === != <> !== < > <= >=
逻辑运算符：&& || !
位运算符：& | ^ ~ << >>
字符串运算符：.

## **流程控制** 
if 
if else 
elseif
switch
match
while
do while
for
foreach
declare
include
require_once
include_once
goto




### **数组**
$a = array（）；
函数：
- sort() - 对数组进行升序排列
- rsort() - 对数组进行降序排列
- asort() - 根据关联数组的值，对数组进行升序排列
- ksort() - 根据关联数组的键，对数组进行升序排列
- arsort() - 根据关联数组的值，对数组进行降序排列
- krsort() - 根据关联数组的键，对数组进行降序排列

**超级全局变量**
$GLOBALS  -包含一个引用指向每个当前脚本的全局范围内又要的变量
$_SERVER -web服务器或者直接与当前脚本的执行环境向关联
$_REQUEST - get post Cookie 机制提交到脚本的变量
$_POST  -由 post 方法提交到脚本的变量
$_GET   -由 get 方法提交到脚本的变量
$_FILES - 由HTTP post文件上传提交到脚本的变量
$_ENV - 执行环境提交到脚本的变量
$_COOKIE - 由HTTP cookies 方法提交至脚本的变量
$_SESSION - 当前注册给脚本会话的变量
## 表单处理
$\_GET(name) 获取get模式表单中的值
$\_POST(name) 获取post模式表单中的值

表单验证
empty（） 判空
ptrh_match（） 匹配正则表达式
