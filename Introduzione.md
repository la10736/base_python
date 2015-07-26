# Introduzione a *Python*

*Python* è un linguaggio di programmazione e è uno dei tanti modi che abbiamo per parlare al computer e dirgli quello 
che **deve fare**. Per far capire la lingua *Python* al nostro computer dobbiamo aver installato il programma di 
traduzione (vedi la [pagina requisiti](requisiti.md)) e l'ambiente di sviluppo.

Possiamo parlare con il nostro computer nella lingua *Python* in due modi

* Interattivo
* Continua

In modalità interrattiva noi diremo delle cose al computer e lui ci risponderà subito. In modalità continua noi 
prepariamo tutto quello che dobbiamo dire e crediamo che il computer debba sapere per fare quello che vogliamo, gli 
diamo da leggere la pappardella e quardiamo la risposta.

E' neccessario sapere che tutti i linguaggi sono basati essenzialmente su parole inglesi e quindi sfortunatamente 
non potremo dire al computer cose del tipo

    se valore == valore_da_indovinare:
        stampa("Sei stato un grande....hai indovinato")
    altrimentise valore > valore_da_indovinare:
        stampa("Sei ancora un po abbondante")
    altrimenti:
        stampa("Io aggiungerei qualcosina")
        
Ma dovremmo usare comandi del tipo:

    if valore == valore_da_indovinare:
        print("Sei stato un grande....hai indovinato")
    elif valore > valore_da_indovinare:
        print("Sei ancora un po abbondante")
    else:
        print("Io aggiungerei qualcosina")

Notare che alcune parole sono necessariamente in inglese come `if`, `else`, `print` (`se`, `altrimenti`, `stampa`) 
altre sono forma contratte come `elif` che e' una contrazzione di `else if` e altre restano in italiano. *Solo le parole
base del linguaggio o quelle che ci danno altri per fare cose già fatte **devono** essere in inglese, noi per le nostre
cose possiamo usare l'italiano*.


## La prima chiacchierata: ci presentiamo a *Python*
Bene, è venuto il momento di presentarci a questo serpentone bonaccione. Apriamo IDLE o PyCharm (vedi la 
[pagina requisiti](requisiti.md)) iniziamo a parlare con la console (modo interattivo) 

    >>> ciao come ti chiami?

La risposta è:

    SyntaxError: invalid syntax

Cosa significa questo?

1. Che si chiama `SyntaxError` e che nella sua lingua tu come ti chiami si dice `invalid syntax`
2. Che non ha voglia di parlare e non dobbiamo disturbarlo
3. Che non capisce quello che abbiamo scritto dato che ha trovato un *errore di sintassi*

La risposta giusta è la 3 e ci dice anche che *Python* (da ora in poi *Pitone* per gli amici) capisce solo se si scrive 
esattamente nella sua lingua: è molto schizzinoso a rigurdo, quando non seguiremo le regole ci maderà improperi del
tipo:

    SyntaxError: invalid syntax
    SyntaxError: unexpected indent

Ma andiamo avanti con i nostri esperiemnti (il *Pitone* incoraggia gli esperimenti):

    >>> 1.3
    1.3
    >>> 4
    4
    >>> ciao
    Traceback (most recent call last):
      File "<pyshell#10>", line 1, in <module>
        ciao
    NameError: name 'ciao' is not defined
    >>> "ciao"
    'ciao'
    >>> 'ciao'
    'ciao'
    >>> "ciao" == 'ciao'
    True
    >>> ciao come stai
    SyntaxError: invalid syntax
    >>> 'ciao come stai'
    'ciao come stai'
    >>> 7a
    SyntaxError: invalid syntax

Quanti comportamenti diversi!!!!!

* `1.3` sembra che abbia fatto il pappagallo e ci abbia ripetuto `1.3` senza arrabbiarsi: forse ci siamo capiti questo 
è un *numero*?
* `4` ancora il pappagallo senza arrabbiarsi: sembra proprio che lo abbia capito che è un *numero*...
* `ciao` non è andato benissimo: dice che ciao non è definito... concludiamo che i numeri sono definiti e `ciao` no!
* `"ciao"` di nuovo il quasi pappagallo ( *quasi* perché ha cambiato le virgolette): `"ciao"` è definito, ma `ciao` no 
... strano
* `'ciao'`pappagallo : `"ciao"` e `'ciao'` sono definiti... saranno forse uguali?
* `"ciao" == 'ciao'` ci risponde `True` ( **vero** in italiano)... abbiamo chiesto al *Pitone* di toglierci un dubbio 
che ci era venuto `"ciao"` e `'ciao'` sono la stessa cosa
* `ciao come stai` non ci capisce... di nuovo la sintassi sbagliata
* `'ciao come stai'` questo lo capisce e fa di nuovo il pappagallo: mi sa che quando riconosce un valore (numero o 
stringa che sia) lo ripete...
* `7a` Sintassi invalida: non dice che non è definito ma dice che la sintassi è invalida... vuol forse dire che `7a`
non può essere definito?

Possiamo quindi riassumere alcune regole:

1. Quando trova un valore definito lo riproduce
2. Non tutto può essere definito
3. I numeri sono definiti
4. Le frasi tra virgolette (singole `'` o doppie `"`) sono definite

## Ampliare le conoscenze del *Pitone*: definiamo nuove parole

