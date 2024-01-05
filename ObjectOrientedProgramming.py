
def simple_constructor():
    class Stack:  # Defining the Stack class.
        def __init__(self):  # Defining the constructor function.
            print("Hi!")


    stack_object = Stack()  # Instantiating the object.
# OUTPUT: Hi!



def object_w_property():
    class Stack:
        def __init__(self):
            self.stack_list = []


    stack_object = Stack()
    print(len(stack_object.stack_list))
# OUTPUT: 0



def private_property():
    class Stack:
        def __init__(self):
            self.__stack_list = []


    stack_object = Stack()
    print(len(stack_object.__stack_list))
# OUTPUT: AttributeError: 'Stack' object has no attribute '__stack_list'



def complete_stack():
    class Stack:
        def __init__(self):
            self.__stack_list = []


        def push(self, val):
            self.__stack_list.append(val)


        def pop(self):
            val = self.__stack_list[-1]
            del self.__stack_list[-1]
            return val


    stack_object = Stack()

    stack_object.push(3)
    stack_object.push(2)
    stack_object.push(1)

    print(stack_object.pop())
    print(stack_object.pop())
    print(stack_object.pop())
# OUTPUT: 
# 1
# 2
# 3
