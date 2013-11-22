
=========
AeroWrite
=========

this is part software of AeroPack (set of tools for the aerotech juggling probs)
It's very useful to generate glo file.

Requirement:
============
python3
aerotech prob
multi platform but at the moment only tested with linux

install
=======

you can do :
$ git clone https://github.com/LaurentBa/AeroWrite.git
$ cd AeroWrite
$ sudo python setup.py install

and test the example below :

$ cd docs/exemple
$ python exemple.py


exemple
=======

#!/usr/bin/python

from aerowrite import PropFile, Color

"""
This is a simple temporary exemple of how to use aerowrite
you'll find this example in AeroWrite/docs/exemple/
we'll create 15 glo files with this python file.
But python is powerful you can imagine many many things

the program is in development sorry for bugs
However, it is already useful to me
May be it will be for you too.
"""

# First We create a list of our 8 class ProbFile for clubs

club = list()
for i in range(8):
    club.append( PropFile('./glo_file/testClub{}.glo'.format(str(i))))


# And we create a list of our 7 class ProbFile for balls
ball = list()
for i in range(7):
    ball.append( PropFile('./glo_file/testBall{}.glo'.format(str(i))))


# create an instance of color for later
mvcolor = Color(255,0,0)
# and vars
step = 20
uMax = 255



# create 1 loop function for the loop method exemple
# line 71
def myloop(i):
    ball[i].c(255,0,255, cmt="loop")
    ball[i].d(69)
    ball[i].c(10,10,10)


# Let's start clubs prog
for i in range(8):
    club[i].cmt("start verification")
    club[i].r(255)
    club[i].d(3000, "wait 30 seconds, and light me")
    club[i].r(0)
    club[i].d(300)
    club[i].ramp(255,155,44,200, "starting the wonderful show")
    club[i].d(300,"wonderful comment")
    club[i].d(300)
    club[i].c(0,0,255)

    # you can see all methods in aerowrite/prop.py currently lacks only sub
    # you can also use the Color object with cc() et cramp()  methods
    club[i].cc(mvcolor, cmt="test cc same as c but with Color object")

    if (mvcolor.get_R() <= uMax - step):
        mvcolor.set_R(mvcolor.get_R() + step )
    else :
        mvcolor.set_R(0)

    club[i].end()


# Let's start balls prog
for i in range(7):
    print(i)
    ball[i].d(3000+300*3+200, "wait the end of club")
    ball[i].loop(4, myloop, i)
    
    ball[i].end()
