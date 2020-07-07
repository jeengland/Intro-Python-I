import sys


def sieve(max):
    num_list = []
    for i in range(max + 1):
        if(i == 0 or i == 1):
            num_list.append(False)
        else:
            num_list.append(True)
    for i in range(len(num_list)):
        if num_list[i]:
            count = 2
            while(i * count <= max):
                num_list[i * count] = False
                count += 1
    primes = [number[0] for number in enumerate(num_list) if number[1] is True]
    return primes


print(sieve(int(sys.argv[1])))
