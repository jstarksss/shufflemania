"""Run this to begin a shuffle session"""
import shufflemania as sm

sh = sm.Shufflemania()

# There are 3 modes,
# 'True Random' :       Swap to a random window that isn't the current one
# 'Sequential Random' : Swap to a random window that hasn't been seen yet.
#                       Once all windows have been seen the process restarts.
#                       This ensures that each game is played for roughly the same amount of time,
#                       while keeping the order that they will be swapped to less predictable.
# 'Sequential' :        Swap to the windows in a consistent order.
sh.swap_mode = 'True Random'

# How often to swap to a new window, in seconds.
# The time it takes will be randomly selected from this range for each swap
sh.duration_min = 15
sh.duration_max = 30

# Change this to the path to your Dolphin.exe file
DOLPHIN = r'dolphin.exe file path'

# Change the two strings below to the locations of the appropriate files.
# Copy/paste/remove as many of the below lines as you want,
# each corresponding to a save state you want to shuffle.
sh.add_window(sm.ShuffleWindow(DOLPHIN,r'game file path',r'save state file path'))

sh.shuffle()
