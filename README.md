#----------------------------------------------------------------------------------------------------------------------#
													kNN Visualizer
#----------------------------------------------------------------------------------------------------------------------#

How to use:

Option 1:
First, (if not already done) install python. Then, open the installation directory in a terminal and install the 
required packages. Then run main.py

Option 2:
Run kNN Visualizer.exe, then enter the number of points and nearest neighbors you want the program to use. Currently,
however, kNN Visualizer.exe is out of date. This method is not recommended.

How to import your own points:

Install the prerequisites to run the code.
In objects.py, you can create a new array of points and their colors, then import it to main and set it equal to 
pointsArray.
Finally, run the program.

#----------------------------------------------------------------------------------------------------------------------#
														Brief
#----------------------------------------------------------------------------------------------------------------------#

This project creates an image of various points, with each pixel colored according to that pixel's distance to the
nearest couple of points and their respective colors. The user can specify the number of total points as well as the
number of nearst points (or nearest neighbours) to be taken into account when creating the color of the pixel.

I apologise in advance for the render time. I tried forcing it to run on the gpu, but the graphics.py module does not
work well with jit. Creating my own graphics environment is, at the time of making, both out of scope for the project 
and my skill level in python. I invite you to try and make the program run a little faster yourself.

#----------------------------------------------------------------------------------------------------------------------#
										Required Packages and Installation
#----------------------------------------------------------------------------------------------------------------------#

This code will not function without the Zelle graphics package, which itself requires tKinter

1: Install graphics.py
	$> pip install graphics.py           (FOR ALL OPERATING SYSTEMS)

2: Install tKinter
	$> pip install tk                    (FOR WINDOWS)
	$> sudo apt-get install python-tk    (FOR UBUNTU AND MAC)
	$> sudo pacman -S tk                 (FOR ARCH)

3: Run the program
	$> python main.py					(FOR ALL OPERATING SYSTEMS)