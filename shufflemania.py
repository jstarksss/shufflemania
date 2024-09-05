import signal
import random
import subprocess
import sys
import time
import pygetwindow


class ShuffleWindow:
    """Represents a dolphin window along with the relevant data that the Shufflemania
       instance will use to modify it"""

    def __init__(self,dolphin:str,game:str,sav:str):
        self.dolphin = dolphin
        self.sav = sav
        self.game = game
        self.window = None

    def start(self):
        """Launches a dolphin window"""
        command = str(self.dolphin + ' -b -e "' + self.game + '" -s "' + self.sav + '"')
        subprocess.Popen(command)
        time.sleep(3) #wait in order to make sure the window opens before making it active
        self.window = pygetwindow.getActiveWindow() #if the window just opened it should be active
        print(self.window)
        time.sleep(0)

    def activate(self):
        """Make the shufflewindow the active window"""
        try:
            self.window.activate()
        except pygetwindow.PyGetWindowException:
            self.window.minimize()
            self.window.restore()

    def close(self):
        """Closes the window"""
        self.window.close()


class Shufflemania:
    """Main logic handler for shufflemania.
       Responsible for starting, managing, and closing ShuffleWidnows"""

    def __init__(self,swap_mode:str='True Random',duration_min:float=30.0,duration_max:float=0.0):
        self.swap_mode = swap_mode
        self.duration_min = duration_min
        if duration_max == 0:
            duration_max = duration_min + 0.1
        #min and max cannot be equal or the random function has a fit,
        #users probably won't notice the 0.1 difference anyways
        if duration_min == duration_max:
            self.duration_max = duration_max + 0.1
        else:
            self.duration_max = duration_max
        self.shuffle_windows = []
        self.sequential_random_remaining = []
        self.window_index = 0

    def add_window(self,shuffle_window:ShuffleWindow):
        """Adds a ShuffleWindow to the list"""
        self.shuffle_windows.append(shuffle_window)

    def remove_window(self,shuffle_window:ShuffleWindow):
        """Removes a shufflewindow from the list"""
        shuffle_window.close()
        self.shuffle_windows.remove(shuffle_window)

    def stop(self):
        """Closes all windows"""
        for i in self.shuffle_windows:
            i.close()

    def generate_swap_time(self) -> float:
        """Returns how long the next swap will last, in seconds"""
        return random.uniform(self.duration_min,self.duration_max)

    def next_window(self):
        """Used to activate the next window in accordance with the swap_mode"""
        if self.swap_mode == "Sequential":
            #Get the next window in a sequential looping order
            self.window_index = (self.window_index + 1) % len(self.shuffle_windows)
        elif self.swap_mode == "Sequential Random":
            #regenerate the remaining items if they have run out
            if not self.sequential_random_remaining:
                for i in range(len(self.shuffle_windows)):
                    self.sequential_random_remaining.append(i)
            #select a new item and remove it from the list
            self.window_index = random.choice(self.sequential_random_remaining)
            self.sequential_random_remaining.remove(self.window_index)
        elif self.swap_mode == "True Random":
            #Generate a random index that isn't the same as the current one
            current_index = self.window_index
            while current_index == self.window_index:
                self.window_index = random.randint(0, len(self.shuffle_windows) - 1)
        self.shuffle_windows[self.window_index].activate()

    def shuffle(self):
        """Main loop, call once shuffle_windows have been added to begin"""
        #Make sure all windows have been activated so that they are in the correct spot & paused
        for i in self.shuffle_windows:
            i.start()
        #Do the main loop
        while True:
            time.sleep(self.generate_swap_time())
            self.next_window()
