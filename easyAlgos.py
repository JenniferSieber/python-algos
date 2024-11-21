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
