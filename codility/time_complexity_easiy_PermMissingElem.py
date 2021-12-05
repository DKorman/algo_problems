# LINK: # LINK: https://app.codility.com/programmers/lessons/3-time_complexity/

# PROBLEM: An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
#
# Your goal is to find that missing element.
#
# Write a function:
#
# class Solution { public int solution(int[] A); }
#
# that, given an array A, returns the value of the missing element.
#
# For example, given array A such that:
#
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

# TAKE 1:

def solution(A):

    # sort the list
    A.sort()

    # create a shifted version of the list
    A_rotated = A.copy()
    A_rotated.pop(0)

    # remove the last element since it is redundant for subtraction
    A.pop(-1)

    # subtract the values of original and the rotated list
    subtracted = [new - og for new,og in zip(A_rotated,A)]

    # get idx where the subtracted value is greater than 1
    idx = [index for index,value in enumerate(subtracted) if subtracted[index]>1][0]

    # use this idx to get value and subtract to get the missing element
    missing = A_rotated[idx]-1

    return missing


# Task Score: 50% - not all cases were solved

# COMMENT: adding these lines of code:

# if(len(A) == 0): return 1
# elif(len(A) == 1):
#     if(A[0] == 1): return 2
#     else: return 1

# will solve for some additional cases, but I am not pleased with the problem statement of this task.
# From the description of the problem it doesnt seem obvious to me that empty lists, single element lists and double element lists need to be taken into consideration



# SOLUTION FROM THE FORUMS:
def solution(A):

    # sum of consecutive integers from 1 to n has a mathematical solution

    # length of the list if no elements were missing
    n = len(A)+1

    # expected sum if there were no missing integers
    expected = n * (n + 1)//2

    # actual sum of the list with the missing integer
    actual = sum(A)

    return  expected - actual

#Score: 100%, detected time complexity is O(N) or O(N * log(N))