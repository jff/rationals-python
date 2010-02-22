# vim: et ts=4

# This Python class is an object-oriented implementation of the algorithm
# that I and Roland Backhouse created in 2008 to enumerate the positive 
# rational numbers in two different ways. The algorithm is new and it has 
# never been implemented in Python before (as far as I know). 
# See [0] for the complete formal derivation, proofs, and other details.

# [0] Recounting the Rationals: Twice!, Roland Backhouse and Joao F. Ferreira,
#     Published in Mathematics of Program Construction, Springer-Verlag, LNCS 5133,
#     pp. 79--91 (proceedings of the 9th International Conference Mathematics of
#     Program Construction, MPC 2008, Marseille, France, July 15--18, 2008)
#     Available from http://joaoff.com/publications/2008/rationals

# I am using the matrices datatype from numpy
from numpy import matrix

class RationalsEnumeration:
    """This class represents an enumeration of rational numbers"""

    def __init__(self, m=matrix([[1,0],[0,1]])):
        """The constructor initializes the enumeration with the matrix given as argument.
           If the user does not provide a matrix, the identity matrix is used."""
        self._counter = 0
        self._current = m


    def se(self):
        """This method returns the current Stern-Eisenstein rational."""
        m = [1,1] * self._current
        return (m[0,1],m[0,0])

    def cw(self):
        """This method returns the current Stern-Eisenstein rational. We provide the name cw,
        because some people call this the Calkin-Wilf rational"""
        return self.se()

    def sb(self):
        """This method returns the current Stern-Brocot rational."""
        m = self._current * [[1],[1]]
        return (m[0,0],m[1,0])


    def next(self):
        """This method returns the next rational (in both orders)."""
        # For convenience, we extract the elements of the matrix
        d00 = self._current[0,0];
        d10 = self._current[1,0];
        d01 = self._current[0,1];
        d11 = self._current[1,1];

        if (d00+d10 == 1):
            # This is the boundary case
            self._current = matrix([[1,0],[d01+d11,1]])
        else:
            # This is when the matrix is not at the boundary of the tree
            j = int((d01 + d11 -1)/(d00 + d10))
            self._current *= matrix([[2*j+1,1],[-1,0]])
        
        # Increase the counter by 1
        self._counter += 1

        return self


    def previous(self):
        """This method returns the previous rational (in both orders)."""
        if(self._counter < 1):
            return self
        else:
            # For convenience, we extract the elements of the matrix
            d00 = self._current[0,0];
            d10 = self._current[1,0];
            d01 = self._current[0,1];
            d11 = self._current[1,1];
    
            if (d01+d11 == 1):
                # This is the boundary case
                self._current = matrix([[1,d10-1],[0,1]])
            else:
                # This is when the matrix is not at the boundary of the tree
                j = int((d00 + d10 -1)/(d11 + d01))
                self._current *= matrix([[0,-1],[1,2*j+1]])
        
            # Decrease the counter by 1
            self._counter -= 1

            return self


    def jump(self,offset=0):
        """This method jumps to the rational (in both orders) located at the 
           distance given in the argument. If the offset given is negative, it jumps
           backwards."""
        if (offset>0):
            for i in range(0,offset):
                self.next()
        elif (offset<0):
            for i in range(0,abs(offset)):
                self.previous()
            
        return self


    def goto(self, offset):
        """This method jumps to the rational (in both orders) located at the 
           position given in the argument."""
        if(offset!=self._counter):
            if(offset==0):
                self.__init__()
            else:
                self.jump(offset - self._counter)
        return self


    def __str__(self):
        s = "Current position in the enumeration: %d\n"%self._counter

        (n,d) = self.sb()
        s += "Current rational (Stern-Brocot order):     (%d,%d)\n"%(n,d)

        (n,d) = self.cw()
        s += "Current rational (Stern-Eisenstein order): (%d,%d)\n"%(n,d)

        return s
