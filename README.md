# PRG -- Kameny

[![Join the chat at gitter.im/spseol/Python](https://badges.gitter.im/spseol/PRG-No.svg)](https://gitter.im/spseol/Python?utm_source=share-link&utm_medium=link&utm_campaign=share-link)

Ve škole jsme si vytvořili objektovou třídu `Stone`. Najdete ji v souboru
[kameny.py](kameny.py). **Vašim úkolem bude zařídit to tak, aby se kameny
odráželi od okrajů hrací plochy.** Pokud se vám kameny nelíbí dejte si místo
nich třeba bubliny, záleží jen na vás.

Takovou malou nápovědou jak začít tento problém řešit je metoda `bounce`. Tu je
třeba přepsat, protože celý problém trochu očurává. Vaše řešení bude samozřejmě
tak jak to má být, tedy že **úhel dopadu se bude rovnat úhlu odrazu**.

## Než začnete tvořit

Používáme zde knihovnu/framework [pyglet](https://pyglet.readthedocs.io).
Nejprve je třeba ji nainstalovat. K tomu můžete použít mini-návod
[venv.md](venv.md).


## Malé připomenutí trošky teorie

Obrovskou výhodou objektového programování je, že popis objektu napíšeme jen
jednou (to se děje v objektové třídě `Stone`), ale "žijících" objektů této
objektové třídy můžeme vytvořit velice jednoduše více. Popis chování objektu
nalezneme v objektové třídě. Samotné vytvoření objektu se děje když zavoláme
objektovou třídu jakoby to byla funkce:

    stone = Stone()

Kromě vytvoření objektu je třeba ještě zaregistrovat jeho metodu `tick` aby se
pravidelně (30 krát za sekundu) prováděla a překreslovala kameny na obrazovce.

    pyglet.clock.schedule_interval(stone.tick, 1 / 30)

A je také dobré si všechny vytvořené objekty zapamatovat a uložit si je do
seznamu

    stones.append(stone)

## Aby se nám to nerozsypalo

*Následující řádky jsou pro ty, co se chtějí dozvědět trochu víc...*

Pokud se pořádně zadíváte na třídu `Stone` zjistíte, že máme zaděláno na malý
zádrhel: jedna a ta stejná informace se uchovává ve dvou atributech
`Stone.sprite.x` i `Stone.x`. Očekávali bychom, že pokud něco zapíšeme do
atributu `Stone.x`, přesune se objekt na zadanou souřadnici. To se ale nestane,
protože zápis do `Stone.x` nijak neovlivní `Stone.sprite.x`. Prostě a jednoduše
bychom potřebovali nějak svázat `Stone.sprite.x` i `Stone.x`. 

Stejné je to se `Stone.sprite.y` a `Stone.y`.

Z atributu tedy uděláme *vlastnost* --
[*property*](https://docs.python.org/3/library/functions.html?highlight=property#property)
a můžeme její čtení nebo zápis (nebo mazání) svázat s libovolnou další akcí.

První možnost jak to celé napsat je použít 
[decorator](https://docs.python-guide.org/writing/structure/#decorators)
`@property`.

Řešení najdete v souboru [kameny-property.py](kameny-property.py)
[c66e727](https://github.com/spseol/PRG-kameny/commit/c66e72759c7e8135347f045e17c6375b0455b857)

Dalším řešením je použít vestavěných funkcí
[`setattr`](https://docs.python.org/3/library/functions.html?highlight=property#setattr),
[`getattr`](https://docs.python.org/3/library/functions.html?highlight=property#getattr)
a [`property`](https://docs.python.org/3/library/functions.html?highlight=property#property).
Děje se de-facto to stejné jako v předchozím případě, jen je to trochu jinak zapsané.

Řešení je v souboru [kameny-property_proxy.py](kameny-property_proxy.py)
[d7641a3](https://github.com/spseol/PRG-kameny/commit/d7641a35909a0b891624327dbef12ba8867d975a)
