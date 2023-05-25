# a7_test.py
# Prof. Bracy, AWB93
# Mar 10, 2023

import cornellasserts as ca
import inspect  # to print the name of a (test) function that is running
import a7
import dice, a6, printer

# helper written by Prof. Lee, LJL2
def print_testing(start_or_end):
    """If start_or_end is 'start',
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

def test_a_hand(value_list, category, expected):
    """ This is a helper function that we strongly encourage you to use
    and even more strongly encourage you NOT TO MODIFY.

    Please look at how this function is called in the examples below.

    value_list: [int list] of the 5 dice you want in your hand
    category:   [int] a number from 0 to 12 (CHANCE to YAHTZEE) indicating
                     how you would like to categorize that hand
    expected:   [int] the score this hand earns in this category
    """
    error_msg = "failed test: " +str(value_list)+ ", " +str(category)+ ", "+\
        str(expected)+" @ line "+str(inspect.currentframe().f_back.f_lineno)

    sc = a7.Scorecard()
    dice_list = []
    for n in value_list:
        dice_list.append(dice.Die(n))
    hand = a6.Hand(a7.Rules.NUM_DICE, dice_list)
    if sc.categories[category] != None:
        sc.categories[category].score(hand)
    else:
        cat_msg = str(category)+" (\'"+a7.Rules.names[category]+"\')"
        ca.quit_with_error("Scorecard @ index " +cat_msg+ " is None. \n"+\
        "Cannot test this category until it is properly initialized.\n" +\
        "See Scorecard __init__() method in a7.py\n"+error_msg)

    points = sc.categories[category].points
    error_msg += f"\nexpected score: {expected}\ncomputed score: {points}\n"
    ca.assert_equals(expected, points, error_msg)

# ---------------------------------------------------------
# SOME test code for you A7 is below.
# You are encouaged to add more test cases.
# ---------------------------------------------------------

def test_ones(): 
    print_testing('start')
    # [1,1,1,2,1] as Ones should yield 4 points
    test_a_hand([1,1,1,2,1], a7.Rules.ONES, 4)
    # [2,4,1,2,1] as Ones should yield 2 points
    test_a_hand([2,4,1,2,1], a7.Rules.ONES, 2)
    # [4,4,4,4,4] as Ones should yield 0 points
    test_a_hand([4,4,4,4,4], a7.Rules.ONES, 0)
    # Test for when all dice values are 1
    test_a_hand([1,1,1,1,1], a7.Rules.ONES, 5)
    # Test for when all dice values are different and none are 1
    test_a_hand([2,3,4,5,6], a7.Rules.ONES, 0)
    # Test for when only one die has a value of 1
    test_a_hand([2,4,1,2,5], a7.Rules.ONES, 1)
    # Test for when no dice have a value of 1
    test_a_hand([2,4,3,2,5], a7.Rules.ONES, 0)
    print_testing('end')

def test_3ofakind():
    print_testing('start')
    # [1,1,1,2,1] as Three of a Kind should yield 6 points
    test_a_hand([1,1,1,2,1], a7.Rules.THREE_OF_A_KIND, 6)
    # [2,4,1,2,1] as Three of a Kind should yield 0 points
    test_a_hand([2,4,1,2,1], a7.Rules.THREE_OF_A_KIND, 0)
    # [4,4,4,4,4] as Three of a Kind should yield 20 points
    test_a_hand([4,4,4,4,4], a7.Rules.THREE_OF_A_KIND, 20)
    # Test for when all dice values are the same (3 of a kind)
    test_a_hand([3,3,3,3,3], a7.Rules.THREE_OF_A_KIND, 15)
    # Test for when 4 dice values are the same (4 of a kind)
    test_a_hand([2,2,2,2,5], a7.Rules.THREE_OF_A_KIND, 13)
    # Test for when only 2 dice values are the same
    test_a_hand([1,1,2,2,3], a7.Rules.THREE_OF_A_KIND, 0)
    # Test for when no dice values are the same
    test_a_hand([1,2,3,4,5], a7.Rules.THREE_OF_A_KIND, 0)
    print_testing('end')

def test_4ofakind():
    print_testing('start')
    # [1,1,1,2,1] as Four of a Kind should yield 6 points
    test_a_hand([1,1,1,2,1], a7.Rules.FOUR_OF_A_KIND, 6)
    # [2,1,1,2,1] as Four of a Kind should yield 0 points
    test_a_hand([2,1,1,2,1], a7.Rules.FOUR_OF_A_KIND, 0)
    # [4,4,4,4,4] as Four of a Kind should yield 20 points
    test_a_hand([4,4,4,4,4], a7.Rules.FOUR_OF_A_KIND, 20)
    # Test for when all dice values are the same (4 of a kind)
    test_a_hand([4,4,4,4,4], a7.Rules.FOUR_OF_A_KIND, 20)
    # Test for when all dice values are the same (Yahtzee)
    test_a_hand([1,1,1,1,1], a7.Rules.FOUR_OF_A_KIND, 5)
    # Test for when 3 dice values are the same
    test_a_hand([2,2,2,4,2], a7.Rules.FOUR_OF_A_KIND, 12)
    # Test for when no dice values are the same
    test_a_hand([1,2,3,4,5], a7.Rules.FOUR_OF_A_KIND, 0)
    print_testing('end')

def test_yahtzee(): 
    print_testing('start')
    # [1,1,1,2,1] as Yahtzee should yield 0 points
    test_a_hand([1,1,1,2,1], a7.Rules.YAHTZEE, 0)
    # [2,1,1,2,1] as Yahtzee should yield 0 points
    test_a_hand([2,1,1,2,1], a7.Rules.YAHTZEE,0)
    # [4,4,4,4,4] as Yahtzee should yield 50 points
    test_a_hand([6,6,6,6,6], a7.Rules.YAHTZEE,  a7.Rules.YAHTZEE_PTS)
    # Test for when all dice values are the same (Yahtzee)
    test_a_hand([6,6,6,6,6], a7.Rules.YAHTZEE, 50)
    # Test for when all dice values are not the same
    test_a_hand([1,2,3,4,5], a7.Rules.YAHTZEE, 0)
    # Test for when only 4 dice values are the same (4 of a kind)
    test_a_hand([2,2,2,2,5], a7.Rules.YAHTZEE, 0)
    # Test for when only 3 dice values are the same (3 of a kind)
    test_a_hand([1,1,1,2,3], a7.Rules.YAHTZEE, 0)
    print_testing('end')

def test_full_house():
    print_testing('start')
    # [1,1,1,2,1] as Full House should yield 0 points
    test_a_hand([1,1,1,2,1], a7.Rules.FULL_HOUSE, 0)
    # [2,1,1,2,1] as Full House should yield 25 points
    test_a_hand([2,1,1,2,1], a7.Rules.FULL_HOUSE, a7.Rules.FULL_HOUSE_PTS)
    # [4,4,4,4,4] as Full House should yield 0 points
    test_a_hand([4,4,4,4,4], a7.Rules.FULL_HOUSE, 0)
    print_testing('end')

def test_small_straight():
    print_testing('start')
    # [1,1,1,2,1] as Small Straight should yield 0 points
    test_a_hand([1,1,1,2,1], a7.Rules.SM_STRAIGHT, 0)
    # [2,4,3,2,1] as Small Straight should yield 30 points
    test_a_hand([2,4,3,2,1], a7.Rules.SM_STRAIGHT, a7.Rules.SM_STRAIGHT_PTS)
    # [1,5,2,3,4] as Small Straight should yield 30 points
    test_a_hand([1,5,2,3,4], a7.Rules.SM_STRAIGHT, a7.Rules.SM_STRAIGHT_PTS)
    print_testing('end')

def test_large_straight():
    print_testing('start')
    # [1,1,1,2,1] as Large Straight should yield 0 points
    test_a_hand([1,1,1,2,1], a7.Rules.LG_STRAIGHT, 0)
    # [2,4,3,2,1] as Large Straight should yield 0 points
    test_a_hand([5,4,3,2,6], a7.Rules.LG_STRAIGHT, a7.Rules.LG_STRAIGHT_PTS)
    # [1,5,2,3,4] as Large Straight should yield 40 points
    test_a_hand([1,5,2,3,4], a7.Rules.LG_STRAIGHT, a7.Rules.LG_STRAIGHT_PTS)
    print_testing('end')

if __name__ == '__main__':

    # you can turn printing back on if you want to see the dice,
    # but we kind of liked testing with the dice turned off....
    printer.print_f = False

    # STUDENTS: You should test all 13 categories. We've done 4 for you.
    #test_chance() #? Done
    test_ones() #? Done
    test_3ofakind() #? Done
    test_4ofakind() #? Done 
    test_yahtzee()  #? Done
    test_full_house() #? Done
    test_small_straight() #! Pending...
    test_large_straight() #! Pending...
    
