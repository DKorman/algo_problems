# LINK: https://app.codility.com/programmers/lessons/2-arrays/
# PROBLEM:
# A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.
#
# For example, in array A such that:
#
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the elements at indexes 0 and 2 have value 9,
# the elements at indexes 1 and 3 have value 3,
# the elements at indexes 4 and 6 have value 9,
# the element at index 5 has value 7 and is unpaired.
# Write a function:
#
# def solution(A)
#
# that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.
#
# For example, given array A such that:
#
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the function should return 7, as explained in the example above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.


# TAKE 1:
def solution(A):

    odd = set()

    for i in A:
        # removes the number if present in the list - this happens only if it was an 'even'th appearance
        if i in odd:
            odd.remove(i)
        else:
            # adds the number if it occurs for the first time or for an 'odd'-th time (first is an odd too)
            odd.add(i)

    # eventually, all  numbers that occur even number of times are removed and only odd one remains
    return list(odd)[0]

# SCORE: 100%, Performance 100%
# COMMENT: thought this would be considered slowish



#  SOLUTION FOUND ON WEB:
def solution2(A):
    result = 0
    for number in A:
        result ^= number
    return result

# SCORE: 100%, Performance 100%
# COMMENT: A good reminder that there are bitwise operators, but stil not 100% sure why does this operation always gives the odd number as a result
