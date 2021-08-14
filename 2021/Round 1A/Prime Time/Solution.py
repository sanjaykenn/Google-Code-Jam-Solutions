import math


def main():
	m = int(input())

	primes = [list(map(int, input().split())) for _ in range(m)]
	n = sum(map(lambda p: p[1], primes))

	min_prime = primes[0][0]
	max_prime = primes[-1][0]
	max_nb = math.ceil(math.log(n * max_prime, min_prime))  # maximum number of cards in group b
	max_b_sum = max_nb * max_prime  # maximum sum in group b
	sum_all = sum(map(lambda p: p[0] * p[1], primes))  # sum of all cards

	# iterate through all possible sums for group a
	for y in range(max(2, sum_all - max_b_sum), sum_all + 1)[::-1]:
		sum_a = 0
		prod_b = y

		for j, (p, c) in enumerate(primes):
			if j <= prod_b:
				while prod_b % p == 0 and c > 0:
					prod_b //= p
					c -= 1

			sum_a += p * c

		if sum_a == y and prod_b == 1:
			return y

	return 0


if __name__ == "__main__":
	for case in range(1, int(input()) + 1):
		print(f"Case #{case}:", main())
