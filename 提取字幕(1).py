# -*- coding:utf-8 -*-
import re
x=input('Enter the name of doc!\n')
f = open(x, "r")
content = f.read()
f.close()
for line in content.split('\n'):
    fields = line.split(',,')
    sentence = fields[len(fields)-1]
    sentence = sentence.replace(r'\N{\fs14}', '\n')
    new_name=x.replace('.ass','.txt')
    new=open(new_name,'a')
    new.write(sentence+'\n')
print('Finished!')
