from tkinter import *
import asyncio
from random import randrange

class Zetamac:
    # Class used to play vanilla/naive zetamac
    def __init__(self, timer,ctr, metadata, problem_bar, input_box):
        self.addn_spec = [(2,100),(2,100)]
        #self.subtn_spec 
        self.multn_spec = [(2,12), (2,100)]
        #self.divn_spec
        self.answer = None
    
        # Received for display
        self.timer = timer
        self.ctr = ctr
        self.metadata = metadata
        self.problem_bar = problem_bar
        self.input_box = input_box

        # Wire a stringvar to the input box for input checking
        self.input_var = StringVar()
        self.input_var.trace_add('write', self.input_callback)
        self.input_box.configure(textvariable = self.input_var)

        # Init for first problem
        self.next_problem()

    def input_callback(self, var, idx, mode):
        # Check whether the number can be parsed as an int
        if self.input_var.get().isdigit():
            v = int(self.input_var.get())

            if v == self.answer:
                self.next_problem()

    def next_problem(self):
        self.input_box.delete(0, END)
        next_prob = self.sample()
        self.problem_bar.configure(text = next_prob)


    def sample(self):
        # Grab pairs uniformly out of the distr,
        # return a string to display
        c = randrange(0,4)
        if c == 0:
            a,b = randrange(*self.addn_spec[0]), randrange(*self.addn_spec[1])
            self.answer = a + b
            return str(a) + ' + ' + str(b)
        elif c == 1:
            a,b = randrange(*self.addn_spec[0]), randrange(*self.addn_spec[1])
            c = a + b
            self.answer = a
            return str(c) + ' - ' + str(b)
        elif c == 2:
            a,b = randrange(*self.multn_spec[0]), randrange(*self.multn_spec[1])
            self.answer = a * b
            return str(a) + ' * ' + str(b)
        elif c == 3:
            a,b = randrange(*self.multn_spec[0]), randrange(*self.multn_spec[1])
            self.answer = a
            return str((a * b)) + ' / ' + str(b)

     
def zetamac(numeracyapp):

    # Clear previous menu
    numeracyapp.display_menu(clean=True)

    # Create elements
    zm_frame = Frame(numeracyapp.root, bg='red') 
    zm_header = Frame(zm_frame, bg='green')
    zm_header_ctr = Button(zm_header, text='CTR', font=('Arial Bold', 25))
    zm_header_timer = Button(zm_header, text='timer', font=('Arial Bold', 25))
    zm_header_ctr_right = Button(zm_header, text='hiscore, ma', font=('Arial Bold', 25))
    


    problem_bar = Label(zm_frame, text='gottem', font=('Helvetica', 40))
    input_box = Entry(zm_frame, font=('Helvetica', 20))

    # Hand to Zetamac to initialise values

    zm_engine = Zetamac(zm_header_timer,
                        zm_header_ctr,
                        zm_header_ctr_right,
                        problem_bar,
                        input_box)
    
    # Pack into place
    zm_frame.pack(fill=BOTH, expand=YES)
    zm_header.pack(side=TOP, fill=X)
    zm_header_timer.pack(side=LEFT, fill=X)
    zm_header_ctr.pack(side=LEFT, fill=X)
    zm_header_ctr_right.pack(side=RIGHT, fill=X)
    problem_bar.pack(side=TOP)
    input_box.pack(side=TOP)
    
