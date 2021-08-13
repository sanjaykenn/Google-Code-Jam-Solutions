def main():
	n = int(input())
	l = list(map(int, input().split()))
	result = 0

	for i in range(len(l) - 1):
		j = min(range(i, len(l)), key=l.__getitem__) + 1
		result += j - i
		l[i:j] = reversed(l[i:j])

	return result


if __name__ == "__main__":
	for case in range(1, int(input()) + 1):
		print(f"Case #{case}:", main())
