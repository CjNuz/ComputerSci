from tkinter import * 

class Student ():
    
    def __init__(self, name):
        self.first_name = "Tushan"

    def display_name(self):
        print(self.first_name)
    
    def set_grade(self, grade):
        self.grade = grade 

    def get_grade(self):
        return self.grade
    
def show_grade():
    grade_label.config(text=csc_level_2[1].get.grade())
    pass


csc_level_2 = []

csc_level_2.append(Student("Shauryya"))
csc_level_2[0].set_grade("Merit")


window =Tk()
window.geometry("500x500")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()