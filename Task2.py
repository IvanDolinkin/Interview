from Task1 import Stack

brackets = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}',
    '}{}',
    '{{[(])]}}',
    '[[{())}]',
    '[([])((([[[]]])))]{()}'
]


def main(kit):
    stack = Stack()
    if len(kit) % 2 != 0:
        return 'Несбалансированно'
    for bracket in kit:
        if bracket in '([{':
            stack.push(bracket)
        elif bracket == ')':
            if stack.pop() == '(':
                continue
            else:
                return 'Несбалансированно'
        elif bracket == ']':
            if stack.pop() == '[':
                continue
            else:
                return 'Несбалансированно'
        elif bracket == '}':
            if stack.pop() == '{':
                continue
            else:
                return 'Несбалансированно'
    return 'Сбалансированно'


if __name__ == '__main__':
    for kit in brackets:
        print(kit)
        print(main(kit))
