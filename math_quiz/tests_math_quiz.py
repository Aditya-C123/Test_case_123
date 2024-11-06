import unittest
from math_quiz import random_function, random_operator, final_operation


class TestMathGame(unittest.TestCase):

    def test_random_function(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_function(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        for _ in range(100):  # Run multiple times to check randomness
            operator = random_operators()
            self.assertIn(operator, valid_operators, 
                          f"Operator {operator} is not in the expected operators {valid_operators}")
        pass

    def final_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                question, answer = final_operation(operand1, operand2, operator)
                self.assertEqual(answer, expected_answer, 
                f"For question '{question}', expected answer {expected_answer} but got {answer}")

if __name__ == "__main__":
    unittest.main()
