import numpy as np

t = int(input())
p = int(input())


def main():
	a = np.array([list(input()) for _ in range(100)], dtype=np.int64)

	question_correct = a.sum(0)
	player_correct = a.sum(1)

	question_sorted = np.argsort(-question_correct)
	player_sorted = player_correct.argsort()

	wrong_cumsum = (1 - a[player_sorted[:, np.newaxis], question_sorted]).cumsum(1)
	correct_sum = a[player_sorted].sum(1)
	inv = wrong_cumsum.sum(1, where=a[player_sorted[:, np.newaxis], question_sorted] == 1)
	score = inv / wrong_cumsum[:, -1] / correct_sum

	return player_sorted[np.argmax(score)] + 1


if __name__ == "__main__":
	for case in range(1, t + 1):
		print(f"Case #{case}:", main())
