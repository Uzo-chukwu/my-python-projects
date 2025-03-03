

def plus_one(digits):
    for count in range(len(digits) - 1, -1, -1):
        if digits[count] == 9:
            digits[count] = 0
        else:
            digits[count] += 1
            return digits
    return [1] + digits

print(plus_one([9,9,9,9]))
print(plus_one([1,2,3,4]))