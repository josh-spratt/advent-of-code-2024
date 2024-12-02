from src.fetch_input_data import DataRetriever
from src.input_parser import parse_input_to_matrix
from src.logger import AdventLogger
import os
import time

logger = AdventLogger("day02part02").get_logger()
    

def solve():
    start_time = time.time()
    logger.info("Starting to solve Day 02, Part 02")
    env = os.environ
    logger.debug("Fetching input data")
    data_retriever = DataRetriever(2024, 2, env["AOC_COOKIE"])
    input_data_string = data_retriever.fetch_input_data()

    reports = parse_input_to_matrix(input_data_string, " ")
    reports = [[int(x) for x in report] for report in reports]

    safe_reports = 0

    for report in reports:
        increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
        decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

        unsafe_jump = any(
            abs(report[i] - report[i + 1]) > 3 for i in range(len(report) - 1)
        )

        if (increasing == True or decreasing == True) and unsafe_jump == False:
            safe_reports += 1
        else:
            for i in range(len(report)):
                new_report = []
                new_report.extend(report[:i])
                new_report.extend(report[i + 1 :])

                increasing = all(
                    new_report[i] < new_report[i + 1]
                    for i in range(len(new_report) - 1)
                )
                decreasing = all(
                    new_report[i] > new_report[i + 1]
                    for i in range(len(new_report) - 1)
                )

                unsafe_jump = any(
                    abs(new_report[i] - new_report[i + 1]) > 3
                    for i in range(len(new_report) - 1)
                )

                if (increasing == True or decreasing == True) and unsafe_jump == False:
                    safe_reports += 1
                    break

    logger.info(f"Safe reports: {safe_reports}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"Solution completed in {elapsed_time:.2f} seconds")
    return safe_reports
