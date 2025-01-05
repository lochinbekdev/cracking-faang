# Problem Statement for the First Problem
# Title: Count Non-Unique Elements in an Array

# Problem Description: You are given an integer array numbers of size n. Your task is to determine how many unique elements occur more than once in the array.

# Input:

# An integer n (3 <= n <= 1000), representing the size of the array numbers.
# An array numbers of size n containing integers (1 <= numbers[i] <= 1000).
# Output:

# An integer representing the count of elements that appear more than once in the array.
# Example Input:

# plaintext
# 8
# 1 3 1 4 5 6 3 2
# Example Output:

# plaintext
# 2
# Explanation:

# In the given array, the elements 1 and 3 occur more than once.
# Therefore, the output is 2.
# Constraints:

# The size of the array numbers is at least 3 and at most 1000.
# Each element in the array is between 1 and 1000 inclusive.
# Note:

# The input is read from standard input in the following format:
# First line contains an integer n.
# The next n lines contain one integer each, representing the elements of the array.

def countDuplicate(numbers):
    n = len(numbers)
    checked = []
    duplicate_count = 0

    for i in range(n):
        if numbers[i] not in checked:
            count = 0
            for j in range(n):
                if numbers[i] == numbers[j]:
                    count += 1
            if count > 1:
                duplicate_count += 1
            checked.append(numbers[i])

    return duplicate_count