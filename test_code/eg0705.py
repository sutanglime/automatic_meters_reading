#Main_program_class_module

from Class_module import *

my_box2=Box2(10,10,10)
print('立方体的体积是%d'%(my_box2.volume()))
print('立方体的表面积是%d'%(my_box2.area()))
print('Box颜色%s，材质%s，类型%s'%(my_box2.color,my_box2.material,my_box2.type))
