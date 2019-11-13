# When describing the efficiency of an algorithm, we could say something like "the run-time of the algorithm increases linearly with the input size". This can get wordy and it also lacks precision. So as an alternative, mathematicians developed a form of notation called big O notation.

# The "O" in the name refers to the order of the function or algorithm in question. And that makes sense, because big O notation is used to describe the order—or rate of increase—in the run-time of an algorithm, in terms of the input size (n).

# We've been approximating efficiency by counting the number of lines of code that get executed. But when we are thinking about the run-time of a program, what we really care about is how fast the computer's processor is, and how many operations we're asking the processor to perform. Different lines of code may demand very different numbers of operations from the computer's processor. For now, counting lines will work OK as an approximation.

# Space Complexity Examples
# When we refer to space complexity, we are talking about how efficient our algorithm is in terms of memory usage. This comes down to the datatypes of the variables we are using and their allocated space requirements. In Python, it's less clear how to do this due to the the underlying data structures using more memory for house keeping functions (as the language is actually written in C).

# For example, in C/C++, an integer type takes up 4 bytes of memory to store the value, but in Python 3 an integer takes 14 bytes of space. Again, this extra space is used for housekeeping functions in the Python language.

# For the examples of this lesson we will avoid this complexity and assume the following sizes:

# Type	Storage size
# char	1 byte
# bool	1 byte
# int	4 bytes
# float	4 bytes
# double	8 bytes
# It is also important to note that we will be focusing on just the data space being used and not any of the environment or instructional space.