class MyStack:
    """
    class
    """
    def __init__(self):
        """
        initializing.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        push element x onto stack.
        """
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1
    def pop(self):
        """
        get the top element and remove it from the stack.
        """
        if self.empty():
            return None
        return self.q1.pop(0)
    def top(self):
        """
        get the top element without removing it from the stack."""
        if self.empty():
            return None
        return self.q1[0]
    def empty(self):
        """
        return true if the stack is empty.
        """
        return len(self.q1) == 0
