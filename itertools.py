
lst1 = []
lst2 = []


def div_grp(inut, n, s):

    if n == s:
        return lst1, lst2
    print(inut[s + 1])
    print(inut[s])
    if inut[s + 1] / n == inut[s]:
        print(lst1)
        print(lst2)
        lst1.append(inut[s])
        lst2.append(inut[s + 1])
        s += 1
        print(s)
        div_grp(inut, n, s)


l1, l2 = div_grp([1, 2, 3, 4, 5, 6], 2, 0)
print(l1)
print(l1)
print(zip(l1, l2))
