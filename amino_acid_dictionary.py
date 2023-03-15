# Dictionary Tools to have information as required
# dict written by calling amino acid one-letter abbreviation
# nested dict is information
# name is name of amino acid, abr is 3-letter abbreviation, ltr is 1-letter abbreviation - also this is the key, codon is a list of corresponding codons, mw is molecular weight in daltons
amino_acid_dict = {"K": {"name": "Lysine", "abr": "Lys", "ltr": "K", "codon": ["AAA", "AAG"], "MW": 128}, "Y": {"name": "Tyrosine", "abr": "Tyr", "ltr": "Y", "codon": ["UAU", "UAC"], "MW": 163}, "T": {"name": "Threonine", "abr": "Thr", "ltr": "T", "codon": ["ACU", "ACA", "ACC", "ACG"], "MW": 101}, "S": {"name": "Serine", "abr": "Ser", "ltr": "S", "codon": ["AGU", "AGC", "UCU", "UCC", "UCA", "UCG"], "MW": 87}, "R": {"name": "Arginine", "abr": "Arg", "ltr": "R", "codon": ["AGA", "AGG", "CGU", "CGC", "CGA", "CGG"], "MW": 156}, "I": {"name": "Isoleucine", "abr": "Ile", "ltr": "I", "codon": ["AUU", "AUC", "AUA"], "MW": 113}, "M": {"name": "Methionine", "abr": "Met", "ltr": "M", "codon": ["AUG"], "MW": 131}, "H": {"name": "Histidine", "abr": "His", "ltr": "H", "codon": ["CAU", "CAC"], "MW": 137}, "Q": {"name": "Glutamine", "abr": "Gln", "ltr": "Q", "codon": ["CAA", "CAG"], "MW": 128}, "P": {"name": "Proline", "abr": "Pro", "ltr": "P", "codon": ["CCU", "CCC", "CCA", "CCG"], "MW": 97}, "L": {"name": "Leucine", "abr": "Leu", "ltr": "L", "codon": ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"], "MW": 113}, "D": {"name": "Aspartic Acid", "abr": "Asp", "ltr": "D", "codon": ["GAU", "GAC"], "MW": 115}, "E": {"name": "Glutamic Acid", "abr": "Glu", "ltr": "E", "codon": ["GAA", "GAG"], "MW": 129}, "A": {"name": "Alanine", "abr": "Ala", "ltr": "A", "codon": ["GCU", "GCC", "GCA", "GCG"], "MW": 71}, "G": {"name": "Glycine", "abr": "Gly", "ltr": "G", "codon": ["GGU", "GGC", "GGA", "GGG"], "MW": 57}, "V": {"name": "Valine", "abr": "Val", "ltr": "V", "codon": ["GUU", "GUC", "GUA", "GUG"], "MW": 99}, "C": {"name": "Cysteine", "abr": "Cys", "ltr": "C", "codon": ["UGU", "UGC"], "MW": 103}, "W": {"name": "Tryptophan", "abr": "Trp", "ltr": "W", "codon": ["UGG"], "MW": 186}, "F": {"name": "Phenylalanine", "abr": "Phe", "ltr": "F", "codon": ["UUU", "UUC"], "MW": 147},"N": {"name": "Asparagine", "abr": "Asn", "ltr": "N", "codon": ["AAU", "AAC"], "MW": 114}}

# STOP CAN BE ADDED AS NEEDED (# or no hash/make it a comment or not) to the dict - not useful in MW-based dictionaries as you can start to get key errors
# amino_acid_dict["STOP"] = {"name": "STOP", "abr": "STOP", "ltr": "STOP", "codon": ["UAA", "UAG", "UGA"], "MW": 0},

# REMOVE ONE AS NEEDED
# alphabet provided
# Alphabet = {57: 'G', 71: 'A', 87: 'S', 97: 'P', 99: 'V', 101: 'T', 103: 'C', 113:'I/L', 114: 'N', 115: 'D', 128: 'K/Q', 129: 'E', 131: 'M', 137: 'H', 147: 'F', 156: 'R', 163: 'Y', 186: 'W'}
# modified alphabet (I/L = X, K/Q = Z)
Alphabet = {57: 'G', 71: 'A', 87: 'S', 97: 'P', 99: 'V', 101: 'T', 103: 'C', 113:'X', 114: 'N', 115: 'D', 128: 'Z', 129: 'E', 131: 'M', 137: 'H', 147: 'F', 156: 'R', 163: 'Y', 186: 'W'}

# converts dictionary to have any new item as key
# DOES NOT WORK ON codon AS LIST CANNOT BE A DICTIONARY KEY
# if key is 'MW' the dictionary length will go from 20 to 18, any subsequent dict from a MW key dict will remain at a length of 18 keys
def NewAAKeyInstaller(aa_dictionary, new_key):
    abr_amino_acid_dict = {}
    for key in aa_dictionary:
        if aa_dictionary[key][new_key] == 113:
            abr_amino_acid_dict[aa_dictionary[key][new_key]] = {"name": "Leucine/Isoleucine", "abr": "Leu/Ile", "ltr": "X", "codon": ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG", "AUU", "AUC", "AUA"], "MW": 113}
        elif aa_dictionary[key][new_key] == 128:
            abr_amino_acid_dict[aa_dictionary[key][new_key]] = {"name": "Lysine/Glutamine", "abr": "Lys/Gln", "ltr": "Z", "codon": ["AAA", "AAG", "CAA", "CAG"], "MW": 128}
        else:
            abr_amino_acid_dict[aa_dictionary[key][new_key]] = aa_dictionary[key]
    return abr_amino_acid_dict

# USEFUL DICT CONVERSION
# name based for the nerds trying to have a cheat sheet
name_amino_acid_dict = NewAAKeyInstaller(amino_acid_dict, "name")
# pass-through to simply get the modified dictionary, reduces to length of 18. 
MW_amino_acid_dict = NewAAKeyInstaller(amino_acid_dict, "MW")
# now amino_acid dict is by "ltr", however only 18 items rather than 20 items with same molecular weight have been combined to I/L = X, K/Q = Z
mod_amino_acid_dict = NewAAKeyInstaller(MW_amino_acid_dict, "ltr")
