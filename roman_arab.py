romans = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}

special_cases = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']

# ordered = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV', 'M', 'D', 'C', 'L', 'X', 'V', 'I']

def roman_to_int(s: str) -> int:
    if not (1 <= len(s) <= 15):
        raise ValueError
    for char in s:
        if char not in romans:
            raise ValueError
    output = 0
    for item in special_cases:
        if item in s:
            output += romans[item]
            s = s[:s.index(item)] + s[s.index(item) + 2:]
    
    output += sum((romans[it] for it in s))
    return output


