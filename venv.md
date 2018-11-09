# Virtuální prostředí


Pro správu závislostí vašeho projektu používejte 
[virtuální prostředí](https://docs.python.org/3/tutorial/venv.html)
a
[pip](https://pip.pypa.io/en/stable/).

Jaký problém že řeší virtuální prostředí? Čím více Python projektů  máte, tím
je pravděpodobnější, že potřebujete pracovat s různými verzemi té stejné
knihovny nebo dokonce samotného Pythonu. Novější verze knihoven pro jeden
projekt mohou narušit kompatibilitu v jiném projektu.

Virtuální prostředí, jsou nezávislé skupiny Pythonních knihoven, jedena skupina
pro každý projekt. Balíčky nainstalované pro jeden projekt nebudou mít vliv na
ostatní projekty nebo balíky operačního systému.

Python 3 je dodáván s modulem 
[`venv`](https://docs.python.org/3/library/venv.html),
který vytváří virtuální prostředí.


## Vytvoření virtuálního prostředí

Vytvořte si složku pro projekt. Virtuální prostředí umístíme do složky `.venv`
v našem projektu.

Linux:

    $ mkdir myproject
    $ cd myproject
    $ python3 -m venv venv

Windows:

    $ py -3 -m venv venv


## Aktivace virtuálního prostředí

Linux:

Než začnete práci na projektu, je třeba příslušné virtuální prostředí
aktivovat: 

Linux:

    $ . venv/bin/activate

Windows:


    > venv\Scripts\activate

Jakmile aktivujete virtuální prostředí změní se vám váš 
[prompt](https://cs.wikipedia.org/wiki/Příkazový_řádek#Prompt).


## Deaktivace virtuálního prostředí

Někoho možná zajímá jak se to vypne:

    $ deacitvate
    > deacitvate



# Instalace 

V aktivovaném virtuálním prostředí potom můžeme nainstalovat požadovanou
knihovnu(y).

    $ pip install pyglet
    $ pip install Flask
    $ pip install Flask-misaka
    $ pip install markdown
    $ pip install 'markdown==2.6.7'

Ještě je myslím dobré poznamenat, že `pip` pro instalaci knihoven je možné
použít i mimo virtuální prostředí. Instalace bude potom provedena do systému.
To znamená, že k tomu budete potřebovat administrátorská práva a že se
připravíte o všechny výše popsané výhody.



