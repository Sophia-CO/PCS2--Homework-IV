dna = 'CCATTCCATTGGTATTCTGTATGTACTCGTGTCGCGGCCAAACGCCTGGGGAGAATCTGAGGGTAATGGGCCGGTGGCGTATTCGTCATATGATTATAATCCGTGAAGCCGTTTTTGGTCTCAAAGGGACAGGCGCGAACATGCGATCTTTAATTGGAAGGTCTGACACAGTCTTATTTGGTGCTCTCAAGGGCACCTCGACTCTGATAGTCGAGAGCAGTGTCATCATCTTTTTGAGATGGTAGGGGCGTCGTACCCCAAAACGCCGATGGCATTTCTGGCTGTCATCGGTTCAAGATCCTTGGCCTAAATTTGATCAATTTACTTCAAATGAACATCACAAACCATACCAGCGACCGCCCAACCTGGGATAGTGTCACAGCAGTAAGCTCAGTGTTAAAATTTCAGTGTTAAAACGGGCCATGGACCCCATTAGGGGCTTAGATTTCGGCGCGCGCTTGACGACCCGGTGATCACCCGGGAAAATATGGAGGACATAGGTTTTAAGACCCTCAGCTAGGGTGAGCCCTCTAATCAGATAACTAGCATAAGTATGTCATGTGCTCCCAATTCGCCTTCAGGTCGGGTGATTGACCGCGTTTAGCGGGATAAGTACCGGGCCGGAAAGTCGCTCCGCCGTCCGTTTAGTCGGTTACCTCTGCACGCCGCTTTACTGAGGCAGCTAGTTACCGCGCGTTGATTCAGTTAACTGTTGAGCGGATAGTGGTATTAAGAAAACGCCATAGTTAGTTGGTCCACTGCGCGACTAAATGTTGCAGCGGGCTAATGAAGTTGTCCAACGGGATCCGCTAAAAAGTTAACGGCCGGTTCCGCCGCGTGGAAATGCGCGTGTCCCCAGGTGCCACGGGGTTAGGCACCAGTCTTGAAA'
count = [0,0,0,0]
for i in dna:
    if i == 'A':
        count [0] += 1
    if i == 'C':
        count [1] += 1
    if i == 'G':
        count [2] += 1
    if i == 'T':
        count [3] += 1

for i in count:
    print (str(i))