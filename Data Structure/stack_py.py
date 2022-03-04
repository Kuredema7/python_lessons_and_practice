class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def print_stack(self):
        print(self.items)

    def balanced(self, item):
        for val in item:
            if val == '(':
                self.push(val)
            elif val == ')':
                if self.is_empty():
                    return False
                self.pop()

        if self.is_empty():
            return True
        else:
            return False


exp_one = Stack()
# expression = '(x+y)*(x-z)-9'
expression = '(a() eee))'

print(exp_one.balanced(expression))
# exp_one.print_stack()
