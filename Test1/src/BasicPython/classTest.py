class myClass():
    def method1(self):
        print ("myClass method1")

    def method2(self, someString):
        print ("myClass method2: " + someString)

class class2(myClass):
    def method1(self):
       myClass.method1(self)
       print("Yolo")


# exercise the class methods



c = myClass()
c.method1()
c.method2("This is a string")

d = class2()
d.method1()