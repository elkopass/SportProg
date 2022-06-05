import requests
handle = 'Fefer_Ivan'

listOfHandles = input()
listOfHandles = listOfHandles.split(" ")
for i in listOfHandles:
    handle = i
    x = requests.get(f'https://codeforces.com/api/user.status?handle={handle}&from=1&count=1000000000').json()
    
    mySet = set()
    for i in x["result"]:
        if(i["verdict"] == "OK" ):
            mySet.add(str(i["problem"]["contestId"]) + i["problem"]["index"] )
    print(f"Никнейм пользователя: {handle}\nКоличество решенных задач пользователя: {len(mySet)}")