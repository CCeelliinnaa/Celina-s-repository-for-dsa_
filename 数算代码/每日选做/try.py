def maxSquare(n, m, matrix):
    if n == 0 or m == 0:
        return 0

    # Initialize the DP table
    dp = [[0] * m for _ in range(n)]
    max_side = 0

    # Fill the DP table
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    
    return max_side

# Read input
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the maximum square size
result = maxSquare(n, m, matrix)
print(result)
