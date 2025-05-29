condition = True
while condition:
                
                
                print("Are you a student?")
                entry = input("Enter yes/no: ")
                if entry == "yes":
                    class Student:
                        def __init__(self, name, age, grade):
                            self.name = name
                            self.age = age
                            self.grade = grade
                        def __str__(self):
                            return f"{self.name}"    
                            
                    name_entry = input("Enter your name: ")
                    age_entry = input("Enter your age: ")
                    grade_entry = input("Enter your grade: ")
                    
                    student_entry = Student(name=name_entry, age=age_entry, grade=grade_entry)
                    STUDENT_INFO = {
                        "name" : name_entry,
                        "age" : age_entry,
                        "grade" : grade_entry
                        }
                    
                    # STUDENT.append(STUDENT_INFO)
                    with open ("studentlog.txt", "a")  as file:
                        file.write(f"{student_entry}    {age_entry}     {grade_entry}\n")

                    
                    
                    print(f"Hello, {student_entry} \n welcome to tokyo high")
                    print("Do you want to add more students?")
                    con_input = input("Please, Enter yes/no: ")
                    if con_input  == "no":
                        print("Thanks for having us")
                        condition = False
                        exit()
                    if con_input == "yes":
                          condition = True
                    else:
                          print("message unclearified")
            
                
                elif entry == "no":
                    print("sorry only students are allowed") 
                    exit()
                else:
                      print("command not found") 
                      exit()