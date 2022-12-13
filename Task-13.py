#Task-1
def test():
    x = 1
    y = 2
    str1= "hello"


print(test.__code__.co_nlocals)



#Task-2
def test(a):
        def add(b):
                nonlocal a
                a += 1
                return a+b
        return add
func= test(20)
print(func(1))


#Task-3
nums1 = [1, 2, 3, 4, 5,-10,2000,-9999,110]

nums2 = [1, -2, 3, -4,5,0,12,22]


def choose_func(nums: list, func1,func2):
    if func1 == square_nums:
        res = square_nums(nums)
        print(res)
    else:
        res_1 = remove_negatives(nums)
        print(res_1)
    


def square_nums(nums):
    return [num ** 2 for num in nums]

             
def remove_negatives(nums):
    return [num for num in nums if num > 0]



choose_func(nums1,square_nums, remove_negatives) 
choose_func(nums2,remove_negatives,square_nums)