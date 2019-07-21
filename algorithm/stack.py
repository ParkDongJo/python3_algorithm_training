class Stack:
    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)
    
    def pop(self):
        self.list.pop()

    def size(self):
        return len(self.list)