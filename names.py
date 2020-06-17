alphabet = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}


def calculate(name_list):
    product = []
    for i in range(len(name_list)):
        summ = 0
        for j in name_list[i]:
            summ += alphabet.get(j)
        i += 1
        product.append(summ * i)
        i -= 1
    return sum(product)


if __name__ == '__main__':
    with open('names.txt') as f:
        for line in f:
            sub_str = line.split(',')
            names = [i.strip('\'"') for i in sub_str]

    print(f'result : {calculate(sorted(names))}')
    # result : 871853874
