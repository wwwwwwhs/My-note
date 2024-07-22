<!--
 * @Author: 崩布猪
 * @Date: 2024-04-12 14:11:28
 * @LastEditors: 崩布猪
 * @LastEditTime: 2024-04-16 09:13:19
 * @FilePath: \P_code\Py_base\class.md
 * @Description: 
 * 
-->
# 类
类是面向对象编程（OOP）的核心概念。类是一组数据和函数的集合，用来描述一个对象的属性和行为。类可以创建实例，每个实例都拥有自己的属性值和方法。类可以继承其他类，从而扩展其功能。类可以被多态地使用，即一个方法可以有不同的实现，具体使用哪个实现取决于运行时环境。

实例化
跟据类创建的对象成为实例化

## 创建类和实用类
创建Dog类：

```python
class Dog:
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        self.Xb = man # 给属性指定默认值
              
    def  sit（self）：
        print(self.name + " is now sitting.")

    def  roll_over（self）：

# 创建实例化对象
my_dog = Dog("Buddy", 3)
print(f"My dog's name is {my_dog.name} and age is {my_dog.age}.")
```

## 修改属性的值

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        # --snip--
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值，如果新值比当前值小，则打印一条警告消息。
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """
        将里程表读数增加指定的量。
        """
        self.odometer_reading += miles
# 创建实例化对象
my_new_car = Car("Toyota", "Corolla", 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 修改属性的值 直接修改
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 修改属性的值 调用方法
my_new_car.update_odometer(45)
my_new_car.read_odometer()

# 通过方法堆属性的值进行递增
my_new_car.increment_odometer(10)
my_new_car.read_odometer() 

```

## 继承
一个类继承另一个类，可以获得另一个类的所有属性和方法。

```python
    class Car:
      """一次模拟汽车的简单尝试。"""

      def __init__(self,make,model,year):
          self.make = make
          self.model = model
          self.year = year
          self.odometer_reading = 0

      def get_descriptive_name(self):
          long_name = f"{self.year} {self.make} {self.model}"
          return long_name.title()

      def read_odometer(self):
          print(f"This car has {self.odometer_reading} miles on it.")

      def update_odometer(self,mileage):
          if mileage >= self.odometer_reading:
              self.odometer_reading = mileage
          else:
              print("You can't roll back an odometer!")

      def increment_odometer(self,miles):
          self.odometer_reading += miles

    class ElectricCar(Car):
      """电动汽车的独特之处。"""

      def __init__(self,make,model,year):
          """初始化父类的属性。
          在初始化子类属性"""
          super().__init__(make,model,year)
          self.battery_size = 70

      def describe_battery(self):
          """打印电瓶容量"""
          print(f"This car has a {self.battery_size}-kWh battery.")
      # 重写父类的方法 子类中定义一个与要重写的父类方法同名的方法
      def read_odometer(self):
          """电动汽车没有里程表，所以打印一条消息并返回None"""
          print("This car doesn't have a meter.")
          return None

# 创建实例化对象
my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
```

