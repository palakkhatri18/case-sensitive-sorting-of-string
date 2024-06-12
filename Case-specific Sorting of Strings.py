# Given a string S consisting of only uppercase and lowercase characters. The task is to sort uppercase and lowercase letters separately such that if the ith place in the original string had an Uppercase character then it should not have a lowercase character after being sorted and vice versa.
#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        #code here
        lower_chars = []
        upper_chars = []
        
        # Separate the characters into the respective lists
        for char in s:
            if char.islower():
                lower_chars.append(char)
            elif char.isupper():
                upper_chars.append(char)
        
        # Sort the lists individually
        lower_chars.sort()
        upper_chars.sort()
        
        # Create iterators for the sorted lists
        lower_iter = iter(lower_chars)
        upper_iter = iter(upper_chars)
        
        # List to hold the final result
        result = []
        
        # Reconstruct the string by placing sorted characters back into original positions
        for char in s:
            if char.islower():
                result.append(next(lower_iter))
            elif char.isupper():
                result.append(next(upper_iter))
        return "".join(result)        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends