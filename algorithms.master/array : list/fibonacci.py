# 0 1 1 2 3 5 8 13 ..

# print fibanacci series
def fib(n):

    series = []

    for i in range(n):
        if i==0 or i==1:
            series.append(i)
        else:
            series.append(series[i-1]+ series[i-2])



fib(1)

def fibR(n):
 if n==1 or n==2:
  return 1
 return fibR(n-1)+fibR(n-2)
print fibR(5)
