list=[i*i for i in range(1,10)]
print(list)

#list=[i for in range(1,100)]
l=[i for i in list if i%2==0]
print(l)

dict={i:i for i in range(1,100) if i%2==0}
print(dict)

#tuple compression is not supported

d={i*1:i*2+1 for i in range(1,20)}
print(d)