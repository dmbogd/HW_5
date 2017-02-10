# HW_5
#1
import random

'''
Написать списковые выражения, которые:
a. создают список из строк всех нечетных чисел от 1 до 100
b. создают список из объектов другого списка, кроме итерируемых
c. создают список из фразы 'The quick brown fox jumps over the lazy dog',
где каждый объект списка - кортеж из: слова в верхнем регистре, слова
в случанйном регистре (qUIcK) и длины слова
'''

odd_numbers = [str(x) for x in range(1, 100, 2)]
print(odd_numbers)


input_list = [123, 'abc', [0, 1, 2], ('a', 'b'), 456]
not_iter_items = [x for x in input_list if not hasattr(x, '__iter__')]
print(not_iter_items)

phrase = 'The quick brown fox jumps over the lazy dog'
formatted_phrase = [(x.upper(), ''.join([random.choice([y.upper(), y.lower()])
                    for y in x]), len(x)) for x in phrase.split()]
print(formatted_phrase)

#2

class IntToStr(object):

    def __init__(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError('You can sum only integers and/or strings')
        self.value = value

    def __add__(self, value):
        if isinstance(value, str):
            return str(self.value) + value
        else:
            return self.value + value

    def __radd__(self, value):
        if isinstance(value, str):
            return value + str(self.value)
        else:
            return value + self.value

n1 = IntToStr(9.2)
print(n1 + 3)
print('a' + n1)
print(n1 + 'z')

#3

class Stack(object):

    def __init__(self):
        self.list = []

    def push_method(self, value):
        self.list.append(value)

    def pop_method(self):
        if self.list == []:
            raise IndexError('The stack is empty!')
        else:
            stack_index = len(self.list) - 1
            self.list.pop(stack_index)


# данные для проверки работы программы:
object1 = Stack()
object1.push_method(3)
object1.push_method('five')
object1.push_method(5)
object1.push_method('six')

print(object1.list)
object1.pop_method()
print(object1.list)

object2 = Stack()
print(object2.list)
object2.pop_method()
print(object2.list)
