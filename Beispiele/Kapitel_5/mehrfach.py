class A:

    def __init__(self):
        self.s = "A"

    def zeige(self):
        print("Zeige von A: self.s = ", self.s)


class B:

    def __init__(self):
        self.s = "B"

    def zeige(self):
        print("Zeige von B: self.s = ", self.s)


class AB(A,B):

    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def zeigeAB(self):
        print("Zeige von AB: self.s = ", self.s)
        self.zeige()


ab = AB()
ab.zeigeAB()
