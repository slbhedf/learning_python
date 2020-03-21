# -*- coding: utf-8 -*-

def number_to_strwithcomma(number):
    isminus = number < 0
    if isminus:
        number *= -1
        
    intpart_str = str(int(number))
    i = len(intpart_str) % 3
    number_str = intpart_str[0:i]
    
    if i != 0 and len(intpart_str) > 3:
        number_str += ","
    
    while i+3 <= len(intpart_str):
        number_str += intpart_str[i:i+3]
        if i <= len(intpart_str)-6:
            number_str += ","
        i+=3
    
    if number - int(number) > 0:
        decpart_str = str(number)[len(str(int(number))):]
        number_str += decpart_str
    
    if isminus:
        number_str = "-" + number_str
    
    return number_str
    
if __name__ == '__main__':
    d = 1.2345678901234567890
    while abs(d) < 100000000000:
        print("{:>30}" .format(number_to_strwithcomma(d)))
        d *= 10

    d = -1.2345678901234567890
    while abs(d) < 100000000000:
        print("{:>30}" .format(number_to_strwithcomma(d)))
        d *= 10

# output
#            1.2345678901234567
#            12.345678901234567
#            123.45678901234567
#           1,234.5678901234567
#           12,345.678901234567
#           123,456.78901234567
#          1,234,567.8901234567
#          12,345,678.901234567
#          123,456,789.01234567
#         1,234,567,890.1234567
#         12,345,678,901.234568
#           -1.2345678901234567
#           -12.345678901234567
#           -123.45678901234567
#          -1,234.5678901234567
#          -12,345.678901234567
#          -123,456.78901234567
#         -1,234,567.8901234567
#         -12,345,678.901234567
#         -123,456,789.01234567
#        -1,234,567,890.1234567
#        -12,345,678,901.234568
