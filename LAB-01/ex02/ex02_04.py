j = []
 
for i in range(2000,3201):
    if(i % 7 == 0) and (i % 5 != 0 ):
        j.append(str(i))
print(f"Các số chia hết cho 7 và không chia hết cho 5 là:")
for i in range(0, len(j)-1):
    print(j[i], end=", ")
print(j[len(j)-1])