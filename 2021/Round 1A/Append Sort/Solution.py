import math


def main():
	n = int(input())
	x = list(map(int, input().split()))

	cost = 0

	for i, j in zip(range(n), range(1, n)):
		if x[i] == x[j]:
			x[j] *= 10
			cost += 1
		elif x[i] > x[j]:
			len1 = int(math.log10(x[i]) + 1)  # length of x[i]
			len2 = int(math.log10(x[j]) + 1)  # length of x[j]
			len_dif = len1 - len2
			suffix = 10 ** len_dif
			if len1 == len2:
				x[j] *= 10
				cost += 1
			else:
				prefix = x[i] // suffix  # first len2 digits of x[i]

				if x[j] == prefix:
					if x[i] % suffix == suffix - 1:
						# in case of 999...
						x[j] *= suffix * 10
						cost += len_dif + 1
					else:
						x[j] = x[i] + 1
						cost += len_dif
				elif x[j] > prefix:
					x[j] *= suffix
					cost += len_dif
				else:
					x[j] *= suffix * 10
					cost += len_dif + 1

	return cost


if __name__ == "__main__":
	for case in range(1, int(input()) + 1):
		print(f"Case #{case}:", main())
