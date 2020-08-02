##AUTHOR KORRE D. HENRY
'''DESCRIPTION: This progam displays a GIF of a randomly colored portrait with birds flying
across the image constantly. In this program, given the user's
mouse's and y coordinate on the image, the user can move their mouse up and down as the image
moves along with giving the illusion that the user is discovering more about the image
then what it actually being displayed. This concept is called motion parallaxing.
Ths program will also display the times of day ranging from a moon display and
a display of the sun. Depending your mouse's position is on the display it
will display user freindly text to show what the user is hovering over
for example; 'Mountaint, Sun, Moon,etc.)'''
from graphics import graphics
import random

def sky (gui,c,x=0,y=0):
    #c  = color type
    '''Creates the blue sky in the background of the image, this does not change
    position'''
    gui.rectangle (0,0,600,500,c[0])
    day (gui,c,x,y)
    
    
def mountains (gui,colors,x=0,y=0):
    '''Creates the 3 mountains, using random colors, passed in from a list. It
    uses x and y values to change the position of the mountain.'''
    ## Back Tallest Mountain
    gui.triangle (100+(x/50),450+(y/70),315+(x/50),150+(y/70),560+(x/50),450+(y/70),colors[0])
    ## Middle Mountain
    gui.triangle (-130+(x/50),550-(y/30),195+(x/50),175-(y/30),490+(x/50),550-(y/30),colors[1])
    ### Front Triangle
    gui.triangle (160+(x/50),550-(y/50),455+(x/50),150-(y/50),750+(x/50),550-(y/50),colors[2])

def birds (gui,x=0):
    '''Creates the birds which are constantly given new x positions,allowing
    it to move across the screen'''
    for i in range (1,6):
        gui.line (-500+ (i*80)+x, 190+ (i*20), -460 +(i*80)+x, 200+ (i*20), 'black')
        gui.line (-460 +(i*80)+x,200+ (i*20),-430+ (i*80)+x,190+ (i*20),'black')


def lawn (gui,x=0,y=0):
    '''Creates the lawn, lawn and tree, passing in new x and y values'''
    for i in range (-200, 900,10):
        gui.line (0+i+(x/5), 450+(y/15),3+i+(x/5),450-10+(y/15),'green')
    gui.rectangle (-200+(x/5),450+(y/15),800,150,'green')
    gui.rectangle (410+(x/15),420+(y/15),30,60,'brown')
    gui.ellipse (425+(x/15),400+(y/15),70,80,'green')
    return [425+(x/15),400+(y/15)]#Returns a list of x and y values for the tree
    
def day (gui,c,x=0,y=0):
    '''Creates the sun or moon'''
    gui.ellipse (450+(x/70),75+(y/70),75,75,c[1])
    return [450+(x/70),75+(y/70)]#Returns 

def parallax (gui,i=0,time=0):
    '''Passes in new x,y coordinates into specifc functions that
    are constantly updated based upon the user's mouse position'''
    colors = colorSort (gui)
    while True:
        gui.clear ()
        y, x = gui.mouse_y, gui.mouse_x
        if i > 1000 : i = 0 #Sets X position for the birds
        else: i += 5 #Changes X position for the birds
        if time % 50 == 0: timeOfDay = ['deep sky blue','yellow2']
        if time % 150 == 0:
            colors = colorSort (gui)
            timeOfDay = ['blue4','ghost white']
        sky (gui,timeOfDay,x,y)
        time +=1
        mountains (gui,colors,x,y)
        lawn (gui,x,y)
        birds (gui,i)
        moralCompass (gui,timeOfDay,x,y)
        gui.update_frame (100)
        
def moralCompass (gui,timeOfDay,x,y):
    '''Displays direction and location of the user's mouse at any
    given instance of time per frame rate'''
    if gui.mouse_x > 500 and gui.mouse_y < 200: gui.text (gui.mouse_x, gui.mouse_y, 'East')
    elif gui.mouse_x > lawn (gui,x,y)[0]-60 and gui.mouse_x < lawn (gui,x,y)[0]+60 and gui.mouse_y > lawn (gui,x,y)[1]-70 and gui.mouse_y < lawn (gui,x,y)[1]+70:
        gui.text (gui.mouse_x, gui.mouse_y, 'Tree')
    elif gui.mouse_x > 70 and gui.mouse_y > 180 and gui.mouse_y < 420: gui.text (gui.mouse_x, gui.mouse_y, 'Mountain')        
    elif gui.mouse_x < 200 and gui.mouse_y < 150: gui.text (gui.mouse_x, gui.mouse_y, 'West')
    elif gui.mouse_x > 220 and gui.mouse_x < 380 and gui.mouse_y < 200: gui.text (gui.mouse_x, gui.mouse_y, 'North')
    elif gui.mouse_x < 230 and gui.mouse_y > 450 or gui.mouse_x > 400 and gui.mouse_y > 450: gui.text (gui.mouse_x, gui.mouse_y, 'Lawn')
    elif gui.mouse_x > 250 and gui.mouse_x < 400 and gui.mouse_y > 450: gui.text (gui.mouse_x, gui.mouse_y, 'South')
    elif gui.mouse_x > day (gui,timeOfDay,x,y)[0]-75 and gui.mouse_x < day (gui,timeOfDay,x,y)[0]+75 and gui.mouse_y > day (gui,timeOfDay,x,y)[1]-75 and gui.mouse_y < day (gui,timeOfDay,x,y)[1]+75:
        if 'yellow' in timeOfDay[1]: gui.text (gui.mouse_x, gui.mouse_y, 'Sun')
        else: gui.text (gui.mouse_x, gui.mouse_y, 'Moon')
            
def colorSort (gui):
    '''Returns a list of color values'''
    colors = []
    for i in range (0,3):
        r = random.randint (0,255)
        g = random.randint (0,255)
        b = random.randint (0,255)
        color = gui.get_color_string (r,g,b)
        colors.append (color)
    return colors
        
def main ():
    '''Entry point to the program'''
    gui = graphics (600,600,'Landscape')
    parallax (gui)
main ()
