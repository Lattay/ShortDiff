# Time complexity O(N*M)
# Space complexity O(M+1 + M*N)
#          distance --^     ^-- path

from copy import deepcopy as dcpy

def kind(goto, pos):
    n1, m1 = goto
    n2, m2 = pos
    if n1 == n2:
        return 'i'
    elif m1 == m2:
        return 'd'
    else:
        return 'k'

def differ(old, new):
    N, M = len(old), len(new)
    dist_mat = [j for j in range(M+2)]
    path_mat = []
    for i in range(N+1):
        path_mat.append([(0,0) for j in range(M+1)])

    for n in range(1, N+1):
        for m in range(1, M+1):
            d_keep = dist_mat[m] if old[n-1] == new[m-1] else 2 + N + M
            d_del = dist_mat[m+1] + 1
            d_ins = dist_mat[m-1] + 1

            dist = min(d_keep, d_del, d_ins)

            if d_keep == dist:
                comefrom = path_mat[n-1][m-1]
                if kind((n-1, m-1), comefrom) != 'k' :
                    comefrom = (n-1, m-1)
            elif d_ins == dist:
                comefrom = path_mat[n][m-1]
                if kind((n, m-1), comefrom) != 'i' :
                    comefrom = (n, m-1)
            else: # d_del == dist:
                comefrom = path_mat[n-1][m]
                if kind((n-1, m), comefrom) != 'd' :
                    comefrom = (n-1, m)

            dist_mat[m] = dist
            path_mat[n][m] = comefrom
        for j in range(M,-1,-1):
            dist_mat[j+1] = dist_mat[j]
        dist_mat[0] = n+1

    pos = (N,M)
    path = []
    while pos != (0,0):
        n, m = pos
        path.append(pos)
        pos = path_mat[n][m]

    path.reverse()

    return dist_mat[M+1], path

def create_patch(old_txt, new_txt):
    old_seq = old_txt.splitlines(True)
    new_seq = new_txt.splitlines(True)

    old_hash = list(map(hash, old_seq))
    new_hash = list(map(hash, new_seq))
    dist, path = differ(old_hash, new_hash)
    
    patch = []
    pos = (0,0)
    for goto in path:
        k = kind(goto, pos)
        if k == 'd':
            n = goto[0] - pos[0]
            patch.append(f'd{n}\n')
        elif k == 'i':
            n = goto[1] - pos[1]
            lines = ''.join(new_seq[pos[1]:goto[1]])
            patch.append(f'i{n}\n{lines}')
        elif k == 'k':
            n = goto[1] - pos[1]
            patch.append(f'k{n}\n')
        pos = goto

    return ''.join(patch)

def check(test, msg=""):
    assert test, "Ill formed patch. "+msg

def to_int(s):
    try:
        return int(s)
    except ValueError:
        raise ValueError("Ill formed patch.")

def apply_patch(old_txt, patch):
    old_seq = old_txt.splitlines(True)
    patch_seq = patch.splitlines(True)

    old_c = 0
    old_l = len(old_seq)
    patch_c = 0
    patch_l = len(patch_seq)

    new_seq = []

    while patch_c < patch_l:
        check(patch_seq[patch_c])
        cmd = patch_seq[patch_c][0]
        check(cmd in 'idk', 'line == ' + patch_seq[patch_c] + ' patch_c == ' + str(patch_c))

        if cmd == 'i':
            n = to_int(patch_seq[patch_c][1:-1])
            
            new_seq.extend(patch_seq[patch_c+1:patch_c+n+1])
            patch_c += n
        elif cmd == 'd':
            n = to_int(patch_seq[patch_c][1:-1])
            check(old_c + n <= old_l, f'Have to delete {n} lines from {old_l} '
            f'lines long file starting at {old_c}')
            old_c += n
        else:  # cmd = 'k'
            n = to_int(patch_seq[patch_c][1:-1])
            check(old_c + n <= old_l, f'Have to keep {n} lines from {old_l} '
            f'lines long file starting at {old_c}')
            new_seq.extend(old_seq[old_c:old_c+n])
            old_c += n
        patch_c += 1
    return "".join(new_seq)

