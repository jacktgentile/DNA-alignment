import sys
from random import randint, seed
from optimal_align import load_submatrix, align

# generate random bp sequence of length L
def random_sequence(L):
    baselist = ["A","C","G","T"]
    result = []
    for i in range(L):
        result.append(baselist[randint(0,3)])
    return result

# generate mutation of given sequence based on project description
def mutate_sequence(sequence):
    new_sequence = sequence.copy()
    L = len(sequence)
    baselist = ["A","C","G","T"]
    # make L/10 random changes
    for i in range(int(L/10)):
        idx = randint(0,len(new_sequence)-1)
        if randint(0,1) == 0:
            # deletion
            new_sequence.pop(idx)
        else:
            # change base
            offset = randint(1,3)
            j = baselist.index(new_sequence[idx])
            j = (j + offset) % 4
            new_sequence[idx] = baselist[j]
    return new_sequence

# write the sequence to a fasta file
def write_sequence_to_file(sequence, filename, seq_desc="random gene sequence"):
    # opens filename in write-only mode, erases original file content
    f = open(filename, 'w')
    f.write(">" + seq_desc + "\n")
    count = 0
    for bp in sequence:
        f.seek(0,2)
        f.write(bp)
        count += 1
        if (count % 80) == 0:
            count = 0
            f.seek(0,2)
            f.write("\n")


if __name__ == "__main__":
    seed()
    # take L parameter
    L = int(sys.argv[1])
    submatrix = load_submatrix("subs.txt")
    origin_seq = random_sequence(L)
    seq2 = mutate_sequence(origin_seq)
    seq3 = mutate_sequence(origin_seq)
    write_sequence_to_file(origin_seq, "seq1.fasta", "unmutated sequence")
    write_sequence_to_file(seq2, "seq2.fasta", "mutated sequence 1")
    write_sequence_to_file(seq3, "seq3.fasta", "mutated sequence 2")
    align(seq2, seq3, submatrix, -50)
