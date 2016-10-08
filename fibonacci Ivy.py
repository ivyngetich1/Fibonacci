def fib(n):
    num = 1
    currNum = 0
    prevNum = 0

    for counter in range (2,n):
    	prevNum = currNum
    	currNum = num
    	num = prevNum + currNum
    	print (num)
