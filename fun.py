import os 
k=os.popen("ifconfig").read()
print(k)
