import xmltodict, json


def main():
    with open("data/universities.xml", "r") as f:
        o = xmltodict.parse(f.read(), encoding="utf-8")
    with open("data/univerisities.json", "w") as f:
        json.dump(o, f)


if __name__ == "__main__":
    main()
