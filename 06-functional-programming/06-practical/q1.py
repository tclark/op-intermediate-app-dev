# The function doubler() below is not a pure function. Explain why. Then,
# write the function pure_doubler() below the returns the same results but
# in a purely functional way

def doubler(ls):  # note that ls is a list
    for i in range(len(ls)):
        ls[i] = ls[i] * 2
    return ls

def pure_doubler(ls):
    pass

nums = [1, 2, 3, 4]
print(doubler(nums))
print(nums)

pure_nums = [1, 2, 3, 4]
print(pure_doubler(pure_nums))
print(pure_nums)

# Explain why the function doubler() is not pure.
