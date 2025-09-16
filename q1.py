python={"smith","hari","jhon","maneesh","aromal","sitha","ram"}
data_science={"karthik","hari","nithin","ram","manoj","aromal","akshai"}
print(f"total students enrolled : {python | data_science}")
print (f"total students enrolled python and data science: {python & data_science}")
print(f"the student only enrolled python:{python - data_science}")
print(f"the student only enrolled data science:{data_science - python}")
dict={"python" :len(python),"data_science":len(data_science)}

print(f"number of students enrolled in each course: {dict}")

for x,y in dict.items():
    print(f"number of students enrolled in {x}:{y}")

