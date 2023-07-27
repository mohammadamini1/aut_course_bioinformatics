#!/usr/bin/python3


s_match, s_mismatch, s_gap = 3, -1, -2
debug = False
debug = True


def global_align(x, y, s_match, s_mismatch, s_gap):
    A = []
    for i in range(len(y) + 1):
        A.append([0] * (len(x) + 1))
    for i in range(len(y) + 1):
        A[i][0] = s_gap * i
    for i in range(len(x) + 1):
        A[0][i] = s_gap * i
    for i in range(1, len(y) + 1):
        for j in range(1, len(x) + 1):
            A[i][j] = max(
                A[i][j - 1] + s_gap,
                A[i - 1][j] + s_gap,
                A[i - 1][j - 1] + (s_match if (y[i - 1] == x[j - 1] and y[i - 1] != '-') else 0) + (
                    s_mismatch if (y[i - 1] != x[j - 1] and y[i - 1] != '-' and x[j - 1] != '-') else 0) + (
                    s_gap if (y[i - 1] == '-' or x[j - 1] == '-') else 0)
            )
    align_X = ""
    align_Y = ""
    i = len(x)
    j = len(y)
    while i > 0 or j > 0:
        current_score = A[j][i]
        if i > 0 and j > 0 and (
                ((x[i - 1] == y[j - 1] and y[j - 1] != '-') and current_score == A[j - 1][i - 1] + s_match) or
                ((y[j - 1] != x[i - 1] and y[j - 1] != '-' and x[i - 1] != '-') and current_score == A[j - 1][
                    i - 1] + s_mismatch) or
                ((y[j - 1] == '-' or x[i - 1] == '-') and current_score == A[j - 1][i - 1] + s_gap)
        ):
            align_X = x[i - 1] + align_X
            align_Y = y[j - 1] + align_Y
            i = i - 1
            j = j - 1
        elif i > 0 and (current_score == A[j][i - 1] + s_gap):
            align_X = x[i - 1] + align_X
            align_Y = "-" + align_Y
            i = i - 1
        else:
            align_X = "-" + align_X
            align_Y = y[j - 1] + align_Y
            j = j - 1
    return (align_X, align_Y, A[len(y)][len(x)])


def get_input():
    if debug:
        return ['TQPLGLLRL', 'TVPGLLKV', 'TLIILIVELC', 'TAINLLAYV', 'TLILIVEL']                 ## 4
        return ['TYIMREAQYESAQ', 'TCIVMREAYE', 'YIMQEVQQER', 'WRYIAMREQYES']                    ## 1
        return ['MEKKITGYTT', 'NMFFVSANPW', 'MLNELQQ', 'MNAHTAFL']                              ## 3
        return ['NVNVRAV', 'LNVTVVTSL', 'VNLLNPT', 'VRRARP']                                    ## 5
        return ['TAGCTACCAGGA', 'CAGCTACCAGG', 'TAGCTACCAGT', 'CAGCTATCGCGGC', 'CAGCTACCAGGA']  ## 2

    s = []
    for n in range(int(input())):
        s.append(input())
    return s



def add_diffrence_gap(a, old, new):
    o_l = len(old)
    n_l = len(new)
    if o_l == n_l: return a


    ##* best gap match
    gaps = n_l - o_l
    cset = [a]
    for i in range(gaps):
        newset = []
        for c in cset:
            for g in range(len(a) + 1):
                newset.append(c[:g] + '-' + c[g:])

        newset = list(set(newset))
        newset.sort(reverse=True)
        # newset.sort()
        cset = newset.copy()

    best = cset[0]
    max_point = cal_score([new, best])
    for c in cset:
        s = cal_score([new, c])
        if s > max_point:
            max_point = s
            best = c

    if debug:
        print("best results:")
        for c in cset:
            s = cal_score([new, c])
            if s == max_point:
                print("!!!!!!!!!!!!   {} score: {}".format(c, max_point))
        print("+ return best for {} -> {}".format(a, best))

    ##!! if use best match with highest score
    # return best

    add_to_first = True
    add_to_first = False

    if add_to_first:
        a = a[::-1]
        old = old[::-1]
        new = new[::-1]


    ## last gap match (with index)
    o = 0
    n = 0
    ai = o
    while True:
        if o >= len(old) or n >= len(new): break
        if old[o] == new[n]:
            o += 1
            ai += 1
            n += 1
            continue

        # if debug:
        #     print("")

        a = a[:ai] + '-' + a[ai:]
        ai += 1
        n += 1

    if add_to_first:
        a = a[::-1]
        old = old[::-1]
        new = new[::-1]


    if debug:
        print("+ new align for", a)

    return a


