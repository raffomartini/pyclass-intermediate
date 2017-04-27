'''Copiright (c) 1993 Fly-by-Night, Inc.

CHEAPO LICENSE.
You have purchased the Cheapo License. You can use this software as-is, 
with no guarantees, and no maintenacne.
All bugs are features. You do not have the legal right to modify this sourcecode. Good luck!
'''

import math

def sqrts(numbers):
    return [math.sqrt(x) for x in numbers]

'''
Ruby on Rails:
    
    using ActiveRecords
    5.days.from_now
'''
# Zen of Python: Explicit is better than implicit

from datetime import datetime, timedelta
datetime.now() + timedelta(days=5)