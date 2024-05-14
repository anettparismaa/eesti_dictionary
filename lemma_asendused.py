import os

def loe_yhend(path= "yhend.txt"):
    lemmad = []
    with open(path, "r", encoding = "UTF-8") as f:
        for line in f:
            lemmad.append(line.strip())
    return lemmad

def generate_replacements_extended(string, index, current, results):
    replacements = {'a':['4', '@'], 'e':'3', 'i':['1', '!'], 'o':'0', 's':['5', 'z'], 't': '7', 'õ':['6', 'o'], 'ä':['2', '@', 'a'], 'ö':'o', 'l':'1',  'ü':['y', 'u']}
    if index == len(string):
        results.add(current)
        return
    if string[index] in replacements.keys():
        for i in replacements.get(string[index]):
            generate_replacements_extended(string, index + 1, current + i, results)

    generate_replacements_extended(string, index + 1, current + string[index], results)

def generate_replacements(string, index, current, results):
    replacements = {'a':['4'], 'e':'3', 'i':'1', 'o':'0', 's':'5', 'õ':['6', 'o'], 'ä':['2', 'a'], 'ö':'o', 'l':'1',  'ü':['y', 'u']}
    if index == len(string):
        results.add(current)
        return
    if string[index] in replacements.keys():
        for i in replacements.get(string[index]):
            generate_replacements(string, index + 1, current + i, results)

    generate_replacements(string, index + 1, current + string[index], results)
    
def find_all_combinations(string):
    results = set()
    if len(string) < 20:
        generate_replacements_extended(string, 0, '', results)
    else: 
        generate_replacements(string, 0, '', results)
    return results


yhend = loe_yhend()

tahed = dict()

for l in yhend:
    try:
        tahed[l[0]].append(l)
    except:
        tahed[l[0]] = [l]
        
for taht in tahed.keys():
    print(taht)
    try:
        os.mkdir(f"generated/replacements/{taht}")
    except:
        pass
    with open(f"generated/replacements/{taht}/yhend_lemmad_{taht}.txt", "w", encoding="UTF8") as f:
        for l in tahed[taht]:
            lemmad = list(find_all_combinations(l))
            lemmad = [lemma.capitalize() for lemma in lemmad]
            f.write("\n".join(lemmad))
            f.write("\n")