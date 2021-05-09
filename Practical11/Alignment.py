a = open('RandomSeq.fa','r')
b = open('SOD2_mouse.fa','r')
c = open('SOD2_human.fa','r')
for i in a:
 if i.startswith('>') != True:
  a = i.strip()
for i in b:
 if i.startswith('>') != True:
  b = i.strip()
for i in c:
 if i.startswith('>') != True:
  c = i.strip()
edit_distance1 = 0
for i in range(len(a)):
 if a[i]==b[i]:
  edit_distance1 += 1
edit_distance2 = 0
for i in range(len(b)):
 if b[i]==c[i]:
  edit_distance2 += 1
edit_distance3 = 0
for i in range(len(c)):                                                          
 if c[i]==a[i]:
  edit_distance3 += 1
percentage1 = edit_distance1/len(a)*100
percentage2 = edit_distance2/len(a)*100
percentage3 = edit_distance3/len(a)*100
print(str(edit_distance1) + ' ' + str(percentage1) + '%' + '\n' + str(edit_distance2) + ' ' + str(percentage2) + '%' + '\n' +str(edit_distance3) + ' ' + str(percentage3) + '%')



