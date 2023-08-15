"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


def two_sum(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return i, j


# Get input from the user and split it into a list
input_string = input("Enter elements of the list separated by spaces or commas: ")

# Split the input_string into a list using either spaces or commas as separators
input_list = input_string.split()  # This creates a list of strings

# If you want to convert the input elements to integers
input_list = [int(item) for item in input_list]

target = int(input("Enter the target: "))

print(two_sum(input_list, target))
