#!/usr/bin/python

from aerowrite import PropFile

club = PropFile("fileTest.glo")
club.cmt("hello world")
print("hello")
