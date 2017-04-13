from distutils.core import setup
import py2exe

setup(
    console=['pacman.py'],
    options = {
        'py2exe': {
            'packages': ['colorama']
            }
        }
    )
