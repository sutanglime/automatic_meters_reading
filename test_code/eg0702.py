#property_BoxClass

class Color1():
    def __init__(self,index=0):
        self.set_color=['white','red','black','green','pink','yellow','oringe','puper','blue']
        self.index=index
    def setColor(self):
        return self.set_color[self.index]

class Box1():
    '''求立方体的类'''
    def __init__(self,length1,width1,height1,c1=0):
        self.length=length1
        self.width=width1
        self.height=height1
        self.color0=Color1(c1).setColor()
    def volume(self):
        return self.length*self.width*self.height

my_box1=Box1(10,10,10,5)
print(my_box1.color0)
