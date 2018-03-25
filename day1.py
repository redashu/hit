#!/usr/bin/python3

#  supervised ML apple & orange 
import  os
from  sklearn  import tree
# assume smooth == 0 and  bumpy == 1
features=[[120,0],[130,0],[140,1],[150,1]]
label=["apple","apple","orange","orange"]

algo=tree.DecisionTreeClassifier()
trained=algo.fit(features,label)

x=[[133,0]]
output=trained.predict(x)
print(output)
sound="echo  apple  |  festival --tts"
os.system(sound)

if  output == "apple" :
	print("apple show")
	os.system('eog  apple.jpg')
else :
	print("orange show")
	os.system('eog  orange.jpeg')






























'''
import time
import  webbrowser

x=raw_input(" enter first number   ")

#print  type(x)

if  int(x) == 5 :
	print "showing current time"
	print  time.ctime()
elif  int(x) ==  10 :
	print  "opening google.com "
	webbrowser.open_new_tab('https://www.google.com')
else :

	print  "must execute"

y=raw_input(" enter second number   ")
# swaping numbers 
x,y=y,x

print  "plz wait numebers are swapping "
time.sleep(3)

print x
print y
'''
