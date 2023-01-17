'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "". 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings. 

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

def longest_common_prefix(strs):
    
    min_len = min([len(word) for word in strs])
    for word in strs:
        if len(word) == min_len:
            shortest = word
            break
    
    strs = strs[:strs.index(shortest)] + strs[strs.index(shortest) + 1:]
    
    if not shortest:
        return ''

    if not all([word.startswith(shortest[0]) for word in strs]):
        return ''
    prefix = ''


    i = 1
    for chr in shortest:
        if all([word.startswith(prefix) for word in strs]):
            prefix = shortest[:i]
            i += 1            
        else:            
            return prefix[:-1]
            # print(f"from else: {i=} {prefix=}")

    return prefix

strs = ["flower","flower","flower","flower", "flower"]
strs = ['flight', "flow","flower"]
if __name__ == '__main__':
    print(longest_common_prefix(strs))