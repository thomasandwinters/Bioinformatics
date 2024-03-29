import math

codon = {
    "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
    "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
    "UUA": 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
    "UUG": 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
    "UCU": 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
    "UCC": 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
    "UCA": 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
    "UCG": 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
    "UAU": 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
    "UAC": 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
    "UAA": '*',      'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
    "UAG": '*',      'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
    "UGU": 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
    "UGC": 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
    "UGA": '*',      'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
    "UGG": 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'}


def reverse_compliment(dna):
    compliment = ""
    for c in dna:
        if c == 'T':
            compliment += "A"
        if c == 'A':
            compliment += "T"
        if c == "G":
            compliment += "C"
        if c == "C":
            compliment += "G"
    return compliment[::-1]


def reverse_palindromes(dna):
    palindromes = []
    if len(dna) >= 6:
        for x in range(len(dna)-5):
            if dna[x:x+6] == reverse_compliment(dna[x:x+6]):
                palindromes.append((dna[x:x+6], x))

    return palindromes


def find_reading_frames(dna):
    frames = []
    dna = dna.upper()
    m_dna = dna.replace("T", "U")
    r_dna = reverse_compliment(dna).replace("T", "U")
    print(r_dna)
    for buffer in range(3):
        frame = ""
        for x in range(math.floor(len(m_dna)/3)):
            if m_dna[3*x+buffer:3*x+buffer+3] in codon:
                frame += codon[m_dna[3*x+buffer:3*x+buffer+3]]
                if frame[-1:] == "*":
                    print("breaking")
                    break
        frames.append(frame)
        if len(frames) == 3:
            break
    for buffer in range(3):
        frame = ""
        for x in range(math.floor(len(r_dna)/3)):
            if r_dna[3*x+buffer:3*x+buffer+3] in codon:
                frame += codon[r_dna[3*x+buffer:3*x+buffer+3]]
                if frame[-1:] == "*":
                    print("breaking")
                    break
        frames.append(frame)
        if len(frames) == 3:
            break


    #if len(dna) >= 3:
    #    for x in range(len(dna)-2):
    #        if dna[x:x+3] in codon:
    #            print(codon[dna[x:x+3]])

    return frames


def main():
    cont = True
    while cont:
        print("Functions:\n"
              "* 1 - Reverse Compliment\n"
              "* 2 - Reverse Palindrome\n"
              "* 3 - Find Frames\n"
              "* 4 - Quit\n"
              "Please enter request:", end=' ')
        request = input()
        if request == "1":
            print("Please enter the nucleotide sequence:", end=' ')
            print(reverse_compliment(input()))
        if request == "2":
            print("Please enter the nucleotide sequence:", end=' ')
            for r in reverse_palindromes(input()):
                print(f'{r[0]} at position {r[1]+1}')
        if request == "3":
            print("Please enter the nucleotide sequence:", end=' ')
            frames = find_reading_frames(input())
            print("Forward reading frames:")
            for x in range(3):
                print(frames[x])
            print("Backward reading frames:")
            for x in range(3, 6):
                print(frames[x])

        if request == "4":
            cont = False

    return


main()
