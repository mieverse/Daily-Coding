# 1

def result(lis, k):
  p = 0
  q = len(lis)  #4
  for i in range(0,q):
    p=i+1
    while p <= (q-1): #3
      sum = lis[i] + lis[p]
      p+=1
      if sum == k:
        return True
      else:
        return False

a = [10, 15, 3, 7]
b = 16
result(a,b)
