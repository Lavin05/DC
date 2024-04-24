print("Enter the number of processes")
n = int(input())
name = []
print("The processes are :")
for i in range(n):
    print(f"P{i} , process id {i}")
    name.append(f'P{i}')
c = list(range(0, n))
print(c)
print(name)
coordinator = f"P{max(c)}"
while True:
    print('\n')
    print(name)
    print(c)
    print("\nEnter 1 to crash a process\n2 for recovery of process\n3 to display coordinator\n4 to exit")
    inp = int(input())
    if inp == 4:
        break
    if inp == 3:
        coordinator = max(c)
        name_process = name[c.index(max(c))]
        print("current coordinator is",name_process , coordinator)
    if inp == 1:
        print(f"Enter the process you want to crash ")
        crash = int(input())
        if crash == max(c):
            c.remove(crash)
            name.remove(f"P{crash}")
            coordinator = f"P{max(c)}"
        else:
            c.remove(crash)
            name.remove(f"P{crash}")
    if inp ==2:
        print("enter the process to recover (write id as the name is the id)")
        id = int(input())
        c.append(id)
        name.append(f"P{id}")


