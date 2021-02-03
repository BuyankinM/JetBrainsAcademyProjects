class Stack():

    def __init__(self):
        self.data = []

    def push(self, el):
        self.data.append(el)

    def pop(self):
        last_elem = self.data[-1]
        self.data = self.data[:-1]
        return last_elem

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return not self.data
