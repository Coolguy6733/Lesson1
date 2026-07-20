class myClass:
    __privatevar = 27
    def __privMeth(self):
        print("I'm inside a class my class")

    def hello(self):
        print("Private Variable value:", myClass.__privatevar)

foo = myClass()
foo.hello()
foo.__privMeth