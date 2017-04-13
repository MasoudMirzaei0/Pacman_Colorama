# Pacman_Colorama
A Simplified Version of Pacman Game Coded with Python 2.7 using "Colorama" Module.

Has "Auto saving" and "game speed" option!

Check out the executable version in dist folder!

![alt tag](https://github.com/mkaafy/Pacman_Colorama/blob/master/ScreenShot.png)

(Help)

Requirements:

<tab>OS: Windows (Because of "msvcrt" Module)

<tab>Python Version 2.7

<tab>Colorama Module

Source code is in "pacman.py" file.

I also used "py2exe" Module for building a ".exe version" of the game which is stored in "dist" folder.

Saving option uses python pickle files.

You can create your own map file.

Map format description:

<tab>First line: Indicates Size of Console Window. (Width Height)
  
<tab>Second line: Indicates number of walls.
  
<tab>Last line: Indicates number of enemies.
  
<tab>Other lines: Indicates position of walls.


Command for running game (in CMD):

<tab>python<space>pacman.py

Requires colorama. If not installed, simply install it using Python Package Index (pip):

<tab>pip<space>install<space>colorama
