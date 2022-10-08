# ----------------------------------------------------------------------------------------------------------------------
#                                                   BRIEF
# ----------------------------------------------------------------------------------------------------------------------
# This project creates an image of various points, with each pixel colored according to that pixel's distance to the
# nearest couple of points and their respective colors. The user can specify the number of total points as well as the
# number of nearst points (or nearest neighbours) to be taken into account when creating the color of the pixel
#
# ----------------------------------------------------------------------------------------------------------------------
#                                        REQUIRED PACKAGE INSTALL NOTE
# ----------------------------------------------------------------------------------------------------------------------
# This code will not function without the Zelle graphics package.
# 1:
# >>> pip install graphics.py           (FOR ALL)
# 2:
# >>> pip install tk                    (FOR WINDOWS)
# >>> sudo apt-get install python-tk    (FOR UBUNTU AND MAC)
# >>> sudo pacman -S tk                 (FOR ARCH)
#


from graphics import *
import random
import math
import objects


def determine_least(x, y, z):
    if x < y:
        return x
    if y < z:
        return y
    return z


def generate_points(numPoints, winX, winY):
    pointsArray = []
    for i in range(numPoints):
        coords = Point(winX + random.randint(-180, 180), winY + random.randint(-180, 180))
        pointsArray.append(coords)
    return pointsArray


def find_color(i, j, winX, winY, numPoints, k, pointsArray):
    # inspect starts at the top left of the work area then goes down before it goes across

    # create a di array which stores the distances to the points and their indexes
    dArr = []
    # get the distance to each point and assign it to the diArray along with the index
    for l in range(numPoints):
        currentDistance = math.sqrt(((i + winX - 200) - pointsArray[l].x) * ((i + winX - 200) - pointsArray[l].x) +
                                    ((j + winY - 200) - pointsArray[l].y) * ((j + winY - 200) - pointsArray[l].y))
        dArr.append(currentDistance)

    # create an array that contains both the index and distance of each element
    dcArr = [[0, 0] for _ in range(numPoints)]
    for l in range(numPoints):
        dcArr[l] = [dArr[l], objects.arrColors[l]]

    # make a new dcArr with k taken into account
    # dArr.sort()

    dArr.sort()
    dArr.reverse()
    for l in range(numPoints - k):
        dArr.pop(0)
    dArr.reverse()

    kdcArr = [[0.0, [0.0, 0.0, 0.0]] for _ in range(k)]
    for l in range(k):
        kdcArr[l][0] = dArr[l]
        for m in range(numPoints):
            if kdcArr[l][0] == dcArr[m][0]:
                kdcArr[l][1] = dcArr[m][1]

    # create the color
    weightedColor = [0, 0, 0]
    if k != 1:
        # weigh the distance
        totalDistance = 0
        for l in range(k):
            totalDistance += kdcArr[l][0]
        weightedDistances = [0 for _ in range(k)]

        for l in range(k):
            if kdcArr[l][0] != 0:
                weightedDistances[l] = 1 - (kdcArr[l][0] / totalDistance)

        for l in range(k):
            weightedDistances[l] = weightedDistances[l] / (k - 1)

        # delinearize the weighted distances by running them through the equation:
        # y(x) = 1 / (1 + e ^ (-1.5 * pi (2x-1)))
        for l in range(k):
            weightedDistances[l] = 1 / (1 + pow(math.e, (-1.5 * math.pi * (2 * weightedDistances[l] - 1))))

        # make tne new color
        for l in range(k):
            weightedColor[0] += kdcArr[l][1][0] * weightedDistances[l]
            weightedColor[1] += kdcArr[l][1][1] * weightedDistances[l]
            weightedColor[2] += kdcArr[l][1][2] * weightedDistances[l]

    else:
        weightedColor = [kdcArr[0][1][0], kdcArr[0][1][1], kdcArr[0][1][2]]

    return color_rgb(int(weightedColor[0]), int(weightedColor[1]), int(weightedColor[2]))


def main():
    # initialization

    pInput = input("Enter the number of points to be randomly generated: (n < 9): ")
    numPoints = int(pInput)

    print("The recommended amount of neighbours in for k is " + str(round(math.sqrt(numPoints))) + ".")

    kInput = input("Enter the number of nearest neighbours you would like to account for (k): ")
    k = int(kInput)

    win = GraphWin('kNN Example', 500, 500)
    winX = win.getWidth() / 2
    winY = win.getHeight() / 2
    topLeft = Point(winX - 200, winY - 200)
    bottomRight = Point(winX + 200, winY + 200)

    # making sure there are no errors
    if numPoints > 9:
        print("Sorry but the maximum amount of random points you can generate is 9!")
        return

    # generate the array of points
    pointsArray = generate_points(numPoints, winX, winY)

    # kNN
    for i in range(400):
        for j in range(400):
            inspect = Point(i + topLeft.x, j + topLeft.y)
            inspect.setFill(find_color(i, j, winX, winY, numPoints, k, pointsArray))
            inspect.draw(win)

    # formatting the workspace
    outline = Rectangle(bottomRight, topLeft)
    outline.draw(win)
    yAxis = Line(Point(winX, winY - 200), Point(winX, winY + 200))
    yAxis.draw(win)
    xAxis = Line(Point(winX - 200, winY), Point(winX + 200, winY))
    xAxis.draw(win)

    # drawing the points
    for i in range(numPoints):
        pRect = Rectangle(Point(pointsArray[i].x - 5, pointsArray[i].y - 5),
                          Point(pointsArray[i].x + 5, pointsArray[i].y + 5))
        pRect.setFill(objects.zelleColors[i])
        pRect.setOutline('black')
        pRect.draw(win)
        pointsArray[i].draw(win)

    message = Text(Point(winX, 2 * winY - 25), str(numPoints) + ' total points, k = ' + str(k))
    message.draw(win)

    # exit
    xit = False
    while not xit:
        win.getKey()
        a = win.getKey()
        if a == 'q':
            xit = True
    win.close()


main()

# Created by Phineas Howell on 9/26/22
