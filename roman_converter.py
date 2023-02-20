str_input = input()

def roman(string):
    '''This function converts roman number less than 4000(!)
    to arabic number.
    input is string with roman number
    returns decimal value of this roman number'''

    unnorm_roman = {'IV': '4', 'IX': '9', 'XL': '40', 'XC': '90', 'CD': '400', 'CM': '900'}
    normal_roman = {'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}
    result = 0
    str_arr = list(string)
    if len(string) > 1:
        for i in range(len(str_arr)-1):
            char = str_arr[i]+str_arr[i+1]
            if char in unnorm_roman.keys():
                result += int(unnorm_roman[char])
                i += 1
    new_str = string
    for c in unnorm_roman.keys():
        new_str = new_str.replace(c,'')

    for c in new_str:
        result += int(normal_roman[c])
    return result

print(roman(str_input))