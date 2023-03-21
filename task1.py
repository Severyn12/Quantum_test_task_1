def calculate_sum(N: int) -> int:
    return int(N/2 * (2*1 + N-1)) # sum of arithmetic progression

if __name__ == "__main__":
    print(f"Sum from 1 to {8}: {calculate_sum(8)}")
    N = int(input())
    print(f"Sum from 1 to {N}: {calculate_sum(N)}")