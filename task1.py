n = int(input("Nhap giai thua ban muon: "))
def factorial(n):
    if n == 1:
        return 1
    elif n <= 0:    
        return "Khong hop le, n khong phai so nguyen duong"
    else:
        return n * factorial(n-1)
print(factorial(n)) 
