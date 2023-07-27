import pandas as pd


PAM250 = {
    'A': {'A':  2, 'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N':  0, 'P':  1, 'Q':  0, 'R': -2, 'S':  1, 'T':  1, 'V':  0, 'W': -6, 'Y': -3},
    'C': {'A': -2, 'C': 12, 'D': -5, 'E': -5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S':  0, 'T': -2, 'V': -2, 'W': -8, 'Y':  0},
    'D': {'A':  0, 'C': -5, 'D':  4, 'E': 3, 'F': -6, 'G':  1, 'H':  1, 'I': -2, 'K':  0, 'L': -4, 'M': -3, 'N':  2, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
    'E': {'A':  0, 'C': -5, 'D':  3, 'E': 4, 'F': -5, 'G':  0, 'H':  1, 'I': -2, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
    'F': {'A': -3, 'C': -4, 'D': -6, 'E': -5, 'F':  9, 'G': -5, 'H': -2, 'I':  1, 'K': -5, 'L':  2, 'M':  0, 'N': -3, 'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W':  0, 'Y':  7},
    'G': {'A':  1, 'C': -3, 'D':  1, 'E': 0, 'F': -5, 'G':  5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N':  0, 'P':  0, 'Q': -1, 'R': -3, 'S':  1, 'T':  0, 'V': -1, 'W': -7, 'Y': -5},
    'H': {'A': -1, 'C': -3, 'D':  1, 'E': 1, 'F': -2, 'G': -2, 'H':  6, 'I': -2, 'K':  0, 'L': -2, 'M': -2, 'N':  2, 'P':  0, 'Q':  3, 'R':  2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y':  0},
    'I': {'A': -1, 'C': -2, 'D': -2, 'E': -2, 'F':  1, 'G': -3, 'H': -2, 'I':  5, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -5, 'Y': -1},
    'K': {'A': -1, 'C': -5, 'D':  0, 'E': 0, 'F': -5, 'G': -2, 'H':  0, 'I': -2, 'K':  5, 'L': -3, 'M':  0, 'N':  1, 'P': -1, 'Q':  1, 'R':  3, 'S':  0, 'T':  0, 'V': -2, 'W': -3, 'Y': -4},
    'L': {'A': -2, 'C': -6, 'D': -4, 'E': -3, 'F':  2, 'G': -4, 'H': -2, 'I':  2, 'K': -3, 'L':  6, 'M':  4, 'N': -3, 'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V':  2, 'W': -2, 'Y': -1},
    'M': {'A': -1, 'C': -5, 'D': -3, 'E': -2, 'F':  0, 'G': -3, 'H': -2, 'I':  2, 'K':  0, 'L':  4, 'M':  6, 'N': -2, 'P': -2, 'Q': -1, 'R':  0, 'S': -2, 'T': -1, 'V':  2, 'W': -4, 'Y': -2},
    'N': {'A':  0, 'C': -4, 'D':  2, 'E': 1, 'F': -3, 'G':  0, 'H':  2, 'I': -2, 'K':  1, 'L': -3, 'M': -2, 'N':  2, 'P':  0, 'Q':  1, 'R':  0, 'S':  1, 'T':  0, 'V': -2, 'W': -4, 'Y': -2},
    'P': {'A':  1, 'C': -3, 'D': -1, 'E': -1, 'F': -5, 'G':  0, 'H':  0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N':  0, 'P':  6, 'Q':  0, 'R':  0, 'S':  1, 'T':  0, 'V': -1, 'W': -6, 'Y': -5},
    'Q': {'A':  0, 'C': -5, 'D':  2, 'E': 2, 'F': -5, 'G': -1, 'H':  3, 'I': -2, 'K':  1, 'L': -2, 'M': -1, 'N':  1, 'P':  0, 'Q':  4, 'R':  1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
    'R': {'A': -2, 'C': -4, 'D': -1, 'E': -1, 'F': -4, 'G': -3, 'H':  2, 'I': -2, 'K':  3, 'L': -3, 'M':  0, 'N':  0, 'P':  0, 'Q':  1, 'R':  6, 'S':  0, 'T': -1, 'V': -2, 'W':  2, 'Y': -4},
    'S': {'A':  1, 'C':  0, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P':  1, 'Q': -1, 'R':  0, 'S':  2, 'T':  1, 'V': -1, 'W': -2, 'Y': -3},
    'T': {'A':  1, 'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  0, 'H': -1, 'I':  0, 'K':  0, 'L': -2, 'M': -1, 'N':  0, 'P':  0, 'Q': -1, 'R': -1, 'S':  1, 'T':  3, 'V':  0, 'W': -5, 'Y': -3},
    'V': {'A':  0, 'C': -2, 'D': -2, 'E': -2, 'F': -1, 'G': -1, 'H': -2, 'I':  4, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -6, 'Y': -2},
    'W': {'A': -6, 'C': -8, 'D': -7, 'E': -7, 'F':  0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4, 'P': -6, 'Q': -5, 'R':  2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y':  0},
    'Y': {'A': -3, 'C':  0, 'D': -4, 'E': -4, 'F':  7, 'G': -5, 'H':  0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2, 'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W':  0, 'Y': 10}
}



def u_input():
    # --- User Input ---
    seq1 = "HEAGAWGHE"    # Sequence 1
    seq2 = "PAWHEA"      # Sequence 2
    gp = -9                 # gap penalty

    # --- Format input correctly ---
    arr1 = ['gap'] + [c for c in seq1]
    arr2 = ['gap'] + [c for c in seq2]
    return arr1, arr2, gp

def initialize(seq1, seq2, gp): 

    # --- Creating two matrices and initializing them to known values ---
    scoring = pd.DataFrame(columns=seq1, index=seq2)
    direct = pd.DataFrame(columns=seq1, index=seq2)
    sc = 0
    for p in seq1:
        scoring.loc['gap', p] = sc
        direct.loc['gap', p] = "none"
        sc = sc # add gp for global assignment
    sc = 0 
    for p in seq2:
        scoring.loc[p, 'gap'] = sc
        direct.loc[p, 'gap'] = "none"
        sc = sc # add gp for global assignment
    # print(scoring) # DEBUG
    # print(direct) # DEBUG
    return scoring, direct 

def allign(seq1, seq2, gp, score, direct, blossom):

    # --- creating the square matrice of maximum scores ---
    for i in (range(1, len(seq2))):
        # print(score) # DEBUG
        # print(direct) # DEBUG
        for j in range(1, len(seq1)):
            # print(i, ' ', j) # DEBUG
            diag = score.iloc[i-1,j-1] + blossom[seq1[j]][seq2[i]]
            horz = score.iloc[i, j-1] + gp
            vert = score.iloc[i-1, j] + gp
            # print('line:\t', diag, '\t', vert, '\t', horz) # DEBUG
            val = max(zip([diag, vert, horz, 0], ['d', 'v','h', 'none'])) # remove the zero to use global allignment
            score.iloc[i,j] = val[0]
            direct.iloc[i,j] = val[1]

def semi_glob_index(score, i_max, j_max):
    # --- finding the maximum index in the last row and column ---
    max_c = (i_max, j_max)
    max_v = score.iloc[i_max,j_max]

    for i in range(0, i_max):
        if max_v < score.iloc[i, j_max]:
            max_v = score.iloc[i, j_max]
            max_c = (i, j_max)
    for j in range(0, j_max):
        if max_v < score.iloc[i_max, j]:
            max_v = score.iloc[i_max, j]
            max_c = (i_max, j)
    return max_c

def pair(i, j, direct, score):
    # --- creating the allignment by backtracing ---
    allg1 = []
    allg2 = []
    while (direct.iloc[i,j] != 'none'):
        c = direct.iloc[i,j]
        # print(score.iloc[i,j], ' ', c, ' ', i, ' ', j) # DEBUG
        if c=='d':
            allg1 = [direct.columns[j]]+allg1
            allg2 = [direct.index[i]]+allg2
            i = i-1
            j = j-1
        elif c=='h':
            allg1 = [direct.columns[j]]+allg1
            allg2 = ['-']+allg2
            j = j-1
        elif c=='v':
            allg1 = ['-']+allg1
            allg2 = [direct.index[i]]+allg2
            i = i-1
        elif c=='none':
            break
    return allg1, allg2

def score_matrix():
    # blossom = pd.read_csv("blossom.csv")
    seq1, seq2, gp = u_input()
    score, direct = initialize(seq1, seq2, gp)
    allign(seq1, seq2, gp, score, direct, PAM250)
    i, j = semi_glob_index(score, len(seq2)-1, len(seq1)-1) # compare all values for maximum for local allignment
    allg1, allg2 = pair(i, j, direct, score) # pass the bottom-right index for global allignment
    print("Your scoring matrix is:\n", score)
    print("Your directions are:\n", direct)
    print("The respective allignment is:\n", allg1,'\n', allg2)
    
score_matrix()