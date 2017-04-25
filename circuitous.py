''' Copyright (c) 2017 Circuitous, Inc.

Eric Ries, "Lean Startup Method".
Agile : Waterfall :: Lean Startup : Business Plan
Build an MVP, then talk to customers.
"Get out of the building"

YAGNI: Ya ain't gonna need it.

Classes are for SHARED informations
instances are for UNIQUE informations

bound method        instance.method()
    regular method call
    implicitly passes the instance as the first arf
    
unbound method      Class.method(instance)
    calling a method from the class 
    must explicitly pass the instance as the first arg
    
static methond      Class.method()
    method called from the class
    but does not require an instance, implicit or explicit 
'''

from collections import namedtuple
import math

# namedtuple help readability for versioning
Version = namedtuple('Version', 'major minor patch')

PI = math.pi

class Circle:
    'an advanced circle analytics toolkit'

    version = Version(0,2,4)
    # you increase the major when you break compatibility
    # you increase the minor when you add features
    # you increase the revision when you patch


    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return '{}(radius={!r})'.format(self.__class__.__name__,self.radius)
        # !r force to use the repr rather than the str

    def area(self):
        return PI * self.radius ** 2

    def circumference(self):
        return PI * self.radius * 2

    @staticmethod
    # used so you can call Circle.angle_to_grade() without defining an instance first
    def angle_to_grade(angle):
        '''
        Convert an inclinometer reading in degrees to a percent grade  
        '''
        return math.tan(math.radians(angle)) * 100.0
