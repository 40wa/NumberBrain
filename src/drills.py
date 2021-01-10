from tkinter import *
from quizzer import Quizzer
from random import randrange
import time
import numpy as np
import pandas as pd

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
        self.quiz_name = 'rapidaddition'
        if self.numeracyapp.profiles[self.quiz_name] is None:
            self.numeracyapp.profiles[self.quiz_name] = pd.DataFrame([],
                                                                     columns=[
                                                                        'problem',
                                                                        'answer', 
                                                                        'meta',
                                                                        'elapsed_runs',
                                                                        'mean',
                                                                        'variance'])

        self.save_profile = self.numeracyapp.profiles[self.quiz_name]

        self.curr_run = []
        self.laddn_spec = (1,10)
        self.raddn_spec = (1,10)

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
        print(self.save_profile)
        for t in self.curr_run:
            print(t)
        
        sp = self.save_profile

        for t in self.curr_run:
            t_problem = t[0]
            t_answer = t[1]
            t_meta = t[2]
            t_elapsed = t[3]

            # Has this pair been seen before?
            idx_search = sp.index[sp['problem'] == t_problem]
            if len(idx_search) == 0:
                # Not seen before
                print('not seen before')
                sp.loc[len(sp)] = [t_problem, t_answer, -1, [t_elapsed], t_elapsed, 0]
                 
            elif len(idx_search) == 1:
                # Seen before
                # Correct row:
                row = sp.iloc[idx_search[0]]

                runs = row['elapsed_runs']
                runs.append(t_elapsed)
                if len(runs) > 10:
                    runs = runs[-10:]
                row['mean'] = np.mean(runs)
                row['variance'] = np.var(runs)

                sp.iloc[idx_search[0]] = row

            else:
                raise Exception('Multiple rows with the same problem')

        if len(self.curr_run) > 0: 
            sp.sort_values(by=['answer', 'problem'])
            self.numeracyapp.save_savedata(self.quiz_name)
            




