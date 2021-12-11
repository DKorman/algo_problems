# LINK: https://app.codility.com/programmers/lessons/4-counting_elements/

# TASK:

# A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.
#
# You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.
#
# The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.
#
# For example, you are given integer X = 5 and array A such that:
#
#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.
#
# Write a function:
#
# def solution(X, A)
#
# that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.
#
# If the frog is never able to jump to the other side of the river, the function should return −1.
#
# For example, given X = 5 and array A such that:
#
#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# the function should return 6, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N and X are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..X].

# TAKE 1:

def solution(X, A):
    # write your code in Python 3.6

    positions = list(range(1, X + 1))

    for idx, value in enumerate(A):

        if value in positions:
            positions.remove(value)

        if len(positions) == 0:
            return idx

    if len(positions) > 0:
        return -1

# SCORE: correctnes:100 %, performance 20%
# COMMENT: too many ifs for all elements of the list, and also unnecessary comparison if the element is inside an external list



# TAKE 2:
def solution(X, A):
    # write your code in Python 3.6

    s = sum(range(1, X+1))

    covered = set()

    for idx, value in enumerate(A):

        if value<=X:

            covered.add(value)

            if sum(covered) == s:
                return idx

    return -1

# SCORE: even worse than above - runtime error for single element, and it was even slower


## TAKE 3: try to compare with length of the set instead of the sums
def solution(X, A):
    full_set = set(range(1, X + 1))
    current_set = set()

    for idx, value in enumerate(A):
        if value <= X:
            current_set.add(value)
            if len(current_set) == len(full_set):
                return idx

    return -1


# score: 100%
# comment: just needed to avoid unncessary sums and similar things