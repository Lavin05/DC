allocated = [[1,3,4,2],[1,2,3,0],[1,2,3,3]]
max_claim = [[3,2,2,1],[2,1,3,4],[1,3,4,0]]
num_processes = 3
available = [3,4,1,2]
safe_sequence = []



need = [[max_claim[i][j] - allocated[i][j] for j in range(len(max_claim[0]))] for i in range(num_processes)]
print(need)

finish = [False] * num_processes
print(finish)
work = available

while True:
    found = False
    for i in range(num_processes):
        if not finish[i] and all(need[i][j] <= work[j] for j in range(len(available))):
            work = [work[j] + allocated[i][j] for j in range(len(available))]
            print(work)
            finish[i] = True
            safe_sequence.append(i)
            found = True

    if not found:
        break

print("safe :",all(finish), "\nseq :",safe_sequence)
