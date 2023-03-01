import matplotlib.pyplot as plt
import numpy as np


#tmp = "0a:0f:0a:0f:0a:0f:0a:0f:0a:0f:0a:0e"
tmp = "0c:0f:0a:0f:0a:0f:0a:0f:0a:0f:0a:0e"

binr=[]
res=[]
hist=[]
hex= tmp.split(":")
for i in range(0,len(hex)):
    conv_c = bin(eval('0x'+hex[i]))
    conv_c = conv_c.replace('0b','')
    binr.append(conv_c)
for i in range(0,len(binr)):
    res.append([])
    for j in range(0,4):
        res[i].append(binr[i][j])

for i in range(0,len(res[0])):
    sum = int(0)
    for j in range(0,len(res)):
        sum+=int(res[j][i])
    hist.append(sum)



print(hist)
a = np.random.randint(100, size =(50))
 
# Creating plot
fig = plt.figure(figsize =(10, 7))
 
plt.hist(hist, bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12 ])
 
plt.title("Decoded Histogram") 

# show plot
plt.show()

