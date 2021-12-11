# LINK: https://app.codility.com/programmers/lessons/2-arrays/
# PROBLEM:
# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).
#
# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
#
# Write a function:
#
# def solution(A, K)
#
# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
#
# For example, given
#
#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:
#
#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given
#
#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0]
#
# Given
#
#     A = [1, 2, 3, 4]
#     K = 4
# the function should return [1, 2, 3, 4]
#
# Assume that:
#
# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment
#


# TAKE 1)

def solution(A, K):
    if K > len(A):
        K = K % len(A)

    temp_array = A * 2

    temp_counter = 0
    array_counter = 0

    for i in temp_array:

        if temp_counter >= K:

            if len(A) == K:
                break

            A[array_counter] = temp_array[temp_counter - 1]

            array_counter += 1

            if array_counter >= len(A):
                break

        temp_counter += 1

    return A

# RESULT: 12%
# COMMENT: approach was far from ideal - the whole conpcept of iterating over a 'doubled' array and shifting was bad. Retry fresh tomorrow


# TAKE 2
def solution(A, K):

    # code will break if A is an empty array. Just return it then
    if len(A) == 0:
        return A

    # solve for cases when K>len(A)
    K = K % len(A)

    # pretty simple actually
    return A[-K:] + A[:-K]

# RESULT: 100%
# COMMENT: facepalm because I didnt think of this in the first try