.. _oop:

********************************
Objektorientiertes Programmieren
********************************

In diesem Kapitel soll ein, wenn auch knapper, Einblick in das
objektorientierte Programmieren gegeben werden. Dabei spielt das Konzept von
Objekten eine zentrale Rolle, die gewisse Eigenschaften, sogenannte Attribute,
haben, sowie Methoden bereitstellen, um mit dem Objekt zu kommunizieren.  Damit
wird eine Kapselung von Daten erreicht, und es werden definierte Schnittstellen
festgelegt. Attribute und Methoden sind in einer Art Bauplan, der
Klassendefinition, festgelegt. Im Programm wird dann mit Instanzen,
tatsächlichen Realisierungen der abstrakten Definition, gearbeitet.  Ein
weiteres wichtiges Konzept ist die Vererbung, die es erlaubt, verwandte Klassen
voneinander abzuleiten. Damit wird es möglich, dass eine Unterklasse Attribute
und Methoden von einer Basisklasse erbt.

===============================
Klassen, Attribute und Methoden
===============================

Diese abstrakten Bemerkungen werden klarer, wenn wir gleich ein konkretes
Beispiel betrachten. Wir haben eine ganze Reihe an Datentypen kennengelernt,
die von Python zur Verfügung gestellt werden. Echte Brüche waren jedoch nicht
darunter [#fractions]_. Im Folgenden soll nun gezeigt werden, wie ein solcher
Datentyp zur Verfügung gestellt werden kann.  Offenbar besitzt ein Bruch
Attribute, nämlich den Wert des Zählers sowie den des Nenners. Darüber hinaus
gibt es Methoden. Man kann beispielsweise Brüche addieren oder multiplizieren
oder sie in verschiedenen Weisen ausgeben.

Wir definieren uns nun zunächst eine Klasse ``Bruch`` zusammen mit der Konstruktormethode
:func:`__init__`

.. code-block:: python
   :linenos:

   class Bruch:
   
       def __init__(self, zaehler, nenner=1):
           self.zaehler = zaehler
           self.nenner = nenner
    
und wenden diese Klassendefinition sofort an

.. code-block:: python
   :linenos:

   >>> x = Bruch(2, 5)
   >>> print(x.zaehler, x.nenner)
   2 5

Während die Klassendefinition die Attribute ``zaehler`` und ``nenner`` in
abstrakter Weise definiert, wird bei der Zuweisung an die Variable ``x`` eine
Instanz, also eine konkrete Realisierung eines Bruchs erzeugt. Dabei wird die
Konstruktormethode :func:`__init__`, die in der Klassendefinition in den Zeilen
3-5 definiert wird, mit Hilfe des Klassennamens aufgerufen. In unserem Beispiel
handelt es sich um die Anweisung ``Bruch(2, 5)``. Die Variable ``self``, die in
der Konstruktormethode als erstes Argument auftritt, kann man sich als
Platzhalter für die tatsächliche Instanz vorstellen. Man beachte, dass dieses
Argument im Aufruf der Konstruktormethode immer fehlt. Bei der Ausführung der
Konstruktormethode werden in den Zeilen 4 und 5 die Argumente der
Konstruktormethode den Attributen des Objekts zugewiesen. Auf diese Attribute
kann im Hauptprogramm zugegriffen werden, wie die Zeile 2 im zweiten Codeblock
zeigt. Dabei wird der Attributname mit einem Punkt an den Variablenname des
Objekts angehängt.  Schließlich sei noch angemerkt, dass der Defaultwert für
``nenner`` hier dafür sorgt, dass auch bei nur einem Argument im Aufruf der
Konstruktormethode eine sinnvolle Instanz des ``Bruch``-Objekts erzeugt wird.  
Im Folgenden wird angenommen, dass die Konstruktormethode mit strikt positiven
ganzen Zahlen aufgerufen wird.

Nun müssen wir unsere ``Bruch``-Klasse mit etwas Funktionalität ausstatten. Zunächst einmal
wollen wir den Fall vorsehen, dass der Bruch gekürzt werden kann. Außerdem wollen wir den
Bruch ausgeben können, ohne explizit auf seine Attribute zugreifen zu müssen. Dies wird von
dem folgenden Code erledigt

.. code-block:: python
   :linenos:

   class Bruch:
   
       def __init__(self, zaehler, nenner=1):
           self.zaehler = zaehler
           self.nenner = nenner
           self.__reduce()
   
       def __reduce(self):
           a = self.zaehler
           b = self.nenner
           while a!=b and a!=1 and b!=1:
               a, b = min(a, b), abs(a-b)
           if a==b:
               self.zaehler = self.zaehler//a
               self.nenner = self.nenner//a
   
       def __str__(self):
           if self.nenner!=1:
               return "{}/{}".format(self.zaehler, self.nenner)
           else:
               return str(self.zaehler)
   

wie hier zu sehen ist
    
.. code-block:: python

   >>> x = Bruch(21, 15)
   >>> print(x)
   7/5

Zum Kürzen des Bruchs rufen wir in Zeile 6 die Methode :func:`__reduce` auf. Da
es sich um eine in der Klasse ``Bruch`` definierte Methode handelt, muss ein
von einem Punkt gefolgtes ``self`` vorangestellt werden. Sonst würde nach einer
Funktion außerhalb der Klassendefinition gesucht werden.  Die zwei Unterstriche
zu Beginn des Methodennamens machen die Methode zu einer privaten Methode, die
nur zum Aufruf innerhalb der Klasse gedacht ist. Auf entsprechende Weise kann
man auch private Attribute einführen. Wie schon in der Konstruktormethode
:func:`__init__` muss das erste Argument ``self`` sein.  Damit stehen die
Attribute ``zaehler`` und ``nenner`` in der Methode zur Verfügung. In den
Zeilen 9-15 ist der euklidsche Algorithmus zur Bestimmung des größten
gemeinsamen Teilers implementiert, mit dessen Hilfe der Bruch gekürzt werden
kann.

In den Zeilen 17-21 ist eine Methode mit dem speziellen Namen
:func:`__str__` implementiert, die automatisch immer dann aufgerufen wird, wenn
das ``Bruch``-Objekt in einen String umgewandelt werden soll. Dies ist
beispielsweise bei der Ausgabe mit ``print`` der Fall. Solche speziellen
Methodennamen existieren zum Beispiel auch für die Addition, die Multiplikation
und einige andere Operationen mehr.  Wir wollen uns hier auf die
Implementierung der ersten beiden Methoden, der Umwandlung in den ``float``-Typ
sowie zweier Vergleichsmethoden beschränken und erweitern unsere
Klassendefinition in folgender Weise:

.. code-block:: python
   :linenos:

   class Bruch:
   
       def __init__(self, zaehler, nenner=1):
           self.zaehler = zaehler
           self.nenner = nenner
           self.__reduce()
   
       def __reduce(self):
           a = self.zaehler
           b = self.nenner
           while a!=b and a!=1 and b!=1:
               a, b = min(a, b), abs(a-b)
           if a==b:
               self.zaehler = self.zaehler//a
               self.nenner = self.nenner//a
   
       def __str__(self):
           if self.nenner!=1:
               return "{}/{}".format(self.zaehler, self.nenner)
           else:
               return str(self.zaehler)
   
       def __add__(self, other):
           return Bruch(self.zaehler*other.nenner+self.nenner*other.zaehler,
                        self.nenner*other.nenner)
   
       def __mul__(self, other):
           return Bruch(self.zaehler*other.zaehler,
                        self.nenner*other.nenner)
   
       def __float__(self):
           return float(self.zaehler)/self.nenner

       def __lt__(self, other):
           return self.zaehler*other.nenner < other.zaehler*self.nenner

       def __eq__(self, other):
           return self.zaehler==other.zaehler and self.nenner==other.nenner 

Jetzt sind wir in der Lage, echte Brüche zu addieren und zu multiplizieren, sie
in Gleitkommazahlen umzuwandeln und zu vergleichen:

.. code-block:: python

   >>> x = Bruch(2, 5)
   >>> y = Bruch(3, 7)
   >>> print(x+y)
   29/35
   >>> print(x*y)
   6/35
   >>> float(y)
   0.428571428571
   >>> x>y
   False
   >>> x = Bruch(20, 15)
   >>> y = Bruch(8, 6)
   >>> x==y
   True

Dieses Beispiel zeigt, dass man in einem Programm durchaus mehrere Instanzen
einer Klasse verwenden kann. Das objektorientierte Programmieren erlaubt es,
mit diesen Instanzen zu arbeiten, ohne sich um deren »Innenleben« kümmern zu
müssen. Zähler und Nenner sind in unserem Beispiel zwar zugänglich, bei der
Addition oder Multiplikation brauchen wir uns um diese jedoch nicht explizit zu
kümmern. Dadurch gewinnt das Programm enorm an Übersichtlichkeit. Dies ist ein
nicht zu unterschätzender Vorteil dieser Programmweise.

Bis jetzt haben wir spezielle Methoden definiert, die mit Operatoren wie zum
Beispiel ``+`` und ``*`` verknüpft sind. Damit wurden diese Operatoren, die
zunächst für andere Datentypen definiert waren, auch für Brüche bereitgestellt.
Man spricht hier vom Überladen von Operatoren.  Wir können aber auch Methoden
definieren, die mit ihrem Namen von außerhalb der Klasse aufgerufen werden. Als
Beispiel definieren wir eine :func:`prettyprint`-Methode, die den Bruch in
mehreren Zeilen mit einem horizontalen Bruchstrich ausgeben soll. Unsere
Klassendefinition nimmt dann die folgende Form an:

.. code-block:: python

   class Bruch:
   
       def __init__(self, zaehler, nenner=1):
           self.zaehler = zaehler
           self.nenner = nenner
           self.__reduce()
   
       def __reduce(self):
           a = self.zaehler
           b = self.nenner
           while a!=b and a!=1 and b!=1:
               a, b = min(a, b), abs(a-b)
           if a==b:
               self.zaehler = self.zaehler//a
               self.nenner = self.nenner//a
   
       def __str__(self):
           if self.nenner!=1:
               return "{}/{}".format(self.zaehler, self.nenner)
           else:
               return str(self.zaehler)
   
       def __add__(self, other):
           return Bruch(self.zaehler*other.nenner+self.nenner*other.zaehler,
                        self.nenner*other.nenner)
   
       def __mul__(self, other):
           return Bruch(self.zaehler*other.zaehler,
                        self.nenner*other.nenner)
   
       def __float__(self):
           return float(self.zaehler)/self.nenner
   
       def __lt__(self, other):
           return self.zaehler*other.nenner < other.zaehler*self.nenner

       def __eq__(self, other):
           return self.zaehler==other.zaehler and self.nenner==other.nenner 
   
       def prettyprint(self):
           zaehler_str = str(self.zaehler)
           nenner_str = str(self.nenner)
           feldbreite = max(len(zaehler_str), len(nenner_str))
           bruchstrich = "-"*feldbreite
           print "{}\n{}\n{}".format(zaehler_str.center(feldbreite), 
                                     bruchstrich, 
                                     nenner_str.center(feldbreite))

Nun können wir die :func:`prettyprint`-Methode anwenden:

.. code-block:: python

   >>> x = Bruch(213, 53)
   >>> y = Bruch(7, 3091)
   >>> z = x*y
   >>> z.prettyprint()
    1491 
   ------
   163823
   >>> (x+y).prettyprint()
   658754
   ------
   163823

Wie beim Aufruf der :func:`__reduce`-Methode in der Konstruktormethode der
``Bruch``-Klasse wird der Methodenname mit einem Punkt an das Objekt angehängt.
Letzteres kann durch eine Variable, hier ``z``, spezifiziert sein oder durch
einen Ausdruck, hier ``x+y``. Im Allgemeinen können beim Aufruf einer Methode
natürlich auch Argumente übergeben werden.

Nun wird klar, dass wir auch in früheren Kapiteln immer wieder Methoden
aufgerufen haben ohne uns dessen wirklich bewusst gewesen zu sein. Wenn wir
bespielsweise im Kapitel über :ref:`einausgabe` die Anweisung ``datei.write(…)``
verwendet haben, so hatten wir ein Dateiobjekt ``datei`` benutzt und dessen
``write``-Methode aufgerufen.

|weiterfuehrend| Zum Abschluss dieses Unterkapitels soll noch auf zwei Aspekte
im Zusammenhang mit dem hier entwickelten Beispiel eingegangen werden. Vor allem
wenn man eine Klasse programmiert, um sie anderen Nutzern zur Verfügung zu stellen,
ist die Dokumentation der Methoden wichtig, mit deren Hilfe der Nutzer mit den
Objekten arbeiten kann. Wie schon im Kapitel :ref:`funcdoc` für Funktionen
besprochen, kann auch bei Methoden in einer Klassendefinition ein Dokumentationstext
direkt nach der mit ``def`` beginnenden Zeile eingebaut werden. Die Methode ``prettyprint``
könnte dann folgendermaßen aussehen:

.. code-block:: python

       def prettyprint(self):
           """Gibt den Bruch dreizeilig aus, wobei Zähler und Nenner
           zentriert gesetzt sind.

           """
           zaehler_str = str(self.zaehler)
           nenner_str = str(self.nenner)
           feldbreite = max(len(zaehler_str), len(nenner_str))
           bruchstrich = "-"*feldbreite
           print "{}\n{}\n{}".format(zaehler_str.center(feldbreite), 
                                     bruchstrich, 
                                     nenner_str.center(feldbreite))

In der Python-Shell kann man Information über alle Methoden in folgender Weise bekommen:

.. code-block:: python

   >>> help(Bruch)

   Help on class Bruch in module __main__:

   class Bruch
   |  Methods defined here:
   |  
   |  __add__(self, other)
   |  
   |  __eq__(self, other)
   |  
   |  __float__(self)
   |  
   |  __init__(self, zaehler, nenner=1)
   |  
   |  __lt__(self, other)
   |  
   |  __mul__(self, other)
   |  
   |  __str__(self)
   |  
   |  prettyprint(self)
   |      Gibt den Bruch dreizeilig aus, wobei Zähler und Nenner
   |      zentriert gesetzt sind.
  […]

   >>> help(Bruch.prettyprint)

   Help on method prettyprint in module __main__:

   prettyprint(self)
       Gibt den Bruch dreizeilig aus, wobei Zähler und Nenner
       zentriert gesetzt sind.

Man kann also Informationen über alle Methoden oder aber über eine spezifische Methode
erhalten, wie wir das schon in den Kapiteln :ref:`mathfunc` und :ref:`ode` kennengelernt
haben. Hier sehen wir zudem, dass Python sich bemüht, hilfreiche Informationen über die
Methoden zur Verfügung zu stellen, selbst wenn keine expliziten Dokumentationstexte
vorhanden sind. Dies ist jedoch keinesfalls eine Entschuldigung dafür, auf eine
Dokumentation von Seiten des Programmierers zu verzichten!

|weiterfuehrend| Ein Manko unserer bisherigen Version der ``Bruch``-Klasse besteht
darin, dass stillschweigend vorausgesetzt wird, dass Zähler und Nenner als Integers
übergeben werden müssen. Dies ist unnötig restriktiv. Es würde ausreichen, wenn
die entsprechenden Werte in Integers umwandelbar sind. Die ``__init__()``-Methode
könnte zum Beispiel wie folgt erweitert werden:

.. code-block:: python
   :linenos:

   def __init__(self, zaehler, nenner=1):
       try:
           self.zaehler = int(zaehler)
           self.nenner = int(nenner)
       except ValueError:
           raise ValueError("Die Bruchklasse erwartet ganzzahlige Zähler und Nenner.")
       self.__reduce()

In den Zeilen 3 und 4 wird versucht, die Werte der Variablen ``zaehler`` und
``nenner`` in Integers umzuwandeln. Da dies durchaus misslingen kann, wie wir
gleich noch sehen werden, wird hier die ``ValueError``-Ausnahme abgefangen. Um
dem aufrufenden Programm den Fehler mitzuteilen, wird in Zeile 6 diese Ausnahme
gleich wieder geworfen. Dies bietet die Gelegenheit, eine aussagekräftige
Fehlermeldung mitzuliefern, und ermöglicht es dem aufrufenden Programmteil, den
Fehler adäquat zu behandeln.

.. code-block:: python
   :linenos:

   >>> x = Bruch("33", "47")
   >>> print(x)
   33/47
   >>> y = Bruch("a", "b")
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "bruch.py", line 10, in __init__
       raise ValueError, "Die Bruchklasse erwartet ganzzahlige Zähler und Nenner."
   ValueError: Die Bruchklasse erwartet ganzzahlige Zähler und Nenner.
   >>> z = Bruch([22, 33], 44)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "bruch.py", line 7, in __init__
       self.zaehler = int(zaehler)
   TypeError: int() argument must be a string or a number, not 'list'

In den Zeilen 1 bis 3 sieht man, dass die neue ``__init__()``-Methode in der Lage ist,
auch Strings korrekt zu verarbeiten, sofern sie sich in Integers umwandeln lassen.
In Zeile 4 ist dies nicht der Fall, und es wird somit eine ``ValueError``-Ausnahme
ausgelöst, die mit einer entsprechenden Fehlermeldung in Zeile 9 versehen ist. 
Wie die Zeilen 10 bis 15 zeigen, kann man allerdings auch eine ``TypeError``-Ausnahme
hervorrufen, die somit in der ``__init__()``-Methode noch adäquat abgefangen werden
müsste.

=========
Vererbung
=========

Bei der Definition von Klassen kann man auf Attribute und Methoden anderer Klassen
zurückgreifen, die dann nicht noch einmal implementiert werden müssen, sondern
vererbt werden. Wir wollen die Vererbung anhand zweier Objekte illustrieren, dem
Massepunkt und dem Rotationskörper. Der Massepunkt besitze seine Position als
Attribut. Als Methoden wollen wir vorsehen, dass der Körper verschoben werden kann
und dass sich seine aktuelle Position ausgeben lässt. Diese Attribute und Methoden
lassen sich für den Schwerpunkt des Rotationskörpers direkt übernehmen. Hinzu
kommt als neues Attribut der Vektor in dessen Richtung die Achse des Rotationskörpers
zeigt. Neben der Methode, die die Richtung der Achse ausgibt, wollen wir eine Methode
implementieren, die die Achse des Körpers dreht, wobei Drehwinkel und Drehachse 
als Argumente übergeben werden.

Wir definieren zunächst eine Klasse für den Massepunkt.

.. code-block:: python

   import numpy as np

   class Massepunkt:
    
       def __init__(self):
           self.pos = np.array([0, 0, 0])

       def verschiebe(self, shift):
           self.pos = self.pos+shift

       def position(self):
           print("Die Masse befindet sich am Ort ({:g}, {:g}, {:g}).".format(*self.pos))

Die Konstruktormethode legt den Massepunkt in den Ursprung. Da wir für die Drehung 
des Rotationskörpers Skalar- und Kreuzprodukt benötigen, verwenden wir die NumPy-Bibliothek
um Vektoren zu definieren. Die :func:`verschiebe`-Methode verschiebt den Massepunkt um den
Vektor ``shift``. Mit der :func:`position`-Methode lässt sich die aktuelle Position des
Massepunkts ausgeben, auf die sich auch mit Hilfe des Attributs ``pos`` zugreifen lässt.
Testen wir zunächst die Funktionalität dieser Klasse:

.. code-block:: python

   >>> m = Massepunkt()
   >>> m.pos
   array([0, 0, 0])
   >>> m.position()
   Die Masse befindet sich am Ort (0, 0, 0).
   >>> m.verschiebe(np.array([2, 9, -3]))
   >>> m.position()
   Die Masse befindet sich am Ort (2, 9, -3).
   >>> m.verschiebe(np.array([1, -5, 0]))
   >>> m.position()
   Die Masse befindet sich am Ort (3, 4, -3).

Von der ``Massepunkt``-Klasse leiten wir nun die ``Rotationskoerper``-Klasse ab und bekommen
so insgesamt den folgenden Code:

.. code-block:: python
   :linenos:

   import numpy as np
   from math import sqrt, sin, cos, pi
   
   class Massepunkt:
       
       def __init__(self):
           self.pos = np.array([0, 0, 0])
   
       def verschiebe(self, shift):
           self.pos = self.pos+shift
   
       def position(self):
           print("Die Masse befindet sich am Ort ({:g}, {:g}, {:g}).".format(*self.pos))
   

   class Rotationskoerper(Massepunkt):
   
       def __init__(self):
           self.achse = np.array([0, 0, 1])
           Massepunkt.__init__(self)
   
       def drehe(self, drehachse, winkel):
           drehachse = drehachse/np.linalg.norm(drehachse)
           winkel = winkel*pi/180
           self.achse = self.achse*cos(winkel) + \
                        drehachse*np.dot(drehachse, self.achse)*(1-cos(winkel)) + \
                        np.cross(drehachse, self.achse)*sin(winkel)
   
       def orientierung(self):
           print("Die Achse des starren Körpers liegt in Richtung "
                 "des Vektors ({:g}, {:g}, {:g}).".format(*self.achse))

In Zeile 16 wird die Basisklasse ``Massepunkt`` als Argument der Klasse ``Rotationskoerper``
angegeben, so dass Attribute und Methoden der Basisklasse geerbt werden können. Im Prinzip ist
es möglich, auch mehrere Basisklassen anzugeben. In der Konstruktormethode der
``Rotationskoerper``-Klasse initialisieren wir zunächst die Achse, die die Orientierung des Körpers
angibt. Um die Position des Körpers zu initialisieren, greifen wir auf die Konstruktormethode der
``Massepunkt``-Klasse zurück. Dies ist sinnvoll, aber keineswegs verpflichtend.

|weiterfuehrend| Um auf die Konstruktormethode der Elternklasse zuzugreifen, könnte man in
Zeile 20 alternativ ``super().__init__()`` verwenden.

In der ``Rotationskoerper``-Klasse definieren wir zwei neue Methoden. Es wäre
durchaus auch möglich, Methoden der ``Massepunkt``-Klasse zu überladen. Wir
wollen dies hier jedoch nicht tun, da wir die Methoden dieser Klasse
unverändert verwenden wollen. Sehen wir uns nun an, ob die
``Rotationskoerper``-Klasse wie gewünscht funktioniert:

.. code-block:: python

   >>> rk = Rotationskoerper()
   >>> rk.position()
   Die Masse befindet sich am Ort (0, 0, 0).
   >>> rk.orientierung()
   Die Achse des starren Körpers liegt in Richtung des Vektors (0, 0, 1).
   >>> rk.verschiebe(np.array([2, 1, 3]))
   >>> rk.position()
   Die Masse befindet sich am Ort (2, 1, 3).
   >>> rk.orientierung()
   Die Achse des starren Körpers liegt in Richtung des Vektors (0, 0, 1).
   >>> rk.drehe(np.array([1, 1, 0]), 45)
   >>> rk.orientierung()
   Die Achse des starren Körpers liegt in Richtung des Vektors (0.5, -0.5, 0.707107).
   >>> rk.drehe(np.array([0, 0, 1]), 45)
   >>> rk.orientierung()
   Die Achse des starren Körpers liegt in Richtung des Vektors (0.707107, -5.55112e-17, 0.707107).

Das ``Rotationskoerper``-Objekt ``rk`` besitzt tatsächlich sowohl die Objektattribute der 
``Massepunkt``-Klasse als auch die der ``Rotationskoerper``-Klasse. Zudem können die Methoden
beider Klassen verwendet werden.

.. |weiterfuehrend| image:: images/symbols/weiterfuehrend.*
           :height: 1em
.. |python3| image:: images/symbols/python3.*
           :height: 1em
.. [#fractions] Python stellt Brüche über das Modul ``fractions`` zur Verfügung. Weitere
    Informationen sind in der Python-Dokumentation unter
    `https://docs.python.org/3/library/fractions.html <https://docs.python.org/3/library/fractions.html>`_
    verfügbar.
