codons = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAC": "Tyrosine",
    "UAU": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
}


def proteins(strand):
    strand = strand.upper()
    i = 0
    proteins = []
    while i <= len(strand):
        codon = strand[i : i + 3]
        if codon in ("UAA", "UAG", "UGA"):
            break

        try:
            protein = codons[codon]
            proteins.append(protein)
            codon = ""
        except KeyError:
            pass

        i += 3

    return proteins
