import json
with open('dic.json') as json_file:
    dic = json.load(json_file)
a = open("seq.fasta", "r")
fil = a.read().replace('>EMBOSS_001', '').replace('\n', '')
n = 10
arr = [fil[i:i+n] for i in range(0, len(fil), n)]
uhohcount = 0
for elem in arr:
  if elem.upper() in dic:
    dic[elem.upper()] = dic.get(elem.upper(), 0) + 1
  ch = list(elem.upper())
  uhohcount = ch.count("N")
  if uhohcount == 1:
    dic[elem.upper().replace('N', 'A')] = dic.get(elem.upper().replace("N", "A"), 0) + 0.5
    dic[elem.upper().replace("N", "G")] = dic.get(elem.upper().replace("N", "G"), 0) + 0.5
    dic[elem.upper().replace("N", "T")] = dic.get(elem.upper().replace("N", "T"), 0) + 0.5
    dic[elem.upper().replace("N", "C")] = dic.get(elem.upper().replace("N", "C"), 0) + 0.5
dic = dict((k, v) for k, v in dic.items() if v > 0)
dic = dict(sorted(dic.items(), key=lambda item: item[1]))
with open('ans.json', 'w') as ans:
    print(dic, file=ans)
