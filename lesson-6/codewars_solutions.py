# Kata 1. ------Convert a String to an Array------
# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d

def string_to_array(s):
    return s.split()

#kata2 ----Given a list of numbers, return the sum of only the positive ones.
#Ignore 0 and negatives.

#-https://www.codewars.com/kata/5715eaedb436cf5606000381
#notes 
# positive_sum([1, -4, 7, 12]) ➜ 20
#positive_sum([-1, -2, -3, -4]) ➜ 0
#positive_sum([]) ➜ 0
def positive_sum(arr):
    return sum(x for x in arr if x > 0)

#Kata3 -----Given a list, return a new list with all duplicates removed.
#Preserve the original order of first appearances.-------
# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118

def distinct(seq):
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
