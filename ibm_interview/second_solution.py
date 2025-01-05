# Problem Explanation
# You are given n square-shaped chips, with their side lengths provided in the array imageDim. The goal is to determine the maximum number of chips that can be hidden inside other chips based on the following conditions:

# A chip can only be hidden inside another chip if the larger chip’s size is at least k times the smaller chip’s size. Mathematically:
# imageDim[i]
# ×
# 𝑘
# ≤
# imageDim[j]
# imageDim[i]×k≤imageDim[j]
# where imageDim[i] is the smaller chip and imageDim[j] is the larger chip.
# At most one chip can be hidden inside another chip.
# Example:
# Input:
# imageDim = [8, 6, 2, 4, 4, 14]
# k = 3
# Process:
# Chip with size 2 can be hidden inside chip with size 8 because:
# 2
# ×
# 3
# ≤
# 8
# 2×3≤8
# Chip with size 4 can be hidden inside chip with size 14 because:
# 4
# ×
# 3
# ≤
# 14
# 4×3≤14
# Output:
# The maximum number of hidden chips is 2.

# Constraints
# Each chip can only hide one other chip, and a chip can only be hidden once.
# You are required to find the maximum number of chips that can be hidden inside other chips.
# Key Notes:
# The chips should be sorted in increasing order of size to simplify the process.
# Iterate over the smaller chips and find valid larger chips to hide them, ensuring that a larger chip is not reused.

def getMaxHiddenChips(imageDim, k):
    imageDim.sort()
    n = len(imageDim)
    hidden_count = 0
    j = 0
    
    for i in range(n):
        while j < n and (imageDim[i] * k > imageDim[j] or i >= j):
            j += 1
        if j < n:
            hidden_count += 1
            j += 1
    
    return hidden_count
