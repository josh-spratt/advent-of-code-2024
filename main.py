import time
from src.logger import AdventLogger
from solutions import (
    day_01_part_01,
    day_01_part_02,
    day_02_part_01,
    day_02_part_02,
    day_03_part_01,
    day_03_part_02,
    day_04_part_01,
    day_04_part_02,
)


def main():
    logger = AdventLogger("all_solutions").get_logger()
    start_time = time.time()
    day_01_part_01.solve()
    day_01_part_02.solve()
    day_02_part_01.solve()
    day_02_part_02.solve()
    day_03_part_01.solve()
    day_03_part_02.solve()
    day_04_part_01.solve()
    day_04_part_02.solve()
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"All solutions completed in {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
