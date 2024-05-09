def minOperations(n):
    if n == 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i  # At worst, we can paste 'i' times
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n]

# Example usage
n = 9
print(minOperations(n))  # Output: 6

