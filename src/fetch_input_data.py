import requests


class DataRetriever:
    def __init__(self, year: int, day: int, cookie: str):
        self.year = year
        self.day = day
        self.cookie = cookie

    def fetch_input_data(self):
        return requests.get(
            url=f"https://adventofcode.com/{self.year}/day/{self.day}/input",
            cookies={"session": self.cookie},
        ).text
