#!/usr/bin/python
#encoding: utf-8

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" %name
print "He's %r inches tall." %height
print "He's %d pounds heavy." %weight
print "Acutally that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usally %s depending on the coffee." %teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)


inchetocm = 2.54

inche = 10

print "%d inche equals to %d cm." %(inche, inchetocm * inche)
