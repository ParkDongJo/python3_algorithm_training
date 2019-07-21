class Queue:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)
    
    def pop(self):
        self.list.pop(0)

    def size(self):
        return len(self.list)