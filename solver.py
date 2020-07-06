# -*- coding: utf-8 -*-
import operator

# Define operator mapper.
operator_mapper = {
    "plus": operator.add,
    "minus": operator.sub,
    "times": operator.mul,
    "divide": operator.truediv
}

# Define errors.
FORMAT_ERROR = "Solver accepts either a list or three elements or directly the three elements, where the" \
               " elements are: Operand 1, Operator, Operand 2. Example -> [3, 'Plus', 1]."
BAD_OPERAND = "At least one of the operands is not valid."
BAD_OPERATOR = f"Operator is not valid. Please check the valid operators: {operator_mapper.keys()}"


class Solver:
    """
    Object that will solve an operation provided as argument. The structure of the arguments must be
    "operand1, operator, operand2" that could be provided directly or inside a list. The string method
    will return the operation = solution.
    """
    operation = None
    solution = None

    def __init__(self, *args):
        """
        Init method that extracts the arguments into operation according to the description.
        :raises:
            - ValueError -> In case the format of the arguments is not correct.
        """
        if len(args) == 1:
            self.operation = args[0]

        elif len(args) == 3:
            self.operation = [args[0], args[1], args[2]]

        else:
            raise ValueError(FORMAT_ERROR)

        self.solution = self.calculate(self.operation)

    def __str__(self):
        """
        String method that concatenates the operation with the solution.
        """
        return f"{self.operation} = {self.solution}"

    @staticmethod
    def validate_operation(operation):
        """
        Static method that validates the operation.
        :param operation: (list) Arguments provided in a 3 elements list.
        :return: Cleaned up elements of the operation.
        """
        assert len(operation) == 3, FORMAT_ERROR
        operand1, op, operand2 = operation

        assert str(operand1).isdigit() or isinstance(operand1, list), BAD_OPERAND
        if str(operand1).isdigit():
            operand1 = float(operand1)

        assert isinstance(op, str), BAD_OPERATOR
        op = op.lower()
        assert operator_mapper.get(op, False), BAD_OPERATOR

        assert str(operand2).isdigit() or isinstance(operand2, list), BAD_OPERAND
        if str(operand2).isdigit():
            operand2 = float(operand2)

        return operand1, op, operand2

    def calculate(self, operation):
        """
        Recursive method that will calculate the operation. If an operand is another operation, it will
        call itself to run the calculation.
        :param operation: (list) Arguments provided in a 3 elements list.
        :return: (float) Solved operation.
        """
        operand1, op, operand2 = self.validate_operation(operation)

        if isinstance(operand1, list):
            operand1 = self.calculate(operand1)

        if isinstance(operand2, list):
            operand2 = self.calculate(operand2)

        op = operator_mapper[op]

        return op(operand1, operand2)


# Define the test cases.
tests = [[3, "Plus", 1], [6, "Times", 2], [3, "Plus", [6, "Times", 2]]]

# Run the tests.
for i, test in enumerate(tests):
    print(f"Running test {i + 1}...")
    s = Solver(test)
    print(s)

