def isValid0(s: str) -> bool:
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
                # print(target)
            else:
                target.insert(count_open, c)
                target.insert(count_open, brackets[c])
        
            count_open -= 1
        else:
            # print('hi from else: ', target)
            count_open -2

        previous = c
    
    return ''.join(target)


def isValid1(s: str) -> bool:


    brackets = ['{}',
                '()',
                '[]',
                ]

    if not any(ele in s for ele in brackets):
        return s == ''
    else:
        for ele in brackets:
            if ele in s:
                return isValid(s[:s.index(ele)] + s[s.index(ele) + 2:])
            

def isValid(s: str) -> bool:


    brackets = ['{}',
                '()',
                '[]',
                ]
    test = s
    while any(ele in test for ele in brackets):
        for ele in brackets:
            if ele in test:
                test = (test[:test.index(ele)] + test[test.index(ele) + 2:])
                print(test)


    return test == ''



print(isValid("(([]){})"))
print(isValid(''))
print(isValid('['))
    





                                
   