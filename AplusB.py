// Write a function that add two numbers A and B without using the operater "+"


class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb(self, a, b):
        # write your code here
        while b:
            a, b = (a^b) & 0xFFFFFFFF, ((a&b)<<1) & 0xFFFFFFFF
        return a
        
    # a^b -> all the different bits(which won't produce any carry bits)
    # a&b -> all the '1' and '1' bits. which will profuce carry bits. Therefore left shift one bit.
    # due to some issue with Python's automatic type casting, we next extra work like "& 0xFFFFFFFF" to limit the result within 32bits.
    
        
        
        
        