Ora chiediamoci: quale e' un modo semplice per definire qualcosa? La maniera più semplice per definire qualcosa è ...
dire che qualcosa è uguale a qualcos'altro

    >>> ciao = 'ciao'
    >>> ciao
    'ciao'
    >>> ciao = 3
    >>> ciao
    3
    >>> ciao = "Basta non ti voglio più salutare! Lasciami stare!"
    >>> ciao
    'Basta non ti voglio più salutare! Lasciami stare!'

Ora, dopo che abbiamo definito `ciao` non si arrabbia più se scriviamo solo `ciao`, anzi ci risponde con quello che gli 
abbiamo detto che vale 

**ATTENZIONE** Questa volta il *Pitone* non ci ha risposto nulla quando abbiamo definieto `ciao`... questo ci porta a 
capire altre due regole

1. Per definire qualcosa basta associarlo a qualcosa di definito
2. Il *Pitone* stampa solo se trova un errore o gli diamo qualcosa di definito

## Le operazioni con il *Pitone*

### I Numeri

    >>> 2 + 2
    4
    >>> 3 * 2
    6
    >>> 2 / 3
    0.6666666666666666
    >>> 6 / 3
    2.0
    >>> 5 - 7
    -2
    >>> 7 / 0
    Traceback (most recent call last):
      File "<pyshell#29>", line 1, in <module>
        7 / 0
    ZeroDivisionError: division by zero
    >>> 2 ** 3
    8
    >>> 3 ** 2
    9
    >>> 7 % 3
    1
    
E' abbastanza chiaro che il *Pitone* è bravo a fare i conti e come tutti si arrabbia se gli si chiede di dividere 
qualcosa per 0. Inoltre oltre alle classiche somme, sottrazoni e divisioni permette di fare elevamenti a potenza 
`**` e calcolare il resto di una divisione `%`. Inoltre conosce tantissime altre funzioni matematiche, bisogna solo
dirgli dove cercarle (`import math`) ma di questo magari parliamo più avanti.

E se definiamo qualcosa come dei numeri possiamo fare le operazioni? **Certamente**
    

    >>> a = 5
    >>> b = 3
    >>> c = 2
    >>> d = (a + b)/c
    >>> d
    4.0

### Le stringhe

Ok, se abbiamo due numeri le operazioni sono chiare, ma se abbiamo delle strighe cosa succede?

Ricordatevi: **Il *Pitone* non si arrabbia se voi provate**. Comunque non morde, e il computer non scoppia!

Quindi:

    >>> 'ciao' + ' ' + 'a tutti'
    'ciao a tutti'
    >>> 'ciao' * 2
    'ciaociao'
    >>> 'ciao' + 2
    Traceback (most recent call last):
      File "<pyshell#48>", line 1, in <module>
        'ciao' + 2
    TypeError: Can't convert 'int' object to str implicitly
    >>> 'ciao' * 2.1
    Traceback (most recent call last):
      File "<pyshell#49>", line 1, in <module>
        'ciao' * 2.1
    TypeError: can't multiply sequence by non-int of type 'float'
    >>> 'ciao' / 2
    Traceback (most recent call last):
      File "<pyshell#45>", line 1, in <module>
        'ciao' / 2
    TypeError: unsupported operand type(s) for /: 'str' and 'int'
    >>> 'ciao' - 'ciao'
    Traceback (most recent call last):
      File "<pyshell#46>", line 1, in <module>
        'ciao' - 'ciao'
    TypeError: unsupported operand type(s) for -: 'str' and 'str'
    >>> 'ciao' * 'ciao'
    Traceback (most recent call last):
      File "<pyshell#47>", line 1, in <module>
        'ciao' * 'ciao'
    TypeError: can't multiply sequence by non-int of type 'str'

Non solo molte le operazioni che possiamo fare con le strighe, ma sono quelle ragionevoli:

* Sommare una stringa a un'altra vuol dire concatenarle
* Moltiplicare una stringa per un numero `n` intero vuol dire conatenare la stringa `n` volte

Quindi cosa vuol dire moltiplicare una striga per un numero negativo intero... chiediamo al *Pitone*:

    >>> 'ciao' * (-1)
    ''
La cosa più ovvia: la stringa vuota.

### E con i nuovi nome definiti?

Cosa succede se definiamo dei nuovi nomi (da ora in poi siamo adulti e li chiamiamo *varibili*) e facciamo operazioni 
con loro? 

E se definiamo qualcosa come dei numeri o delle stribnghe possiamo fare le operazioni? **Certamente**
    

    >>> a = 5
    >>> b = 3
    >>> c = 2
    >>> d = (a + b)/c
    >>> d
    4.0
    >>> ciao = 'ciao'
    >>> spazio = ' '
    >>> ciao + spazio + ciao
    'ciao ciao'
    >>> ciao * a
    'ciaociaociaociaociao'
    >>> che_bel_saluto = (ciao + spazio) * b
    >>> •••••••••••
    SyntaxError: invalid character in identifier
    >>> che_bel_saluto
    'ciao ciao ciao '
    
Quanto è furbo sto *Pitone*: *capisce le operazioni da giuste da fare*.
 
## Condizioni e Cicli

Parlare di

* `if`, `else` e `elif`
* `while cond` e in particolare `while True`...`break`
* `for x in ...`

## Il primo gioco python: indovina il numero!



## Lo zen del *Pitone*
**Da rimuovere anche se bisogna trovare un punto dove citarlo e richiamare alcune note**

    >>> import this
    The Zen of Python, by Tim Peters
    
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!



