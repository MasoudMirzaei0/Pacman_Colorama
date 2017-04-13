# Pacman_Colorama
A Simplified Version of Pacman Game Coded with Python 2.7 using "Colorama" Module.

Has "Auto saving" and "game speed" option!

Check out the executable version in dist folder!

![alt tag](https://github.com/mkaafy/Pacman_Colorama/blob/master/ScreenShot.png)

(Help)

  + Requirements:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; OS: Windows (Because of "msvcrt" Module)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python Version 2.7

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Colorama Module

* Source code is in "pacman.py" file.

* I also used "py2exe" Module for building a ".exe version" of the game which is stored in "dist" folder.

* Saving option uses python pickle files.

* You can create your own map file.

  + Map format description:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; First line: Indicates Size of Console Window. (Width Height)
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Second line: Indicates number of walls.
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Last line: Indicates number of enemies.
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Other lines: Indicates position of walls.


* Command for running game (in CMD):

    python pacman.py

* Requires colorama. If not installed, simply install it using Python Package Index (pip):

    pip install colorama
