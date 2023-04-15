a = int(input())
b = int(input())
d = 1

#брутфорс вместо поиска простых чисел :( 
while d % a != 0 or d % b !=0 : 
    d += 1

print(int(d))