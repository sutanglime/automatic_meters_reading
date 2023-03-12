#inher_BoxClass

class Box1():
    '''求立方体的类'''
    def __init__(self,length1,width1,height1):
        self.length=length1
        self.width=width1
        self.height=height1
    def volume(self):
        return self.length*self.width*self.height

class Box2(Box1):                                                   #继承Box1定义子类Box2
    def __init__(self,length1,width1,height1):
        super().__init__(length1,width1,height1)        #super实现父类与子类的关联
        self.color='white'
        self.material='paper'
        self.type='fish'
    def area(self):
        re=self.length*self.width+self.length*self.height+self.width*self.height
        return re*2
    '''在子类中重写方法，只要求函数名称与父类保持一致'''
    def volume(self,num=1):
        return self.length*self.width*self.height*num

my_box2=Box2(10,10,10)
print('立方体的体积是%d'%(my_box2.volume()))
print('7个立方体的体积是%d'%(my_box2.volume(7)))
print('立方体的表面积是%d'%(my_box2.area()))
print('Box颜色%s，材质%s，类型%s'%(my_box2.color,my_box2.material,my_box2.type))
