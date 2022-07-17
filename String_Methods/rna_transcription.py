def to_rna(dna_strand):

    rna_strand = []

    for letter in dna_strand:
        if letter == 'C':
            rna_strand.append(letter.replace('C', 'G'))
        elif letter == 'G':
            rna_strand.append(letter.replace('G', 'C'))
        elif letter == 'T':
            rna_strand.append(letter.replace('T', 'A'))
        elif letter == 'A':
            rna_strand.append(letter.replace('A', 'U'))
    return ''.join(rna_strand)
