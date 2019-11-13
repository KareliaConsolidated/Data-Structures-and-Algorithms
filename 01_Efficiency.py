# Which Algo is More Efficient ? 

def some_function(n):
    for i in range(2):
        n += 100
    return n

def other_function(n):
    for i in range(100):
        n += 2
    return n

# `some_function` is more efficient
# Although the two functions have the exact same end result, one of them iterates many times to get to that result, while the other iterates only a couple of times.
# This was admittedly a rather impractical example (you could skip the for loop altogether and just add 200 to the input), but it nevertheless demonstrates one way in which efficiency can come up.

# Counting lines
# With the above examples, what we basically did was count the number of lines of code that were executed. Let's look again at the first function:

def some_function(n):
    for i in range(2):
        n += 100
    return n
# There are four lines in total, but the line inside the for loop will get run twice. So running this code will involve running 5 lines.

# Now let's look at the second example:

def other_function(n):
    for i in range(100):
        n += 2
    return n
# In this case, the code inside the loop runs 100 times. So running this code will involve running 103 lines!

# Counting lines of code is not a perfect way to quantify efficiency, and we'll see that there's a lot more to it as we go through the program. But in this case, it's an easy way for us to approximate the difference in efficiency between the two solutions. We can see that if Python has to perform an addition operation 100 times, this will certainly take longer than if it only has to perform an addition operation twice!

# Now, here's a new function:

def say_hello(n):
    for i in range(n):
        print("Hello!")
# Suppose we call it like this:

say_hello(3)
# And then we call it like this:

say_hello(1000)

# Yes — `say_hello(1000)` will involve running more lines of code.

def say_hello(n):
    for i in range(n):
        for i in range(n):
            print("Hello!")

# Notice that when the input goes up by a certain amount, the number of operations goes up by the square of that amount. If the input is 2, the number of operations is 2^2 or 4. If the input is 3, the number of operations is 3^2 or 9.

# To state this in general terms, if we have an input, nn, then the number of operations will be n^2

# This is what we would call a quadratic rate of increase.

# Let's compare that with the linear rate of increase. In that case, when the input is n, the number of operations is also n.            