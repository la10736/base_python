# Indovina il Numero

## Introduzione

Potremmo provare a scrivere il gioco in modalità interattiva, ma poi dovremmo riscriverlo ogni volta che vogliamo 
giocare, quindi useremo il modo continuo anche se interrogheremo il *Pitone* in modo interrativo per verificare
continuamente quello che stiamo facendo.

Lo scopo del nostro primo gioco è molto semplice: *Il computer sceglie un numero e noi dobbiamo indovinarlo*. Ma per 
arrivare al risultato finale faremo tante prove intermedie:

1. Il numero non viene scelto a caso ma fissato da noi e il programma non conta i tentativi e non fornisce alcun 
suggerimento
2. Il programma conta il numero di tentativi, scrive sempre quale tentativo stiamo facendo e alla fine dice quanti
tentativi abbiamo usato
3. Da indicazioni se bisogna mettere un numero più alto o più basso
4. Facciamo scegliere il numro a caso
5. Capisce se non scriviamo un numero e ci dice di riprovare
6. Tutto funziona ma non è un po troppo difficile da capire? Possiamo scriverlo meglio?

## Scriviamo il nostro primo programma

### Il testo di partenza

* *IDLE* : *File* -> *New File*, nella nuova finestra usare *File* -> *Save* e andare nella cartella creata per il
 programma e usare il nome `indovina.py`
* *PyCharm* : *File* -> *New* e chiamarlo `indovina`. 

Questi file il *Pitone* li chiama moduli e contengono le informazioni del programma che deve essere eseguito. Dentro
a questo file copiamo il programma [indovina_base.py] ... dopo ci preoccuperemo di capire cosa dice.

```python
numero_da_indovinare = 1234

while True:
    tentativo = input("Inserisci un numero: ")
    numero_provato = int(tentativo)
    if numero_provato == numero_da_indovinare:
        print("BRAVO!!!! Hai indovinato")
        import sys
        sys.exit()
    print("Peccato non hai indovinato... prova ancora!")
```

Per chi usa *IDLE* ricordarsi di salvare il programma con *File* -> *Save* ( *PyCharm* salva sempre da solo)

### La prima partita

Ok, lo abbiamo scritto e salvato e adesso lo eseguiamo per fare la nostra prima partita:

* *IDLE* : Nella finestra *`indovina.py`* aprite *Run* -> *Run Module* (oppure *F5*)
* *PyCharm* : *Run* -> *Run `'indovina'`* (oppure *Alt* + *Maiuscolo* + *X*)

Ora il nostro programma è partito e ci chiede `Inserisci un numero: `. Noi sappiamo già il risultato giusto, ma non ci 
interessa vincere, ma solo vedere se funziona come vogliamo. Facciamo quindi un po di prove e vediamo cosa succede.

    Inserisci un numero: 36
    Peccato non hai indovinato... prova ancora!
    Inserisci un numero: 56
    Peccato non hai indovinato... prova ancora!
    Inserisci un numero: 1234
    BRAVO!!!! Hai indovinato

Funziona proprio come vogliamo!!! ... ma perché?

### Usiamo il *Pitone* per capire il programma

Una cosa che viene semplice da fare con il *Pitone* è sperimentare, provare in modalità interattiva cosa succede se...

Bene, noi useremo questo continuamente: sarà la nostra palestra dove sperimenteremo ogni riga prima di metterla nel 
programma.

#### Definiamo un nuovo nome `numero_da_indovinare`

La prima riga che troviamo è `numero_da_indovinare = 1234`. Come abbiamo già visto nelle prime prove con il *Pitone* 
questo equivale a dire che esiste un nuovo nome definito che si chiama `numero_da_indovinare` e quando lo trova il 
*Pitone* lo soatituisce con il numero `1234`. Anche se lo sappiamo già proviamolo lo stesso nella console. 

