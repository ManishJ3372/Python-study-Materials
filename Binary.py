# f=open("C:/Users/manis/Desktop/py/1.jpg","rb")
# f1=open("demo.jpg","wb")
# for i in f:
#     f1.write(i)

f1=open("C:/Users/manis/Desktop/py/1.jpg","rb")
f2=open("demo1.jpg","wb")
bytes=f1.read()
f2.write(bytes)
