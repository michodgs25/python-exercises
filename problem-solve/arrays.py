# Arrays are one of the fundamental data structures in computer science.
# An Array is represented as a fixed sized, contiguous block of memory,
# with 0(1) time to store and access an element.

# Because of this efficiency, many other data structures frequently use arrays,
# for their implementation, such as strings, stacks, queues, and hash tables.

# Picture an array as a bounded row of labelled containers, starting at 0,
# where you can quickly put items in, take them out,
# or look up a value from an index or label.

# |_0_|_1_|_2_|_3_|_4_|_5_|_6_|_7_|

# In the diagram above, we have an array of 8.
# We can set and get the value associated with the third index in constant time,
# using the following operations:

array[2] = 'foo'

x = array[2] # 'foo'

# Arrays do have some limitations.
# Looking an element up by value typically requires an entire traversal of the array,
# unless it is sorted in some way.
# Deleting an element from an array means that all subsequent elements have to be shifted left by one,
# leading an an O(n) time operation.
# If possible it is better to overwrite the value.
# Similarly, inserting an element early in the array requires the rest of the elements to shift right,
# so this should be done sparingly.

# Arrays have a fixed bound, which means they may not be suitable for applications,
# where the size of the collection of elements is not known ahead of time.

# In an interview setting, be careful of one off errors that lead to trying to access an element,
# outside the range of the array.

# Python does not have native support for arrays, typically you'll use the list data structure,
# which dynamically resizes under the hood.
# What this means is that to you, the developer, it seems like the list is unbounded.
# In reality, as the list grows, the data structure may allocate a larger(typically twice the size) array,
# copy all it's elements to the larger one, and then use that as the underlying array.


#                     Common array interview questions 1.1

#  Given an array of integers, return a new array, such that each element at index i of the new array,
#        is the product of all the numbers in the original array except the one at i.


# for example, if input: [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]
# If our input was [3, 2, 1], the expected output would be [2, 3, 6]


#                                   Solution

# This problem would be easy with division:
# an optimal Solution could just find the product of all the numbers in the array, and then divide by each of the numbers.

# To solve this without division, we will rely on a common technique in array problems:
#          precomputing results from subarrays, and building up a solution from those results.
#          To find the value associated with i'th element, we must compute the product of all numbers before i and the product of all number after i.
#          If we could efficiently calculate these two, we can multiply them out to get the desired product.

# In order to find the product of numbers before i, we can generate a list of prefix products.
# Specifically, the i'th element in the list will be a product of all numbers including i.
# We can generate, a list of suffix products.
# For each index we can multiply the appropriate prefix and suffix values to obtain our solution.


def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result from the product of prefixes and suffixes
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(
                prefix_products[i - 1] * suffix_products[i + 1]
            )
    return result

# This runs in O(n) time and space,
# since iterating over the input array O(n) time and the prefix and suffix arrays take up O(n) space.
