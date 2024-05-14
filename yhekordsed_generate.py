def loe_yhend(path= "yhend.txt"):
    lemmad = []
    with open(path, "r", encoding = "UTF-8") as f:
        for line in f:
            lemmad.append(line.strip())
    return lemmad

def caps_lemma(yhend, filename):
    with open(f"generated/{filename}.txt", "w", encoding="UTF-8") as f:
        yhend = [lemma.capitalize() for lemma in yhend]
        f.write("\n".join(yhend))


def caps_lemma_hyyumark (yhend, filename):
    with open(f"generated/{filename}!.txt", "w", encoding="UTF-8") as f:
        yhend = [lemma.capitalize()+"!" for lemma in yhend]
        f.write("\n".join(yhend))  

def caps_lemma_punkt (yhend, filename):
    with open(f"generated/{filename}!.txt", "w", encoding="UTF-8") as f:
        yhend = [lemma.capitalize()+"." for lemma in yhend]
        f.write("\n".join(yhend))  

def low_lemma_hyyumark (yhend, filename):
    with open(f"generated/{filename}!.txt", "w", encoding="UTF-8") as f:
        f.write("!\n".join(yhend))
        f.write("!")

def low_lemma_punkt (yhend, filename):
    with open(f"generated/{filename}..txt", "w", encoding="UTF-8") as f:
        f.write(".\n".join(yhend)) 
        f.write(".")

yhend = loe_yhend()


caps_lemma(yhend, "caps_lemma")

caps_lemma_hyyumark (yhend,  "caps_lemma!") 

caps_lemma_punkt (yhend, "caps_lemma") 

low_lemma_hyyumark (yhend, "low_lemma")

low_lemma_punkt (yhend, "low_lemma")