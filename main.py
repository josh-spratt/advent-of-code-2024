import time
import solutions.day01.part_01
import solutions.day01.part_02
import solutions.day02.part_01
import solutions.day02.part_02
import solutions.day03.part_01
import solutions.day03.part_02
import solutions.day04.part_01
import solutions.day04.part_02
import solutions.day05.part_01
import solutions.day05.part_02
import solutions.day06.part_01
import solutions.day06.part_02
import solutions.day07.part_01
import solutions.day07.part_02
import solutions.day08.part_01
import solutions.day08.part_02
from src.logger import AdventLogger


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
    solutions.day05.part_01.solve()
    solutions.day05.part_02.solve()
    solutions.day06.part_01.solve()
    solutions.day06.part_02.solve()
    solutions.day07.part_01.solve()
    solutions.day07.part_02.solve()
    solutions.day08.part_01.solve()
    solutions.day08.part_02.solve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"All solutions completed in {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
