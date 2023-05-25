# a6_test.py
# Jonathan Tran, (jdt98)
# Apr 14, 2023

import cornellasserts as ca
import inspect  # to print the name of a (test) function that is running
from copy import deepcopy

from dice import Die, Dots
from a6 import Hand
import printer

# if your testing generates too many print statements, un-comment this line,
# and all the print statements except those from this file will go away.
# printer.print_f = False

def print_testing(start_or_end):
    """
    helper written by Prof. Lee, LJL2
    If start_or_end is 'start',
        print message about starting function that called this function
       If start_or_end is 'end'
        print message about ending function that called this function

    Precondition: start_or_end is either 'start' or 'end'"""
    caller = inspect.currentframe().f_back.f_code.co_name
    if start_or_end == 'start':
        print("Starting " + caller)
    elif start_or_end == 'end':
        print(caller + " seems to have passed (didn't crash/stop mid-way).")
        print("\n")


# ---------------------------------------------------------
# Test code for your 7 functions are below.
# Note: not all tests are exhuastive.
#    You are encouaged to add more test cases.
# ---------------------------------------------------------

ONE_DIE_LIST = [Die(3)]
FIVE_DIE_LIST = [Die(3), Die(2), Die(1), Die(6), Die(5)]
LENGTH1_OUTPUTS = [3]
LENGTH5_OUTPUTS = [3, 2, 1, 6, 5]
LENGTH1_STR = """.-------.
| O     |
|   O   |
|     O |
.-------.
"""

LENGTH5_STR = """.-------..-------..-------..-------..-------.
| O     || O     ||       || O   O || O   O |
|   O   ||       ||   O   || O   O ||   O   |
|     O ||     O ||       || O   O || O   O |
.-------..-------..-------..-------..-------.
"""

# STUDENTS: these tests are not exhaustive!
def test_init():
    print_testing('start')

    length1_hand = Hand(1, None)
    length1_hand = Hand(1, deepcopy(ONE_DIE_LIST))
    length5_hand = Hand(5, deepcopy(FIVE_DIE_LIST))

    ca.assert_equals(1, length1_hand.get_n_dice())
    ca.assert_equals(5, length5_hand.get_n_dice())
    for i, out in enumerate(LENGTH5_OUTPUTS):
        mydice = length5_hand.get_dice()
        ca.assert_equals(out, mydice[i].value)

    print_testing('end')

# STUDENTS: these tests are not exhaustive!
def test_get_n_dice():
    print_testing('start')

    h1 = Hand(-9)
    h2 = Hand(2)
    h5 = Hand(5)
    h8 = Hand(10)

    ca.assert_equals(1, h1.get_n_dice())
    ca.assert_equals(2, h2.get_n_dice())
    ca.assert_equals(5, h5.get_n_dice())
    ca.assert_equals(8, h8.get_n_dice())

    print_testing('end')

# STUDENTS: these tests are not exhaustive!
def test_get_dice():
    print_testing('start')

    h5 = Hand(5, FIVE_DIE_LIST)
    ca.assert_equals(FIVE_DIE_LIST, h5.get_dice())

    print_testing('end')

# STUDENTS: these tests are not exhaustive!
def test_mask_valid():
    print_testing('start')
    h = Hand(5)
    ca.assert_equals(False, h.mask_valid("1"))
    ca.assert_equals(False, h.mask_valid("3"))
    ca.assert_equals(False, h.mask_valid("101010"))
    ca.assert_equals(False, h.mask_valid("22222"))
    ca.assert_equals(False, h.mask_valid("3222223"))

    ca.assert_equals(True, h.mask_valid(""))
    ca.assert_equals(True, h.mask_valid("00000"))
    ca.assert_equals(True, h.mask_valid("11111"))
    ca.assert_equals(True, h.mask_valid("10111"))

    print_testing('end')

# STUDENTS: these tests are not exhaustive!
def test_contains():
    print_testing('start')

    length1_list = Hand(1, deepcopy(ONE_DIE_LIST))
    length5_list = Hand(5, deepcopy(FIVE_DIE_LIST))

    for i in range(7):
        if i in LENGTH1_OUTPUTS:
            ca.assert_equals(True, length1_list.contains(i))
        else:
            ca.assert_equals(False, length1_list.contains(i))
    for i in range(7):
        if i in LENGTH5_OUTPUTS:
            ca.assert_equals(True, length5_list.contains(i))
        else:
            ca.assert_equals(False, length5_list.contains(i))

    print_testing('end')

# STUDENTS: these tests are not exhaustive!
def test_score():
    print_testing('start')

    length1_hand = Hand(1, deepcopy(ONE_DIE_LIST))
    length5_hand = Hand(5, deepcopy(FIVE_DIE_LIST))

    ca.assert_equals(sum(LENGTH1_OUTPUTS), length1_hand.score())
    ca.assert_equals(sum(LENGTH5_OUTPUTS), length5_hand.score())

    print_testing('end')

# STUDENTS: these tests are not exhaustive!
def test_reroll():
    print_testing('start')

    length5_list = Hand(5, deepcopy(FIVE_DIE_LIST))
    mask1 = "11111"
    mask2 = "00000"
    mask3 = "01010"
    mask4 = "00010"

    ca.assert_equals(True, length5_list.reroll(mask1))
    ca.assert_equals(False, length5_list.reroll(mask2))
    ca.assert_equals(True, length5_list.reroll(mask3))
    ca.assert_equals(True, length5_list.reroll(mask4))

    print_testing('end')

# STUDENTS: these tests are not exhaustive!
def test_str():
    print_testing('start')

    length1_list = Hand(1, deepcopy(ONE_DIE_LIST))
    length5_list = Hand(5, deepcopy(FIVE_DIE_LIST))

    ca.assert_equals(LENGTH1_STR, str(length1_list))
    ca.assert_equals(LENGTH5_STR, str(length5_list))

    print_testing('end')


if __name__ == '__main__':

    test_init()
    test_get_n_dice()
    test_get_dice()
    test_mask_valid()
    test_contains()
    test_score()
    test_reroll()
    test_str()
