"""
Python Operators - Complete Guide
==================================

This module covers all built-in Python operators with examples.

Table of Contents:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Identity Operators
7. Membership Operators
8. Operator Precedence
"""


# =============================================================================
# 1. ARITHMETIC OPERATORS
# =============================================================================
"""
Used for mathematical operations.

+   Addition       -   a + b
-   Subtraction    -   a - b
*   Multiplication -   a * b
/   Division       -   a / b (always returns float)
//  Floor Division  -   a // b (rounds down)
%   Modulus        -   a % b (remainder)
**  Exponentiation -   a ** b (power)
"""

class ArithmeticOperators:
    """Examples for arithmetic operators."""

    @staticmethod
    def run():
        a, b = 10, 3

        print("=== Arithmetic Operators ===")
        print(f"a = {a}, b = {b}")

        # Addition
        print(f"a + b = {a + b}")    # 13

        # Subtraction
        print(f"a - b = {a - b}")    # 7

        # Multiplication
        print(f"a * b = {a * b}")    # 30

        # Division (always returns float)
        print(f"a / b = {a / b}")    # 3.333...

        # Floor Division (rounds down)
        print(f"a // b = {a // b}")  # 3

        # Modulus (remainder)
        print(f"a % b = {a % b}")    # 1

        # Exponentiation
        print(f"a ** b = {a ** b}")  # 1000

        # Negative numbers
        print(f"-a = {-a}")          # -10

        # With floats
        print(f"7 // 2 = {7 // 2}")  # 3
        print(f"7 % 2 = {7 % 2}")    # 1


# =============================================================================
# 2. ASSIGNMENT OPERATORS
# =============================================================================
"""
Used to assign values to variables.

=   Assign              -   x = 5
+=  Add and assign      -   x += 3  (x = x + 3)
-=  Subtract and assign -   x -= 3  (x = x - 3)
*=  Multiply and assign -   x *= 3  (x = x * 3)
/=  Divide and assign   -   x /= 3  (x = x / 3)
//= Floor divide and assign - x //= 3
%=  Modulus and assign  -   x %= 3  (x = x % 3)
**= Exponent and assign -   x **= 3 (x = x ** 3)
&=  AND and assign      -   x &= 3
|=  OR and assign       -   x |= 3
^=  XOR and assign      -   x ^= 3
>>= Right shift and assign - x >>= 3
<<= Left shift and assign  - x <<= 3
"""

class AssignmentOperators:
    """Examples for assignment operators."""

    @staticmethod
    def run():
        print("=== Assignment Operators ===")

        # Basic assignment
        x = 5
        print(f"x = 5 → x = {x}")

        # Add and assign
        x = 5
        x += 3
        print(f"x = 5; x += 3 → x = {x}")  # 8

        # Subtract and assign
        x = 5
        x -= 3
        print(f"x = 5; x -= 3 → x = {x}")  # 2

        # Multiply and assign
        x = 5
        x *= 3
        print(f"x = 5; x *= 3 → x = {x}")  # 15

        # Divide and assign
        x = 10
        x /= 3
        print(f"x = 10; x /= 3 → x = {x}")  # 3.333...

        # Floor divide and assign
        x = 10
        x //= 3
        print(f"x = 10; x //= 3 → x = {x}")  # 3

        # Modulus and assign
        x = 10
        x %= 3
        print(f"x = 10; x %= 3 → x = {x}")  # 1

        # Exponent and assign
        x = 2
        x **= 3
        print(f"x = 2; x **= 3 → x = {x}")  # 8


# =============================================================================
# 3. COMPARISON OPERATORS
# =============================================================================
"""
Used to compare values. Returns True or False.

==  Equal               -   a == b
!=  Not equal           -   a != b
>   Greater than        -   a > b
<   Less than           -   a < b
>=  Greater or equal    -   a >= b
<=  Less or equal       -   a <= b
"""

class ComparisonOperators:
    """Examples for comparison operators."""

    @staticmethod
    def run():
        print("=== Comparison Operators ===")

        a, b = 10, 5

        print(f"a = {a}, b = {b}")

        # Equal
        print(f"a == b → {a == b}")  # False

        # Not equal
        print(f"a != b → {a != b}")  # True

        # Greater than
        print(f"a > b → {a > b}")    # True

        # Less than
        print(f"a < b → {a < b}")    # False

        # Greater or equal
        print(f"a >= b → {a >= b}")  # True

        # Less or equal
        print(f"a <= b → {a <= b}")  # False

        # Chaining (Python specialty)
        x = 5
        print(f"\nx = {x}")
        print(f"0 < x < 10 → {0 < x < 10}")  # True
        print(f"0 < x < 5 → {0 < x < 5}")    # False (not inclusive)