def cal_score(seqs):
    l = len(seqs)
    max_l = -1
    for sss in range(l):
        if len(seqs[sss]) > max_l:
            max_l = len(seqs[sss])

    # if debug:
    #     print("%\%\ cal score for:")
    #     for sss in seqs:
    #         print(sss)

    for sss in range(l):
        if len(seqs[sss]) != max_l:
            seqs[sss] = seqs[sss] + '-' * (max_l - len(seqs[sss]))

    s = 0
    sl = len(seqs[0])
    for i in range(l - 1):
        for j in range(i + 1, l):
            for k in range(sl):
                if seqs[i][k] == seqs[j][k]:
                    if seqs[i][k] != '-':
                        s += s_match
                else:
                    if seqs[i][k] == '-' or seqs[j][k] == '-':
                        s += s_gap
                    else:
                        s += s_mismatch
    return s


def c_star(seqs):
    l = len(seqs)
    ##! remove gaps
    for s in range(l):
        seqs[s] = seqs[s].replace('-', '')

    if debug:
        print("cstar input:")
        for d in range(l):
            print(d, ':', seqs[d])

    ##! calculate distance matrix
    distance_matrix = []
    for i in range(l):
        distance_matrix.append([0] * l) # create 0 matrix

    row_scores = []
    for i in range(l - 1):
        for j in range(i + 1, l):
            r = global_align(seqs[i], seqs[j], s_match, s_mismatch, s_gap)
            distance_matrix[i][j] = r[2]
            distance_matrix[j][i] = r[2]
        row_scores.append(sum(distance_matrix[i]))
    row_scores.append(sum(distance_matrix[l - 1]))


    ##! find center & priority indexes
    distinct_scores = list(set(row_scores))
    distinct_scores.sort(reverse=True)
    priority_index = []
    for score in distinct_scores:
        for i in range(l):
            if row_scores[i] == score:
                priority_index.append(i)

    if debug:
        print("distance matrix:")
        for d in range(len(distance_matrix)):
            print(distance_matrix[d], '->', row_scores[d], '*' if d == priority_index[0] else '')
        print("priority indexes:", priority_index)

    ##! align center with each row
    center_index = priority_index[0]
    for index_ in range(1, len(priority_index)):
        index = priority_index[index_]
        r = global_align(
            seqs[index],
            seqs[center_index],
            s_match, s_mismatch, s_gap,
        )
        if debug:
            print("\n= align {} with {}:".format(center_index, index))
            print("{}: {}\n{}: {}".format(index, seqs[index], center_index, seqs[center_index]))

        old_center = seqs[center_index]
        seqs[index] = r[0]
        seqs[center_index] = r[1]

        if debug:
            print("result:")
            print(seqs[index])
            print(seqs[center_index])

        ## add gap for previous aligned seqs
        for add_gap_index in priority_index[1:index_]:
            seqs[add_gap_index] = add_diffrence_gap(seqs[add_gap_index], old_center, seqs[center_index])

    # l = len(seqs)
    # max_l = -1
    # for sss in range(l):
    #     if len(seqs[sss]) > max_l:
    #         max_l = len(seqs[sss])

    # for sss in range(l):
    #     if len(seqs[sss]) != max_l:
    #         seqs[sss] = seqs[sss] + '-' * (max_l - len(seqs[sss]))

    # if debug:
    #     print("output:")
    #     for d in range(l):
    #         print(d, ':', seqs[d])

    return seqs


