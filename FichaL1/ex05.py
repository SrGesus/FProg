from math import sqrt

def deviation(nums, average):
    temp = []
    for i in range(len(nums)):
        temp.append((nums[i] - average)**2)
    return sqrt(sum(temp) /4)

def inputmany(number):
    nums = []
    for i in range(number):
        print("Introduza o ", i+1,"º número : ", sep='')
        nums.append(int(input()))
    return nums

nums = inputmany(5)
average = sum(nums) / len(nums)
desvio = deviation(nums, average)
print("Números :", nums)
print("Média :", average)
print("Desvio padrão: ", desvio)

