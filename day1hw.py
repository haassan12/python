import random
rice=45
sugar=40
oil=130

buyrice=3
buysugar=2.5
buyoil=1.8

ricecost=rice*buyrice
sugarcost=sugar*buysugar
oilcost=oil*buyoil

totalcost=ricecost+sugarcost+oilcost

print(f"total rice cost is:{ricecost}")
print(f"total sugar cost is:{sugarcost}")
print(f"total oil cost is:{oilcost}")
print(f"total cost is:{totalcost}")
print(f"total cost in int is{int(totalcost)}")
print(f"total cost in string is:{str(totalcost)}")

delivery=random.randint(5,10)
print(f"total cost including delivery charge is:{totalcost+delivery}")