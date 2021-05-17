fhand = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa') 
import re
lines = ''
result = ''
b = '' 
x = False
for line in fhand:
 if line.startswith('>'):
   if x == True:
    result = result + str(b) + "   " + str(len(lines)) + '\n' + lines + '\n'
    lines = ''
    b = ''
    x = False
   if 'unknown' in line:
     b = re.findall(r'>(.+?)_mRNA',line)
     b = b[0]
     x = True
 else:
   if x == True:
     lines = lines + line.rstrip()
fhand.close()
output = open('unknown_function.fa','w')
output.write(result)
output.close()

