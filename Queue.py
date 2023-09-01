class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_data

    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def print_queue(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.print_queue()         # Output: 10 -> 20 -> 30 -> None
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 10
print("Peek:", queue.peek())        # Output: Peek: 20
print("Is empty?", queue.is_empty())  # Output: Is empty? False
