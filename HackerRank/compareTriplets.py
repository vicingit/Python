def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1

        elif a[1] < b[i]:
            bob_score += 1

    return [alice_score, bob_score]

a = [3, 2, 3]
b = [3, 7, 1]

result = compareTriplets(a, b)

print(result)