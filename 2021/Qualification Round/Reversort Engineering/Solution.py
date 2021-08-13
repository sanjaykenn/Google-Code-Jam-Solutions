from collections import deque


def main():
	n, c = map(int, input().split())

	l = list(range(1, n + 1))

	# possible costs for each iteration go from [1, 1, 1, ..., 1] to [n, n - 1, n - 2, ..., 2]
	if n - 1 > c or c >= n * (n + 1) // 2:
		return 'IMPOSSIBLE'

	points_left = c - n + 1  # each iteration contains at least cost 1
	twist = deque()  # note all iterations where there should be reversed (iterations have either cost i or cost 1)

	for i in range(1, n)[::-1]:
		if points_left <= 0:
			break
		elif points_left >= i:
			points_left -= i
			twist.appendleft(i + 1)

	for i in twist:
		l[-i:] = reversed(l[-i:])

	return ' '.join(map(str, l))


if __name__ == "__main__":
	for case in range(1, int(input()) + 1):
		print(f"Case #{case}:", main())
