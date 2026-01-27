def to_rna(dna_strand: str) -> str:
    dnamap = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }
    return "".join([dnamap[char] for char in dna_strand])
