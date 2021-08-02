def TransformTransform(a, n):
    def s(my_list, n):
        b = []
        for i in range(n):
            for j in range(n - i):
                k = i + j
                b.append(max(my_list[j:k + 1]))
        return b, len(b)

    list1 = s(*s(a, n))[0]
    if sum(list1) % 2 == 0:
        return True
    else:
        return False
