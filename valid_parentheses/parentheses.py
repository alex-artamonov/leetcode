def isValid(s: str) -> bool:
    brackets = {
        '(': ')',
        '{': '}',
        '[': ']',
        }
    target = []
    previous = ''
    count_open = 0
    for c in s:
        if c in brackets:
            if not previous in brackets:
                target += c + brackets[c]
                print(target)
            else:
                target.insert(count_open, c)
                target.insert(count_open, brackets[c])
        
            count_open -= 1
        previous = c
    
    return ''.join(target) == s

   