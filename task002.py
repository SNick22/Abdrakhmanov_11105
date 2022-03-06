class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def __str__(self):
        output = ''
        cur_node = self.head
        while cur_node != None:
            if cur_node.get_next() == None:
                output += str(cur_node.get_value())
            else:
                output += str(cur_node.get_value()) + ' -> '
            cur_node = cur_node.get_next()
        return output

    def __len__(self):
        cur_node = self.head
        length = 0
        if cur_node == None:
            return length
        else:
            while cur_node != None:
                length += 1
                cur_node = cur_node.get_next()
        return length

    def pop(self, index):
        if index == 0 and len(self) != 0:
            m = self.head.get_value()
            self.head = self.head.get_next()
            return m
        elif index > 0 and index < len(self):
            cur_node = self.head
            for i in range(index - 1):
                cur_node = cur_node.get_next()
            m = cur_node.get_next().get_value()
            cur_node.set_next(cur_node.get_next().get_next())
            return m
        elif len(self) == 0:
            raise Exception('pop from empty list')
        elif index >= len(self):
            raise Exception('pop index out of range')

    def count(self, value):
        count = 0
        cur_node = self.head
        while cur_node != None:
            if cur_node.get_value() == value:
                count += 1
            cur_node = cur_node.get_next()
        return count

    def append_list(self, lst: list):
        cur_node = self.head
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        for i in lst:
            cur_node.set_next(Node(i))
            cur_node = cur_node.get_next()

    def clear(self):
        self.head = None


class LinkedStack:
    def __init__(self):
        self.head = None

    def __len__(self):
        cur_node = self.head
        length = 0
        if cur_node == None:
            return length
        else:
            while cur_node != None:
                length += 1
                cur_node = cur_node.get_next()
        return length

    def __str__(self):
        output = ''
        cur_node = self.head
        while cur_node != None:
            if cur_node.get_next() == None:
                output += str(cur_node.get_value())
            else:
                output += str(cur_node.get_value()) + ' -> '
            cur_node = cur_node.get_next()
        return output

    def push(self, value):
        new_node = Node(value)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        new_node.set_next(self.head)
        self.head = new_node

    def pop(self):
        cur_node = self.head
        if len(self) == 1:
            elem = cur_node.get_value()
            self.head = None
            return elem
        elif len(self) == 0:
            raise Exception('stack is empty')
        else:
            elem = cur_node.get_value()
            self.head = cur_node.get_next()
            return elem

    def count(self, value):
        count = 0
        cur_node = self.head
        while cur_node != None:
            if cur_node.get_value() == value:
                count += 1
            cur_node = cur_node.get_next()
        return count

    def append_list(self, lst: list):
        for i in lst:
            a = Node(i)
            a.set_next(self.head)
            self.head = a

    def clear(self):
        self.head = None


class LinkedQuery:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        new_node.set_next(self.head)
        self.head = new_node

    def __len__(self):
        cur_node = self.head
        length = 0
        if cur_node == None:
            return length
        else:
            while cur_node != None:
                length += 1
                cur_node = cur_node.get_next()
        return length

    def __str__(self):
        output = ''
        cur_node = self.head
        while cur_node != None:
            if cur_node.get_next() == None:
                output += str(cur_node.get_value())
            else:
                output += str(cur_node.get_value()) + ' -> '
            cur_node = cur_node.get_next()
        return output

    def pop(self):
        if len(self) == 0:
            raise Exception('query is empty')
        elif len(self) == 1:
            res = self.head.get_next().get_value()
            self.head.set_next(None)
            return res
        else:
            cur_node = self.head
            while cur_node.get_next().get_next() != None:
                cur_node = cur_node.get_next()
            res = cur_node.get_value()
            cur_node.set_next(None)
            return res

    def count(self, value):
        count = 0
        cur_node = self.head
        while cur_node != None:
            if cur_node.get_value() == value:
                count += 1
            cur_node = cur_node.get_next()
        return count

    def append_list(self, lst: list):
        for i in lst:
            a = Node(i)
            a.set_next(self.head)
            self.head = a

    def clear(self):
        self.head = None


