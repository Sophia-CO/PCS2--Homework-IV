s='ATGCCTTATGCCTTTGATGCCTTGTTCATGCCTTTCATGCCTTAATGCCTTGATGCCTTATGCCTTCCACATGCCTTTATGCCTTGCGATGCCTTCGGTATGCCTTGCGCGCGATGCCTTCCAATGCCTTCTATGCCTTGCCGATGCCTTGGTATGCCTTATGCCTTGATGCCTTCATGCCTTCGATGCCTTTAATGCCTTAATGCCTTATGCCTTTTCATGCCTTTTATGCCTTATGCCTTTATGCCTTGAATGCCTTCTGGCATGCCTTATGCCTTTATGCCTTAGACCAGATGCCTTAGAAGATGCCTTATGCCTTATGCCTTGCCACACATGCCTTTGAGATGCCTTATGCCTTAACATATATGCCTTAGGACCAACGAGATAAACGTTCATGCCTTTACCGCAATGCCTTATGCCTTTATGCCTTGATGCCTTCATGCCTTGTGGCCTCGATCGCGGCTGACAATGCCTTGTAATGCCTTAATGCCTTCGAAATGCCTTCGATGCCTTATCGATGCCTTACCCTGATGCCTTATGCCTTATGCCTTTGGCATGCCTTATCGAATGCCTTTGTTCGCATGCCTTACCATGCCTTATGCCTTTCGCATGCCTTAATGCCTTCCTTTTGGATGCCTTATGCCTTGATGCCTTGATGCCTTGATGCCTTTGAATGCCTTATGCCTTATGCCTTGGAGATGCCTTTGATGCCTTCATGCCTTTCTATGCCTTCAAAATGCCTTCTATGCCTTTCATGCCTTATATGCCTTAAATGCCTTATGCCTTAGGGACTACATGCCTTAGAGCAGATAATTAGCTTATGCCTTTATGCCTTACCTGGGCCTGATATCATGCCTTATGCCTTATGCCTTATGCCTTT'
t='ATGCCTTAT'
ts = [] #list
for i in range(len(s)-len(t)+1):
    if s [i:i+len(t)] == t:
        ts.append(i+1)
for i in ts:
    print (i)