# LINK: https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

# TASK:
# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
#
# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
#
# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
#
# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
#
# For example, consider array A such that:
#
#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# We can split this tape in four places:
#
# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7
# Write a function:
#
# class Solution { public int solution(int[] A); }
#
# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.
#
# For example, given:
#
#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# the function should return 1, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−1,000..1,000].

# TAKE 1:

def solution(A):
    # things do not need consideration: empty array,
    # things to consider: array of size 2

    abs_diffs = []

    for i in range(1, len(A)):
        first_half = A[:i]
        second_half = A[i:]

        diff = abs(sum(first_half) - sum(second_half))

        abs_diffs.append(diff)

    return (min(abs_diffs))


# SCORE: correctness 100%, performance (0%)
# COMMENT: cannot say that bad performance came as a shock


### SOLUTION FOUND ON WEB:
def solution(A):
    # sum is a key to the solution
    s = sum(A)

    # variable which tracks the sum of the front part
    front = 0

    # variable used for storage and comparison of min value
    m = float('inf')

    for i in A[:-1]:
        # incrementally sum values from the front part
        front += i

        # first subtract the front part from the sum to get the sum of the right part
        # then subtract it again to find the difference between the front part and the back part
        abs_diff = abs(s - 2 * front)

        # compare the subtracted value with the thusfar minimum value and store if it is lower than current min
        m = min(abs_diff, m)

    return m

## COMMENT: no need to iterate over range, slicing list many times is expensive, float('inf') can be useful

