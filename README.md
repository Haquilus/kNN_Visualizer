![Logo](https://i.ibb.co/tzL8Hgt/Untitled-1.png)
# kNN Visualizer 

This project creates an image of various points, with each pixel colored according to that pixel's distance to the
nearest couple of points and their respective colors. The user can specify the number of total points as well as the
number of nearst points (or nearest neighbours) to be taken into account when creating the color of the pixel.

## Installation

This program will not function without the Zelle graphics package, which itself requires tKinter.

For Windows:
```bash
  git clone https://github.com/Haquilus/kNN_Visualizer.git kNN_Visualizer
  cd kNN_Visualizer
  pip install graphics.py 
  pip install tk
```

For Ubuntu and Mac:
```bash
  git clone https://github.com/Haquilus/kNN_Visualizer.git kNN_Visualizer
  cd kNN_Visualizer
  pip install graphics.py
  sudo apt-get install python-tk
```

For Arch
```bash
  git clone https://github.com/Haquilus/kNN_Visualizer.git kNN_Visualizer
  cd kNN_Visualizer
  pip install graphics.py
  sudo pacman -S tk
```
## Running the Program

For all operasting systems:
```bash
  python main.py
```
Make sure you are inside the project dirctory, i.e. the kNN_Visualizer folder.
## Optimizations


I apologise in advance for the render time. I tried forcing it to run on the gpu, but the graphics.py module does not
work well with jit. Creating my own graphics environment is, at the time of making, both out of scope for the project 
and my skill level in python. I invite you to try and make the program run a little faster yourself.
## Documentation

How to import your own points:

Install the prerequisites to run the code.
In objects.py, you can create a new array of points and their colors, then import it to main and set it equal to 
pointsArray. Finally, run the program.

The exe file is currently out of date and should not be used. 

Thanks for checking out my program!