def complement(seq):
    compl={'A':'T','C':'G','G':'C','T':'A'}
    cseq=''
    i=len(seq)-1
    while i>=0:
        cseq=cseq+compl.get(seq[i], 'N')
        i-=1
    return cseq
print(complement("ATGCCGTATAGC"))
