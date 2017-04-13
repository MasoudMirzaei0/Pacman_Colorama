# Pacman_Colorama
A Simplified Version of Pacman Game Coded with Python 2.7 using "Colorama" Module.

Has "Auto saving" and "game speed" option!

Check out the executable version in dist folder!

![alt tag](https://github.com/mkaafy/Pacman_Colorama/blob/master/ScreenShot.png)

(Help)

Requirements:

&nsbp;&nsbp;&nsbp;&nsbp;OS: Windows (Because of "msvcrt" Module)

&nsbp;&nsbp;&nsbp;&nsbp;Python Version 2.7

&nsbp;&nsbp;&nsbp;&nsbp;Colorama Module

Source code is in "pacman.py" file.

I also used "py2exe" Module for building a ".exe version" of the game which is stored in "dist" folder.

Saving option uses python pickle files.

You can create your own map file.

Map format description:

&nsbp;&nsbp;&nsbp;&nsbp;First line: Indicates Size of Console Window. (Width Height)
  
&nsbp;&nsbp;&nsbp;&nsbp;Second line: Indicates number of walls.
  
&nsbp;&nsbp;&nsbp;&nsbp;Last line: Indicates number of enemies.
  
&nsbp;&nsbp;&nsbp;&nsbp;Other lines: Indicates position of walls.


Command for running game (in CMD):

&nsbp;&nsbp;&nsbp;&nsbp;python<space>pacman.py

Requires colorama. If not installed, simply install it using Python Package Index (pip):

&nsbp;&nsbp;&nsbp;&nsbp;pip<space>install<space>colorama
