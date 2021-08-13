import re

r_q = re.compile('\\?*')
r_cj = re.compile('([CJ])\\?*([CJ])')


def main():
	x, y, s = input().split()

	if len(s) < 2:
		return 0

	x = int(x)
	y = int(y)

	q = r_q.search(s)
	i = q.end()

	# collection of all functions for '{first_letter}{last_letter}' with only '?' between
	if x + y < 0:
		functions = {
			'CC': lambda length: (length - 1) // 2 * (x + y),
			'CJ': lambda length: length // 2 * (x + y) - y,
			'JC': lambda length: length // 2 * (x + y) - x,
			'JJ': lambda length: (length - 1) // 2 * (x + y)
		}
	else:
		functions = {
			'CC': lambda length: 0,
			'CJ': lambda length: x,
			'JC': lambda length: y,
			'JJ': lambda length: 0
		}

	if i == len(s):
		# if string contains '?' only
		return min(map(lambda c: c(len(s)), functions.values()))
	elif i == 0:
		# if string starts with 'C' ir 'J'
		result = 0
	else:
		# if string starts with '?'
		result = min(functions[f'C{s[i]}'](i + 1), functions[f'J{s[i]}'](i + 1))

	while i < len(s) - 1:
		m = r_cj.search(s, i)

		if m is None:
			# for all '?' at the end of the string
			return result + min(functions[f'{s[i]}C'](len(s) - i), functions[f'{s[i]}J'](len(s) - i))

		i = m.end() - 1
		result += functions[f'{m[1]}{m[2]}'](len(m.group()))

	return result


if __name__ == "__main__":
	for case in range(1, int(input()) + 1):
		print(f"Case #{case}:", main())
