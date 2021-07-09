MP = ['CTAACCGAGA', 'AGTATCACTA', 'TGTATCACTA', 'GGTATCACTA', 'CGTATCACTA']
a = open("cons_shrinked_1.fasta", "r")
fil = a.read().replace('>EMBOSS_001', '').replace('\n', '')
n = 10
arr = [fil[i:i + n] for i in range(0, len(fil), n)]
uhohcount = 0
for elem in arr:
	if elem.upper() in MP:
		elem = elem.upper()
	ch = list(elem.upper())
	uhohcount = ch.count("N")
	if uhohcount == 1:
		if elem.upper().replace('N', 'A') in MP:
			elem = elem.upper()
		elif elem.upper().replace("N", "G") in MP:
			elem = elem.upper()
		elif elem.upper().replace("N", "T") in MP:
			elem = elem.upper()
		elif elem.upper().replace("N", "C") in MP:
			elem = elem.upper()
stringans = ''.join(arr)
with open('ans.txt', 'w') as ans:
	print(stringans, file=ans)
