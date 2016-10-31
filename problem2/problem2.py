# Problem 2: Even fibonacci numbers
#   Sum of even-valued terms of numbers in fibonacci seq. that
#   do not exceed four million
#   https://projecteuler.net/problem=2

if __name__ == "__main__":
    i = 1
    j = 2
    sumVal = 0
    while j < 4000000:
        sumVal += (j if j%2==0 else 0)
        temp = j
        j += i
        i = temp

    print sumVal

