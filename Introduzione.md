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
* `"ciao"` di nuovo il quasi pappagallo (*quasi* perché ha cambiato le virgolette): `"ciao"` è definito, ma `ciao` no 
... strano
* `'ciao'`pappagallo : `"ciao"` e `'ciao'` sono definieti... saranno forse uguali?
* `"ciao" == 'ciao'` ci risponde `True` (vero in italiano)... abbiamo chiesto al *Pitone* di toglierci un dubbio che ci
era venuto `"ciao"` e `'ciao'` sono la stessa cosa
* `ciao come stai` non ci capisce... di nuovo la sintassi sbagliata
* `'ciao come stai'` questo lo capisce e fa di nuovo il pappagallo: misa che quando riconosce un valore (numero o 
stringa che sia) lo ripete...


