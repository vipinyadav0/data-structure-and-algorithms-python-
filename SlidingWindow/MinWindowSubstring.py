'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

'''
def minWindow(self, s:str, t: str) -> str:
    
    if t == "":
        return ""
    countT , window = {}, {}
    for c in t:
        countT[c] = countT.get(c, 0) + 1
    l, min_len, min_start = 0, float('inf'), 0
    
    for r in range(len(s)):
        if s[r] in countT:
            window[s[r]] = window.get(s[r], 0) + 1
            if window[s[r]] == countT[s[r]]:
                while s[l] not in countT or window[s[l]] > countT[s[l]]:
                    if s[l] in countT:
                        window[s[l]] -= 1
                    l += 1
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_start = l
        if r - l + 1 == min_len:
            return s[min_start:min_start+min_len]