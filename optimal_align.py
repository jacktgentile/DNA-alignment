import sys

# return string of base pairs
def load_sequence(filename):
    f = open(filename)
    read_str = f.read()
    read_list = read_str.split("\n")
    result = ""
    for substr in read_list:
        if len(substr) == 0:
            continue
        if substr[0] != '>' and substr[0] != ';':
            result += substr
    return result

# return 2D list with substitution matrix values
def load_submatrix(filename):
    f = open(filename)
    read_str = f.read()
    read_list = read_str.split()
    result = []
    for i in range(4):
        templist = []
        for j in range(4):
            templist.append(int(read_list[4*i+j]))
        result.append(templist)
    return result

# calculate optimal alignment of 2 sequences
def align(sequence1, sequence2, submatrix, gapPenalty):
    return 0

# main function
if __name__ == "__main__":
    # take in parameters
    fastafilename1 = sys.argv[1]
    fastafilename2 = sys.argv[2]
    submatrixfile = sys.argv[3]
    gapPenalty = int(sys.argv[4])
    # assign values from file contents
    sequence1 = load_sequence(fastafilename1)
    sequence2 = load_sequence(fastafilename2)
    submatrix = load_submatrix(submatrixfile)
