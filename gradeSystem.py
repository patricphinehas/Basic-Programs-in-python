class student:
    student_count = 0
    # int(input("enter the number of students"))

    def __init__(self, name,m1,m2,m3,m4,m5):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        student.student_count += 1
    
    def displayCount(self):
        print("total number od students %d" % student.student_count)
    
    def displayMark(self): 
        print("Name : ", self.name)

    def gradeCheck(self):
        self.flag = 0
        if(self.m1<50) or (self.m2<50) or (self.m3<50) or (self.m4<50) or (self.m5<50):
            self.flag = 1
            print("has to re appear")
        
        else:
            self.total = self.m1+self.m2+self.m3+self.m4+self.m5
            self.avg = self.total/5
            if(self.avg>90):
                self.grade= "a"
            elif(self.avg>80):
                self.grade="b"
            elif(self.avg>70):
                self.grade="c"
            elif(self.avg>60):
                self.grade="d"
            else:
                self.grade="e"

        print(self.name, "has passed with ", self.grade, " and a total of ", self.total)
        
        
    
    # def gradeCheck(self):
    #     mark=[]
    #     n = int(input("enter the number of subjects"))
    #     for i in range(1, n+1):
    #         m = int(input("enter the mark"))
    #         mark.append(m)

while(1):
    name=input("enter the student name")
    m1 = int(input("enter the mark for subject 1"))
    m2 = int(input("enter the mark for subject 2"))
    m3 = int(input("enter the mark for subject 3"))
    m4 = int(input("enter the mark for subject 4"))
    m5 = int(input("enter the mark for subject 5"))
    st1 = student(name,m1,m2,m3,m4,m5)
    
    st1.displayMark()