class LinkedDeque:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        cur_node = self.head
        length = 0
        if cur_node == None:
            return length
        else:
            while cur_node != None:
                length += 1
                cur_node = cur_node.get_next()
        return length

    def __str__(self):
        output = ''
        cur_node = self.head
        while cur_node != None:
            if cur_node.get_next() == None:
                output += str(cur_node.get_value())
            else:
                output += str(cur_node.get_value()) + ' <-> '
            cur_node = cur_node.get_next()
        return output

    def push_right(self, value):
        new_node = Node(value)
        cur_node = self.tail
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.set_prev(cur_node)
        cur_node.set_next(new_node)
        self.tail = new_node

    def push_left(self, value):
        new_node = Node(value)
        cur_node = self.head
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        cur_node.set_prev(new_node)
        new_node.set_next(cur_node)
        self.head = new_node

    def pop_right(self):
        if len(self) == 0:
            raise Exception('deque is empty')
        elif len(self) == 1:
            res = self.head.get_value()
            self.head = None
            self.tail = None
            return res
        else:
            res = self.tail.get_value()
            cur_node = self.tail.get_prev()
            self.tail = cur_node
            self.tail.set_next(None)
            return res

    def pop_left(self):
        if len(self) == 0:
            raise Exception('deque is empty')
        elif len(self) == 1:
            res = self.head.get_value()
            self.head = None
            self.tail = None
            return res
        else:
            res = self.head.get_value()
            cur_node = self.head.get_next()
            self.head = cur_node
            self.head.set_prev(None)
            return res

    def count(self, value):
        count = 0
        cur_node = self.head
        while cur_node != None:
            if cur_node.get_value() == value:
                count += 1
            cur_node = cur_node.get_next()
        return count

    def append_list_right(self, lst: list):
        for i in lst:
            self.push_right(i)

    def append_list_left(self, lst: list):
        for i in lst:
            self.push_left(i)

    def clear(self):
        self.head = None
        self.tail = None


class LinkedSet:
    def __init__(self):
        self.head = None

    def __len__(self):
        cur_node = self.head
        length = 0
        if cur_node == None:
            return length
        else:
            while cur_node != None:
                length += 1
                cur_node = cur_node.get_next()
        return length

    def __str__(self):
        output = ''
        cur_node = self.head
        while cur_node != None:
            if cur_node.get_next() == None:
                output += str(cur_node.get_value())
            else:
                output += str(cur_node.get_value()) + ' -> '
            cur_node = cur_node.get_next()
        return output

    def append(self, value):
        new_node = Node(value)
        cur_node = self.head
        if cur_node == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            if cur_node.get_value() == new_node.get_value():
                return
            cur_node = cur_node.get_next()
        if cur_node.get_value() != new_node.get_value():
            cur_node.set_next(new_node)

    def pop(self, index):
        if index == 0 and len(self) != 0:
            m = self.head.get_value()
            self.head = self.head.get_next()
            return m
        elif index > 0 and index < len(self):
            cur_node = self.head
            for i in range(index - 1):
                cur_node = cur_node.get_next()
            m = cur_node.get_next().get_value()
            cur_node.set_next(cur_node.get_next().get_next())
            return m
        elif len(self) == 0:
            raise Exception('pop from empty list')
        elif index >= len(self):
            raise Exception('pop index out of range')

    def append_list(self, lst: list):
        for i in lst:
            self.append(i)

    def clear(self):
        self.head = None


if __name__ == '__main__':
    mySet = LinkedSet()
    mySet.append(1)
    mySet.append(2)
    mySet.append(2)
    mySet.append(3)
    mySet.append(4)
    mySet.append(2)
    mySet.append_list([1,2,3,4,5,6,7,8,9,0])
    print(mySet.pop(2))
    print(str(mySet))


