from tkinter import *
import random
names_list = []
global questions_answers
asked = []


# Dictionary has key of number (for each question number) and : the value for each is a list that has 7 items, so index 0 to 6
questions_answers = {
    1: ["What must you do when you see blue and red flashing lights behind you?", # item 1, index 0 will be the question
       'Speed up to get out of the way', # item 2, index 1 will be first choice
       'Slow down and drive carefully', # item 3, index 2 will be second choice 'Slow down and stop', # item 4, index 3 will be third choice
       'Drive on as usual',# item 5, index 4 will be fourth choice
       'Slow down and stop' # item 6, index 5 will be the write statement we need to display the right statement if the user enters wrong choice
       ,3], # item 7, index 6 will be the position of the right answer (index where right answer sits), this will be our check if answer is correct or no
    
    2: ["You may stop on a motorway only:", 'if there is an emergency', 'To let down or pick up passengers', 'to make a U-turn', 'to stop and take a photo',
        'if there is an emergency',1],
    3: ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?", "Speed up before the pedestrians cross",
        'Stop and give way to pedestrians on any part of the crossing', "Sound the horn on your vehicle to warn the perestrians", "slow down to 30kmh",
        'Stop and give way to pedestrians on any part of the crossing',2],
    4: ["Can you stop on a bus stop in a private motor vehicle?", 'Only between midnight and 6am", "Under no circumstances',
        "When dropping off passengers", 'Only if it is less than 5 minutes', "Under no circumstances", 2],
    5: ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)", '70 km/h',
       "100 km/h so you do not hold up traffic", "80 km/h and if the wheel spacer displays a lower limit that applies",
       "90 km/h", "80 km/h and if the wheel spacer displays a lower limit that applies", 3],
    6: ["When following another vehicle on a dusty road, you should: ", 'Speed up to get passed',
        "Turn your vehicle's windscreen wipers on", "Stay back from the dust cloud", 'Turn your vehicles headlights on', "Stay back from the dust cloud", 3],
    7: ["What does the sign containing the letters 'LSZ' mean", 'Low safety zone', "Low stability zone", "Lone star zone", 'Limited speed zone', 'Limited speed zone',4],
    8: ["What speed are you allowed to pass a school bus that has stopped to let students get on or off?", '20 km/h', "30 km/h", "70 km/h", '10 km/h', '20 km/h',1],

    9: ["What is the maximum distance a load may extend in front of a car?", '2 meters forward of the front edge of the front seat', "4 meters forward of the front edge of the front seat",
         '3 meters forward of the front edge of the front seat',3],
    10: ["To avoid being blinded by the headlights of another vehicle coming towards you what should you do?", 'Look to the left of the road', "Look to the centre of the road",
          "Wear sunglasses that have sufficient strength", 'Look to the right side of the road', 'Look to the left of the road',1],
}

def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


class QuizStarter:
    def __init__(self, parent):
        background_color="OldLace"
        #frame set up
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        #Label widget for our heading
        self.heading_label = Label (self.quiz_frame, text = "NZ Road Rules", font=("Tw Cen MT", "18", "bold"), bg=background_color)
        self.heading_label.grid(row=0)

        #Lbael for user name prompt
        self.user_label = Label ( self.quiz_frame, text="Please enter your name below", font=("Tw Cen MT", "16"), bg=background_color)
        self.user_label.grid(row=1, pady=20)

        #iser input is taken by an Entry widget
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2, pady=20)

        #contine button
        self.continue_button = Button (self.quiz_frame, text = "Continue", bg="blue", command=self.name_collection)
        self.continue_button.grid(row=3, pady=20)

    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        print(names_list)
        self.quiz_frame.destory()
        Quiz(root)

class Quiz:
    def __init__(self, parent):
        background_color="OldLace"
        #frame set up
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()
        #randomiser will randomly pick a question number which is qnum
        randomiser()

        #Label widget for our heading
        self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font=("Tw Cen MT", "18", "bold"), bg=background_color)
        self.question_label.grid(row=0, padx=10, pady=10)

        #holds the value of radio button
        self.var1=IntVar()


        #radio button 1
        self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
        self.rb1.grid(row=1, sticky=W)

        #radio button 2
        self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("helvetica", "12"), bg=background_color, value=2, variable=self.var1, pady=10)
        self.rb2.grid(row=2, sticky=W)

        #radio button 3
        self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("helvetica", "12"), bg=background_color, value=3, variable=self.var1, pady=10)
        self.rb3.grid(row=3, sticky=W)

        #radio button 4
        self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("helvetica", "12"), bg=background_color, value=4, variable=self.var1, pady=10)
        self.rb4.grid(row=4, sticky=W)

        #confirm answer button
        self.confirm_button = Button(self.quiz_frame, text="Confirm", bg="pink")
        self.confirm_button.grid(row=5)
        


#******************Starting point of program***********************#
randomiser()
if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    quizStarter_object = QuizStarter(root) #instantiation, making an instance of the class Quizstarter to create the fram with its widgets, passing root as
    root.mainloop()#so the window doesnt dissapear