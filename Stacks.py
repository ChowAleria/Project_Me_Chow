#ALERIA, MADEL S.
#Stacks(7)

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(1, item)

    def pop(self):
        return self.items.pop(1)

    def peek(self):
        return self.items[3]

    def size(self):
        return len(self.items)

s = Stack()
print(s.isEmpty())
s.push('1')
s.push('2')
s.push('3')
s.push('4')
s.push('5')
s.push('6')

print(s.peek())
print (s.size())
print (s.isEmpty())

s.push("mo more push")
print(s.pop())
print (s.size())