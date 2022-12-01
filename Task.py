#Task-1
def detect():
    x = 1
    y = 2
    z = 3
    str1= "test"
    print("Work")

print(detect.__code__.co_nlocals)


detect()

#Task-2
def first(a):
    def second(b):
        nonlocal a
        a +=1
        return a+b

    return second

f = first(4)
print(f(4))


#Task-3

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]

def choose_func(nums: list, func1, func2):
    print(func1(nums))
    print(func2(nums))



choose_func(nums2,remove_negatives,square_nums)









