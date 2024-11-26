def matrix_chain_multiplication(N, arr):
    # Check for invalid cases: N must be at least 2, and arr should have valid dimensions
    if N < 2:
        return "Error: There must be at least two matrices for multiplication"

    if len(arr) != N + 1:  # For N matrices, there must be N+1 dimensions
        return "Error: The dimensions array length must be N+1"

    # Check for negative or zero values in dimensions
    for dim in arr:
        if dim <= 0:
            return "Error: Matrix dimensions must be positive values"

    # Initialize the dp table
    dp = [[0 for _ in range(N)] for _ in range(N)]

    # Loop over chain lengths from 2 to N
    for L in range(2, N):  # L is the chain length
        for i in range(1, N - L + 1):  # i is the starting index of the chain
            j = i + L - 1  # j is the ending index of the chain
            dp[i][j] = float('inf')

            for k in range(i, j):  # Find the optimal split point
                q = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], q)

    return dp[1][N - 1]

def tests():
    test_cases = [
        # Valid test cases (positive test cases) for meteorological data (assuming 5 cities)
        ([7, 5, 4, 6, 7, 8], 5),  
        ([3, 7, 5, 10, 15], 4),  
        ([2, 4, 5, 6, 8], 4),    
        ([4, 8, 6, 7, 9], 4),    
        ([7, 3, 6, 4, 8], 4),    

        # Invalid test cases (negative test cases)
        ([3, 7, 4, 7, 5], 5),    # Invalid: Missing one dimension for multiplication (4 matrices)
        ([2, 5, 6], 1),          # Invalid: Not enough matrices for multiplication
        ([10, 20, 30], 2),       # Invalid: Matrix dimensions array length doesn't match the number of matrices
        ([10, 20], 1),           # Invalid: One matrix (should have 2 for multiplication)
        ([10, -20, 10], 2),      # Invalid: Negative dimension value
        ([0, 20, 10], 2),        # Invalid: Zero dimension value
    ]

    for tc, N in test_cases:
        print(f"Test case with N={N} and arr={tc}: {matrix_chain_multiplication(N, tc)}")

tests()

