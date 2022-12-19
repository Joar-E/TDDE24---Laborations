# Write your code for lab 8d here.

from test_driver import store_test_case, run_free_spans_tests


# Create additional test cases, and add to them to create_tests_for_free_span().

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()

    store_test_case(
        test_cases,
        1,
        start_str    = "08:00",  # Search interval starts
        end_str      = "21:00",  # Search interval ends
        booking_data = ["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result   = ["09:00-13:00", "18:00-21:00"],
    )  # Expected free time

    store_test_case(
        test_cases,
        2,
        start_str    = "14:00",
        end_str      = "23:00",
        booking_data = ["10:00-12:00", "13:00-16:00", "20:00-22:00"],
        exp_result   = ["16:00-20:00", "22:00-23:00"]
    )

    store_test_case(
        test_cases,
        3,
        start_str    = "10:00",
        end_str      = "15:00",
        booking_data = ["11:00-12:30", "15:00-17:00"],
        exp_result   = ["10:00-11:00", "12:30-15:00"]
    )

    store_test_case(
        test_cases,
        4,
        start_str    = "10:10",
        end_str      = "16:00",
        booking_data = ["09:00-17:00"],
        exp_result   = []
    )

    store_test_case(
        test_cases,
        5,
        start_str    = "09:00",
        end_str      = "16:00",
        booking_data = ["07:00-10:00", "12:00-13:00", "15:00-17:00"],
        exp_result   = ["10:00-12:00", "13:00-15:00"]
    )

    # -------- YOUR TEST CASES GO HERE -----------------------
    # For each case, add a brief description of what you want to test.

    print("Test cases generated.")

    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
