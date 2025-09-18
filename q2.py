a=0
b=0
att=[18,20,19,15,21]
for x in att:
    if x>=20:
        print(f"{x} attendance was full")
        a+=1
    else:
        print(f"{x} attendance was not full")
    b+=x
    
print(f"{a} days was full students")
print(f"total attendance in 5 days is: {b}")
