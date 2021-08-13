from collections import deque

t, n, q = map(int, input().split())


def main():
	# quick sort, but with 2 pivots
	def quick_sort_2(pivot1, pivot2, values):
		if len(values) <= 0:
			return [pivot1, pivot2]

		# 3 groups split by pivot1 and pivot2 (assuming pivot1 < pivot2)
		groups = [deque(), deque(), deque()]

		# separate values in groups
		for value in values:
			print(pivot1, pivot2, value)
			median = int(input())

			if median == pivot1:
				groups[0].append(value)
			elif median == pivot2:
				groups[2].append(value)
			else:
				groups[1].append(value)

		# new pivots of every group
		pivots = [(), (), ()]

		for i in range(len(groups)):
			groups[i] = list(groups[i])
			if len(groups[i]) >= 2:
				# tracking result by knowing that pivot2 is larger than the other two values (except for group 3)
				print(groups[i][0], groups[i][1], pivot2)
				piv2 = int(input())
				piv1 = groups[i][0] if piv2 == groups[i][1] else groups[i][1]
				pivots[i] = piv1, piv2

		# pivot2 is smaller than group3, so the result got reversed before
		pivots[2] = tuple(reversed(pivots[2]))

		for i in range(len(groups)):
			if len(groups[i]) >= 2:
				groups[i] = quick_sort_2(pivots[i][0], pivots[i][1], groups[i][2:])

		groups[0].append(pivot1)
		groups[1].append(pivot2)
		return groups[0] + groups[1] + groups[2]

	return ' '.join(map(str, quick_sort_2(1, 2, list(range(3, n + 1)))))


if __name__ == "__main__":
	for case in range(1, t + 1):
		print(main())
		if input() != '1':
			exit()
