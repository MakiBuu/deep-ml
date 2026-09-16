import numpy as np
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	lis1 = np.array(a)
	lis2 = np.array(b)
	if lis1.shape != lis2.shape:
		return -1
	return lis1+lis2
	pass