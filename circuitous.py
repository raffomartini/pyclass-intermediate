''' Copyright (c) 2017 Circuitous, Inc.

Eric Ries, "Lean Startup Method".
Agile : Waterfall :: Lean Startup : Business Plan
Build an MVP, then talk to customers.
"Get out of the building"

YAGNI: Ya ain't gonna need it.
'''

class Circle:
    'an advanced circle analytics toolkit'

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def circumference(self):
        return 3.14 * self.radius * 2
