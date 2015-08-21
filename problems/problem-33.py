"""33. Fraction digit cancelling."""

from fractions import Fraction
from operator import mul
from myToolbox import timed
import re
#output:
#1/100
#pe_33() finished in 0.228625 seconds.


@timed
def pe_33():
    result = set()
    for denom in range(11,100):
        if denom % 10:
            for num in range(11, denom):
                frac = '%s/%s'%(num,denom)
                if lucky_guess(frac):
                    result.add(frac)
    print reduce(mul,map(Fraction,result))


def lucky_guess(frac):
    """Takes a fraction string 34/47 and performs bad simplification."""
    guess_1 = re.sub(r'(\d)(\d/\d)\1' ,r'\2',frac)
    guess_1 = Fraction(guess_1) if len(guess_1) == 3 else 0
    guess_2 = re.sub(r'(\d)/\1','/',frac)
    guess_2 = Fraction(guess_2) if len(guess_2) == 3 else 0
    frac = Fraction(frac)
    return guess_1 == frac or guess_2 == frac



pe_33()


def test():
    assert lucky_guess('56/67')==False
    assert lucky_guess('49/98')==True
    print 'tests pass'

#test()
