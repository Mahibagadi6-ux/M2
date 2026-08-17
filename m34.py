if __name__ == '__main__':
    records = []
    s = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        s.add(score)

    sec_low_score = sorted(s)[1]
    sec_lowest_name = []

    for name, score in records:
        if score == sec_low_score:
            sec_lowest_name.append(name)

    for name in sorted(sec_lowest_name):
        print(name)
