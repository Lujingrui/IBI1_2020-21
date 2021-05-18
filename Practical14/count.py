from xml.dom.minidom import parse
import xml.dom.minidom
import re
import matplotlib.pyplot as plt

# Define the variables
count_DNA = 0
count_RNA = 0
count_Protein = 0
count_Oligosaccharide = 0
son_namelist = []
# Input the file and extract specific element
file = xml.dom.minidom.parse("go_obo.xml") 
root_element = file.documentElement
terms = root_element.getElementsByTagName("term")
# Use functions to count.
def counter(x):
 print("============= 	the number of childNodes associated with "+ x +" =============")
 n = 0
 son_namelist1 = [0]
 son_namelist2 = []
 terms = root_element.getElementsByTagName("term")
 fathers = []
 son = []
 global sons
 sons = []
 print("looking for parents ......")
 for term in terms:
     defstr = term.getElementsByTagName('defstr')[0]
     is_a = term.getElementsByTagName('is_a')
     father = term.getElementsByTagNameNS('*','id')[0]
     if re.search(x, defstr.childNodes[0].data):
         fathers.append(father.childNodes[0].data)
 print("The number is : " + str(len(fathers)))
 print("")
 print("looking for sons......")
 for term in terms:
     if term.getElementsByTagNameNS(term.namespaceURI,'is_a') != []:
         son_id = term.getElementsByTagNameNS(term.namespaceURI,'id')[0].childNodes[0].data
         is_a = term.getElementsByTagNameNS(term.namespaceURI,'is_a')
         for item in is_a:
             if item.childNodes[0].data in fathers:
                     son = son_id
                     sons.append(son)
                     break
 print("The first generation have been found")
 print("The number is : " + str(len(sons)))
 print("")
 print("looking for other sons ...")
 while len(son_namelist1) != len(son_namelist2):
     n += 1
     print("Sorry, this takes some patience.")
     print(n)
     son_namelist1 = list(sons)
     for term in terms:
         if term.getElementsByTagNameNS('*','is_a') != []:
             is_a = term.getElementsByTagNameNS(term.namespaceURI,'is_a')
             son_id = term.getElementsByTagNameNS(term.namespaceURI,'id')[0].childNodes[0].data
             for item in is_a:
                 if item.childNodes[0].data in sons:
                     sons.append(son_id)
                     break
     sons = list(set(sons))
     son_namelist2 = sons
     print("Now the number is : "+ str(len(sons)))
     print("")
 print("The results come out.")
 print("The number of childNodes associated with "+x+"  is %s" % len(sons))
 print("")
 return sons

# Get the number of specific items
counter("DNA")
countDNA = len(sons)
counter("RNA")
countRNA = len(sons)
counter("protein")
countProtein = len(sons)
counter("oligosaccharide")
countOligosaccharide = len(sons)

# Demonstrate the final result
print("The result is: ")
print("The DNA number is %s" % countDNA)
print("The Protein number is %s" % countProtein)
print("The RNA number is %s" % countRNA)
print("The Oligosaccharide number is %s" % countOligosaccharide)
        
# Draw the pie chart
explode = (0, 0, 0, 0.1)
number = (countDNA, countProtein, countOligosaccharide,countRNA)
labels = ("count_DNA", "count_Protein", "count_Oligosaccharide", "count_RNA")
colors = ("lightskyblue","pink","yellow","peachpuff")
plt.pie(number, explode=explode,labels=labels, colors=colors, autopct='%1.1f%%', shadow=None, startangle=90)
plt.axis('equal')
plt.title('The proportion of the macromolecule number')
plt.show()
