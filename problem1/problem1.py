# 5-19-2016
# Problem 1: Multiples of 3 & 5
#   Get sum of all multiples of 3 or 5 below 1000
#   https://projecteuler.net/problem=1

if __name__ == "__main__":
  # method: Sieve of Erastosthenes
  maxNum = 1000
  sum = 0
  for i in range(maxNum):
    if i%2 == 0:
      continue
    else:
      

