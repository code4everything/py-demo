# coding:utf-8


# 类中定义的方法一个参数永远是实例变量 self ，在调用时不要传递该参数
class Student(object):
    # 类属性，所有实例均可访问
    id = 12847347

    def __init__(self, name, score):
        self.name = name
        # 对象私有，外部无法访问
        self.__score = score
        # 私有变量，外部可访问，但不推荐外部访问
        self._see = True

    def print_score(self):
        print('%s: %s' % (self.name, self.__score))

    def __len__(self):
        """
        自定义长度
        """
        return 99


ming = Student('xiao', 89)
print(ming, ming._see)
ming.name = 'xiao ming'
ming.print_score()
print(Student.id, ming.id)
print('class length:', len(ming))


class Animal(object):
    def run(self):
        print('animal is running')


class Cat(Animal):
    def eat(self):
        print('cat is eating')


class Dog(Animal):
    # 覆盖父类方法
    def run(self):
        print('dog is running')


animal = Dog()
animal.run()
cat = Cat()
cat.run()
cat.eat()

# 判断对象类型
print(type(animal) == type(cat))
print(isinstance(cat, Animal))
# 列出对象的属性和方法
print(dir(cat))
