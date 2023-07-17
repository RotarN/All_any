# Google Secret Side project for interviewing: https://foobar.withgoogle.com/
# 5 Challenges: 1 & 2 presented here:
"""
1.
I Love Lance & Janice
=====================

You've caught two of your fellow minions passing coded notes back and forth
-- while they're on duty, no less! Worse, you're pretty sure it's not job-related
-- they're both huge fans of the space soap opera ""Lance & Janice"".
You know how much Commander Lambda hates waste, so if you can prove that
these minions are wasting time passing non-job-related notes,
it'll put you that much closer to a promotion.

Fortunately for you, the minions aren't exactly advanced cryptographers.
In their code, every lowercase letter [a..z] is replaced with the corresponding
one in [z..a], while every other character (including uppercase letters and punctuation)
is left untouched.  That is, 'a' becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.
For instance, the word ""vmxibkgrlm"", when decoded, would become ""encryption"".

Write a function called solution(s) which takes in a string and returns the deciphered
string so you can show the commander proof that these minions are talking about
""Lance & Janice"" instead of doing their jobs.

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
Output:
    did you see last night's episode?

Input:
solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
Output:
    Yeah! I can't believe Lance lost his job at the colony!!
"""

import string


def solution(x):
	return


result = solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
assert result == "did you see last night's episode?"
result = solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
assert result == "Yeah! I can't believe Lance lost his job at the colony!!"
result = solution("vmxibkgrlm")
assert result == "encryption"

"""
2. 
Gearing Up for Destruction
==========================

As Commander Lambda's personal assistant, you've been assigned 
the task of configuring the LAMBCHOP doomsday device's axial orientation gears. 
It should be pretty simple -- just add gears to create the appropriate rotation ratio. 
But the problem is, due to the layout of the LAMBCHOP and the complicated system of 
beams and pipes supporting it, the pegs that will support the gears are fixed in place.
The LAMBCHOP's engineers have given you lists identifying the placement of 
groups of pegs along various support beams. 
You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). 
The engineers have plenty of gears in all different sizes stocked up, 
so you can choose gears of any size, from a radius of 1 on up. 
Your goal is to build a system where the last gear rotates at twice the rate 
(in revolutions per minute, or rpm) of the first gear, no matter the direction. 
Each gear (except the last) touches and turns the gear on the next peg to the right.
Given a list of distinct positive integers named pegs representing the 
location of each peg along the support beam, write a function solution(pegs) which, 
if there is a solution, returns a list of two positive integers a and b representing 
the numerator and denominator of the first gear's radius in its simplest form in order to 
achieve the goal above, such that radius = a/b. 
The ratio a/b should be greater than or equal to 1. 
Not all support configurations will necessarily be capable of creating the proper rotation ratio, 
so if the task is impossible, the function solution(pegs) should return the list [-1, -1].
For example, if the pegs are placed at [4, 30, 50],
then the first gear could have a radius of 12, 
the second gear could have a radius of 14, 
and the last one a radius of 6. 
Thus, the last gear would rotate twice as fast as the first one. 
In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].
The list pegs will be given sorted in ascending order and will contain at least 2 
and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.
Languages
=========
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.
	-- Python cases -- 

		Input:
			solution.solution([4, 17, 50])
		Output:
			-1,-1

		Input:
			solution.solution([4, 30, 50])
		Output:
			12,1
"""


def solution(pegs):
	# Your code here
	pass
