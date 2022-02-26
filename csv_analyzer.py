import csv


class EuropeanCSV(csv.excel):
    delimiter = ';'


def main():
    with open('data/FinUniversity.json', mode='r') as infile:
        reader = csv.reader(infile, dialect=EuropeanCSV)
        iter = 0
        keys = None
        for row in reader:
            if iter == 0:
                keys = row
            else:
                pass
            iter += 1

        mydict = {rows[0]: rows[1] for rows in reader}
        print(mydict)


if __name__ == "__main__":
    main()
