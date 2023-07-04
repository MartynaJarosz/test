def delta(seq):
    suma_koncowa = sum(seq)
    suma = 0
    max_index = -1
    
    for i, num in enumerate(seq):
        partial_sum += num
        if partial_sum < suma_koncowa - suma:
            max_index = i
    
    return max_index