# def check_prime_number(num):
#     for n in num:
#         if n<=1:
#             print("The number must be greater than 1")
#             continue
#
#         for d in range(2,n):
#             if n%d == 0:
#                 print("not prime")
#                 break
#
#         else:
#             print("prime")


num = [1,2,3,4,5]


def is_prime(num):
    primes = []
    for n in num:
        if n<=1:
            continue

        for d in range(2,n):
            if n%d == 0:
                break
        else:
            primes.append(n)
    return primes

print(is_prime(num))



def is_prime(n):
    if n<=1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


print(is_prime(7))






