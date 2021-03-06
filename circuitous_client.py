'''
Our customers' code.
'''

from circuitous import Circle
from random import random, seed


def customer_0():
    '''
    Customer 0: Our academic friends
    :return: 
    '''

    print 'Aproposal to reserach the areas of circles'
    print 'with Circuitous(tm)', Circle.version
    n = 5
    seed(42)
    #circles = [Circle(random()) for i in xrange(n)]
    # with parenthesis it becomes a generator
    circles = (Circle(random()) for i in xrange(n))
    # areas = [c.area() for c in circles]
    areas = (c.area() for c in circles)
    print 'The average aread of', n , 'random circles'
    print 'seeded with the Answer to Life and Everything'
    print 'is', sum(areas) / n



def customer_1():
    '''Customer 1: Local rubber sheet company
    company that cuts rounds sheets of rubber
    '''

    cuts = [0.7, 0.3, 0.5]
    circles = [Circle(radius) for radius in cuts]
    for c in circles:
        print 'A circle with radius', c.radius
        print 'has an area {:.2f}'.format(c.area())
        print 'and a perimeter {:.2f}'.format(c.circumference())
        c.radius *= 1.1
        print 'and a warm area {:.2f}'.format(c.area())

# customer 2: Regional tyre company

class Tyre(Circle):

    # def __init__(self, radius, pressure):
    #     Circle.__init__(self, radius)
    #     self.pressure = pressure

    def circumference(self):
        'adjusted perimeter for width of tyre'
        # unbound method call
        return 1.25 * Circle.circumference(self)

    __circumference = circumference

def customer_2():
    t = Tyre(22)
    print 'a tyre of radius', 22
    print 'has an area {:.2f}'.format(t.area())
    print 'and a circumference {:.2f}'.format(t.circumference())

# Customer 3 - a national trucking company

def customer_3():
    angle = 7.0
    print 'a hill with {:.0f} degree incline'.format(angle)
    print 'is a {:.0f}% grade'.format(Circle.angle_to_grade(7))

# Customer 4 - an international graphic company
# we have money and power
# We build circles NOT with radius
# but with bounding box diagonal

def customer_4():
    bbd = 10
    c = Circle.from_bbd(bbd)
    print 'a circle with bounding box diagonal of {}'.format(bbd)
    print 'has a radius of {:.2f}'.format(c.radius)
    print 'has an area of {:.2f}'.format(c.area())

# Customer 5: the government
# we like to micromanage
# we'll tell you not just WHAT to build
# but also HOW to build it

# ISO-12345-fake
# Thou shalt not directyl access the radius
# inside area methods. Area methods must
# infer the radius from the circumference.
# --> this requires name mangling

# ISO-123456-fake
# Circle instances must not store the radius
# A circle instance must store the diameter and ONLY the diameter.
# --> this requires properties

def customer_5():
    pass

if __name__ == '__main__':
    print
    # customer_0()
    # customer_1()
    # customer_2()
    # customer_3()
    # customer_4()
    customer_5()