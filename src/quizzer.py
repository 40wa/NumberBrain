from tkinter import *
import asyncio

class Quizzer:
    def __init__(self, timer, ctr, metadata, problem_bar, input_box):

        # Received for display
        self.timer = timer
        self.ctr = ctr
        self.metadata = metadata
        self.problem_bar = problem_bar
        self.input_box = input_box

        # Wire a StringVar to the input box for input checking
        self.input_var = StringVar()
        self.input_var.trace_add('write', self.input_callback)
        self.input_box.configure(textvariable = self.input_var)

        # Init for first problem
        self.next_problem()

    def input_callback(self, var, idx, mode):
        print("input callback CALLED")
        pass

    def next_problem(self):
        print('next problem CALLED')
        pass

