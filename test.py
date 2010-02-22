#!/usr/bin/python

from rationals import *

e = RationalsEnumeration()  # create a new enumeration
print e                     # show the first rational (see note below)
print e.next()              # show the second rational
print e.previous()          # show the first rational again
print e.se()                # show the current stern-eisenstein rational (as a pair)
print e.sb()                # show the current stern-brocot rational (as a pair)
print e.jump(5)             # show the fifth rational
print e.jump(-5)            # show the first rational again
print e.goto(10)            # show the tenth rational
print e.goto(0)             # show the first rational again

# Note: an object of RationalsEnumeration keeps track of the current
#       position in the enumeration and both rationals (the stern-einsenstein
#       and the stern-brocot rationals). Example:

# Current position in the enumeration: 0
# Current rational (Stern-Brocot order):     (1,1)
# Current rational (Stern-Eisenstein order): (1,1)
