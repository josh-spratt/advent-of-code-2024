import requests
import os

class DataRetriever:
    def __init__(self, year: int, day: int, cookie: str):
        self.year = year
        self.day = day
        self.cookie = cookie
        self.file_path = f"inputs/{self.day}/in.txt"

    def fetch_input_data(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                return f.read()
        else:
            res = requests.get(
                url=f"https://adventofcode.com/{self.year}/day/{self.day}/input",
                cookies={"session": self.cookie},
            ).text
            with open(self.file_path, "w") as f:
                f.write(res)
            return res
