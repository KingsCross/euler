# Problem 1: Multiples of 3 & 5
#   Get sum of all multiples of 3 or 5 below 1000
#   https://projecteuler.net/problem=1

if __name__ == "__main__":
  maxNum = 1000
  sum = 0
  multiples_list = [3,5]
  for i in range(maxNum):
    for num in multiples_list:
    	if i%num == 0:
      		sum+=i
      		# number only needs to be checked to see if 
      		# it's a multiple of one number in the list
      		break

print sum 



    

      

