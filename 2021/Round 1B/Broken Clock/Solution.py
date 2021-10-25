import itertools

total_second = 10**9
total_minute = 60*total_second
total_hour = 60 * total_minute
total_time = 12 * total_hour


def main():
	for a_h, a_m, a_s in itertools.permutations(map(int, input().split())):
		for h in range(12):
			n = (total_hour * h - a_h + a_m) / 11

			if n.is_integer():
				time = h * 3600 * 10 ** 9 + int(n)
				if (11 * time + a_h) % total_time == a_m and (719 * time + a_h) % total_time == a_s:
					return ' '.join(map(str, [
						time // total_hour % 12,
						time // total_minute % 60,
						time // total_second % 60,
						time % total_second
					]))


if __name__ == "__main__":
	for case in range(1, int(input()) + 1):
		print(f"Case #{case}:", main())
