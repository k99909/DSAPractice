#Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.
#Be sure to return the indices, not the elements themselves.
#There is guaranteed to be one such pair whose product is the target.

# def pair_product(numbers, target_product):
#     previous_nums = {}
#     for index, number in enumerate(numbers):
#        complement = target_product / number

#        if complement in previous_nums:
#            return (index, previous_nums[complement])

#        previous_nums[number] = index
           

# #test_00:
# print(pair_product([3, 2, 5, 4, 1], 8)) # -> (1, 3)
# #test_01:
# print(pair_product([3, 2, 5, 4, 1], 10)) # -> (1, 2)
# #test_02:
# print(pair_product([4, 7, 9, 2, 5, 1], 5)) # -> (4, 5)
# #test_03:
# print(pair_product([4, 7, 9, 2, 5, 1], 35)) # -> (1, 4)
# #test_04:
# print(pair_product([3, 2, 5, 4, 1], 10)) # -> (1, 2)
# #test_05:
# print(pair_product([4, 6, 8, 2], 16)) # -> (2, 3)


# intersection
# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.

def intersection(a, b):
    common_nums = []
    a_dict = {}

    for num in a:
        a_dict[num] = True

    for num in b:

        if num in a_dict:
            common_nums.append(num)

    return common_nums

# test_00:
print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]
# test_01:
print(intersection([2,4,6], [4,2])) # -> [2,4]
# test_02:
print(intersection([4,2,1], [1,2,4,6])) # -> [1,2,4]
# test_03:
print(intersection([0,1,2], [10,11])) # -> []
# test_04:
a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
print(intersection(a, b)) # -> [0,1,2,3,..., 49999]