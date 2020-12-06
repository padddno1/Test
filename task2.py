print("Chao mung ban den voi chuong trinh ve hinh")
user_input = int(input("Ban muon ve may dong? "))
user_choice = int(input("Ban muon ve hinh gi nhi? "))
print("1. Dung hinh sao")
print("2. Dung day so")
print("3. Dung ky tu cua ban")
print("4. Thoat chuong trinh")

if user_choice == 1: 
    print("Ban chon dung hinh sao")
    for i in range (1, user_input+1):
        for j in range(1, i+1):
            print("*", end= " ")
        print(" " * user_input)

elif user_choice == 2:
    print("Ban chon dung day so")
    for i in range (1, user_input+1):
        for j in range(1, i+1):
            print(j, end= " ")
        print(" " * user_input)
    
elif user_choice == 3: 
    print("Ban chon dung ky tu cua ban")
    user_symbol = input("Ban muon ky tu gi? ")
    for i in range (1, user_input+1):
        for j in range(1, i+1):
            print(user_symbol, end= " ")
        print(" " * user_input)


    