from tkinter import *
from quizzer import Quizzer
from random import randrange
import time

class Zetamac(Quizzer):
    def init_state(self):
        self.addn_spec = [(2,101),(2,101)]
        self.multn_spec = [(2,13),(2,101)]

    def next_problem(self):
        self.input_box.delete(0, END)
        self.tic = time.time()
        self.problem_bar.configure(text = self.sample())

    def input_callback(self, var, idx, mode):
        if self.input_var.get().isdigit():
            v = int(self.input_var.get())

            if v == self.answer:
                self.solved_ctr += 1
                self.next_problem()

    def sample(self):
        # Grab pairs uniformly out of the distr,
        # return a string to display
        c = randrange(0,4)
        if c == 0:
            a,b = randrange(*self.addn_spec[0]), randrange(*self.addn_spec[1])
            self.answer = a + b
            return ' + '.join((str(a), str(b)))
        elif c == 1:
            a,b = randrange(*self.addn_spec[0]), randrange(*self.addn_spec[1])
            c = a + b
            self.answer = a
            return ' - '.join([str(c), str(b)])
        elif c == 2:
            a,b = randrange(*self.multn_spec[0]), randrange(*self.multn_spec[1])
            self.answer = a * b
            return ' * '.join([str(a), str(b)])
        elif c == 3:
            a,b = randrange(*self.multn_spec[0]), randrange(*self.multn_spec[1])
            self.answer = a
            return ' / '.join([str(a*b), str(b)])
    
    def save_trial(self):
        pass

class TimesTables(Quizzer):
    def init_state(self):
        self.lmult_spec = (1,26)
        self.rmult_spec = (1,26)

    def next_problem(self):
        self.input_box.delete(0, END)
        self.tic = time.time()
        self.problem_bar.configure(text = self.sample())

    def input_callback(self, var, idx, mode):
        if self.input_var.get().isdigit():
            v = int(self.input_var.get())
            if v == self.answer:
                self.solved_ctr += 1
                self.next_problem()

    def sample(self):
        a,b = randrange(*self.lmult_spec), randrange(*self.rmult_spec)
        self.answer = a * b
        return ' * '.join([str(a), str(b)])

    def save_trial(self):
        pass

class RapidAddition(Quizzer):
    def init_state(self):
        self.save_profile = self.numeracyapp.profiles['rapidaddition']
        self.curr_run = []
        self.laddn_spec = (1,1000)
        self.raddn_spec = (1,1000)

    def next_problem(self):
        self.input_box.delete(0, END)
        self.tic = time.time()
        self.problem_bar.configure(text = self.sample())

    def input_callback(self, var, idx, mode):
        if self.input_var.get().isdigit() and int(self.input_var.get()) == self.answer:
            self.solved_ctr += 1
            
            # Items to be logged after trial is over
            problem = self.problem
            answer = self.answer
            meta = -1
            elapsed = time.time() - self.tic


            self.curr_run.append((problem, answer, meta, elapsed))
            print('curr_run len', len(self.curr_run))
            
            self.next_problem()
    
    def sample(self):
        a,b = randrange(*self.laddn_spec), randrange(*self.raddn_spec)
        self.problem = a,b
        self.answer = a + b
        return ' + '.join([str(a), str(b)])

    def save_trial(self):
        pass


