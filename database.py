class Database:
    def __init__(self, filename="data.txt"):
        self.filename = filename

    def save_data(self, data):
        with open(self.filename, "w") as file:
            file.write(str(data))

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                return file.read()
        except FileNotFoundError:
            return None
