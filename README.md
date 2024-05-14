# eesti_dictionary

Siin on kood paroolide sõnastike loomiseks.

Algallikad:
* Eesti kirjakeele sagedussõnastik. https://www.cl.ut.ee/ressursid/sagedused/index.php?lang=et 
* Eesti Keele Instituudi isikunimeandmebaas. https://keeleabi.eki.ee/isikunimed/index.php?t=B
* Eesti Keele Instituudi sõnaloendid. https://www.eki.ee/tarkvara/wordlist
* Mehenimede loend. Vikipeedia. https://et.wikipedia.org/wiki/Mehenimede_loend
* Naisenimede loend. Vikipeedia. https://et.wikipedia.org/wiki/Naisenimede_loend 


## Kaetud mustrid on: 
* Nimi_Nimi
* Nimi_nimi
* NimiNimi
* Niminimi!
* Niminimi
* niminimi
* nimi.
* nimi!
* nimi[1-999]!
* nimi[1-999].
* Nimi[1-999]!
* Nimi[1-999].
* nimi[1900-2024]!
* nimi[1900-2024].
* Nimi[1900-2024]!
* Nimi[1900-2024].
* Niminimi[1-99]
* Lemma
* Lemma!
* Lemma.
* lemma.
* lemma!
* Lemma[1-999]
* Lemma[1-999]!
* Lemma[1-999].
* lemma[1-999]
* lemma[1-999]!
* lemma[1-999].

## Tehtud asendused:
* len [6-19]
  ** {'a':['4', '@'], 'e':'3', 'i':['1', '!'], 'o':'0', 's':['5', 'z'], 't': '7', 'õ':['6', 'o'], 'ä':['2', '@', 'a'], 'ö':'o', 'l':'1',  'ü':['y', 'u']}
* [20-[
** {'a':['4'], 'e':'3', 'i':'1', 'o':'0', 's':'5', 'õ':['6', 'o'], 'ä':['2', 'a'], 'ö':'o', 'l':'1',  'ü':['y', 'u']}

Lemmade näitena on lisatud yhend.txt, mille saab anda näiteks John the Ripperi sisendiks.
