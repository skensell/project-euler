"""
96. Write an algorithm to solve Sudoku.
"""

import re
import doctest
from myToolbox import timed
from myToolbox import trace
from myToolbox import disabled

def solve_sudoku(puzzle):
    """Takes a 9x9 matrix which is a valid Sudoku puzzle (meaning it has
    only 1 solution) and returns the unique solution. The puzzle should be
    a list of lists of integers 0-9 with blank spaces represented by 0's."""

    # This is a dictionary of cell:candidates pairs, e.g. (4,4): set([3,5,7])
    puzzle_dict = make_dictionary(puzzle)
    while True:
        np, np_dict = look_boxes(*look_vertical(*look_across(puzzle,puzzle_dict)))
        if filled_in(np):
            #print "Solved."
            return np
        elif np_dict == puzzle_dict and np == puzzle: # When deduction doesn't work.
            return guess_one(np, np_dict)
        puzzle, puzzle_dict = np, np_dict
        #print "Looping."


def guess_one(puzzle, puzzle_dict):
    """Picks a cell with few candidates and writes in one of them."""
    empty_cells = [(i,j) for i in range(9)
                   for j in range(9) if puzzle[i][j] is 0]
    def number_of_candidates(cell): return len(puzzle_dict[cell])
    chosen_cell = min(empty_cells,key=number_of_candidates)
    guesses = puzzle_dict[chosen_cell]
    while guesses:
        puzzle[chosen_cell[0]][chosen_cell[1]] = a = guesses.pop()
        #print "Guessing %s in cell %s." %(a,chosen_cell)
        try:
            return solve_sudoku(puzzle)
        except NameError: #raised in look_across
            #print "Guess %s in cell %s was wrong." %(a, chosen_cell)
            continue
    raise NameError("Some guess was wrong. Going back.")


def look_across(puzzle,puzzle_dict):
    """Reduce the list of candidates for each cell based on
    the numbers of those in the same rows. A number is written to
    the puzzle if either
    1) the list of candidates for a given cell is just one number
    2) the number appears only once in all the candidates of the row."""

    for r in range(9):

        row_elements = set(puzzle[r])

        # Removes row_elements from cell candidates.
        row_candidates = []
        for c in range(9):
            if puzzle[r][c] is 0:
                puzzle_dict[(r,c)] -= row_elements
                candidates = puzzle_dict[(r,c)]
                row_candidates += list(candidates)
                if len(candidates) is 0:
                    raise NameError('Impossible. Wrong guess.')
                elif len(candidates) is 1:
                    puzzle[r][c] = a = candidates.pop()
                    #print "Writing %s in cell %s." %(a,(r,c))
                    #Note: Above print doesn't work when in look_vertical or boxes.
                    row_elements.update(set([a]))

        if not distinct(puzzle[r]):
            raise NameError('Row is not distinct.  Wrong guess.')

        # If 7 occurs only once in row_candidates then it should be written in.
        # We call 7 a lone_value.
        lone_values = [i for i in row_candidates if row_candidates.count(i) is 1]
        while lone_values:
            loner = lone_values.pop()
            for c in range(9):
                if loner in puzzle_dict[(r,c)]:
                    puzzle[r][c] = loner
                    #print "writing %s in cell %s" %(loner,(r,c))
                    puzzle_dict[(r,c)] = set([loner])
                    break

    return puzzle, puzzle_dict


def filled_in(puzzle): return all([0 not in row for row in puzzle])

def distinct(row):
    """Returns True if all nonzero elts of the row are distinct."""
    return (len(set(num for num in row if num != 0)) ==
            len([num for num in row if num != 0]))


def look_vertical(puzzle,puzzle_dict):
    """Reduces the list of candidates column-wise."""
    return transpose(*look_across(*transpose(puzzle,puzzle_dict)))


def transpose(puzzle, puzzle_dict):
    """Returns puzzle and puzzle_dict transposed."""
    puzzle = [list(c) for c in zip(*puzzle)]
    puzzle_dict = {(cell[1],cell[0]): candidates
                    for (cell, candidates) in puzzle_dict.items()}
    return puzzle, puzzle_dict


