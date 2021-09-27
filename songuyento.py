def not_prime(num):
    flag = False
    if num > 1 :
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                # break
                continue
    return str(flag).lower()
def not_prime_while(num):
    flag = False
    k = 2
    if num >1 :
        while k < num:
            if (num % k) == 0:
                flag = True
                break
            k = k+1 
    return str(flag).lower()
def print_result(k):
    if k == "false":
        print("day la so nguyen to")
    else:
        print("day khong phai la so nguyen to")
        
if __name__ == '__main__':
    i= int(input("nhap so dung de kiem tra: "))
    print_result(not_prime_while(i))
    # if not_prime(int(i))== "false":
    #     print("day la so nguyen to")
    # else:
    #     print("day khong phai la so nguyen to")