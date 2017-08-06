from Students import *
class Ingenieria(Students, object):
    """docstring for Ingenieria."""

    def printFullNameUpperCase(self):
        pollosLocos = super(Ingenieria, self).getAllDataOfStudent()
        return pollosLocos.upper()
