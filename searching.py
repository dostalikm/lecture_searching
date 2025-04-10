import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    allowed_fields = {"unordered_numbers", "ordered_numbers", "dna_sequence"}
    if field not in allowed_fields:
        return None

    with open(file_path, mode="r") as file:
        data = json.load(file)
    return data[field]

def linear_search(sequence, number):
    positions = []
    for idx, value in enumerate(sequence):
        if value == number:
            positions.append(idx)

    return {
        "positions": positions,
        "count": len(positions)
    }

def pattern_search(dna_seq, pattern):
    positions = set()
    for i in range(len(dna_seq) - len(pattern) + 1):
        if dna_seq[i:i+len(pattern)] == pattern:
            positions.add(i)

    return positions



def main():
    numbers = read_data("sequential.json", "unordered_numbers")
    print(numbers)
    seq = read_data("sequential.json", "dna_sequence")
    print(seq)
    slovnik = linear_search(numbers, 5)
    print(slovnik)
    pattern = "AAT"
    mnozina = pattern_search(seq, pattern)
    print(mnozina)



if __name__ == '__main__':
    main()