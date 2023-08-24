# Jack Bianca COMP 3240 Programming Assignment 2
class Assignment2_Python(object):
    ''' This method should accept the number to test and the maximum number of iterations
        to try before halting execution. If num is NOT magic (or the maximum number
        of iterations has been reached), return (-1 \tnum) (i.e., the negative of num).
        If num IS magic, return the number of iterations it took to reduce num to 1.
     
        Remember that a number is magic if it can be reduced to 1 by dividing it by 2 if
        it is even or multiplying it by 3 and adding 1 if it is odd.
        '''
    @staticmethod
    def IsMagic(num: int, max_iterations: int) -> int:
        iterations = 0
        while num != 1:
            if num % 2 == 0:
                num = num / 2
                iterations += 1
            else:
                num = num * 3 + 1
                iterations += 1
            if iterations > max_iterations:
                return (-abs(num))
        return iterations
        

    ''' This method should be used to check if each number in the range [start, stop]
        is a magic number. If all numbers in the range are magic, return the number of
        iterations that it took to reduce the number passed into "stop" to 1. If you 
        find a number that is NOT magic, this method should return the negative of
        that number.
        '''
    @staticmethod
    def TestRange(start: int, stop: int, max_iterations: int) -> int:
        num_iterations = 0
        count = 0

        for num in range(start, stop+1):
            count = Assignment2_Python.IsMagic(num, max_iterations)
        return count
    
start = 5
stop = 20
max_iterations = 500

result = Assignment2_Python.TestRange(start, stop, max_iterations)
print(result)