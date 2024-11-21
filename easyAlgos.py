# Valid Anagram 
# solution creating hashmap
def valid_anagram_01(s,t):
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    # Iterate and validate the hashmaps
    for c in countS:
        if countS[c] != countT.get(c, 0):
          return False
    return True
print(valid_anagram_01('anagram', 'nagaram'))
print(valid_anagram_01('rat', 'car'))

# solution using Counter
from collections import Counter
def valid_anagram_02(s, t):
    return Counter(s) == Counter(t)
print(valid_anagram_02('anagram', 'nagaram'))
print(valid_anagram_02('rat', 'car'))


# solution using sorted
def valid_anagram_03(s, t):
    return sorted(s) == sorted(t)
print(valid_anagram_03('anagram', 'nagaram'))
print(valid_anagram_03('rat', 'car'))

######################
# Valid Palidrome
# solution 1 # built in functions using extra memory
def validPalindrome(s):
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    # compare newStr to newStr reversed
    return newStr == newStr[::-1]

print(validPalindrome("hannah"))
print(validPalindrome("racecar"))
print(validPalindrome("race a car"))
print(validPalindrome("A man, a plan, a canal: Panama")) #amanaplanacanalpanama

# solution 2 --- implement the above modules within code and not using extra memory O(1)
# sliding window Pointer pattern
# deal with spaces and non alphanumerics and convert to lower()
# USE ASCII printable characters to determine if alphanumeric
# Acceptable ASCII codes: --- create helper Function
# A = 65 to Z = 90  || a= 97 to z=122 ||  0 = 48 to 9 = 57
# create while loop  to skip spaces  while character isAlphaNumeric() increment left ++
# Time: O(n) Space: O(1) no extra memory
# alphanumeric helper function
def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

def isPalindrome(s):
    # assign l/r pointers
    l, r = 0, len(s) - 1
    
    # iterate & move pointers validate
    while l < r:
        # validate alphanumeric while not out of bounds -increment/decrement
        while l < r and not alphaNum(s[l]):
          l += 1
        while r > l and not alphaNum(s[r]):
          r -= 1
        if s[l].lower() != s[r].lower(): 
            return False
        # update l/r for increment/decrement
        l, r = l + 1, r - 1
    return True
print("isPalindrome without modules")
print(isPalindrome("hannah"))
print(isPalindrome("racecar"))
print(isPalindrome("race a car"))
print(isPalindrome("A man, a plan, a canal: Panama")) #amanaplanacanalpanama

######################
# Replace Elements with Greatest Element on Right Side (LC1299)
def replaceElements(arr):
    rightMax = -1
    for i in range(len(arr) - 1, -1, -1):
        newMax = max(rightMax, arr[i])
        arr[i] = rightMax
        rightMax = newMax  
    return arr
print(replaceElements([17,18,5,4,6,1]))
#############################
