def table_generator(n):
    table=""
    for i in range(1,11):
        table+=f"{n} X {i} = {n*i}\n"
    with open(f"Tables/Table_{n}.txt",'w') as f:
        f.write(table)

start=int(input("Enter Your Starting Number: "))
end=int(input("Enter Your Ending Number: "))

for i in range(start,end+1):
    table_generator(i)

print("Table Generated Sucessfully!")