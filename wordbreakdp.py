# Function to determine if a string can be segmented into space-separated
# sequence of one or more dictionary words
def wordBreak(dict, str, lookup):
 
    # `n` stores length of the current substring
    n = len(str)
 
    # return true if the end of the string is reached
    if n == 0:
        return True
 
    # if the subproblem is seen for the first time
    if lookup[n] == -1:
 
        # mark subproblem as seen (0 initially assuming string
        # can't be segmented)
        lookup[n] = 0
 
        for i in range(1, n + 1):
            # consider all prefixes of the current string
            prefix = str[:i]
 
            # if the prefix is found in the dictionary, then recur for the suffix
            if prefix in dict and wordBreak(dict, str[i:], lookup):
                # return true if the string can be segmented
                lookup[n] = 1
                return True
 
    # return solution to the current subproblem
    return lookup[n] == 1
 
 
# Word Break Problem Implementation in Python
if __name__ == '__main__':
 
    # List of strings to represent a dictionary
    # we can also use a Trie or a set to store a dictionary
    dict = ["self", "th", "is", "famous", "Word",
            "break", "b", "r", "e", "a", "k", "br",
            "bre", "brea", "ak", "problem"]
 
    # input string
    str = "Wordbreakproblem"
 
    # lookup table to store solutions to subproblems
    # `lookup[i]` stores if substring `str[n-i…n)` can be segmented or not
    lookup = [-1] * (len(str) + 1)
 
    if wordBreak(dict, str, lookup):
        print("The string can be segmented")
    else:
        print("The string can't be segmented")
