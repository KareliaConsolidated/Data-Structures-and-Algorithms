import time

def addUpTo(n):
	start = time.time()
	total = 0
	for i in range(1, n+1):
		total += i
	end = time.time()
	return f"Total is {total} || Elapsed Time: {(end - start)/1000}"

addUpTo(100000)	

def addUpToSmooth(n):
    start = time.time()
    total = n * (n+1) / 2 
    end = time.time()
    return f"Total is {total} || Time Elapsed: {(end - start)/1000} seconds"

addUpToSmooth(100000)    

def logAtLeast5(n):
    for i in range(1, max(5, n+1)):
        print(i)

def logAtMost5(n):
    for i in range(1, min(5, n+1)):
        print(i)