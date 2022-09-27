name = 'maliya'
f = open('/Users/chenxiwang/Desktop/newf/maliya.txt', 'w+')
print(name, file=f)
f.seek(4)
print(f.read())
f.close()

fp = open('/Users/chenxiwang/Desktop/newf/maliya.txt', 'a+')
print(name + 'LOL', file=fp)
fp.seek(3)
print(fp.readlines()[1])
fp.close()

a = 10
b = 20
print('before exchange', a, b)
a, b = b, a
print('after exchange', a, b)
print('is a > b?', a > b is not True)
#b += 1
c = a, b
print(a & b)
print(a | b)
print(a ^ b)
print(c[1])
if a > b:
    print("hey")
elif a == b:
    print("yo")
else:
    print("ハニャァァァ")

#  print(f.read[1]())
    # fp.seek(0)
    #print(fp.read())


# fp.seek(0)
#   print(fp.read())
    #fp.seek(0)
   # print(fp.read())
