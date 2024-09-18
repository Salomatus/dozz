import json

file_path = "../data/products.json"


def open_read_json(file_path):
    with open(file_path, "r") as file:
        json_data = file.read()
        data = json.loads(json_data)
        return data


if __name__ == "__main__":
    data = open_read_json(file_path)
    print(data)