* *IDLE*: la console è quella dove è stato eseguito il programma (dove ci sono i simboli `>>> ` per capirci)
* *PyCharm*: Usare *Tools* -> *Run Python Console* per aprire una cosole dove sperimentare

Scriviamo quindi

```python
>>> numero_da_indovinare = 1234
```

Da questo momento in poi il *Pitone* capisce la parola `numero_da_indovinare` e la sostituisce con `1234`: ma non 
dovete credermi sulla parola, provate!.

```python
>>> numero_da_indovinare
1234
>>> numero_da_indovinare == 1234
True
>>> numero_da_indovinare == 12
False
```

#### `while True` ovvero *Per Sempre*

Ora troviamo una cosa nuova `while True`: per chi ha usato *Scratch* è la stessa cosa del famoso, famigerato e abusato 
*Per Sempre*. In particolare `while qualcosa` esegue quello che c'è sotto fino a che `qualcosa` risulta *vero* 
(`True` in inglese e per il *Pitone*). Con il tempo cercheremo di capire quando il *Pitone* dice che una cosa è vera, 
ma ora guardiamo esattamente cosa viene eseguito.

```python
>>> n = 1
>>> while n < 5:
...     n
...     n = n + 1
... 
1
2
3
4
```

Dopo che abbiamo scritto `while n < 5` sia *IDLE* che *PyCharm* ci *aiutano* facendoci scrivere 4 spazi dopo la `w`,
Quando non vogliamo più scrivere cose da eseguire nel *ciclo* basta che torniamo indietro di uno con il tasto 
che cancella (in alto a destra sulla tastiera): ora il ciclo è finito e il *Pitone* può eseguirlo stampando `n` e 
continuando fino a quando `n < 5` diventa faso... pardon `False`. 

* Quanto vale ora `n`?
* `n < 5` è vero o falso?
* Se riproviamo funziona ancora?
* Perchè all'inizio ha funzionato? 

Non sforziamoci, chiediamolo al *Pitone*

```python
>>> n
5
>>> n < 5
False
>>> 5 < 5
False
>>> while n < 5:
...     n
...     n = n + 1
... 
>>> n = 1
>>> n < 5
True
>>> while n < 5:
...     n
...     n = n + 1
... 
1
2
3
4
```

`while` esegue tutto quello che si trova sotto di lui fino a che non ritrova qualcosa di scritto che inizia dalla
stessa colonna della `w` del `while`. Chiameremo quello che si trova dentro il `while` *blocco*. Anche se dopo il 
`while`potete scegliere il numero di spazi che volete, **la convenzione mondiale è di usarne sempre 4**. Inoltre
tutto quello che è contenuto in un blocco inizia sempre dalla stessa colonna a meno che non inizi un altro *blocco*
interno.
 
Concludendo `while True` significa *esegui il blocco per sempre* dato che *True* non può mai diventare `False`
 
#### Chiediamo un numero
 
Con il comando  `input("Inserisci un numero: ")` cosa facciamo? proviamolo da solo
 
```python
>>> input("Inserisci un numero: ")
Inserisci un numero: >? 23
'23'
```

La console ci scrive indietro `Inserisci un numero: ` ( *PyCharm* aggiunge anche `>? ` perdire che sta aspettando che 
inseriamo qualcosa); quello che scriviamo lo stampa nuovamente con le virgolette attorno (ci sta dicendo che è un 
testo).

Ora quindi se se noi scriviamo `tentativo = input("Inserisci un numero: ")` cosa succede? ...proviamo.

```python
>>> tentativo = input("Inserisci un numero: ")
Inserisci un numero: >? ecco il mio tentativo
>>> tentativo
'ecco il mio tentativo'
```

Quindi tentetivo contiene quello che abbiamo scritto in risposta alla domanda.

Ma noi serve un numero, infatti i testi (noi informatici li chiamiamo **stringhe**) non sono uguali a numeri anche se
contengono un testo con lo stesso numero. Verifichiamolo:

