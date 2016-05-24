def min_attempts_egg_drop(n, k):


    eggFloor = [[0 for x in range(k+1)] for x in range(n+1)]
    print(eggFloor)

if __name__ == '__main__':
    eggs = 2
    floors = 100
    print(min_attempts_egg_drop(eggs, floors))
