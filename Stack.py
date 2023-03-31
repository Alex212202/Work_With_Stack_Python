import numpy as np

class Stack:
    stck = np.arange(21)
    tos = int(0)
    def Stack(self):
        self.tos = -1
    def push(self, item):
        if self.tos == 20:
            print('Стек заполнен')
        else:
            self.tos += 1
            self.stck[self.tos] = item
    def pop(self):
        if self.tos < 0:
            print('Стек не полный')
        else:
            self.tos -= 1
            return self.stck[self.tos]