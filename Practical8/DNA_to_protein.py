seq = 'ATGCGACTACGAGGGCC'
protein = '' 
genes = {'ATG':'M', 'CGA':'R', 'CTA':'L', 'TCG':'S', 'AGG':'R', 'GCC':'A'} 
for n in range (0,len(seq),3):
 if seq[n:n+3] in genes:
  protein = protein + genes[seq[n:n+3]]
print(protein)
 
