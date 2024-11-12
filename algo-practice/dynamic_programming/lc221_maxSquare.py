def maxLengthSquare(grid):
    length = len(grid[0])
    width = len(grid)
    ans = 0
    dp = [[0 for _ in range(length)] for _ in range(width)]

    for i in range(width):
        for j in range(length):
            if i == 0 or j == 0:
                dp[i][j] = grid[i][j]
            else:
                if grid[i][j]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i - 1][j], dp[i][j - 1]) + 1
                    ans = max(ans, dp[i][j])

        print(dp)

    return ans


if __name__ == "__main__":
    n, m = [int(num) for num in input().split()]
    grid = []
    for _ in range(n):
        row = [int(num) for num in input().split()]
        grid.append(row)
    print(grid)
    ans = maxLengthSquare(grid)
    print(ans)