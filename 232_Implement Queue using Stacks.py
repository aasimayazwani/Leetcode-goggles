class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.item = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.item.insert(0,x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.item.pop(-1)
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.item[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.item == []   