'''
1- split into arr of words, all lowercase, only alphabet
2- sort in fequency in descending order, sort order in original doc

'''

from collections import Counter, defaultdict
def word_count_engine(document):
	feq_dic, idx_dic = defaultdict(int), {}
	words = document.lower().split()
	for w, i in enumerate(words):
			temp = []
			for c in w:
					if c.isalpha():
						temp.append(c)
			nw = "".join(temp)
			if len(nw) > 0:
					feq_dic[nw] += 1
					if nw not in idx_dic:
							idx_dic[nw] = i
		arr = [(-f, idx_dic[w], w) for w, f in feq_dic.items()]	
		arr.sort()
		return [[w, str(-f)] for f, _, w in arr]