```python
>>> 34 == 34
True
>>> 34 == '34'
False
>>> numero = 45
>>> testo = '45'
>>> numero == testo
False
```

Come facciamo a trasformare il numero che viene scritto da stringa a numero? Possiamo usare la **funzione** `int()` che
trasforma l'argomento in un **numero intero**... se ci riesce, altrimenti si arrabbia (noi informatici diciamo *lancia
eccezione*). Proviamo:

```python
>>> int(testo)
45
>>> numero == int(testo)
True
>>> tentativo
'ecco il mio tentativo'
>>> int(tentativo)
Traceback (most recent call last):
  File "/usr/lib/python3.4/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'ecco il mio tentativo'
```

Quando abbiamo provato a convertire `tentativo` che conteneva la stringa `'ecco il mio tentativo'` la console ha detto
impettita che ha trovato un errore nei valori passati `ValueError` dato che `'ecco il mio tentativo'` non era un numro
valido in base 10.... magari delle basi parliamo un'altra volta.

Quindi con `numero_provato = int(tentativo)` trasformiamo quello che viene scritto in un numero che possiamo confrontare
con `numero_da_indovinare`.

#### Se hai indovinato allora fine

Bene, abbiamo il `numero_da_indovinare` e il `numero_provato`, quello che dobbiamo fare è verificare se sono uguali e
in caso affermativo dire al giocatore che è riuscito a indovinare e interrompere. Il *Pitone* capisce la parola `if` 
(*se* in inglese) e con la seguente forma

```python
if condizione :
    blocco se vero 
```

Come nel il `while`, anche con `if` segue la condizione, il simbolo `:` e poi a capo con un nuovo blocco (sempre
rientrato preferibilmente di 4 spazi).
 
Per prima cosa identifichiamo la condizzione che ci interessa e poi quello che dobbiamo fare quando la condizione è vera.

La condizzione è verificare che `numero_provato` è uguale a `numero_da_indovinare` e come abbiamo visto già diverse
volte usare `numero_provato == numero_da_indovinare` ritornerà `True` se i numeri sono uguali e `False` altrimenti: 
proprio quello che volevamo fare.

Quando i due numeri sono uguali il programma dice di eseguire `print("BRAVO!!!! Hai indovinato")`: proviamolo

```python
>>> print("BRAVO!!!! Hai indovinato")
BRAVO!!!! Hai indovinato
```

`print(stringa)` stampa semplicemnete la stringa ( *print* in inglese significa stampa).

Ora per uscire dal programma vengono usate due righe

```python
import sys
sys,exit()
```

La prima richiama tutte le cose contenute in un modulo chiamato `sys` e con `sys.exit()` esegue la funzione exit che 
si trova in `sys` e serve per uscire. Se ci provate nella console con *PyCharm* chiuderete la console, mentre con 
*IDLE* non succede niente ... quei bricconi hanno leggermente *truccato le carte per non far chiusìdere la console*.

#### Siamo arrivati alla fine

Bene se il numero è uguale il programma finisce, ma se i due numeri non sono uguali dobbiamo dire qualcosa e 
ricominciare a chiedere di provare.

Siccome siamo nel blocco del `while True:` allora appena finiamo il blocco il programma riprenderà dal richiedere di
fare un tentativo. Quindi come abbiamo già visto con `print(messaggio)` stampiamo il messaggio, perciò proviamo l'ultima
riga che stamperà il messaggio di riprovare ancora.

```python
>>> print("Peccato non hai indovinato... prova ancora!")
Peccato non hai indovinato... prova ancora!
```


## Contiamo I tentativi

Vi ricordate quando abbiamo provato a vedere come funziona il ciclo `while`? abbiamo definito un nuovo nome `n = 0` e 
poi a ogni giro del ciclo `n` veniva aumentato di uno con `n = n + 1`. Bene, credo prorpio che dobbiamo fare la stessa
cosa ma quello che ci manca è come stampiamo il numero di tentativo in corso e il numero totale alla fine?

