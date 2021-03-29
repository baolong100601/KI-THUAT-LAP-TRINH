class A:
    def _init_(self):
        self.x=1
        self._y=1
    def getY(self):
        return self._y
a=A()
a.x=45
print(a.x)
