
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
