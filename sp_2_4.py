s = 'abcdefghijk'
res = ''
res += s[3:6] + ' '
res += s[:6] + ' '
res += s[3:] + ' '
res += s[::-1] + ' '
res += s[-3:] + ' '
res += s[:-6] + ' '
res += s[-1:-10:-2] + ' '
print(res)