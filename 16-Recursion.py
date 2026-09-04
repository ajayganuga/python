### Recursive Function
"""

A function that calls itself within its own definition to solve 
a problem or perform a task.

"""
# Example:

# def recurse():

#     recurse()

# recurse()    

### Recursive Function
"""
**Base Case:** The base case is the condition that specifies when the function 
should stop calling itself and return a result directly. It acts as the stopping criterion for the recursion, 
preventing infinite recursion.

**Recursive Case:** The recursive case is the part of the function that calls itself with a modified
 version of the input, leading to smaller instances of the same problem.

"""

## Recusive function for fibonacci
"""

                         fibonacci(5)
                        /             \
                       /               \
              fibonacci(4)          fibonacci(3)
               /       \              /       \
              /         \            /         \
     fibonacci(3)   fibonacci(2)  fibonacci(2)  fibonacci(1)
       /     \         /   \          /   \
      /       \       /     \        /     \
 fibonacci(2) fibonacci(1) fibonacci(1) fibonacci(0)
    /    \
   /      \
fibonacci(1) fibonacci(0)

"""
"""
###             Recursive Function for Factorial
                ================================


        +-------------------+
        |    find_fact(5)   | <------------------- 5 * 24 = 120
        +-------------------+                         |
                 |                                    |
                 |                                    |
                 v                                    |
        +-------------------+                         |
        |  5! = 5 * 4!     | <-----------------------+
        +-------------------+                         |
          Recursive Case                             |
                 |                                    |
                 |                                    |
                 v                                    |
        +-------------------+                         |
        |  4! = 4 * 3!     | <------------------- 4 * 6 = 24
        +-------------------+                         |
          Recursive Case                              |
                 |                                    |
                 |                                    |
                 v                                    |
        +-------------------+                         |
        |  3! = 3 * 2!     | <------------------- 3 * 2 = 6
        +-------------------+                         |
          Recursive Case                              |
                 |                                    |
                 |                                    |
                 v                                    |
        +-------------------+                         |
        |  2! = 2 * 1      | <------------------- 2 * 1 = 2
        +-------------------+                         |
             Base Case                                |
                                                      |
                                                      |
                    RETURNING THE RESULT <-------------+

                    """