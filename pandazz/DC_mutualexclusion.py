tokens = {1: True , 2: False, 3: False ,4: False,5: False}
request = {1: False , 2: False, 3: False,4: False,5: False}
parents = {1: [], 2: [1], 3: [1], 4:[3] , 5:[3]}  # holding
personel_queue = {1: [], 2: [], 3: [], 4:[] , 5:[]}
qu_id = []
cnt = 0

def request_cs(id):
  # request turns true for id and it adds itsef in its queue
  request[id] = True
  qu_id.append(id)
  # personel_queue[id] = qu_id
  print("queue by each process",personel_queue )
  print("req sent",request)
  print("flow",qu_id)
  #parent add request in its request queue , if parent does not have token it will request its parent
  parent_id = parents[id]
  print("parent its sending to ",parent_id[0])
  if tokens[parent_id[0]] == False:
    request_cs(parent_id[0])
  else:
    final_cs(parent_id[0])

def final_cs(id):
  global cnt
  if cnt == 0: # we are entering the final vaiable here and we need to start backtracking to original node and send it token so this is just for it to assign the queue and release tokens
    qu_id.append(id)
    print(qu_id)
    qu_id.reverse()
    print(qu_id)
    for i in range(len(qu_id)):
      personel_queue[qu_id[i]] = qu_id[i-len(qu_id):]
    print(personel_queue)
    request[id] = True
  # send the token to the requesting node
  cnt = cnt + 1
  list_p = personel_queue[id]
  list_p = list_p[1:]
  new_entry_token = list_p[0]
  # print(list_p)
  personel_queue[id] = list_p
  # print(personel_queue)

  tokens[id] = False
  tokens[new_entry_token] = True
  print("token location",tokens)
  print("currentlt process ",new_entry_token)


  # if len(personel_queue[new_entry_token]) ==0 : no need
  #   print("invalid breaking")
  #   break

  if len(personel_queue[new_entry_token]) != 1:
    final_cs(new_entry_token)


print("first at 4")
request_cs(4)