list = [1, 1, 2, 3, 5, 8, 13, 21, 34,9]
list_under_10=[]
under_what = int(input("What number? "))

for i in list:
    
    if i<under_what:
        list_under_10.append(i)
print(list_under_10)