import json

alph = ['A', 'T', 'G', 'C']
seq = str()

main_dict = dict()
for a in alph:
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    for f in alph:
                        for g in alph:
                            for h in alph:
                                for i in alph:
                                    for n in alph:
                                          seq = a+b+c+d+e+f+g+h+i+n
                                          main_dict.update({seq: 0})


                                            
with open('seq_dict.json', 'w') as js:
    json.dump(main_dict, js)

