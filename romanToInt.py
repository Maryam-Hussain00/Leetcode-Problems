def roman(s):
    key ={
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    for char in s:
        if char not in key:
            print("Invalid entry")
            return "Write valid roman numerals"
    result = 0
    length = len(s)
    for i in range(length):
        if i < length-1:
            if( key[s[i]]< key[s[i+1]]):
                result -= key[s[i]]
            else:
                result += key[s[i]]
        else:
            result += key[s[i]]
    return result

str = input("Enter a valid roman numeral in capital alphabets: ")
print(roman(str))
