def subsequence(tm, lista):
    # print(lista)
    L = [1]*tm
    pre = [0]* tm
    for i in range(1,tm):
        # L[i] =1
        # pre[i] =0
        for j in (1,i-1):
            # print(lista[j],lista[i])
            if lista[j]<lista[i] and 1+L[j]>L[i]:
                # print(lista[j])
                L[i] = 1+L[j]
                pre[i] = j
                
    tm_subsequencia = 0
    for i in range(1,tm):
        tm_subsequencia = max(tm_subsequencia, L[i])

    return tm_subsequencia
