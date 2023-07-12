import random

def extend_array(nums:list[int],enlarge:int) ->list[int]:
    res = [0]*(len(nums)+enlarge)
    for i in range(len(nums)):
        res[i]=nums[i]

    return res

def insert(nums:list[int],num:int,index:int)->None:
    for i in range(len(nums)-1,index,-1):
        nums[i]=nums[i-1]
    nums[index]= num

def remove(nums:list[int],index:int)->None:
    for i in range(index,len(nums)-1):
        nums[i]=nums[i+1]

def traberse(nums:list[int])->None:
    count = 0
    # 通过索引遍历数组
    for i in range(len(nums)):
        count+=1
    
    # 直接遍历数组
    for num in nums:
        count+=1

    # 同时遍历数组索引和元素
    for i,num in enumerate(nums):
        count+=1

def find(nums:list[int],target:int)->int:
    for i in range(len(nums)):
        if(nums[i]==target):
            return i
    return -1
