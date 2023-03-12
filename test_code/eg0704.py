#Class_private

class TeatPrivate():
    def __init__(self):
        self.__say='ok'
    def p(self):
        print(self.__say)
    def __p1(self):
        print(self.__say)

show=TeatPrivate()
show.p()
