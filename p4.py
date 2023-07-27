#!/usr/bin/python3

from math import log2
pseudocount = 2

debug = True
debug = False


def get_input():
    # return ['T-CT', '--CT', 'A-CT', 'ATCT'], 'ATCCTATATCTTCTCTATACTATCCTTCA'
    # return ['HVLIP', 'H-MIP', 'HVL-P', 'LVLIP'], 'LIVPHHVPIPVLVIHPVLPPHIVLHHIHVHIHLPVLHIVHHLVIHLHPIVL'
    # if debug:


    msa = []
    for n in range(int(input())):
        msa.append(input())
    s = input()
    return msa, s


def cal_score(profile_scores, aminos, seq):
    score = 0
    for i in range(len(seq)):
        score += profile_scores[aminos.index(seq[i])][i]
    return score



## 1: get input and aminos
msa, seq = get_input()
aminos = []
scores = []
for m in msa:
    for i in m:
        if aminos.count(i) == 0 and i != '-':
            aminos.append(i)
aminos.append('-')
for a in aminos:
    scores.append([0 for _ in range(len(m))])

if debug:
    print("aminos:", aminos)
    print("score matrix:")
    for s in scores:
        print(s)


## 2: create table
for col in range(len(scores[0])):
    score = [pseudocount for _ in range(len(aminos))]
    for row in msa:
        score[aminos.index(row[col])] += 1
    score_sum = sum(score)
    for row in range(len(aminos)):
        scores[row][col] = score[row] / score_sum

new_scores = []
for row in scores:
    row_sum = sum(row) / len(msa[0])
    new_row = [log2(e / row_sum) for e in row]
    new_scores.append(new_row)
scores = new_scores

if debug:
    print("score matrix:")
    for s in scores:
        print(s)



############################################################ ! find max score


def insert_char(c, string, index):
    return string[:index] + c + string[index:]

def insert_char_all(str, c):
    res = []
    for i in range(0, len(str) + 1):
        res.append(insert_char(c, str, i))
    return res


def method2(msa, aminos, seq, scores):
    # from itertools import permutations
    from itertools import combinations
    max_gap_count = len(msa[0])

    all_combs = []
    for gap_count in range(max_gap_count):
        count = 0
        for index in range(len(seq) - (max_gap_count - 1) + gap_count):
            end = index + max_gap_count - gap_count
            s = seq[index:end]
            count += 1

            combs = [s]
            while True:
                new_combs = []
                for comb in combs:
                    if gap_count != 0:
                        res = insert_char_all(comb, '-')
                    else:
                        res = combs
                    new_combs.extend(res)
                combs = list(set(new_combs))
                if len(combs[0]) == len(msa[0]):
                    break

            all_combs.extend(combs)

    max_score = -100000
    s = ''
    for comb in all_combs:
        sco = cal_score(scores, aminos, comb)
        if sco > max_score:
            max_score = sco
            s = comb

    print(s)


method2(msa, aminos, seq, scores)



