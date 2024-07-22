<!--
 * @Author: 崩布猪
 * @Date: 2024-04-13 09:10:15
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-04-17 16:27:13
 * @FilePath: \CCCC\fangfa.md
 * @Description: 
 * 
-->
# 方法
方法在类或结构中声明，声明时需要指定修饰符、返回类型、方法名、参数列表。方法的作用是用于实现特定功能。方法可以有参数、返回值、异常处理、访问修饰符、重载、可见性等。

定义格式
<访问修饰符> <返回类型> <方法名>(<参数列表>)
{
    // 方法体
}

访问修饰符：
- public：公共访问，可以在任何地方访问
- protected：受保护访问，只能在类或派生类中访问
- private：私有访问，只能在类内部访问
- internal：内部访问，只能在当前程序集中访问
- abstract：抽象方法，不能创建实例，只能在派生类中实现
- static：静态方法，不需要实例化就可以调用
```csharp

public class MyClass
{

    //定义字段
    // 字段是类的成员变量，用于存储数据
    // 字段可以是任何类型，包括值类型和引用类型
    private int field1; //私有字段 默认私有访问
    public string field2;



    // 构造函数
    // 在创建指定类型的对象时，系统会自动调用构造函数来初始化对象
    public MyClass()
    {
        // 构造函数体
    }



    // 析构函数 
    // 系统调用析构函数来释放资源，当对象不再被使用时，系统会自动调用析构函数来释放资源
    // 析构函数不能有返回值，不能有参数
    // 析构函数不能被重写
    // 命名规则 ~<类名>
    ~MyClass()
    {
        // 析构函数体
    }



    // 静态字段 和 静态方法
    // 静态字段是类中所有对象的共享变量，静态方法是不需要实例化就可以调用的方法。
    // 静态字段和静态方法的访问修饰符只能是 public 或 static。
    public static int field3;
    public static void Method2()
    {
        // 方法体
    }



    // 属性
    // 属性是类的成员变量，用于封装数据和操作数据的方法。
    // 属性可以有 getter （获取） 和 setter （设置） 方法，也可以只读属性。
    // 属性的访问修饰符只能是 public 或 protected。
    public int Property1
    {
        get
        {
            // getter 方法体
            return 0;
        }
        set
        {
            // setter 方法体
        }
    }
    
    // 自动实现的属性
    public int Property2 { get; set; }
    Property2 = 10;
    Console.WriteLine(Property2); // 输出 10



    // 方法
    // 方法是类的成员函数，用于实现功能。
    // 方法可以有参数、返回值、异常处理、访问修饰符、重载、可见性等。
    public void Method1()
    {
        // 方法体
    }

    // 方法参数类型 
    // 值参数 实参的值复制到形参中，修改形参的值不会影响实参的值。 ref int a
    // 引用参数 形参 化作 实参的别名，修改形参的值会影响实参的值。 out int b
    // 输出参数 从方法体内把数据传出到调用代码
    // 参数数组 多个实参对应一个特殊的形参 parms int[]c   
    // 可选参数 形参可以不指定实参，系统会自动分配默认值。 int num = 10;
    // this 关键字 指向当前对象的引用。
    // 调用时
   

    
    // 方法重载
    // 方法重载是指在一个类中，存在多个名称相同的方法，但是参数列表不同。
    // 系统根据调用方法时传入的参数列表，自动调用匹配的重载方法。
    public void Method3(int num)
    {
        // 方法体
    }

    public void Method3(string str)
    {
        // 方法体
    }

    // 运算符重载
    // 运算符重载是指在一个类中，存在多个名称相同的运算符，但是参数列表不同。
    // 系统根据调用运算符时传入的参数列表，自动调用匹配的重载运算符。
  
    
    // 对象的复制
    // 潜复制 通过MemberwiseClone 方法实现
    // 深复制 通过序列化实现
    // 注意：深复制会消耗更多的资源，应谨慎使用。

    // 嵌套类
    // 嵌套类是指在一个类中定义另一个类。
    // 嵌套类可以访问外部类的成员，但外部类不能访问嵌套类的成员。
    public class NestedClass
    {
        // 嵌套类定义
    }

    // 索引器
    // 索引器是指在一个类中定义一个特殊的属性，该属性可以根据索引值获取或设置值。
    // 索引器可以有多个参数，也可以没有参数。
    // 索引器的访问修饰符只能是 public 或 protected。
    public int this[int index]
    {
        get
        {
            // getter 方法体
            return 0;
        }
        set
        {
            // setter 方法体
        }
    }
    
    // 非整型索引器
    // 非整型索引器可以根据任意类型的值作为索引值。
    // 非整型索引器的访问修饰符只能是 public 或 protected。
    public string this[string key]
    {
        get
        {
            // getter 方法体
            return "";
        }
        set
        {
            // setter 方法体
        }
    }


}

```
## 命名空间
命名空间是用来解决命名冲突的问题。在C#中，命名空间是通过命名空间声明来实现的。命名空间声明必须位于源文件的开头，并且必须在所有其他代码之前。
在C#中 采用命名空间来管理多个类

命名空间声明格式：
```csharp
// 使用 uning 关键字声明命名空间
using System;
namespace MyNamespace
{
    // 类定义
    class program
    {
        static void Main(string[] args)
        {
            // 代码
        }
    }
}
由于 Main类包含在system中 所以通过引入system命名空间
// 调用命名空间中的类
MyNamespace.MyClass obj = new MyNamespace.MyClass();
// 也可以使用 using 关键字导入命名空间中的类
using MyNamespace;
MyClass obj = new MyClass();

// 自定义命名空间
namespace MyNamespace
{
    public class MyClass
    {   
        // 类定义
    }
}
```


## 委托
委托是一种引用类型，用于封装方法。
委托可以有参数、返回值、异常处理、访问修饰符等。
声明委托格式：
[修饰符] delegate 返回类型 委托类型名字(参数列表);     
```csharp
    // 声明委托
    public delegate void MyDelegate(int num);
    // 实例化委托
    MyDelegate myDelegate = new MyDelegate(Method1);
    myDelegate(10); // 调用委托

```

## 事件
事件是一种通知机制，用于在对象状态发生变化时通知其他对象。
声明事件格式：
[修饰符] event 事件类型 事件名字;
```csharp
    // 声明事件
    public event MyDelegate MyEvent;
    // 实例化事件
    MyEvent += Method1;
    MyEvent -= Method1;
    // 触发事件
    MyEvent(10);
```