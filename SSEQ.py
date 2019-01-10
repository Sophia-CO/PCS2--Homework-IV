s1 = 'CGAAGTGATAGGCTTTATCCCCAAGTTTTGAACAAGGTCCACGAGACGGGAAAGCCATCTTAGGACCCTTAAATCGTCGGTCTTAATAGTGGCCCCCATTATTTAACACCTAGACTAAGCAGCAATACGCCGGTGTTACGCACAGACAGCGACTTCAGAATACGCTTGAAGCCAGCAGTTTGAATTTAACCGTTATGTCTTCTTACAGCCAAGATTTATTGAGTTACAGCCAGTTACCCCAACCATGCTACAATACAACGGGCAGCCCAAGCCCATTTCTGGAGGAGTGGATGATTTAAAAGAGTCGCAGAGACAGGAACGACGTAAGGTTTTGCGGAATGCAGTGAGGCGTTTAGAAAAACGCCGAACTACATAATACAAGTATTGACTAAGCCGAGCTAACATGGCAGTTTAGCAGCGTTGATCATCCTGACCTTACTTGACTCGCCGGTATTGACGTTCTCTCCAGACGTTACTATCAGTCTATCTATGTAGGCTTACGATGTAACCGTGTACTTCAGTCCCTTTAGGTCCGAGGGTAATAAATGGGGGTGGGGAGCGATAAAGTGGGTAGGGGCATCCTTAAGGTCGCATCTCTTGGAGCTGGTCACACGTCTTTAAGATTAGGCTTTTCACAAATATCAAAGAATAGTTCTGCGCTCCCGGCGCTGGTACTAACGCAATTGGACTCCTCGCTGCAAGTGCTGTGCAGCTATTCAAATAACAGTGCATAGCAAGCTTCCTCCGTGGGCTCGGAACTTTCAATGCGATGGTATTTTCTCGAAAGACACAGATGCACCGAATTTGTTAGTTAAAAACCGGCT'
s2 = 'AAAGCATTATTCCTTATTCTGGTGCAACGGTAAATTTTTTATATGCCTTTGTGTAGATGGGGAGGCCTATGGTGAAACTTCAGCGT'
def sseq(s1, s2):
    result = ''
    sq = 0
    for i in s2:
        ssq = s1.find(i)
        result = result + str(ssq + 1 + sq) + " "
        sq = sq + ssq + 1
        s1 = s1[ssq + 1:]
    return result
print(sseq(s1, s2))