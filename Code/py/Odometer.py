def odonumbers() -> [int]:
    odonumbers = []
    i = 0
    for number in range(12, 100): 
        number = str(number)
        if (number[i] > number[i+1]):
            odonumbers.append(number)
        i+=1

#def next_kth(number: int, k: int) -> int:
#    for ks, number in enumerate(ks, number):
#        number++

print(odonumbers())


