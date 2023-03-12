#staticclass.py

class StaticC():
    name='Tom'
    age=20
    address='China'
    call=28380000
    def a():
        i=0
        i+=1
        print('第一个函数%d'%(i))
    def b(add=1):
        print('第二个函数%d'%(add))
    def c(add=1):
        print('第三个函数%d'%(add))
        return add


print('name:%s'%(StaticC.name))
print('age:%d'%(StaticC.age))
print('address:%s,call:%d'%(StaticC.address,StaticC.call))
print(StaticC.a())
print(StaticC.b(3))
print(StaticC.c(5))
