print(3+1*5)
#将数据输出文件中，注意点，1，所指定的盘符存在，2.使用file=fp
fp=open('D:/text1.txt','a+')
print('hello world',file=fp)
fp.close()

#不进行换行输出
print('hello','word','Python')
fb=open('D:/text5','a+')

fc=open('D:/dd.txt','a+')
print('你就是个弟弟',file=fc)
fc.close()

