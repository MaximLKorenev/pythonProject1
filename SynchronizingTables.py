def SynchronizingTables(N, ids, salary):
    ids_sort = ids[:]
    salary_sort = salary[:]
    ids_sort.sort()
    salary_sort.sort()
    for i in range(N):
        n = ids_sort.index(ids[i])
        salary[i] = salary_sort[n]
    return salary
