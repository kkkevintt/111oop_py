from typing import Any

class Student:      
    def __init__(self,name,ID):
        self.name = name 
        self.ID = ID 
        self.grades = []
        
    def add_grade(self , grade):
        self.grades.append(grade)

    def average_grade(self):
        #回傳平均值
        if len(self.grades) == 0:
            return 0
        return sum(self.grades ) / len(self.grades)
    
def main():        
    #三學生
    student1 = Student("kevin ",1)
    student2 = Student("tom ",2)
    student3 = Student("mike ",3)
    #add grades 
    student1.add_grade(85)
    student2.add_grade(92)
    student3.add_grade(78)  

    student1.add_grade(85)
    student2.add_grade(45)
    student3.add_grade(56)  
    #print                                
    print(f"{student1.name } average grade is :{student1.average_grade()} ")
    print(f"{student2.name } average grade is :{student2.average_grade()} ")
    print(f"{student3.name } average grade is :{student3.average_grade()} ")


if __name__ == "__main__":
    main()