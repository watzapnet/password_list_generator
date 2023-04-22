import itertools
import multiprocessing

char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$"
min_length = 8
max_length = 12
batch_size = 100000

def get_combinations(length):
    return itertools.product(char_set, repeat=length)

def write_batch(batch):
    with open("combolist.txt", "a") as file:
        file.write("\n".join(batch) + "\n")

def generate_combinations(lengths):
    with multiprocessing.Pool() as pool:
        for combinations in pool.imap_unordered(get_combinations, lengths):
            batch = []
            for combination in combinations:
                batch.append("".join(combination))
                if len(batch) == batch_size:
                    write_batch(batch)
                    batch = []
            if batch:
                write_batch(batch)

lengths = range(min_length, max_length + 1)
generate_combinations(lengths)
