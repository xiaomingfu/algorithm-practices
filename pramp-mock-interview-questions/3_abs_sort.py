def absSort(arr):
		def cmp(n):
			return abs(n), n
		sorted(arr, key = cmp)
