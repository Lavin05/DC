print("Enter the number of servers and processors")
server,processor = input().split(',')
server = int(server)
processor = int(processor)
def adjust():
    processor_in_server=[0]*(server)
    processor_cnt = (processor)
    print(processor_in_server)
    i=0
    while i!=-1:
        if processor_cnt == 0:
            break
        processor_in_server[i]+= 1
        processor_cnt-= 1
        if i == (server)-1:
            i=-1
        i+=1
    print(processor_in_server)

adjust()
while True:
    print("1.Add Servers 2.Remove Servers 3.Add Processes 4.Remove Processes 5.Exit:")
    inp = int(input())
    if inp == 1:
        print("enter the number of extra servers")
        extra = int(input())
        server+=extra
        adjust()
    if inp == 2:
        print("enter the number of servers to remove")
        rm = int(input())
        server-=rm
        adjust()
    if inp == 3:
        print("enter the number of extra processor")
        extra = int(input())
        processor+=extra
        adjust()
    if inp == 4:
        print("enter the number of processor to remove")
        rm = int(input())
        processor-=rm
        adjust()
    if inp == 5:
        break