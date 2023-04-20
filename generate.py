import itertools

char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$"
min_length = 8
max_length = 12

with open("combolist.txt", "w") as file:
    for length in range(min_length, max_length+1):
        for combination in itertools.product(char_set, repeat=length):
            word = "".join(combination)
            file.write(word + "\n")
