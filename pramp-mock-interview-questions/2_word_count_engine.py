'''
1- split into arr of words, all lowercase, only alphabet
2- sort in fequency in descending order, sort order in original doc

'''

# from collections import Counter, defaultdict
# def word_count_engine(document):
# 	feq_dic, idx_dic = defaultdict(int), {}
# 	words = document.lower().split()
# 	for w, i in enumerate(words):
# 			temp = []
# 			for c in w:
# 					if c.isalpha():
# 						temp.append(c)
# 			nw = "".join(temp)
# 			if len(nw) > 0:
# 					feq_dic[nw] += 1
# 					if nw not in idx_dic:
# 							idx_dic[nw] = i
# 	arr = [(-f, idx_dic[w], w) for w, f in feq_dic.items()]	
# 	arr.sort()
# 	return [[w, str(-f)] for f, _, w in arr]

from collections import defaultdict
def word_count_engine(document):
	dic = {}
	words = document.split()
	for i, w in enumerate(words):
		n_word = "".join(c for c in w.lower() if c.isalpa())
		if n_word not in dic:
			dic[n_word] = [0,i,n_word]
		else:
			dic[n_word][0] -= 1
	return [[e[2], str(-e[0])] for e in sorted(dic.values())]

