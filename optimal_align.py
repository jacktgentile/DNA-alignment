import sys
import numpy as np

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

# calculate optimal alignment of 2 sequences and store results in .txt file
def align(sequence1, sequence2, submatrix, gapPenalty):
    baselist = ["A","T","C","G"]
    width = len(sequence1)
    height = len(sequence2)
    alignment_scores = np.zeros((height+1, width+1), dtype=int)
    alignment_prev = np.zeros((height, width), dtype=int) # TODO describe behavior
    # determine score matrix
    for i in range(1, height+1):
        for j in range(1, width+1):
            n = baselist.index(sequence1[j-1])
            m = baselist.index(sequence2[i-1])
            # score if match/mismatch
            score1 = submatrix[n][m] + alignment_scores[i-1][j-1]
            # score if down movement
            score2 = gapPenalty + alignment_scores[i-1][j]
            # score if right movement
            score3 = gapPenalty + alignment_scores[i][j-1]
            if score1 >= score2 and score1 >= score2 and score1 >= 0:
                alignment_scores[i][j] = score1
                alignment_prev[i-1][j-1] = 1
            elif score2 >= score1 and score2 >= score3 and score2 > 0:
                alignment_scores[i][j] = score2
                alignment_prev[i-1][j-1] = 2
            elif score3 >= score1 and score3 >= score2 and score3 > 0:
                alignment_scores[i][j] = score3
                alignment_prev[i-1][j-1] = 3
            else:
                alignment_scores[i][j] = 0
                alignment_prev[i-1][j-1] = 1
    # find maximum scoring path
    max_score = 0
    coord = (-1,-1)
    for i in range(height):
        for j in range(width):
            if alignment_scores[i+1][j+1] >= max_score:
                max_score = alignment_scores[i+1][j+1]
                coord = (i,j)
    # modified sequences
    modseq1 = []
    modseq2 = []
    curx = coord[1]
    cury = coord[0]
    # end behavior
    if curx < width-1:
        for i in range(width-1, curx, -1):
            modseq1.append(sequence1[i])
            modseq2.append("-")
    elif cury < height-1:
        for i in range(cury+1, height):
            modseq1.append("-")
            modseq2.append(sequence2[i])
    # backtracking
    while curx >= 0 and cury >= 0:
        dir = alignment_prev[cury][curx]
        if dir == 1:
            modseq1.append(sequence1[curx])
            modseq2.append(sequence2[cury])
            curx -= 1
            cury -= 1
        elif dir == 2:
            modseq1.append("-")
            modseq2.append(sequence2[cury])
            cury -= 1
        else:
            modseq1.append(sequence1[curx])
            modseq2.append("-")
            curx -= 1
    # end behavior
    if curx >= 0:
        for i in range(curx, -1, -1):
            modseq1.append(sequence1[i])
            modseq2.append("-")
    elif cury >= 0:
        for i in range(cury, -1, -1):
            modseq1.append("-")
            modseq2.append(sequence2[i])
    # print("".join(modseq1)[::-1])
    # print("".join(modseq2)[::-1])
    f = open("results.txt",'w')
    f.write("The optimal alignment between given sequences has score " + str(max_score) + ".\n")
    f.write("".join(modseq1)[::-1] + "\n" + "".join(modseq2)[::-1])

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
    # print(sequence1)
    # print(sequence2)
    align(sequence1, sequence2, submatrix, gapPenalty)
