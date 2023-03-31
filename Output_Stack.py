from Stack import Stack

class Output(Stack):
    mystck = Stack()
    mystck1 = Stack()

    for i in range(20):
        mystck.push(i)
    for i in range(10):
        mystck1.push(i)

    for i in range(10):
        print(mystck.pop())
    for i in range(10):
        print(mystck1.pop())

output = Output()
print(output)