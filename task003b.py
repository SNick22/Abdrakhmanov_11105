class Stack:
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        res = self.arr.pop()
        return res

    def peek(self):
        return self.arr[-1]

    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        return False


class Queue(Stack):
    def push(self, value):
        self.arr.insert(0, value)


string = input().split()
myStack = Stack()
myQueue = Queue()
for i in string:
    if i != '+' and i != '-' and i != '*' and i != '/' and i != '(' and i != ')':
        myQueue.push(i)
    if i == '+' or i == '-' or i == '*' or i == '/':
        if myStack.isEmpty() or myStack.peek() == '(':
            myStack.push(i)
            continue
        if (i == '*' or i == '/') and (myStack.peek() == '-' or myStack.peek() == '+'):
            myStack.push(i)
        elif i == '*' or i == '/':
            while myStack.peek() != '+' or myStack.peek() != '-' or myStack.peek() != '(':
                myQueue.push(myStack.pop())
                if myStack.isEmpty():
                    break
        else:
            while myStack.peek() != '(':
                myQueue.push(myStack.pop())
                if myStack.isEmpty():
                    break
            myStack.push(i)
    if i == '(':
        myStack.push(i)
    if i == ')':
        while myStack.peek() != '(':
            myQueue.push(myStack.pop())
        myStack.pop()
while not myStack.isEmpty():
    myQueue.push(myStack.pop())
output = ''
while not myQueue.isEmpty():
    output += myQueue.pop()
print(output)