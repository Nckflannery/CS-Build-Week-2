class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.storage = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.head == None:
          self.head = x
        self.storage.append(x)
        self.tail = x

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        out = self.head
        del self.storage[0]
        if self.storage:
          self.head = self.storage[0]
        else:
          self.head = None
        return out

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.head

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.storage:
          return False
        else:
          return True