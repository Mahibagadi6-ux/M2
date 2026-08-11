# dictionary
bithday = {
    "mahesh" : "01-01-2006",
    "vishwari" : "02-01-2006",
    "vidya" : "02-02-2006",

}
print(bithday)
print(bithday["mahesh"])
print(bithday["vishwari"])
print(bithday["vidya"])
# all above common
print(bithday.get("mahesh"),"not found in bithday")
print(bithday.get("vanish"),"not found in bithday")


# modify and in elements while both are same imp remeber
bithday["mahesh"] = "01-06-2006"
print(bithday)
bithday["arpithash"] = "01-07-2006"
print(bithday)

print(bithday.keys())
print(bithday.values())
print(bithday.items())

br1 = {
    "sugar":8,
    "teapowder":9,
    "milk":10

}
br2 = {
    "cherry":10,
    "jola":11,
    "akki":12

}
print(f"three ithmes sum {br1["sugar"]+br2["cherry"]+br2["akki"]}kg")