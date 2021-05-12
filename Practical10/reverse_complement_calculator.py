seq = input("seq: ")
def f(seq):
    translation = {'A':'T','T':'A','G':'C','C':'G'}
    new_seq = ''
    for n in range(0,len(seq),1):
        new_seq = translation[seq[n]] + new_seq
    print("reverse complement: " + new_seq)
f(seq)
  

