from tkinter import * 

class Student ():
    
    def __init__(self, name):
        self.first_name = name

    def display_name(self):
        print(self.first_name)
    
    def set_grade(self, grade):
        self.grade = grade 

    def get_grade(self):
        return self.grade
    
def show_grade():
    grade_label.config(text=csc_level_2[0].get_grade())

csc_level_2 = []

csc_level_2.append(Student("Shauryya"))
csc_level_2[0].set_grade("Merit")
csc_level_2.append(Student("Thusan"))
csc_level_2[0].set_grade("Not Achieve")

window =Tk()
window.title("Students Grade")
window.geometry("500x500")

students_listbox = Listbox(window)
students_listbox.pack()
students_listbox.insert(1, "Shauryya")
students_listbox.insert(2, "Thusan")

#student_list = ["Achive", "Merit", "Excellence"]

#for item in student_list:
    #students_listbox.insert(END, item)

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()