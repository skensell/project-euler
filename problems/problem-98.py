"""98. Find the largest square number occurring in a square anagram word pair."""
import string, re
import itertools
from collections import defaultdict, Counter
from math import sqrt
from myToolbox import show,memo,timed
import time

#Output:
#pe98() finished in 11.840555 seconds.
#('BROAD', 18769, 'BOARD', 17689)
#


words = set(open('text/words.txt').read().strip().replace('"','').split(','))
letter_counts = dict((word,Counter(word)) for word in words)
#words.sort(key=len)


def num_dist_letters(word): return len(set(word))

def word_info():
    dist_lett = map(num_dist_letters,words)
    counts = {}
    for i in range(14):
        counts[i] = dist_lett.count(i)
    show(counts.items())
    print max(words,key=len) #outputs a 14-letter word

#word_info()

def get_anagram_families(words):
    """Takes words and returns a list of (word_length, family) pairs
    with longer word_lengths last."""
    result = []
    while words:
        word = words.pop()
        family = find_anagrams(word,words) | set([word])
        if len(family) > 1:
            result.append((len(word),family))
        words = words - family
    return sorted(result)

def find_anagrams(word,words):
    """Returns a set of anagrams of the word within the set of words"""
    letters_of_word = Counter(word)
    return set(w for w in words if letter_counts[w] == letters_of_word)



@timed
def pe98():
    anagram_fams = get_anagram_families(words)
    squares = set()
    while True:
        word_length, family = anagram_fams.pop()
        if word_length < 5:
            return max(squares, key=lambda x: max(x[1],x[3]))
        while family:
            w1 = family.pop()
            if not family or num_dist_letters(w1) > 10:
                break
            else:
                form1 = 'is_square(%s)'%w1
                solutions = faster_solve(form1)
                for w2 in family:
                    form2 = 'is_square(%s)'%w2
                    for trans_table in solutions:
                        number_form = form2.translate(trans_table)
                        if w2.translate(trans_table)[0] != '0' and\
                           eval(number_form) == True:
                            squares.add((w1, int(w1.translate(trans_table)),\
                                         w2, int(w2.translate(trans_table))))

def is_square(n): return sqrt(n)%1 == 0


###### Modified versions of the CS212 code. ########


def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula."""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((9,8,7,6,5,4,3,2,1,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                yield table #formula.translate(table) #yielding instead of return
        except ArithmeticError:
            pass


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. The first digit of a multi-digit
    number can't be 0. So if YOU is a word in the formula, and the function
    is called with Y eqal to 0, the function should return False."""

    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    leading_letters = set(re.findall(r'\b([A-Z])[A-Z]', formula))
    conditions =  []
    for A in leading_letters:
         conditions.append('%s != 0' % A)
    theformula = ''.join(tokens)
    conditions.append(theformula)
    body = ' and '.join(conditions)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print f
    return eval(f), letters

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word








print pe98()











def test():
    assert  next(faster_solve('int(sqrt(TALKATIVE)) == sqrt(TALKATIVE)'))==\
           'int(sqrt(420824196)) == sqrt(420824196)'
    assert next(faster_solve('int(sqrt(HELLO)) == sqrt(HELLO)')) ==\
           'int(sqrt(12996)) == sqrt(12996)'
    assert [i for i in faster_solve('int(sqrt(AAA)) == sqrt(AAA)')] == []
    print 'tests pass'

#test()













squares = defaultdict(set)
def populate_squares():
    for x in xrange(11,):
        s = x**2
        squares[len(s)].add(s)


def square_families(d):
    families = defaultdict(set)
    for digits in combinations('0123456789',d):
        for ordering in permutations(digits):
            if ordering[0] != '0':
                number = int(''.join(ordering))
                #if is_square(number):
                    #families[digits].add(number)

