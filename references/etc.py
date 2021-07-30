#10진수 -> 2진수, 8진수, 16진수
convert = 32
#방법1
convertBinary = bin(convert)
convertOct = oct(convert)
converHex = hex(convert)
print(convertBinary, convertOct, converHex, type(convertBinary))

#방법2
convertBinary = format(convert, 'b')
convertOct = format(convert, 'o')
converHex = format(convert, 'x')
print(convertBinary, type(convertBinary))

