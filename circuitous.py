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
    
class method        Class.method()
    implicitly receives the class obj as first argument
     useful for alternate constructors
     
name mangling       __name --> _Class__name
    useful for keeping an extra reference to internal dependencies
    to be used when you expect somebody to override your method
     
Liskov substitution principle
    a child should be substitutable for the parent in all situations
    
Open/closed principle
    a class should be open for extension (inheritance)
    and closed for modifications
    overrides should have no surprises/side-effects
    

'''

from collections import namedtuple
import math

# namedtuple help readability for versioning
Version = namedtuple('Version', 'major minor patch')

PI = math.pi

class Circle(object):
    'an advanced circle analytics toolkit'

    version = Version(0,4,1)
    # you increase the major when you break compatibility
    # you increase the minor when you add features
    # you increase the revision when you patch


    def __init__(self, radius):
        'very few people would read docstring on a __method'
        self.radius = radius

    '''
    Old way of defining properties:
    def get_radius(self):
        return self.diameter / 2.0

    def set_radius(self, radius):
        self.diameter = radius * 2.0

    radius = property(get_radius, set_radius)
    '''

    # better way of defining properties
    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0


    @classmethod
    def from_bbd(cls, diagonal):
        'Construct a new Circle from bounding box diagonal'
        radius = diagonal / math.sqrt(2)
        return cls(radius)

    def __repr__(self):
        return '{}(radius={!r})'.format(self.__class__.__name__,self.radius)
        # !r force to use the repr rather than the str

    def area(self):
        'Quadrature on a planar shape of uniform revolution'
        radius = self.__circumference() / PI / 2.0
        return PI * self.radius ** 2

    def circumference(self):
        'Perimeter of a circle'
        return PI * self.radius * 2

    # private reference to protect the internal reference in the method area
    __circumference = circumference

    @staticmethod
    # used so you can call Circle.angle_to_grade() without defining an instance first
    def angle_to_grade(angle):
        '''
        Convert an inclinometer reading in degrees to a percent grade  
        '''
        return math.tan(math.radians(angle)) * 100.0
