# What does Shufflemania do?
This code manages launching and swapping between several Dolphin windows to recreate the shuffling aspect of the [Shufflemania livestream](https://www.youtube.com/watch?v=E2_SpkLltSc) hosted by [DougDoug](https://www.youtube.com/channel/UClyGlKOhDUooPJFy4v_mqPg). For those unfamiliar, several games are opened at once. Only one is played at a time, and which game is being played at any moment is controlled by the program. The players must adapt quickly to the changing situations to stay successful.
# How to use
## Prerequisites
In order to run the code, you will need to download [Dolphin](https://dolphin-emu.org/) and [Python](https://www.python.org/). You will also need the [PyGetWindow](https://pypi.org/project/PyGetWindow/) module, which you can get via the command `pip install pygetwindow`. Note that PyGetWindow currently only supports Windows operating systems.
### Initial Dolphin Setup
Open Dolphin.exe and select `Options -> Configuration`. In the settings window, navigate to the Interface tab and check 'Pause on Focus Loss'. Also ensure that 'Keep Window on Top' is unchecked.
Additionally, ensure that the controls for each player are set up within Dolphin.
## Preparing to shuffle
When a 'shuffle session' begins, the Shufflemania code opens one instance of Dolphin per game you want to shuffle. You must define the location of the Dolphin.exe file, the location of the game's ROM, and finally a savestate file that you have created using Dolphin. Save state files are created by running a game in Dolphin, playing until you are at the spot you want the game to start at during the shuffle session, and then selecting `Emulation -> Save State -> Save State to File`. Note that a shuffle session may have multiple save states from the same game, or save states from several different games. You may also shuffle between different instances loaded from the same save state. In other words, there are no restrictions on what combinations of save states you can play in a single shuffle session.
## Starting a shuffle session
Once the above set-up is complete, modify `launcher.py` as directed in the file, then run it using python to launch the shuffler.
