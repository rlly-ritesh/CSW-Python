word = input("Enter a word: ")
times = int(input("Enter the number of times you want: "))

h = word[0] * times

for i in range(len(h)):
    if i % 2 == 0:
        print(h[i], end="+")
    else:
        print(h[i], end=",")