Se vi ricordate avevamo visto che sommare due stringhe vuol dire concatenarle: proviamoci ancora:

```python
>>> frase = 'ciao,' + ' ' + 'come stai?'
>>> print(frase)
ciao, come stai?
```

Ora ci manca solo come convertire il numero dei tentativi in stringa e possiamo scrivere una frase del tipo
`--- Tentativo numero 5.`. Così come abbiamo visto che `int()` transforma l'argomento in numero, esiste la *funzione* 
`str()` che trasforma l'argomento in stringa. Proviamolo!

```python
>>> str(12)
'12'
>>> str('pippo')
'pippo'
>>> str(1.345)
'1.345'
>>> str(str)
"<class 'str'>"
>>> str(print)
'<built-in function print>'
```

Notare che *prova sempre* a trasformare in stringa l'argomento anche quando passiamo come argomenti cose strane come
funzioni o classi.

Quindi ora abbiamo tutto per modificare il nostro programma... provateci da soli in 5 minuti, se proprio non ci riuscite
guardate [quì](indovina_conta.py).

## Aiutiamo il giocatore con qualche indizio

Quando il giocatore non indovina vogliamo dirgli di mettere un numero maggiore se il suo è troppo piccolo e uno minore
se il suo numero è troppo grande. Pensiamoci bene abbiamo bisogno di qualcosa che dica `True` se `numero_provato` è 
maggiore di `numero_da_cercare` e `False` quando non è maggiore. 

* Idee? 
* Cosa potremmo usare?
* Sperimentiamo?


```python
>>> 5 > 6
False
>>> 6 > 5
True
>>> 5 < 6
True
```

Credo propio che ora ci possiamo riuscire.... Ok 5 minuti mi sembrano sufficenti poi guardate le due soluzioni 
che ho fatto: [prima](indovina_indizi.py), [senonda](indovina_indizi2.py)

## Il Computer sceglie il numero

Fino ad ora il numero da indovinare era fissa to e il gioco non era tanto divertente, ma in questa maniera potevamo 
provare facilmente se funzionava o meno quello che avevamo scritto. Ma ora è venuto il momento di farlo diventare un 
gioco e di non sapere qual'è il numero da indovinare.

Si ma come si fa? Si usano i potenti mezzi del *Pitone* importando nuve funzionalità con la parola chiave `import`. In
inglese casuale si dice *random* e vediamo cosa succede a importare `random`

```python
>>> import random
```

Non succede niente! .... Appunto il *Pitone* ha capito. Bene ora vi potrei spiegare come trovare la funzione che ci 
serve, ma sarò buono velo dico io quella che vi serve

```python
>>> random.randint(0, 5000)
765
```

La funzione `randint(minimo, massimo)` ritorna un numero casuale tra minimo e massimo... ma non mi ricordo bene se 
`minimo` e `massimo` sono compresi, poco male **proviamo**!

```python
>>> random.randint(0, 1)
0
>>> random.randint(0, 1)
1
```

Quindi sono compresi.

Quindi modificate il vostro programma per dare un numero casuale tra `0` e `2000` e dire al giocatore di inserire
un numero in questo intervallo.... Due minuti per farlo e ... 5 per giocare (Io ci sono riuscito in 12 tentativi). 
Dimenticavo la mia versione attuale è [quì](indovina_casuale.py)

## Se l'utente non mette un numero il programma deve funzionare.

Alla mia prima partita dopo quasi una decina di tentativi ho premuto per sbaglio a capo e questo è quello che è 
successo:

```python
--- Tentativo numero 7.
Inserisci un numero tra 0 e 2000:1796
Peccato non hai indovinato... prova ancora con un numero più alto.
--- Tentativo numero 8.
Inserisci un numero tra 0 e 2000:
Traceback (most recent call last):
  File "/home/michele/PycharmProjects/base_python/indovina_casuale.py", line 12, in <module>
    numero_provato = int(tentativo)
ValueError: invalid literal for int() with base 10: ''
```

