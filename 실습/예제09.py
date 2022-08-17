# from pprint import pprint

# fruits = [
    # "Soursop",
    # "Grapefruit",
    # "Apricot",
    # "Juniper berry",
    # "Feijoa",
    # "Blackcurrant",
    #"Cantaloupe",
    # "Salal berry",
# ]

# fruit_count = {}

# or fruit in fruits:
    # if fruit not in fruit_count:
        # fruit_count = {fruit: 1}
    # else:
        # fruit_count[fruit] += 1

# pprint(fruit_count)

# fruit_count = {fruit: 1} 딕셔너리가 잘못되었다. 마지막만 1 추가되는걸로 보임 
# fruit_count[fruit]= 1 이렇게 해야 새로운 fruits가 들어올때마다 입력됨

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit]= 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)