## dont use ...
def backtrack_blocking(seqs):
    if debug:
        print("backtrack_blocking on: ")
        for ssss in seqs:
            print(ssss)

    block = []
    new_seqs = ["" for _ in range(len(seqs))]

    for column_index in range(len(seqs[0])):
        valid = False
        chr = seqs[0][column_index]
        for row in seqs:
            if row[column_index] != chr:
                valid = True
                break

        if valid:
            block.append(column_index)
            if column_index != len(seqs[0]) - 1:
                continue

        ## create block as seqs_
        seqs_ = ["" for _ in range(len(seqs))]
        for c in block:
            for s in range(len(seqs_)):
                seqs_[s] = seqs_[s] + seqs[s][c]

        if len(block) > 1:
            score_before = cal_score(seqs_)
            if debug:
                print(" old seq with score ", score_before)
                for sssssx in seqs_:
                    print(sssssx)
            seqs_ = c_star(seqs_)
            score_after = cal_score(seqs_)
            if debug:
                print(" new seq with score ", score_after)
                for sssssx in seqs_:
                    print(sssssx)
            improved = True
            if score_before < score_after:
                while improved:
                    seqs__ = backtrack_blocking(seqs_)
                    scor_ = cal_score(seqs__)
                    if scor_ > score_after:
                        seqs_ = seqs__
                        score_after = scor_
                    else:
                        if debug:
                            print("-- not improved block backtrack")
                        improved = False
            elif debug:
                print("? skipped block backtrack")

        for r in range(len(seqs_)):
            new_seqs[r] = new_seqs[r] + seqs_[r]

        # add invalid column
        if not valid and seqs[0][column_index] != '-':
            for s in range(len(seqs_)):
                new_seqs[s] = new_seqs[s] + seqs[s][column_index]

        # if debug:
        #     print("\nafter ctsar for block: {}:\n".format(block), seqs_)
        #     for seq in new_seqs:
        #         print(seq)
        #     print()
        #     print()

        block = []
    return new_seqs



def blocking(seqs):
    if debug:
        print("BLOCKING ... on: ")
        for ssss in seqs:
            print(ssss)

    improved = True
    improved_count = 0
    ## score before
    score_before = cal_score(seqs)
    if debug:
        print(" old seq with score ", score_before)
        for sssssx in seqs:
            print(sssssx)
    while improved:
        block = []
        new_seqs = ["" for _ in range(len(seqs))]

        ## find blocks and improve
        for column_index in range(len(seqs[0])):
            ## check column valid
            valid = False
            chr = seqs[0][column_index]
            for row in seqs:
                if row[column_index] != chr:
                    valid = True
                    break

            if valid:
                block.append(column_index)
                if column_index != len(seqs[0]) - 1:
                    continue

            ##! block

            ## create block as seqs_
            seqs_ = ["" for _ in range(len(seqs))]
            for c in block:
                for s in range(len(seqs_)):
                    seqs_[s] = seqs_[s] + seqs[s][c]

            ## cstar
            if len(block) > 1:
                seqs_score_before_cstar = cal_score(seqs_)
                seqs_after_cstar = c_star(seqs_)
                if cal_score(seqs_after_cstar) > seqs_score_before_cstar:
                    seqs_ = seqs_after_cstar

            ## add block to new seqs
            for r in range(len(seqs_)):
                new_seqs[r] = new_seqs[r] + seqs_[r]

            # add invalid column
            if not valid and seqs[0][column_index] != '-':
                for s in range(len(seqs_)):
                    new_seqs[s] = new_seqs[s] + seqs[s][column_index]

            # if debug:
            #     print("\nafter ctsar for block: {}:\n".format(block), seqs_)
            #     for seq in new_seqs:
            #         print(seq)
            #     print()
            #     print()

            block = []

        score_after = cal_score(new_seqs)
        if debug:
            print(" new seq with score ", score_after)
            for sssssx in new_seqs:
                print(sssssx)

        if score_after <= score_before:
            improved = False
        ## if improved
        else:
            seqs = new_seqs
            score_before = score_after


    return seqs


##! get input
seqs = get_input()

##! run c star first time
seqs = c_star(seqs)


if debug:
    print("\n\n//////////////////////////\nfinal first c star:")
    print(cal_score(seqs))
    for seq in seqs:
        print(seq)
    print()
    print()

seqs = blocking(seqs)




if debug:
    print("\n** final c star result:")
print(cal_score(seqs))
for seq in seqs:
    print(seq)




#############33
# a = "TAINLLAYV",
# b = "T---L-ILIVEL-",
# # a = "TLILIVEL"
# # b = "TLIILIVELC"
# print("\n\nglobal allign:")
# g = global_align(
#     a,
#     b,
#     s_match,
#     s_mismatch,
#     s_gap,
# )
# print(g)

# s_match, s_mismatch, s_gap = 3, -1, -2


# T--- LIL- IVEL
# TAIN L-LA YV--
#   -3    2    -2

