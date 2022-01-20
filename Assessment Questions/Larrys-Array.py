# Calculate the total number of inversions
# if the number of inversions are even then the array can be sorted else it cannot be sorted

def larrysArray(A):
    sum = 0

    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                sum += 1

    if sum % 2 == 0:
        return "YES"
    else:
        return "NO"
