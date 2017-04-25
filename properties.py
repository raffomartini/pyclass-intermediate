'''
All about using properties

1982        Normalized Databases

    PriceRange
    =============
    low     real
    high    real
    mid     low + high / 2
    
    SELECT low, mid, high FROM PriceRangeView

'''


from __future__ import division
import validators

class PriceRange(object):

    __slots__ = ('_low', '_high')
    # locks down the object and replace the __dict__ with __slots__

    def __init__(self, low, high):
        self.low = low
        self.high = high

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self,value):
        validators.is_number(value)
        validators.is_positive(value)
        self._low = value

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self,value):
        validators.is_number(value)
        validators.is_positive(value)
        self._high = value

    @property
    def mid(self):
        return (self.low + self.high) / 2

    '''
Setter:
    @mid.setter
    def mid(self,mid):
        'recenter around new mid-point, keeping same distance between the high and the low'
        delta = (self.high - self.low) / 2
        self.low = mid - delta
        self.high = mid + delta
Note: because this is not abvious, the docstring is important, but it will NEVER be seen
In this case it is better to define a separate method
'''

    def recenter_around_mid(self, mid):
        'recenter around new mid-point, keeping same distance between the high and the low'
        delta = (self.high - self.low) / 2
        self.low = mid - delta
        self.high = mid + delta



    def __repr__(self):
        return '{!r}({!r}, {!r})'.format(type(self).__name__, self.low, self.high)


if __name__ == '__main__':
    p = PriceRange(5,10)
    print p
    print p.mid
