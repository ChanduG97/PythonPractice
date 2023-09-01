class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Create a stack
stack = Stack()
# User input loop
while True:
    user_input = input("Enter an item to push onto the stack (or 'no' to stop): ")
    if user_input.lower() == 'no':
        break
    stack.push(user_input)
    print("Item added to the stack.")
print("Stack size:", stack.size())
# Pop and print items until the stack is empty
print("Items popped from the stack:")
while not stack.is_empty():
    popped_item = stack.pop()
    print(popped_item)
