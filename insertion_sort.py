def insertion_sort(sequence):
    for i in range(0, len(sequence)):
        temp = sequence[i]
        j = i-1
        while j >= 0 and temp < sequence[j]:
            sequence[j+1] = sequence[j]
            j -= 1
        sequence[j+1] = temp

    return sequence

print("Enter Elements : ",end="")
a=list(map(int,input().split(" ")))
print("Sorted Elements : ",end="")
print(insertion_sort(a))
