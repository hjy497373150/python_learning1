class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.'% self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)
def main():
    stu1 = Student('何涌硕', 8)
    stu1.study('python程序设计')
    stu1.watch_movie()
    stu2 = Student('胡晋源', 21)
    stu2.study('C++程序设计')
    stu2.watch_movie()

if __name__ == '__main__':
    main()

