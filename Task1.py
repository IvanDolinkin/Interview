# Нужно реализовать класс Stack со следующими методами:
class Stack:
    def __init__(self):
        self.stack = []

    # is_empty — проверка стека на пустоту. Метод возвращает True или False;
    def is_empty(self):
        return self.stack == []

    # push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
    def push(self, elem):
        self.stack.append(elem)

    # pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
    def pop(self):
        return self.stack.pop(-1) if not self.is_empty() else None

    # peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    # size — возвращает количество элементов в стеке.
    def size(self):
        return len(self.stack)


def test():
    some_object = Stack()
    print(some_object.is_empty())
    some_object.push(42)
    print(some_object.is_empty())
    [some_object.push(i) for i in range(10)]
    print(some_object.pop())
    print(some_object.peek())
    print(some_object.size())
    print(some_object.stack)


# test()
print()
