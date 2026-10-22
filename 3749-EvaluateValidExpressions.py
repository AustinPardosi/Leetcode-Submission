# Recursive Descent Parsing
# Time Complexity: O(n)
# Space Complexity: O(n) worst case for the recursion stack

class Solution:
    def evaluateExpression(self, expression: str) -> int:
        def parse(i):
            # Base case: parse a positive or negative integer
            if expression[i].isdigit() or expression[i] == "-":
                start = i

                # Skip the negative sign, if present
                if expression[i] == "-":
                    i += 1

                # Read all digits in the number
                while i < len(expression) and expression[i].isdigit():
                    i += 1

                return int(expression[start:i]), i

            # Parse the operation name: add, sub, mul, or div
            start = i
            while i < len(expression) and expression[i].isalpha():
                i += 1

            op = expression[start:i]
            i += 1  # Skip "("

            # Recursively evaluate the first operand
            val1, i = parse(i)
            i += 1  # Skip ","

            # Recursively evaluate the second operand
            val2, i = parse(i)
            i += 1  # Skip ")"

            # Apply the operation
            if op == "add":
                result = val1 + val2
            elif op == "sub":
                result = val1 - val2
            elif op == "mul":
                result = val1 * val2
            elif op == "div":
                # Integer division truncated toward zero
                result = abs(val1) // abs(val2)
                if (val1 < 0) != (val2 < 0):
                    result = -result

            return result, i

        result, _ = parse(0)
        return result