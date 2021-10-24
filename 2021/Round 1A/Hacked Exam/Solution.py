import itertools
import math
from fractions import Fraction

import numpy as np


# n choose k
def binom(n, k):
	return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


# yield all possible combinations of correct answers in groups
def correct_in_groups(score, group_sizes):
	if len(score) == 1:
		yield np.array(score)
	if len(score) == 2:
		yield np.array([
			(score[0] + score[1] - group_sizes[1]) // 2,
			(score[0] - score[1] + group_sizes[1]) // 2
		])
	if len(score) == 3:
		for all_correct in range(group_sizes[0] + 1):
			correct = np.array([
				all_correct,
				(score[0] + score[1] - group_sizes[2] - group_sizes[3]) // 2 - all_correct,
				(score[0] + score[2] - group_sizes[1] - group_sizes[3]) // 2 - all_correct,
				(-score[1] - score[2] + group_sizes[1] + group_sizes[2]) // 2 + group_sizes[3] + all_correct
			])

			if np.any(0 > correct) or np.any(correct > group_sizes):
				continue

			yield correct


def main():
	n, q = map(int, input().split())
	answers, score = zip(*[input().split() for _ in range(n)])

	answers = np.array(list(map(list, answers))) == 'T'
	score = np.array(score, dtype=int)
	my_answers = np.array(answers[0])

	# types of groups, a group is defined by the combination of which students answer match student 0
	group_types = np.array([np.expand_dims((True,) + a, 1) for a in itertools.product([True, False], repeat=n - 1)])
	groups = np.argmax(np.logical_or(
		np.all(np.expand_dims(answers, 0) == group_types, 1),
		np.all(np.expand_dims(answers, 0) != group_types, 1)
	), 0)  # get group for each question
	group_indexes = [np.argwhere(groups == i).flatten() for i in range(len(group_types))]  # get indexes for each group
	group_sizes = list(map(len, group_indexes))  # group sizes

	# all possible combinations of corrects answers in each group
	correct = np.array(list(correct_in_groups(score, group_sizes))).astype(object)
	count = np.expand_dims([
		np.array(list(map(binom, group_sizes, c)), object).prod() for c in correct
	], 1).astype(object)  # count possibilities for each combination
	total_possibilities = np.sum(count)  # total number of possibilities
	total_correct = np.sum(correct * count, 0)  # how many answers are correct in all total possibilities (per group)

	average_score_1 = np.array([Fraction(c, total_possibilities) for c in total_correct])  # average score for each group
	average_score_2 = group_sizes - average_score_1  # inverted average score
	invert = average_score_2 > average_score_1
	invert_indexes = list(itertools.chain(*np.array(group_indexes, dtype=object)[np.argwhere(invert).flatten()]))

	my_answers[invert_indexes] = np.invert(my_answers[invert_indexes])
	expected_score = sum(np.choose(invert, [average_score_1, average_score_2]))

	ans = ''.join(np.take(['F', 'T'], my_answers))
	return f"{ans} {expected_score}{'/1' if expected_score.denominator == 1 else ''}"


if __name__ == "__main__":
	for case in range(1, int(input()) + 1):
		print(f"Case #{case}:", main())