# =============================================================================
# 4. LOGICAL OPERATORS
# =============================================================================
"""
Used to combine conditional statements.

and     Logical AND     -   True and False → False
or      Logical OR      -   True or False → True
not     Logical NOT     -   not True → False
"""

class LogicalOperators:
    """Examples for logical operators."""

    @staticmethod
    def run():
        print("=== Logical Operators ===")

        a, b = True, False

        print(f"a = {a}, b = {b}")

        # and - both must be True
        print(f"a and b → {a and b}")  # False

        # or - at least one must be True
        print(f"a or b → {a or b}")    # True

        # not - inverts the value
        print(f"not a → {not a}")      # False
        print(f"not b → {not b}")      # True

        # Short-circuit evaluation
        print("\n--- Short-circuit ---")
        x = 5
        print(f"x = {x}")

        # and short-circuit: returns first falsy or last value
        result = x > 0 and x < 10 and "valid"
        print(f"x > 0 and x < 10 and 'valid' → {result}")

        # or short-circuit: returns first truthy or last value
        name = None
        result = name or "Unknown"
        print(f"name or 'Unknown' (name is None) → {result}")

        # Practical example
        edad = 25
        if edad >= 18 and edad < 65:
            print(f"Edad {edad}: Adulto trabajador")


# =============================================================================
# 5. BITWISE OPERATORS
# =============================================================================
"""
Operate on individual bits of numbers.

&   AND         -   Sets bit to 1 if both are 1
|   OR          -   Sets bit to 1 if either is 1
^   XOR         -   Sets bit to 1 if bits are different
~   NOT         -   Inverts all bits
<<  Left shift  -   Shift bits left, fill with 0
>>  Right shift -   Shift bits right
"""

class BitwiseOperators:
    """Examples for bitwise operators."""

    @staticmethod
    def run():
        print("=== Bitwise Operators ===")

        a, b = 5, 2  # 5 = 101 (binary), 2 = 010 (binary)

        print(f"a = {a} (binary: {bin(a)})")
        print(f"b = {b} (binary: {bin(b)})")

        # AND - bit is 1 if both are 1
        print(f"a & b = {a & b}")  # 0 (000 & 010 = 000)

        # OR - bit is 1 if either is 1
        print(f"a | b = {a | b}")  # 7 (101 | 010 = 111)

        # XOR - bit is 1 if different
        print(f"a ^ b = {a ^ b}")  # 7 (101 ^ 010 = 111)

        # NOT - invert all bits
        print(f"~a = {~a}")        # -6 (inverts bits + 1)

        # Left shift - multiply by 2^n
        print(f"a << 1 = {a << 1}")  # 10 (101 → 1010)
        print(f"a << 2 = {a << 2}")  # 20 (101 → 10100)

        # Right shift - divide by 2^n
        print(f"a >> 1 = {a >> 1}")  # 2 (101 → 10)
        print(f"a >> 2 = {a >> 2}")  # 1 (101 → 1)

        # Practical use: fast multiplication/division
        print("\n--- Practical ---")
        x = 8
        print(f"x = {x}")
        print(f"x * 2 = {x << 1}")   # 16
        print(f"x * 4 = {x << 2}")   # 32
        print(f"x / 2 = {x >> 1}")   # 4


# =============================================================================
# 6. IDENTITY OPERATORS
# =============================================================================
"""
Compare if two objects are the same object (same memory location).

is      Same object       -   a is b
is not  Not same object   -   a is not b

IMPORTANT: Use with None, not for comparing values!
"""

