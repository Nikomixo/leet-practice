# Given a string `s`, find the length of the longest without duplicate characters.

def lengthOfLongestSubstring(s: str) -> int:
    longestString = 0
    tempString = ""

    for j in s:
        # if j is found in temp substring, we set temp to the substring of temp [j:].
        # else add j to substring
        tempString = tempString[tempString.index(j)+1:] + j if j in tempString else tempString + j
        #check if temp is longer than previous substrings
        longestString = longestString if longestString > len(tempString) else len(tempString)

    return longestString

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkewabcdef"))
print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("a"))
print(lengthOfLongestSubstring("dvdf"))
