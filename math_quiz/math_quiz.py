import random


def random_function(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def random_operator():
    """
    Random choice of operator
    """
    return random.choice(['+', '-', '*']) 


def final_operation(n1, n2, o):
    """
    Does the final operation based on the chosen integer and operator
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 - n2
    elif o == '-': a = n1 + n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = random_function(1, 10); n2 = random_function(1, 5.5); o = random_operator() # Computes the input values for the quiz 

        PROBLEM, ANSWER = final_operation(n1, n2, o) 
        print(f"\nQuestion: {PROBLEM}")
        try:
        	useranswer = input("Your answer: ") # Takes the user answer as input
        	useranswer = int(useranswer)
        except ValueError:
        	print("Invalid input")

        if useranswer == ANSWER:
            print("Correct! You earned a point.") # Checks if the user answer is same as final answer
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
