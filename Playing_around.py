class A:
    def a(self):
        print("I am A")

class B:
    def b(self):
        print("I am B")

class C(A):
    A().a()



c = C()


