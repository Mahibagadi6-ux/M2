foods = ["idli","dosa","pannir"]
u_foods  =  [item.upper() for item in foods]
print(u_foods)
foods = ["idli","dosa","pannir"]
u_foods  =  [item.split() for item in foods]
print(u_foods)
itmes = {
    "pen" : 10,
    "paper" : 20,
    "book" : 30,
    "squiver" : 40,
    "rubber": 50
}
total = 0
for itmes, value in itmes.items():
    total = total + value
print(total)
itmes = {
    "pen" : 10,
    "paper" : 20,
    "book" : 30,
    "squiver" : 40,
    "rubber": 50
}
lc = {key:value for key, value in itmes.items() if value > 10}
print(lc)

itmes = {
    "pen" : 10,
    "paper" : 20,
    "book" : 30,
    "squiver" : 40,
    "rubber": 50
}
total = 0
print(sum(list(itmes.values())))