Mi sono arrabbiato un sacco dato che ero vicino alla fine!!!! 

* Come facciamo a capire che non è stato inserito un numero?
* Possiamo verificare se il numero inserito è nell'intervallo?

Partiamo con la seconda domanda. Avete qulche idea?

```python
>>> 0 <= 5 <= 2000
True
>>> 0 <= 3000 <= 2000
False
>>> 0 <= -1 <= 2000
False
```

Si ma noi vogliamo trovare una regola per restare in un ciclo fino a quando il numero non è utilizzabile; quindi deve
essere`True` fino a che il numero non è nell'intervallo e diventare `False` quando il numero è nell'intervallo: 
esattamente il contrario di quello che abbiamo scritto. Il *Pitone* fornisce la parola chiave `not` che significa il
contrario di quello che segue:

```python
>>> not True
False
>>> not False
True
>>> not 0 <= 5 <= 2000
False
>>> not 0 <= -1 <= 2000
True
>>> not 0 <= 3000 <= 2000
True
```

Quindi se mettiamo tutto questo in un ciclo.... 3 minuti....[un aiutino](indovina_verifica_intervallo.py)

Adesso viene la parte difficile: *Come facciamo a capire che non è stato inserito un numero?*

Una idea potrebbe essere quella di verificare se `tentativo` è una stringa vuota 

```python
>>> tentativo = ''
>>> tentativo == ''
True
>>> tentativo = '12'
>>> tentativo == ''
False
```

Ma cosa succede se uno per sbaglio scrive delle lettere?

```python
--- Tentativo numero 2.
Inserisci un numero tra 0 e 2000:ab
Traceback (most recent call last):
  File "/home/michele/PycharmProjects/base_python/indovina_verifica_intervallo.py", line 14, in <module>
    numero_provato = int(tentativo)
ValueError: invalid literal for int() with base 10: 'ab'
```

Questo significa che controllare se la stringa è vuota non basta.

```python
>>> tentativo = 'ab'
>>> tentativo == ''
False
```

Bene, il *Pitone* permette dei definire dei blocchi dove se avviene un errore ci si accorge e si può salvare la 
situazione:

```python
try:
    blocclo che può avere problemi
except:
    cosa fare se avviene un problema
```

A dire il vero si possono fare cose **molto** più complesse, ma per ora questo è uno strumento *molto potente che ci
permetterà di risolvere tanti problemi.*

Sperimentiamolo: quello che genera il problema è la riga `numero_provato = int(tentativo)`, per la verità il problema
è `int(tentativo)` quando tentativo non può essere trasformato in numero.

```python
>>> tenativo = 'ab'
>>> int(tentativo)
Traceback (most recent call last):
  File "/usr/lib/python3.4/code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'ab'
```

Proviamo quindi a *catturare* questo problema

```python
>>> try:
...     int(tentativo)
... except:
...     print(tentativo + " non sembra un numero")
... 
ab non sembra un numero
>>> tentativo = "12"
>>> try:
...     int(tentativo)
... except:
...     print(tentativo + " non sembra un numero")
... 
12
```

Bene allora abbiamo tutti gli strumenti.... 3 minuti, non uno di più! Ecco una possibile 
[soluzione](indovina_protetto.py)

## Possiamo scrivere meglio in nostro gioco?

Ci sono tante maniere di scrivere i programmi. Ma anche se danno lo stesso risultato non tutte sono uguali: infatti se 
avessimo usato nomi diversi per chiamare i nostri valori cosa poteva venire fuori? 

Di seguito riporto il programma dove ho solo cambiato i nomi dei valori: risulta migliore o peggiore?

