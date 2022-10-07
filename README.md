#----------------------------------------------------------------------------------------------------------------------#
														kNN Visualizer
#----------------------------------------------------------------------------------------------------------------------#

How to use:
Run kNN Visualizer.exe, then enter the number of points and nearest neighbors you want the program to use.
If you have python installed, you can also run main.py.

How to import your own points:
In objects.py, you can create a new array of points and their colors, then import it to main and set it equal to 
pointsArray. 

If you have more points than 9, delete the error check that stops you from running the code if you have more than 9 
points. The check only exists to prevent people from causing an index out of bounds error in the colors array when 
randomly generating points.