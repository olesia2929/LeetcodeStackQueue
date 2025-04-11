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
        
        Push element x onto stack."""
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.empty():
            return None
        return self.q1.pop(0)

    def top(self):
        if self.empty():
            return None
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0