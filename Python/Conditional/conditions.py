import random

class MyGrade:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
        
        if(grade >= 95):
            print( name + "'s grade was an 'A'")
        
        elif(grade < 95 and grade >= 90):
            print( name + "'s grade is a 'A-'")
        
        elif(grade < 90 and grade >= 86):
            print( name + "'s grade is a 'B+'")
        
        elif(grade < 86 and grade >= 83):
            print( name + "'s grade is a 'B'")
        
        elif(grade < 83 and grade >= 80):
            print( name + "'s grade is a 'B-'")
            
        elif(grade < 80 and grade >=76):
            print( name + "'s grade is a 'C+'")
            
        elif(grade < 76 and grade >= 73):
            print( name + "'s grade is a 'C'")
            
        elif(grade < 73 and grade >= 70):
            print( name + "'s grade is a 'C-'")
            
        elif(grade < 70 and grade >= 70):
            print( name + "'s grade is a 'C-'")
            
        elif(grade < 73 and grade >= 70):
            print( name + "'s grade is a 'C-'")
        
        elif(grade < 70 and grade >= 65):
            print( name + "'s grade is a 'D+'")
        
        elif(grade < 65 and grade >= 60):
            print( name + "'s grade is a 'D+'")
        
        else:
            print( name + "'s grade is a 'F'")
         

submission1 = MyGrade("Anthony", random.randrange(25, 100))
submission2 = MyGrade("Anthony", random.randrange(25, 100))
submission3 = MyGrade("Anthony", random.randrange(25, 100))



