import time
import solutions.day01.part_01
from src.logger import AdventLogger
from solutions.day01 import part_01
from solutions.day01 import part_02
from solutions.day02 import part_01
from solutions.day02 import part_02
from solutions.day03 import part_01
from solutions.day03 import part_02
from solutions.day04 import part_01
from solutions.day04 import part_02


def main():
    logger = AdventLogger("all_solutions").get_logger()
    start_time = time.time()
    solutions.day01.part_01.solve()
    solutions.day01.part_02.solve()
    solutions.day02.part_01.solve()
    solutions.day02.part_02.solve()
    solutions.day03.part_01.solve()
    solutions.day03.part_02.solve()
    solutions.day04.part_01.solve()
    solutions.day04.part_02.solve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"All solutions completed in {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
