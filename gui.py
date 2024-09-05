#pylint: disable=not-callable
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import random
import shufflemania

class SavestateBox(ttk.Frame):
    """Represents the settings (.sav file location, ROM location) for a window to be shuffled"""
    def __init__(self,root):
        ttk.Frame.__init__(self,root,padding="3 3 12 12")
        self.grid(column=0, row=0, sticky=(N ,W ,E ,S))
        self.save_location = StringVar()
        self.rom_location = StringVar()
        ttk.Entry(self, textvariable=self.save_location).grid(column=2,row=1)
        ttk.Entry(self, textvariable=self.rom_location).grid(column=4,row=1)
        ttk.Label(self, text="Savestate:").grid(column=1, row=1)
        ttk.Label(self, text="Game:").grid(column=3,row=1)

class ShufflemaniaGUI:
    """Class representing the GUI for shufflemania"""
    def __init__(self, root):
        self.root = root
        self.shuffler = shufflemania.Shufflemania()
        def save():
            #generate a new savestatebox
            
            SavestateBox(self.mainframe).grid(column=1,row=random.randint(1,4))
            pass
        def start():
            #self.shuffler.shuffle()
            pass

        def stop():
            #self.shuffler.stop()
            pass

        self.root.title("Shufflemania")

        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        #setting type stuff
        self.dolphin_location = StringVar()
        ttk.Entry(self.mainframe,textvariable=self.dolphin_location).grid(column=2,row=0)
        ttk.Label(self.mainframe,text="Dolphin.exe:").grid(column=1,row=0)

        self.shuffle_orders = ('Sequential', 'Sequential Random', 'True Random')
        self.shuffle_order_combobox = ttk.Combobox(self.mainframe,state="readonly",values=self.shuffle_orders)
        self.shuffle_order_combobox.current(0)
        self.shuffle_order_combobox.bind('<<ComboboxSelected>>', self.shuffle_order_combobox.selection_clear())
        self.shuffle_order_combobox.grid(column=4,row=0)
        ttk.Label(self.mainframe,text="Shuffle Order:").grid(column=3,row=0)

        ttk.Label(self.mainframe,text="Shuffle Frequency").grid(column=6,row=0)
        ttk.Label(self.mainframe,text="Min").grid(column=6,row=1)
        ttk.Label(self.mainframe,text="Max").grid(column=6,row=2)

        self.shuffle_time_min = StringVar(value=5)
        self.shuffle_time_max = StringVar(value=10)
        self.entry_min = ttk.Entry(self.mainframe,textvariable=self.shuffle_time_min)
        self.entry_min.grid(column=7,row=1)
        self.entry_max = ttk.Entry(self.mainframe,textvariable=self.shuffle_time_max)
        self.entry_max.grid(column=7,row=2)

        # #savestate file locations
        # self.s1 = StringVar()
        # self.s2 = StringVar()
        # self.s3 = StringVar()
        # self.s4 = StringVar()
        # #game file locations
        # self.g1 = StringVar()
        # self.g2 = StringVar()
        # self.g3 = StringVar()
        # self.g4 = StringVar()
        # self.savestates = [self.s1,self.s2,self.s3,self.s4]
        # self.roms = [self.g1,self.g2,self.g3,self.g4]
        # #where you input the savestate and game locations
        # for i in range(4):
        #     ttk.Entry(self.mainframe,textvariable=self.savestates[i]).grid(column=2,row=i+1)
        #     ttk.Entry(self.mainframe,textvariable=self.roms[i]).grid(column=4,row=i+1)
        #     ttk.Label(self.mainframe,text="savestate:").grid(column=1,row=i+1)
        #     ttk.Label(self.mainframe,text="ROM:").grid(column=3,row=i+1)
        SavestateBox(self.mainframe).grid(column=2,row=1)
        ttk.Button(self.mainframe,text="Save",command=save()).grid(column=1,row=5)
        ttk.Button(self.mainframe,text="Start",command=start()).grid(column=2,row=5)
        ttk.Button(self.mainframe,text="Stop",command=stop()).grid(column=3,row=5)

root = Tk()
ShufflemaniaGUI(root)
root.mainloop()
