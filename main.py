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


#  print(f.read[1]())
    # fp.seek(0)
    #print(fp.read())


# fp.seek(0)
#   print(fp.read())
    #fp.seek(0)
   # print(fp.read())
