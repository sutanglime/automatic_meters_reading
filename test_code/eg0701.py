#boxclass

class Box1():
    '''求立方体的类'''
    def __init__(self,length1,width1,height1):
        self.length=length1
        self.width=width1
        self.height=height1
    def volume(self):
        return self.length*self.width*self.height


my_box1=Box1(10,10,10)
print('立方体的体积是%d'%(my_box1.volume()))
my_box2=Box1(15,7,11)
print('立方体的体积是%d'%(my_box2.volume()))
my_box3=Box1(5,10,12)
print('立方体的体积是%d'%(my_box3.volume()))


tt=my_box1.length
print(tt)

#
