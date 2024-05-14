import os

def append_numbrid(from_filepath, filename, nr):
    for j in range(nr-99, nr, 10):
        with open (from_filepath, "r", encoding="UTF8") as f:
            try:
                os.mkdir(f"generated/{nr}")
            except:
                pass
            with open (f"generated/{nr}/{filename}{j+9}.txt", "w", encoding="UTF8") as w:
                for line in f:
                    for i in range(j, j+10):
                        w.write(line.strip() + str(i) + '\n')

def append_numbrid_symbolid(from_filepath, filename, nr, symbol):
    for j in range(nr-99, nr, 10):
        with open (from_filepath, "r", encoding="UTF8") as f:
            try:
                os.mkdir(f"generated/{nr}")
            except:
                pass
            with open (f"generated/{nr}/{filename}{j+9}.txt", "w", encoding="UTF8") as w:
                for line in f:
                    for i in range(j, j+10):
                        w.write(line.strip() + str(i) + symbol + '\n')



for i in range(100, 1100, 100):
    append_numbrid("generated/caps_lemma.txt", "caps_lemma", i)
    append_numbrid("yhend.txt", "low_lemma", i)
    
for i in range(100, 1100, 100):
    append_numbrid_symbolid("generated/caps_lemma.txt", "caps_lemma_punkt", i, ".")
    append_numbrid_symbolid("generated/caps_lemma.txt", "caps_lemma_hyyu", i, "!")
    append_numbrid_symbolid("yhend.txt", "low_lemma_punkt", i, ".")
    append_numbrid_symbolid("yhend.txt", "low_lemma_hyyu", i, "!")