class IdentityOperators:
    """Examples for identity operators."""

    @staticmethod
    def run():
        print("=== Identity Operators ===")

        # With strings (same content, different objects)
        a = "hello"
        b = "hello"
        c = a

        print(f"a = 'hello', b = 'hello', c = a")
        print(f"a is b → {a is b}")    # True (may vary, interning)
        print(f"a is c → {a is c}")    # True (same object)
        print(f"a is not b → {a is not b}")  # False

        # With lists (always different objects)
        lista1 = [1, 2, 3]
        lista2 = [1, 2, 3]
        lista3 = lista1

        print(f"\nlista1 = [1,2,3], lista2 = [1,2,3], lista3 = lista1")
        print(f"lista1 is lista2 → {lista1 is lista2}")  # False
        print(f"lista1 is lista3 → {lista1 is lista3}")  # True

        # With None (correct way to check)
        x = None
        print(f"\nx = None")
        print(f"x is None → {x is None}")    # True
        print(f"x is not None → {x is not None}")  # False

        # Don't use == with None
        print(f"x == None → {x == None}")    # True (works but not recommended)


# =============================================================================
# 7. MEMBERSHIP OPERATORS
# =============================================================================
"""
Check if a value is in a sequence.

in          In sequence        -   a in list
not in      Not in sequence   -   a not in list
"""

class MembershipOperators:
    """Examples for membership operators."""

    @staticmethod
    def run():
        print("=== Membership Operators ===")

        # With lists
        numeros = [1, 2, 3, 4, 5]
        print(f"numeros = {numeros}")
        print(f"3 in numeros → {3 in numeros}")      # True
        print(f"6 in numeros → {6 in numeros}")      # False
        print(f"6 not in numeros → {6 not in numeros}")  # True

        # With strings
        texto = "Hola mundo"
        print(f"\ntexto = '{texto}'")
        print(f"'mundo' in texto → {'mundo' in texto}")    # True
        print(f"'python' in texto → {'python' in texto}")  # False

        # With dictionaries (checks keys)
        persona = {"nombre": "Ana", "edad": 30}
        print(f"\npersona = {persona}")
        print(f"'nombre' in persona → {'nombre' in persona}")    # True
        print(f"'Ana' in persona → {'Ana' in persona}")          # False (keys only)
        print(f"'Ana' in persona.values() → {'Ana' in persona.values()}")  # True


# =============================================================================
# 8. OPERATOR PRECEDENCE
# =============================================================================
"""
Order in which operators are evaluated (highest to lowest):

1.  ()                  Parentheses
2.  **                  Exponentiation
3.  ~ + -               Unary (not, unary + and -)
4.  * / // %            Multiplication, division, floor, modulus
5.  + -                 Addition, subtraction
6.  >> <<               Bitwise shifts
7.  &                   Bitwise AND
8.  ^                   Bitwise XOR
9.  |                   Bitwise OR
10. == != < <= > >=     Comparisons
11. is, is not          Identity
12. in, not in          Membership
13. not                 Logical NOT
14. and                 Logical AND
15. or                  Logical OR
"""

class OperatorPrecedence:
    """Examples for operator precedence."""

    @staticmethod
    def run():
        print("=== Operator Precedence ===")

        # Without parentheses
        result = 2 + 3 * 4
        print(f"2 + 3 * 4 = {result}")  # 14 (not 20)

        # With parentheses
        result = (2 + 3) * 4
        print(f"(2 + 3) * 4 = {result}")  # 20

        # Complex example
        result = 2 ** 3 * 4 + 5 - 6 / 2
        print(f"2 ** 3 * 4 + 5 - 6 / 2 = {result}")
        # Steps: 2**3=8, 8*4=32, 6/2=3, 32+5=37, 37-3=34

        # Using parentheses for clarity
        result = ((2 ** 3) * 4) + 5 - (6 / 2)
        print(f"((2 ** 3) * 4) + 5 - (6 / 2) = {result}")  # 34

        # Short-circuit with precedence
        x = 0
        result = x != 0 and 10 / x > 1  # Safe!
        print(f"\nx = {x}")
        print(f"x != 0 and 10 / x > 1 → {result}")  # False (short-circuit)


# =============================================================================
# RUN ALL EXAMPLES
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PYTHON OPERATORS - LEARNING MODULE")
    print("=" * 60)

    ArithmeticOperators.run()
    print()

    AssignmentOperators.run()
    print()

    ComparisonOperators.run()
    print()

    LogicalOperators.run()
    print()

    BitwiseOperators.run()
    print()

    IdentityOperators.run()
    print()

    MembershipOperators.run()
    print()

    OperatorPrecedence.run()

    print("\n" + "=" * 60)
    print("COMPLETED")
    print("=" * 60)