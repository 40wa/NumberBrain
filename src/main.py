import drills
from util import *

from functools import partial
import os
from tkinter import *
import pandas as pd 

class NumeracyApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('NumberBrain')
        self.root.geometry('640x480')
        self.root['background']='grey'
        self.current_menu = None

        # A dictionary of menus, name to frame
        self.menus = dict()
        self.menus['main'] = self.init_main()

        # Load in data from all profiles, settings etc
        self.savedata = self.load_savedata()
    
        self.display_menu('main')
        self.root.mainloop()

    def display_menu(self, targmenu=None, clean=None):
        # First purge the previous menu from view
        if self.current_menu:
            self.menus[self.current_menu].grid_remove()
        
        if not clean:
            # Then onboard the target menu as desired
            self.menus[targmenu].grid()
            self.current_menu = targmenu

    def load_savedata(self):
        # for now, we only have a single profile for the addition
        SAVEDIR = './profiles'
        self.profiles = dict()
        self.settings = dict()
        self.profiles['rapidaddition'] = try_load(SAVEDIR, 'rapidaddition.csv')
        self.profiles['timestable'] = try_load(SAVEDIR, 'timestable.csv')
        self.profiles['zetamac vanilla'] = try_load(SAVEDIR, 'zetamac_vanilla.csv')

    def save_savedata(self, name):
        SAVEDIR = './profiles'
        if name in self.profiles:
            self.profiles[name].to_csv(os.path.join(SAVEDIR, name + '.csv'), index=False)
        else:
            raise Exception('Attempting to save a nonexistent profile')


    def init_main(self):
        ret = Frame(self.root)
        
        # Drills menu items
        drills_menu = Frame(ret)
        drills_menu.grid(column=0, row=0)

        drills_header = Label(drills_menu, text='DRILLS', font=('Arial Bold', 30), bg='orange')
        drills_header.pack(side=TOP, fill=X, expand=YES)

        timestable = Button(drills_menu,
                            text='times table',
                            font=('Arial Bold', 20),
                            command=partial(drills.TimesTables, self))
        addition = Button(drills_menu,
                          text='rapid addition',
                          font=('Arial Bold', 20),
                          command=partial(drills.RapidAddition, self))
        zetamac = Button(drills_menu, text='zetamac vanilla', font=('Arial Bold', 20), command=partial(drills.Zetamac, self))

        timestable.pack(side=TOP)
        addition.pack(side=TOP)
        zetamac.pack(side=TOP)

        # Analysis Menu items 
        analysis_menu = Frame(ret)
        analysis_menu.grid(column=1, row=0)

        analysis_header = Label(analysis_menu, text='ANALYSIS', font=('Arial Bold', 30))
        analysis_header.pack(side=TOP)

        return ret

if __name__=='__main__':
    NumeracyApp()
