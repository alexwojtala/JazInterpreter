from error_handler import GenerateError

class Stack:
        def __init__(self):
                self.data = []

        def Push(self, argument):
            self.data.insert(0, argument)

        def Pop(self):
            if len(self.data) > 0:
                return self.data.pop(0)
            else:
                GenerateError("Stack Underflow")
