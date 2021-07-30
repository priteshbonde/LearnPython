map ={
    1:"Ram",
    2: "Shyam",
    3: "Yogi",
    4: "Ajit"
}


map[5] = "Dev"
print(map)

map.update({3: "Anil"})
print(map)


print(map[3])
print(map.get(3))