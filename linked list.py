class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    def size(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total +=1
            cur = cur.next
        return total
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print elems
    def get(self,index):
        if index >= self.size():
            print "ERROR: 'Get' Index out of range"
            return None
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index: return cur_node.data
            cur_index += 1
    def erase(self,index):
        if index >= self.size():
            print "ERROR: 'Erase' Index out of range"
            return
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1


if __name__ == '__main__':

    chowie =  LinkedList()
    chowie.append(5)
    chowie.append(25)
    chowie.append(125)
    chowie.append(298)
    chowie.append(15)

    chowie.display()
