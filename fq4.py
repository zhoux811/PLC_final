a, b, c, d, e = 51, 7, 11, 13, 2

print('sq1: ' + str(a * b - 1 + c))  # sq1: 367
print('sq2: ' + str(((b - 1) * a) / (c % d)))  # sq2: 27.818181818181817
# print('sq3: '+str((a - b) / (c & ((d * e) / (a - 3)))))
print('sq4: ' + str(((a + b) <= c) * (d > (b - e))))  # sq4: 0
print('sq5: ' + str(((-a) or c) == (d and e)))  # sq5: False
print('bitwise sq6: ' + str((((a > b) ^ c) | (d <= 17))))  # bitwise sq6: 10
print('logical sq6: ' + str((((a > b) ^ c) or (d <= 17))))  # logical sq6: 10
print('sq7: ' + str(-(a + b)))  # sq7: -58
print('sq8: ' + str(((a + (b * c)) + d)))  # sq8: 141
# print('sq9: ' + str((a + 1) + 1))



print(13 and 2)
print(-51 or 2)