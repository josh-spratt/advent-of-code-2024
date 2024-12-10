from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_matrix
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day05part02").get_logger()


def follows_rules(rules, pages):
    """Determine if a page follows all rules."""
    position = {num: idx for idx, num in enumerate(pages)}

    for a, b in rules:
        if a in position and b in position:
            if position[a] >= position[b]:
                return False
    return True


def fix_page(rules, page):
    """'Fix' a page if there are numbers that break the rules."""
    changed = True

    while changed:
        changed = False
        for a, b in rules:
            if a in page and b in page:
                pos_a = page.index(a)
                pos_b = page.index(b)
                if pos_a > pos_b:
                    page.pop(pos_a)
                    page.insert(pos_b, a)
                    changed = True
    return page


def get_page_middle(pages):
    middle_index = (len(pages) - 1) // 2
    return pages[middle_index]


def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 05, Part 02")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(
        2024, 5, env["AOC_COOKIE"]
    )  # TODO: Don't forget to update the day if you copy/paste
    input_data_string = data_retriever.fetch_input_data()

    page_ordering_rules = input_data_string.split("\n\n")[0]
    rules = [
        (int(rule.split("|")[0]), int(rule.split("|")[1]))
        for rule in page_ordering_rules.split("\n")
    ]

    pages = input_data_string.split("\n\n")[1].strip()
    pages = [[int(x) for x in page.split(",")] for page in pages.split("\n")]

    middle_page_numbers_sum = 0
    for page in pages:
        if follows_rules(rules, page):
            middle_page_number = get_page_middle(page)
        else:
            page = fix_page(rules, page)
            middle_page_number = get_page_middle(page)
            middle_page_numbers_sum += middle_page_number

    logger.info(
        f"Sum of middle page numbers for fixed pages: {middle_page_numbers_sum}"
    )

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return middle_page_numbers_sum