```python
import random

a = 0
b = 2000
c = random.randint(a, b)
d = 0

while True:
    d = d + 1
    print("--- Tentativo numero " + str(d) + ".")
    e = a - 1
    while not a <= e <= b:
        f = input("Inserisci un numero tra " + str(a) + " e " + str(b) + ":")
        try:
            e = int(f)
        except:
            print("Ma chi vuoi prendere in giro? '" + f + "' non è un numero!")
    if e == c:
        print("BRAVO!!!! Hai indovinato in " + str(d) + " tentativi.")
        import sys
        sys.exit()
    g = "Peccato non hai indovinato... prova ancora con un numero più "
    if e > c:
        g = g + "basso"
    if e < c:
        g = g + "alto"
    print(g + ".")
```

Io lo trovo molto più difficile da capire, ma se provate a usarlo funziona uguale a quello di prima. Quindi la prima 
cosa che impariamo è che bisogna usare nomi per i valori che spiegano subito cosa è il valore, inoltre riutilizzare
vecchi nomi è inutile e non si risparmi niente: usate nomi nuovi ogni volta che avete concetti nuovi.

Comunque anche con i nomi corretti a me sembra un programma difficile da capire: 

* tutte quelle cose insime
* tante rientranze
* un programma lungo

Possiamo scriverlo meglio? Di cosa abbiamo bisogno per renderlo più semplice?

Per esempio se avessimo una funzione `dentro_intervallo(valore, minimo, massimo)` che rende `True` se `valore` è tra
minimo e massimo allora potremmo riscrivere `while not minimo <= numero_provato <= massimo` come

```python
while not dentro_intervallo(numero_provato, minimo, massimo)
```

ma ancora meglio sarebbe

```python
while fuori_intervallo(numero_provato, minimo, massimo)
```

che spiega esattamente cosa stiamo facendo.

Quindi potremmo definire funzioni che spiegano con il loro nome esattamente cosa viene fatto e il nostro programma 
potrebbe diventare qualcosa come.

```python
while True:
    tentativo = tentativo + 1
    stampa_intro(tentativo)
    numero_provato = chiedi_numero_in_intervallo(minimo, massimo)
    stampa_info(tentativo, numero_da_indovinare, numero_provato)
    esci_se_uguale(numero_da_indovinare, numero_provato)
```

Sarebbe un programma semplice capire... vediamo se riusciamo a farlo.

### Come si definisce una funzione

```python
def funzione(a, b, ... ):
    contenuto
    return valore
```

Sperimentiamo: facciamo una funzione che moltiblica gli argomenti passati. 

```python
>>> def moltiplica(a, b):
...     return a*b
... 
>>> moltiplica(2,3)
6
>>> moltiplica("a",3)
'aaa'
```

Sembra semplice, che ne dite di provare a scrivere la funzione `fuori_intervallo(numero, minimo, massimo)` e sostituirla
nel ciclo `while`. 5 Minuti... ce la potete fare! Per un confronto guardate [quì](indovina_refact_1.py)

Ora proviamo a fare 

* `stampa_intro(numero_tentativo)`
* `chiedi_numero_in_intervallo(min_val, max_val)`
* `stampa_info(numero_tentativo, obbiettivo, numero)`
* `esci_se_uguale(obbiettivo, numero)`

Un piccolo aiutino: sostituite `numero_da_indovinare = random.randint(minimo, massimo)` con il vecchio  
`numero_da_indovinare = 1234` e usate il carattere `#` per commentare la vecchia riga fino a quando il vostro programma 
non funzionerà bene come prima. Verificate provando che il gioco funziona a ogni modifica del vostro programma. Qunado
avete finito e tutto funziona bene potete rimettere il numero casuale.

Forse per fare questo ci vuole un po di tempo e tanti tentativi e la soluzione che trovate [quì](indovina_refact_2.py)
è un tantino esagerata (ma non troppo... si può fare molto meglio) ma credo che ora leggendo il vostro gioco capite 
subito quello che fa in ogni punto. Personalmente credo che sia sempre meglio lasciare le cose non solo funzionanti ma 
comprensibili... e trovo questo anche molto **divertente**!


