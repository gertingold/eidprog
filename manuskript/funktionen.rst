**********
Funktionen
**********

Funktionen im mathematischen Sinne sind uns in Physik und
Materialwissenschaften wohlbekannt. Dass solche Funktionen auch von
Programmiersprachen zur Verfügung gestellt werden, haben wir z.B. im Abschnitt
:ref:`mathfunc` gesehen. Allerdings ist der Begriff der Funktionen in
Programmiersprachen wesentlich weiter gefasst. So muss eine Funktion nicht
unbedingt ein Argument besitzen, und sie muss auch nicht unbedingt einen Wert
zurückgeben. In manchen Sprachen wird nach diesem letzten Kriterium
unterschieden. So kennt FORTRAN *functions*, die ein Resultat zurückgeben, und
*subroutines*, die dies nicht tun.

Wozu sind Funktionen gut, wenn man einmal davon absieht, dass Funktionen dem
Naturwissenschaftler vertraut sind? Funktionen eignen sich vor allem dazu,
Programmcode, der sonst im Programm mehrfach auftreten würde, an einer einzigen
Stelle unterzubringen. Wählt man geeignete Funktionsnamen, so kann dies zum
einen die Lesbarkeit des Codes deutlich steigern. Zum andern verbessert sich
auch die Wartbarkeit erheblich, da Korrekturen nur an einer Stelle vorgenommen
werden müssen. Andernfalls muss man auf eine konsistente Korrektur des Programms
an verschiedenen Stellen achten. Stellt man also beim Programmieren fest, dass
sich Code wiederholt, so sollte man sich überlegen, ob es nicht sinnvoll wäre,
für die betreffende Aufgabe eine Funktion zu definieren. Auch ähnliche Aufgaben
kann man in einer Funktion unterbringen, wenn man geeignete Funktionsargumente
einführt. Es hilft, wenn man sich beim Programmieren immer daran erinnert,
sich nicht unnötig zu wiederholen. [#oaoo]_ Schließlich ist die Verwendung
von Funktionen auch dann angebracht, wenn man die gleiche Funktionalität in
verschiedenen Programmen benötigt. Man kann solche Funktionen in einem Modul
sammeln und dann bei Bedarf importieren, wie wir es schon mit dem ``math``-Modul
und den darin enthaltenen Funktionen getan haben.

.. _funcdef:

=====================
Funktionsdefinitionen
=====================

Betrachten wir zunächst eine Funktion, die weder ein Argument besitzt noch
Daten zurückgibt.

.. code-block:: python
   :linenos:

   def f():
       print("in der Funktion f")
   
   print("** Anfang")
   f()
   print("** Ende")

Hier wird in den Zeilen 1 und 2 eine Funktion definiert. In der ersten Zeile
der Definition steht dabei zunächst das Schlüsselwort ``def``. Dann folgt der
Funktionsname, der im Rahmen der auch für Variablen geltenden Regeln gewählt
werden kann. Das anschließende Klammerpaar ist hier leer, weil keine Argumente
übergeben werden. Andernfalls sind hier die Funktionsargumente aufzuführen.
Auf das Klammerpaar kann in Python in keinem Fall verzichtet werden.  Die Zeile
muss mit einem Doppelpunkt enden. Der Inhalt der Funktionsdefinition ergibt
sich wie immer in Python aus der Einrückung. Die nicht mehr eingerückte Zeile 4
gehört somit nicht mehr zur Funktionsdefinition. Die leere Zeile 3 spielt bei
der Interpretation des Codes keine Rolle, sondern dient nur der
Übersichtlichkeit.

Wenn der Pythoninterpreter dieses Beispielprogramm ausführt, wird zunächst die
Funktion ``f`` definiert. Dabei wird jedoch noch nicht der darin enthaltene
Code ausgeführt. Ab Zeile 4 werden dann die Anweisung ausgeführt. die Anweisung
in Zeile 5 weist den Interpreter an, den Funktionscode, hier die Zeile 2, auszuführen.
Anschließend wird mit der Abarbeitung des Programms in Zeile 6 fortgefahren. 
Entsprechend lautet die Ausgabe dieses Programms

::

  ** Anfang
  in der Funktion f
  ** Ende

Einer Funktion können auch ein oder mehrere Argumente übergeben werden. Sehen
wir uns wieder ein einfaches Beispiel an.

.. code-block:: python
   :linenos:

   def f(k):
       print("Das Quadrat von {} ist {}.".format(k, k**2))
   
   for n in range(3):
       f(n)

In den Zeilen 1 und 2 wird die Funktion ``f`` definiert, deren Aufgabe darin
besteht, das Quadrat des Arguments ``k`` zu bestimmen und in geeigneter Weise
auszugeben. In den Zeilen 4 und 5 wird diese Funktion dann in einer Schleife dreimal
mit folgendem Ergebnis ausgeführt:

::

   Das Quadrat von 0 ist 0.
   Das Quadrat von 1 ist 1.
   Das Quadrat von 2 ist 4.

Alternativ könnte man die Funktion den Funktionswert berechnen und an den aufrufenden
Programmteil zurückgeben lassen. Die gleiche Ausgabe lässt sich also auch folgendermaßen
erhalten:

.. code-block:: python

   def f(k):
       ergebnis = k**2
       return ergebnis

   for n in range(3):
       print("Das Quadrat von {} ist {}.".format(n, f(n)))

Im Gegensatz zu einigen anderen Programmiersprachen ist die ``return``-Anweisung
nicht erforderlich, um das Ende der Funktionsanweisung zu kennzeichnen. Dies
geschieht in Python ausschließlich mit Hilfe der Einrückung. Die
``return``-Anweisung wird jedoch benötigt, um Ergebnisse an den aufrufenden
Code zurückzugeben. Die gerade vorgestellte Funktionsdefinition kann noch
kompakter gestaltet werden, da die ``return``-Anweisung nicht nur eine
Variable, sondern einen ganzen Ausdruck enthalten kann:

.. code-block:: python

   def f(k):
       return k**2

Bei Bedarf kann eine Funktion auch mehrere ``return``-Anweisungen enthalten, wie in
dem folgenden Beispiel. Die Funktion :func:`is_prime` soll feststellen, ob es sich
bei der Integer-Variable ``n`` um eine Primzahl handelt.

.. code-block:: python

   def is_prime(n):
       for divisor in range(2, n):
           if n % divisor == 0:
               return False
       return True

   for n in range(2, 20):
       if is_prime(n):
           print(n)

|frage| Der hier vorgestellte Primzahltest ist nicht sonderlich effizient. Wie könnte
man ihn verbessern?

Funktionen können auch mehr als ein Argument besitzen und mehr als einen Wert zurückgeben
wie folgendes Beispiel zeigt:

.. code-block:: python

   def vektorfeld(x, y):
       ax = -y
       ay = x
       return ax, ay

   for x in range(2):
       for y in range(2):
           vx, vy = vektorfeld(x, y)
           print("({:2},{:2}) -> ({:2},{:2})".format(x, y, vx, vy))

Wichtig ist, dass die Zuordnung durch die Position der jeweiligen Variablen erfolgt, nicht
durch deren Namen. Es gibt allerdings auch die Möglichkeit einer namensbasierten Übergabe
der Argumente, die wir im Abschnitt :ref:`funckeywords` kennenlernen werden.

|weiterfuehrend| Eine Funktionsdefinition kommt nicht ohne einen Codeblock aus, der auf
die mit ``def`` beginnende Deklarationszeile folgt. Gelegentlich möchte man beim Entwickeln
eines Programms bereits die zu erstellenden Funktionen notieren, ohne die entsprechende
Funktionalität gleich zu implementieren. Um dennoch schon zu diesem Zeitpunkt ein syntaktisch
korrektes Programm zu haben, kann man den Befehl ``pass`` verwenden, der lediglich dazu
dient, den benötigten Codeblock bereitzustellen. ``pass`` hat ansonsten keinerlei Auswirkungen
auf den Programmablauf.

|weiterfuehrend| Auch wenn eine Funktion keine ``return``-Anweisung
enthält, wird ein Wert zurückgegeben, nämlich ``None`` wie folgendes
einfache Beispiel zeigt.

>>> def f():
...     pass
...
>>> print(f())
None

Gelegentlich kann es vorkommen, dass man sich über diese unerwartete
Rückgabe wundert. Grund hierfür ist dann häufig eine vergessene 
``return``-Anweisung.

.. _funcdoc:

============================
Dokumentation von Funktionen
============================

Wie generell beim Programmieren ist es auch in Funktionen sinnvoll, an eine ausreichende
Dokumentation zu denken. Dies könnte mit Hilfe von Kommentaren erfolgen, die mit einem
``#`` eingeleitet werden. In Python gibt es für Funktionen jedoch eine geeignetere Art der
Dokumentation, nämlich einen Dokumentationsstring, der direkt auf die erste Zeile der
Funktionsdefinition folgt. Das könnte beispielsweise folgendermaßen aussehen:

.. code-block:: python

   from math import sqrt

   def mitternacht(a, b, c):
       """Berechne die beiden Lösungen einer quadratischen Gleichung
       ax^2+bx+c=0.
    
       Es wird die Mitternachtsformel verwendet. 
       Achtung: Es wird stillschweigend vorausgesetzt, dass b^2-4ac>0.
    
       """
       diskriminante = sqrt(b**2-4*a*c)
       root1 = (-b+diskriminante)/(2*a)
       root2 = (-b-diskriminante)/(2*a)
       return root1, root2

Der Dokumentationsstring wird hier nicht nur mit einem, sondern mit drei
Anführungszeichen begrenzt, da er dann über mehrere Zeilen gehen kann. Der
Vorteil dieser Dokumentationsweise besteht darin, dass dieser
Dokumentationstext mit dem Befehl ``help(mitternacht)`` ausgegeben werden kann,
wie wir im Abschnitt :ref:`float` schon gesehen hatten, wo ``help(math)`` die
Dokumentation für das Modul ``math`` ausgab.

.. code-block:: python

   >>> help(mitternacht)

   Help on function mitternacht in module __main__:
   
   mitternacht(a, b, c)
       Berechne die beiden Lösungen einer quadratischen Gleichung ax^2+bx+c=0.
       
       Es wird die Mitternachtsformel verwendet.
       Achtung: Es wird stillschweigend vorausgesetzt, dass b^2-4ac>0.

Weitere Hinweise zu Dokumentationsstrings sind in :pep:`257` zu finden.

.. _lokalglobal:

===========================
Lokale und globale Variable
===========================

Dem letzten Beispiel im Abschnitt :ref:`funcdef` kann man entnehmen, dass die
Benennung der zurückzugebenden Variablen in der Funktionsdefinition (``ax,ay``)
und in der Anweisung, die den Funktionsaufruf enthält, (``vx,vy``)  nicht
identisch sein muss. Gleiches gilt auch für die Argumente, die der Funktion
übergeben werden. Daraus folgt unter anderem, dass die Reihenfolge der
Argumente in der Funktionsdefinition und im Funktionsaufruf übereinstimmen
müssen. Hier hilft es auch nicht, die gleichen Variablennamen zu verwenden, wie
aus den folgenden Überlegungen deutlich wird. Will man die Argumente in einer
willkürlichen Reihenfolge verwenden, so muss man Schlüsselworte verwenden, wie
im Abschnitt :ref:`funckeywords` genauer erklärt wird.

Wie verhält es sich nun mit Variablennamen, die sowohl in der Funktionsdefinition als auch 
im Hauptprogramm vorkommen? Betrachten wir dazu ein Beispiel

.. code-block:: python
   :linenos:

   def f(x):
       x = x+1
       print("lokale Variable: ", locals())
       print("globale Variable:", globals())
       return x*y

   x = 5
   y = 2
   print("f(3) =", f(3))
   print("x =", x)

das die folgende Ausgabe produziert:

.. code-block:: python

   lokale Variable:  {'x': 4}
   globale Variable: {'f': <function f at 0xb7e42ed4>, 
                      '__builtins__': <module '__builtin__' (built-in)>, 
                      '__file__': 'test.py', 
                      '__package__': None,
                      'x': 5, 
                      'y': 2, 
                      '__name__': '__main__', 
                      '__doc__': None}
   f(3) = 8
   x = 5

In Python kann man sich mit Hilfe der eingebauten Funktionen :func:`globals` und
:func:`locals` die globalen bzw. lokalen Variablen ausgeben lassen, die die Funktion
sieht. Die Variable ``x`` kommt dabei sowohl im lokalen als auch im globalen Kontext
vor. Die lokale Variable ``x`` wird zu Beginn der Abarbeitung der Funktion generiert
und gemäß Zeile 9 mit dem Wert 3 belegt. Nach dem Inkrementieren in Zeile 2 ergibt
sich der in :func:`locals` angegebene Wert von 4. Gleichzeitig hat ``x`` im globalen
Kontext den Wert 5. 

Wird auf eine Variable zugegriffen, so sucht Python zunächst in den lokalen
Variablen, dann in den globalen Variablen und zuletzt in den eingebauten
Pythonfunktionen. Für die Variable ``x`` hat dies in der Funktion zur Folge, dass 
die lokale Variable gemeint ist. So verändert das Inkrementieren in Zeile 2 auch
nicht den Wert der globalen Variable ``x``. Nachdem die Variable ``y`` nicht in den
lokalen Variablen vorkommt, greift Python in Zeile 5 auf die globale Variable mit
dem Wert 2 aus Zeile 8 zurück. Innerhalb der Funktion ist es nicht möglich, globale
Variable zu verändern, was in den meisten Fällen auch nicht erwünscht sein dürfte.
Eine wichtige Ausnahme hiervon sind Listen. Den Grund hierfür werden wir in Kapitel
:ref:`listen` besser verstehen.

Greift man beim Programmieren in einer Funktion auf eine globale Variable
zurück, so sollte man sich immer überlegen, ob es nicht günstiger ist, der
Funktion diese Variable als Argument zu übergeben. Dies führt zwar zu
aufwendigeren Funktionsaufrufen, hilft aber, bei Änderungen im aufrufenden
Programmcode Fehler in der Funktion zu vermeiden. Solche Fehler können leicht
dadurch entstehen, dass man die Verwendung der globalen Variable in der Funktion
übersieht. Will man überlange Argumentlisten vermeiden, so können auch Techniken
von Nutzen sein, die wir im Kapitel :ref:`oop` besprechen werden.


====================
Rekursive Funktionen
====================

Um die Verwendung von rekursiven Funktionen zu illustrieren, betrachten wir die
Berechnung der Fakultät ``n!``, die man durch Auswertung des Produkts ``1·2·``
… ``·(n-1)·n`` erhält. Der folgende Code stellt eine direkte Umsetzung
dieser Vorschrift dar:

.. code-block:: python
   :linenos:

   def fakultaet(n):
       produkt = 1
       for m in range(n):
           produkt = produkt*(m+1)
       return produkt
   
   for n in range(1, 10):
       print(n, fakultaet(n))

Alternativ lässt sich die Fakultät auch rekursiv definieren. Mit Hilfe der Beziehung
``n!=(n-1)!·n`` lässt sich die Fakultät von ``n`` auf die Fakultät von ``n-1``
zurückführen. Wenn man nun noch verwendet, dass ``0!=1`` ist, kann man die 
Fakultät rekursiv bestimmen, wie der folgende Code zeigt:

.. code-block:: python
   :linenos:

   def fakultaet_rekursiv(n):
       if n>0:
           return n*fakultaet_rekursiv(n-1)
       elif n==0:
           return 1
       else:
           raise ValueError("Argument darf nicht negativ sein")
   
   for n in range(1, 10):
       print(n, fakultaet_rekursiv(n))

Hier wird nun in der Funktion wiederum die Funktion selbst aufgerufen, was
nicht in jeder Programmiersprache erlaubt ist. Der Vorteil einer rekursiven
Funktion ist häufig die unmittelbare Umsetzung einer Berechnungsvorschrift.
Allerdings muss darauf geachtet werden, dass die Aufrufserie irgendwann beendet
wird. Ist dies nicht der Fall, könnte das Programm nicht zu einem Ende kommen
und, da Funktionsaufrufe auch Speicherplatz erfordern, immer mehr Speicher
belegen. Über kurz oder lang wird das Betriebssystem dann das Programm beenden,
wenn nicht gar der Computer abstürzt und neu gestartet werden muss. Daher ist
in der Praxis die Zahl der rekursiven Aufrufe begrenzt. In Python lässt sich
diese Zahl in folgender Weise bestimmen:

.. code-block:: python

   >>> import sys
   >>> sys.getrecursionlimit()
   1000

Mit ``setrecursionlimit(n)`` lässt sich mit einer natürlichen Zahl ``n``
als Argument notfalls die Rekursionstiefe verändern, was jedoch sicher
kein Ausweg ist, wenn die rekursive Programmierung fehlerhaft durchgeführt
wurde.

.. _funcarg:

=======================================
Funktionen als Argumente von Funktionen
=======================================

In Python können, im Gegensatz zu vielen anderen Programmiersprachen, Funktionen 
Variablen zugewiesen oder als Argumente von anderen Funktionen verwendet werden. 
Folgendes Beispiel illustriert dies:

.. code-block:: python
   :linenos:

   >>> from math import sin, cos
   >>> funktion = sin
   >>> print(funktion(1), sin(1))
   0.841470984808 0.841470984808
   >>> for f in [sin, cos]:
   ...     print("{}: {:.6f}".format(f.__name__, f(1)))
   ...
   sin: 0.841471
   cos: 0.540302

In Zeile 2 wird die Funktion ``sin`` der Variable ``funktion``, die natürlich
im Rahmen der Regeln für die Benennung von Variablen auch anders heißen könnte,
zugewiesen. Statt der Funktion ``sin`` könnte hier auch eine selbst definierte
Funktion stehen. Zu beachten ist, dass der Funktion auf der rechten Seite kein
Argument mitgegeben wird. Aus den Zeilen 3 und 4 wird deutlich, dass nach der
Zuweisung in Zeile 2 auch die Variable ``funktion`` verwendet werden kann, um den 
Sinus zu berechnen. Eine mögliche Anwendung ist in den Zeilen 5 und 6 angedeutet,
wo eine Schleife über zwei Funktionen ausgeführt wird. Zeile 6 zeigt zudem,
dass das Attribut ``__name__`` des Funktionsobjekts den entsprechenden 
Funktionsnamen angibt.

Interessant ist auch die Möglichkeit, Funktionen als Argumente zu übergeben.
Wenn zum Beispiel die Ableitung einer mathematischen Funktion numerisch
bestimmt werden soll, kann man für jede spezielle mathematische Funktion, die
abgeleitet werden soll, eine entsprechende Ableitungsfunktion definieren.
Viel besser ist es natürlich, dies nur einmal für eine beliebige mathematische
Funktion zu tun. Eine mögliche Lösung könnte folgendermaßen aussehen:

.. code-block:: python
   :linenos:

   from math import sin

   def ableitung(f, x):
       h = 1e-7
       df = (f(x+h)-f(x-h))/(2*h)
       return df

   print(ableitung(sin, 0))

Natürlich ist dieser Code verbesserungsbedürftig. Er sollte unter anderem
ordentlich dokumentiert werden, und man müsste sich Gedanken über die
Überprüfung der Konvergenz des Grenzwertes ``h``\ →0 machen. Unabhängig davon
kann der Ableitungscode in den Zeilen 3-6 aber für beliebige abzuleitende
mathematische Funktionen aufgerufen werden.  Jede Verbesserung dieses Codes
würde damit nicht nur der Ableitung einer speziellen mathematischen Funktion
zugute kommen, sondern potentiell jeder numerischen Ableitung einer
mathematischen Funktion mit Hilfe dieses Codes.

.. _lambdafunktionen:

=================
Lambda-Funktionen
=================

In Abschnitt :ref:`funcdef` hatten wir ein Beispiel gesehen, in dem die
Berechnung der Funktion vollständig in der ``return``-Anweisung untergebracht
war. Solche Funktionen kommen relativ häufig vor und können mit Hilfe so 
genannter Lambda-Funktionen in einer einzigen Zeile deklariert werden:

.. code-block:: python
   :linenos:
   
   >>> quadrat = lambda x: x**2
   >>> quadrat(3)
   9

Der Variablenname auf der linken Seite in Zeile 1 fungiert im Weiteren als
Funktionsname so wie wir es schon im Abschnitt :ref:`funcarg` kennengelernt
hatten. ``lambda`` ist ein Schlüsselwort [#keywordverweis]_, das die Definition einer 
Lambda-Funktion andeutet. Darauf folgt ein Funktionsargument, hier ``x``, oder
auch mehrere, durch Komma getrennte Argumente und schließlich nach dem Doppelpunkt 
die Funktionsdefinition.

Solche Funktionsdefinitionen sind sehr praktisch, wenn man eine Funktion als
Argument in einem Funktionsaufruf übergeben möchte, aber auf die explizite
Definition der Funktion verzichten will. Die im Abschnitt :ref:`funcarg`
definierte Ableitungsfunktion könnte beispielsweise folgendermaßen aufgerufen
werden:

.. code-block:: python
   :linenos:

   def ableitung(f, x):
       h = 1e-7
       df = (f(x+h)-f(x-h))/(2*h)
       return df

   print(ableitung(lambda x: x**3, 1))

Von Rundungsfehlern abgesehen liefert dies das korrekte Ergebnis ``3``. In
diesem Fall musste man sich nicht einmal Gedanken darüber machen, wie man die
Funktion benennen will.

.. _funckeywords:

===============================
Schlüsselworte und Defaultwerte
===============================

Bis jetzt sind wir davon ausgegangen, dass die Zahl der Argumente in der
Funktionsdefinition und im Funktionsaufruf übereinstimmen und die Argumente
auch die gleiche Reihenfolge haben. Dies ist nicht immer praktisch. Man kann
sich vorstellen, dass die Zahl der Argumente nicht im Vorhinein feststeht. Es
sind auch optionale Argumente denkbar, die, sofern sie nicht explizit im Aufruf
angegeben werden, auf einen bestimmten Wert, den so genannten Defaultwert,
gesetzt werden. Schließlich ist es vor allem bei längeren Argumentlisten 
praktisch, wenn die Reihenfolge der Argumente nicht zwingend vorgeschrieben ist.

Wir wollen uns zunächst die Verwendung von Schlüsselworten und Defaultwerten
ansehen und ziehen hierzu wiederum die bereits bekannte Funktion zur numerischen
Auswertung von Ableitungen mathematischer Funktionen heran:

.. code-block:: python

   def ableitung(f, x):
       h = 1e-7
       df = (f(x+h)-f(x-h))/(2*h)
       return df

Zu Beginn des Abschnitts :ref:`lokalglobal` hatten wir erklärt, dass die
Variablen im Funktionsaufruf nicht genauso benannt werden müssen wie in der
Funktionsdefinition, und es somit auf die Reihenfolge der Argumente ankommt.
Kennt man die in der Funktionsdefinition verwendeten Variablennamen, so kann
man diese auch als Schlüsselworte verwenden. In diesem Fall kommt es dann nicht
mehr auf die Reihenfolge an. Statt

.. code-block:: python

   print(ableitung(lambda x: x**3, 1))

könnte man auch den Aufruf

.. code-block:: python

   print(ableitung(f=lambda x: x**3, x=1))

oder 

.. code-block:: python

   print(ableitung(x=1, f=lambda x: x**3))

verwenden, wobei das Schlüsselwort ``x`` nichts mit dem in der Definition der
Lambda-Funktion auftretenden ``x`` zu tun hat. Dass es wichtig ist,
verschiedene Bezeichner zu unterscheiden, macht auch die folgende Erweiterung
dieses Aufrufs deutlich.
 
.. code-block:: python

   x = 1
   print(ableitung(x=x, f=lambda x: x**3))

Hier ist im ersten Argument zwischen dem Schlüsselwort ``x``, also dem ersten
``x`` im ersten Argument, und der Variable ``x``, dem zweiten ``x`` im ersten
Argument, zu unterscheiden. Nachdem der Variable ``x`` zuvor der Wert ``1``
zugewiesen wurde, wird also im ersten Argument der Funktion :func:`ableitung`
der Wert ``1`` für die lokale Variable ``x`` übergeben. Die Variable ``x`` in
der Lambdafunktion wiederum hat weder mit dem einen noch mit dem anderen ``x``
im ersten Argument etwas zu tun.

Hat man eine längere Argumentliste und übergibt man manche Argumente ohne und
andere Argumente mit Schlüsselwort, so müssen die Argumente ohne Schlüsselwort
zwingend vor den Argumenten mit Schlüsselwort stehen. Die Argumente ohne
Schlüsselwort werden dann nach ihrer Reihenfolge beginnend mit dem ersten
Argument zugeordnet, die anderen Argumente werden gemäß dem verwendeten
Schlüsselwort übergeben.

Wenn wir dem Benutzer in unserer Ableitungsfunktion die Möglichkeit geben wollen,
die Schrittweite bei Bedarf anzupassen, dies aber nicht unbedingt verlangen wollen,
können wir einen Defaultwert vorgeben. Dies könnte folgendermaßen aussehen:

.. code-block:: python

   def ableitung(f, x, h=1e-7):
       df = (f(x+h)-f(x-h))/(2*h)
       return df

Der Aufruf

.. code-block:: python

   print(ableitung(lambda x: x**3, 1, 1e-3))

würde die Ableitung der dritten Potenz an der Stelle ``1`` auswerten, wobei die
Schrittweite gleich ``0.001`` gewählt ist. Mit dem Aufruf

.. code-block:: python

   print(ableitung(lambda x: x**3, 1))

wird dagegen der Defaultwert für ``h`` aus der Funktionsdefinition, also
10\ :sup:`-7`\ , verwendet. Nach dem
was wir weiter oben gesagt haben, würden die Argumente des Aufrufs

.. code-block:: python

   print(ableitung(lambda x: x**3, h=1e-3, x=1))

folgendermaßen interpretiert werden: Das erste Argument trägt keinen
Variablennamen und wird demnach der ersten Variablen, also ``f``, in der
Funktionsdefinition zugeordnet. Anschließend kommen mit Schlüsselworten
versehene Argumente, bei denen es jetzt nicht mehr auf die Reihenfolge ankommt.
Tatsächlich ist die Reihenfolge im angegebenen Aufruf gegenüber der
Funktionsdefinition vertauscht.  Nach dem ersten Argument mit Schüsselwort
müssen alle folgenden Argumente mit einem Schlüsselwort versehen sein, was hier
in der Tat der Fall ist. Andernfalls liegt, wie im folgenden Beispiel, ein
Syntaxfehler vor.

.. code-block:: python

   print(ableitung(lambda x: x**3, h=1e-3, 1))

     File "<stdin>", line 1
   SyntaxError: non-keyword arg after keyword arg


Neben den besprochenen Möglichkeiten kann man in Python auch noch eine nicht durch
die Funktionsdefinition festgelegte Zahl von Variablen übergeben, wobei auch
Schlüsselworte vorkommen können, die nicht in der Variablenliste der Funktionsdefinition
zu finden sind. Auf diese Art der Argumentübergabe werden wir im Kapitel :ref:`dictionaries`
zurückkommen, da wir erst dort den hierzu benötigten Datentyp kennenlernen werden.

.. |weiterfuehrend| image:: images/symbols/weiterfuehrend.*
   :height: 1em
.. |frage| image:: images/symbols/question.*
           :height: 1em

.. [#oaoo] Dies ist das `OAOO-Prinzip <http://c2.com/cgi/wiki?OnceAndOnlyOnce>`_: 
   once and only once.

.. [#keywordverweis] Siehe hierzu Abschnitt :ref:`variablen`.
