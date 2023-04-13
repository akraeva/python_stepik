n = int(input())
string = 'программист'
end_str = ''

if 1 < n % 10 < 5 :
    end_str = 'а'
if 4 < n % 10 < 10 or n % 10 == 0 or 10 < n % 100 < 20 :
    end_str = 'ов'

print (n, string + end_str)