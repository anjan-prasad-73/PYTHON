tuples = [(1,'a'), (2,'b'), (3,'c')]

nums, chars = zip(*tuples) # * separates the tuple and zip collects the values [1,2,3] and ['a','b','c']

print(list(nums), list(chars))  