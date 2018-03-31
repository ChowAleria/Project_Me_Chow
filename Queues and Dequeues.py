class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self,i):
        return self.items[i]


if __name__ =="__main__":

    kpop_actors = Queue()
    kpop_actors.enqueue("Ji Chang Wook")
    kpop_actors.enqueue("Yoo Seung Ho")
    kpop_actors.enqueue("So Ji Sub")
    kpop_actors.enqueue("Yoo Jae Suk")
    print kpop_actors.items

    kpop_actors.dequeue()
    kpop_actors.dequeue()
    print kpop_actors.items