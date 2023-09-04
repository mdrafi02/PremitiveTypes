number = int(input("Enter the number:"))
num = number
numBits = 0

while num:
    num ^= num & ~(num - 1)
    numBits += 1
    
print(f"number of bits set to 1 in {number} are {numBits}")