def look_boxes(puzzle, puzzle_dict):
    """Reduce the list of candidates box-wise."""
    return boxify(*look_across(*boxify(puzzle,puzzle_dict)))


def boxify(puzzle, puzzle_dict):
    """Turns the boxes into rows accordingly. Note that doing this twice
    gives back the original puzzle since it is a piecewise-transpose."""
    new_puzzle = [[0]*9 for i in range(9)]
    for r in range(9):
        for c in range(9):
            i,j = box_map[(r,c)]
            new_puzzle[i][j] = puzzle[r][c]
    puzzle_dict = {box_map[cell]: candidates
                   for (cell, candidates) in puzzle_dict.items()}
    return new_puzzle, puzzle_dict


def box_trans(r,c): return 3*(r//3) + (c//3), (c%3) + 3*(r%3)

box_map = {(i,j): box_trans(i,j) for i in range(9) for j in range(9)}


def make_dictionary(puzzle):
    """Makes a dictionary of cell:candidates pairs. If the cell is filled in
    then candidates is a set of the number. If the cell is 0 then available is
    a set of range(1,10)."""
    puzzle_dict = {}
    for i in range(9):
        for j in range(9):
            p_ij = puzzle[i][j]
            if p_ij == 0:
                puzzle_dict[(i,j)] = set(range(1,10))
            else:
                puzzle_dict[(i,j)] = set([p_ij])
    return puzzle_dict
    #I think I can rewrite this using dict comprehension











#################### TESTS ########################

# An easy one.

puzzle1 =    [[0, 0, 3, 0, 2, 0, 6, 0, 0],
              [9, 0, 0, 3, 0, 5, 0, 0, 1],
              [0, 0, 1, 8, 0, 6, 4, 0, 0],
              [0, 0, 8, 1, 0, 2, 9, 0, 0],
              [7, 0, 0, 0, 0, 0, 0, 0, 8],
              [0, 0, 6, 7, 0, 8, 2, 0, 0],
              [0, 0, 2, 6, 0, 9, 5, 0, 0],
              [8, 0, 0, 2, 0, 3, 0, 0, 9],
              [0, 0, 5, 0, 1, 0, 3, 0, 0]]

# The next 3 puzzles required me to rework the algorithm to include guess and check.

puzzle6 =      [[1, 0, 0, 9, 2, 0, 0, 0, 0],
                [5, 2, 4, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 0],
                [0, 5, 0, 0, 0, 8, 1, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [4, 0, 2, 7, 0, 0, 0, 9, 0],
                [0, 6, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 3, 0, 9, 4, 5],
                [0, 0, 0, 0, 7, 1, 0, 0, 6]]

puzzle7 =      [[0, 4, 3, 0, 8, 0, 2, 5, 0],
                [6, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 9, 4],
                [9, 0, 0, 0, 0, 4, 0, 7, 0],
                [0, 0, 0, 6, 0, 8, 0, 0, 0],
                [0, 1, 0, 2, 0, 0, 0, 0, 3],
                [8, 2, 0, 5, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 5],
                [0, 3, 4, 0, 9, 0, 7, 1, 0]]

puzzle10 =     [[0, 0, 1, 9, 0, 0, 0, 0, 3],
                [9, 0, 0, 7, 0, 0, 1, 6, 0],
                [0, 3, 0, 0, 0, 5, 0, 0, 7],
                [0, 5, 0, 0, 0, 0, 0, 0, 9],
                [0, 0, 4, 3, 0, 2, 6, 0, 0],
                [2, 0, 0, 0, 0, 0, 0, 7, 0],
                [6, 0, 0, 1, 0, 0, 0, 3, 0],
                [0, 4, 2, 0, 0, 7, 0, 0, 6],
                [5, 0, 0, 0, 0, 6, 8, 0, 0]]

puzzle23 =   [[0,4,0,0,0,0,0,5,0],
              [0,0,1,9,4,3,6,0,0],
              [0,0,9,0,0,0,3,0,0],
              [6,0,0,0,5,0,0,0,2],
              [1,0,3,0,0,0,5,0,6],
              [8,0,0,0,2,0,0,0,7],
              [0,0,5,0,0,0,2,0,0],
              [0,0,2,4,3,6,7,0,0],
              [0,3,0,0,0,0,0,4,0]]

def show_puzzle(puzzle):
    for row in puzzle:
        print row
def show_solution(puzzle):
    print "Original puzzle: "
    show_puzzle(puzzle)
    print "Solution: "
    show_puzzle(solve_sudoku(puzzle))
    print ""

def test_1():
    """Tests look_vertical and look_across."""
    print "Original puzzle: "
    global puzzle1
    show_puzzle(puzzle1)
    puzzle1_dict = make_dictionary(puzzle1)
    for i in range(3):
        puzzle1, puzzle1_dict = look_vertical(*look_across(puzzle1, puzzle1_dict))
    print "Puzzle is now: "
    show_puzzle(puzzle1)

#test_1()

def test_2():
    """Tests boxify."""
    print "Original puzzle: "; show_puzzle(puzzle1)
    puzzle1_dict = make_dictionary(puzzle1)
    print "After boxifying: "
    puzz, puzz_dict = boxify(puzzle1, puzzle1_dict)
    for row in puzz:
        print row

#test_2()

def test_3():
    """Tests solve_sudoku."""
    show_solution(puzzle1)

#test_3()


def test_4():
    """Tests data reading and solves puzzles."""
    puzz_data = open("text/sudoku.txt","r").read().strip()
    puzz_data = re.split('\s*Grid \d\d\s*', puzz_data)
    all_puzzles = []
    for puz_string in puzz_data:
        puzzle = [map(int,list(row)) for row in re.split('\n',puz_string)]
        all_puzzles.append(puzzle)

    for puzzle in all_puzzles[:3]:
        show_solution(puzzle)

#test_4()

def test_5():
    """Solves some puzzles from sudoku.txt. Shows I need to rework method
    since only 38 out of 50 puzzles solved."""
    puzz_data = open("text/sudoku.txt","r").read().strip()
    puzz_data = re.split('\s*Grid \d\d\s*', puzz_data)
    all_puzzles = []
    for puz_string in puzz_data:
        puzzle = [map(int,list(row)) for row in re.split('\n',puz_string)]
        all_puzzles.append(puzzle)

    count = 0
    for puzzle in all_puzzles:
        if solve_sudoku(puzzle):
            print "Solved."
            count += 1
    print "Solved %s out of 50 puzzles."%count

#test_5()



def test_6():
    """Reworking algorithm until these 3 puzzles get solved. These were the
    problematic ones."""
    show_solution(puzzle6)
    #show_solution(puzzle7)
    #show_solution(puzzle10)

#test_6()


@timed
def project_euler_96():
    """Solve all 50 puzzles in sudoku.txt and find the sum of the 50 3-digit
    numbers appearing in the top left."""
    puzz_data = open("text/sudoku.txt","r").read().strip()
    puzz_data = re.split('\s*Grid \d\d\s*', puzz_data)
    all_puzzles = []
    for puz_string in puzz_data:
        puzzle = [map(int,list(row)) for row in re.split('\n',puz_string)]
        all_puzzles.append(puzzle)

    solved_puzzles = [solve_sudoku(puzzle) for puzzle in all_puzzles]
    def three_digit_num(puzz): return 100*puzz[0][0] + 10*puzz[0][1] + puzz[0][2]
    print reduce(lambda x,y:x+y, map(three_digit_num ,solved_puzzles))


project_euler_96()






### Below is my failing attempt to get doctest to work.


class TestSudoku: """

>>> puzzle1 = [[0, 0, 3, 0, 2, 0, 6, 0, 0],
...              [9, 0, 0, 3, 0, 5, 0, 0, 1],
...              [0, 0, 1, 8, 0, 6, 4, 0, 0],
...              [0, 0, 8, 1, 0, 2, 9, 0, 0],
...              [7, 0, 0, 0, 0, 0, 0, 0, 8],
...              [0, 0, 6, 7, 0, 8, 2, 0, 0],
...              [0, 0, 2, 6, 0, 9, 5, 0, 0],
...              [8, 0, 0, 2, 0, 3, 0, 0, 9],
...              [0, 0, 5, 0, 1, 0, 3, 0, 0]]

>>> for row in puzzle1:
...	print row
...
[0, 0, 3, 0, 2, 0, 6, 0, 0]
[9, 0, 0, 3, 0, 5, 0, 0, 1]
[0, 0, 1, 8, 0, 6, 4, 0, 0]
[0, 0, 8, 1, 0, 2, 9, 0, 0]
[7, 0, 0, 0, 0, 0, 0, 0, 8]
[0, 0, 6, 7, 0, 8, 2, 0, 0]
[0, 0, 2, 6, 0, 9, 5, 0, 0]
[8, 0, 0, 2, 0, 3, 0, 0, 9]
[0, 0, 5, 0, 1, 0, 3, 0, 0]

>>> for row in solve_sudoku(puzzle1):
...	print row
...
...
[4, 8, 3, 9, 2, 1, 6, 5, 7]
[9, 6, 7, 3, 4, 5, 8, 2, 1]
[2, 5, 1, 8, 7, 6, 4, 9, 3]
[5, 4, 8, 1, 3, 2, 9, 7, 6]
[7, 2, 9, 5, 6, 4, 1, 3, 8]
[1, 3, 6, 7, 9, 8, 2, 4, 5]
[3, 7, 2, 6, 8, 9, 5, 1, 4]
[8, 1, 4, 2, 5, 3, 7, 6, 9]
[6, 9, 5, 4, 1, 7, 3, 8, 2]

>>> puzzle1_dict = make_dictionary(puzzle1)
>>> for row in boxify(puzzle1,puzzle1_dict)[0]:
...	print row
...
...
[0, 0, 3, 9, 0, 0, 0, 0, 1]
[0, 2, 0, 3, 0, 5, 8, 0, 6]
[6, 0, 0, 0, 0, 1, 4, 0, 0]
[0, 0, 8, 7, 0, 0, 0, 0, 6]
[1, 0, 2, 0, 0, 0, 7, 0, 8]
[9, 0, 0, 0, 0, 8, 2, 0, 0]
[0, 0, 2, 8, 0, 0, 0, 0, 5]
[6, 0, 9, 2, 0, 3, 0, 1, 0]
[5, 0, 0, 0, 0, 9, 3, 0, 0]

>>> for row in transpose(puzzle1, puzzle1_dict)[0]:
...	print row
...
[0, 9, 0, 0, 7, 0, 0, 8, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[3, 0, 1, 8, 0, 6, 2, 0, 5]
[0, 3, 8, 1, 0, 7, 6, 2, 0]
[2, 0, 0, 0, 0, 0, 0, 0, 1]
[0, 5, 6, 2, 0, 8, 9, 3, 0]
[6, 0, 4, 9, 0, 2, 5, 0, 3]
[0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 8, 0, 0, 9, 0]

>>> for row in look_across(*look_vertical(puzzle1,puzzle1_dict))[0]:
...	print row
...
...
[0, 0, 3, 0, 2, 0, 6, 0, 0]
[9, 0, 0, 3, 0, 5, 0, 0, 1]
[0, 0, 1, 8, 0, 6, 4, 0, 0]
[0, 0, 8, 1, 0, 2, 9, 0, 0]
[7, 0, 0, 0, 0, 0, 1, 0, 8]
[0, 0, 6, 7, 0, 8, 2, 0, 0]
[0, 0, 2, 6, 0, 9, 5, 0, 0]
[8, 0, 0, 2, 0, 3, 0, 0, 9]
[0, 0, 5, 0, 1, 0, 3, 0, 0]



>>> box_trans(6,7); box_trans(4,5); box_trans(7,7)
(8, 1)
(4, 5)
(8, 4)

>>> filled_in(puzzle1)
False
>>> filled_in(solve_sudoku(puzzle1))
True


"""

#doctest.testmod()



