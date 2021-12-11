# LINK: https://app.codility.com/programmers/lessons/4-counting_elements/

# # TASK:
# You are given N counters, initially set to 0, and you have two possible operations on them:
#
# increase(X) − counter X is increased by 1,
# max counter − all counters are set to the maximum value of any counter.
# A non-empty array A of M integers is given. This array represents consecutive operations:
#
# if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
# if A[K] = N + 1 then operation K is max counter.
# For example, given integer N = 5 and array A such that:
#
#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the values of the counters after each consecutive operation will be:
#
#     (0, 0, 1, 0, 0)
#     (0, 0, 1, 1, 0)
#     (0, 0, 1, 2, 0)
#     (2, 2, 2, 2, 2)
#     (3, 2, 2, 2, 2)
#     (3, 2, 2, 3, 2)
#     (3, 2, 2, 4, 2)
# The goal is to calculate the value of every counter after all operations.
#
# Write a function:
#
# def solution(N, A)
#
# that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.
#
# Result array should be returned as an array of integers.
#
# For example, given:
#
#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the function should return [3, 2, 2, 4, 2], as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N and M are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..N + 1].


# TAKE 1:
def solution(N, A):
    # no consideration: empty array A
    # to consider: only one counter (M=1), array of size 1(A=1)

    default_value = 0
    counters = dict.fromkeys(range(1, N + 1), default_value)

    for i in A:

        if i <= N:
            counters[i] += 1
        else:
            counters = dict.fromkeys(
                range(1, N + 1),
                max(counters.values())
            )

    return list(counters.values())


# SCORE: 66%; correctnes 100%, performance 40%, big O was N*M

# TAKE 2:
def solution(N, A):
    counters = [0] * N

    for i in A:

        if i <= N:
            counters[i - 1] += 1
        else:
            counters = [max(counters)] * N

    return counters

# SCORE: 66%; correctnes 100%, performance 40%, big O was N*M
# COMMENT: I guess the issue is in the else statement when creating a new list of many elements each thime  X>N




# solution found on web:


def solution(N, A):

    # create a list of counters
    counters = [0] * N

    # min value is  used to store current min value (base number) that any counter should have
    min_value = 0

    # max value is used to store current max value
    max_value = 0

    for i in A:

        if 1 <= i <= N:

            # increase either the current value of the counter or the stored min_value by 1
            counters[i - 1] = max(counters[i - 1], min_value) + 1
            # get the current max value after the addition above
            max_value = max(counters[i - 1], max_value)

        else:
            # set the min_value to the current_max value
            min_value = max_value

    # for loop above is not a complete solution. It doesnt solve the cases where:
    # a) the counter didnt appear at all in the list A
    # b) the min_value was updated but the counter didnt appear again in the list after the update

    # therefore, ad hoc replace the values in the counters for values lower than the min value
    for i in range(N):
        counters[i] = max(counters[i], min_value)

    return counters

# SCORE: 100 %, big O(N + M)
