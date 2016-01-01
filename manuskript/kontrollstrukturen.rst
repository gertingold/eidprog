******************
Kontrollstrukturen
******************

Im Kapitel :ref:`vorschau` hatten wir bereits kurz die Möglichkeit
angesprochen, den Ablauf eines Programms zu beeinflussen, sei es dadurch, dass
ein Programmteil in einer Schleife mehrfach ausgeführt wird oder dass ein
Programmteil nur dann ausgeführt wird, wenn eine gewisse Bedingung erfüllt ist.
Wir werden nun solche Kontrollstrukturen genauer betrachten und neben den
bereits angesprochenen ``for``-Schleifen und Konstrukten der Form ``if`` …
``else`` auch ``while``-Schleifen und komplexere Verzweigungen kennenlernen.

.. _forloop:

============
For-Schleife
============

Sollen bestimmte Anweisungen mehrfach ausgeführt werden, wobei die Anzahl der
Wiederholungen zuvor bestimmt werden kann, bietet sich die Verwendung einer
``for``-Schleife an. Gegenüber der expliziten Wiederholung von Befehlen ergeben
sich eine Reihe von Vorteilen. Zunächst einmal spart man sich Tipparbeit und
verbessert erheblich die Lesbarkeit des Programms. Zudem ist eine explizite
Wiederholung nur möglich, wenn die Zahl der Wiederholungen bereits beim
Schreiben des Programms feststeht und nicht erst beim Ausführen des Programms
berechnet wird. Im Kapitel :ref:`vorschau` hatten wir bereits die wesentliche
Struktur einer ``for``-Schleife kennengelernt, die wir hier nochmals an einem
einfachen Beispiel illustrieren wollen.

.. code-block:: python

   for n in range(5):
       print("{:4} {:4}".format(n, n**2))

   0    0
   1    1
   2    4
   3    9
   4   16

Das Schlüsselwort ``for`` kennzeichnet den Beginn einer Schleife. Dann folgt
der Name der Variable, die bei der Abarbeitung der Schleife vorgegebene Werte
annimmt, und im Rahmen der Schleife verwendet werden kann. Im Allgemeinen
können hier auch mehrere Variablennamen vorkommen, wie wir später im Kapitel
:ref:`zusgdatentypen` sehen werden. Die Werte, die die Variable ``n`` in
unserem Beispiel annehmen kann, werden durch die ``range``-Anweisung bestimmt.
Zwar werden die Werte erst bei Bedarf generiert, aber wir können sie uns wie
folgt ansehen:

>>> list(range(5))
[0, 1, 2, 3, 4]

Es wird also eine Liste von aufeinanderfolgenden ganzen Zahlen erzeugt, die
hier fünf Elemente enthält. Zu beachten ist, dass die Liste mit Null beginnt
und nicht mit Eins.  Wir werden uns im Abschnitt :ref:`listen` diesen Datentyp
noch genauer ansehen. Für den Moment genügt jedoch die intuitive Vorstellung
von einer Liste. In der ersten Zeile der ``for``-Schleife, die mit einem
Doppelpunkt enden muss, wird also festgelegt, welchen Wert die
Schleifenvariable bei den aufeinanderfolgenden Schleifendurchläufen jeweils
annimmt.

Der Codeteil, der im Rahmen der Schleife im Allgemeinen mehrfach ausgeführt
wird und im obigen Beispiel nur aus einer Zeile besteht, ist daran zu erkennen,
dass er eingerückt ist. Vergleichen wir zur Verdeutlichung die beiden
Codestücke

.. code-block:: python

  for n in range(2):
      print("Schleifendurchlauf {}".format(n+1))
      print("Das war's.")

und 

.. code-block:: python

  for n in range(2):
      print("Schleifendurchlauf {}".format(n+1))
  print("Das war's.")

so erhalten wir im ersten Fall die Ausgabe ::

  Schleifendurchlauf 1
  Das war's.
  Schleifendurchlauf 2
  Das war's.

während die Ausgabe im zweiten Fall ::

  Schleifendurchlauf 1
  Schleifendurchlauf 2
  Das war's.

lautet. Im ersten Codestück gehört die zweite ``print``-Anweisung also noch zur
Schleife, während dies im zweiten Codestück nicht der Fall ist. Im Prinzip ist
die Zahl der Leerstellen bei Einrückungen unerheblich, sie muss allerdings
innerhalb einer Schleife immer gleich sein. Das :pep:`8` [#pep]_, in dem Konventionen
für das Programmieren in Python festgelegt sind, empfiehlt, um vier Leerzeichen
einzurücken. Dies ist ein guter Kompromiss zwischen kaum sichtbaren
Einrückungen und zu großen Einrückungen, die bei geschachtelten Schleifen
schnell zu Platzproblemen führen. Tabulatorzeichen sind zwar prinzipiell bei
Einrückungen erlaubt. Es muss aber auf jeden Fall vermieden werden, Leerzeichen
und Tabulatorzeichen zu mischen. Am besten verzichtet man ganz auf die
Verwendung von Tabulatorzeichen.

Da die Verwendung der Einrückung als syntaktisches Merkmal ungewöhnlich ist, 
wollen wir kurz zwei Beispiele aus anderen Programmiersprachen besprechen. In
FORTRAN 90 könnte eine Schleife folgendermaßen aussehen:

.. code-block:: fortran

  PROGRAM Quadrat
  DO n = 0, 4
     PRINT '(2I4)', n, n**2
  END DO
  END PROGRAM Quadrat

Hier wurde nur aus Gründen der Lesbarkeit eine Einrückung vorgenommen. Relevant
für das Ende der Schleife ist lediglich das abschließende ``END DO``. Während
man sich hier selbst dazu zwingen muss, gut lesbaren Code zu schreiben, zwingt
Python den Programmierer durch seine Syntax dazu, übersichtlichen Code zu
produzieren.

Auch im folgenden C-Code sind die Einrückungen nur der Lesbarkeit wegen
vorgenommen worden. Der Inhalt der Schleife wird durch die öffnende
geschweifte Klammer in Zeile 6 und die schließende geschweifte Klammer in Zeile
9 definiert. Würde man auf die Klammern verzichten, so wäre nur die der
``for``-Anweisung folgende Zeile, also Zeile 7, Bestandteil der Schleife.

.. code-block:: c
  :linenos:

  #include <stdio.h>
  
  main(){
     int i;
     int quadrat;
     for(i = 0; i < 5; i++){
           quadrat = i*i;
           printf("%4i %4i\n", i, quadrat);
     }
  }

Kehren wir jetzt aber zu Python zurück und nehmen wir an, dass wir uns nur für
gerade Zahlen interessieren und für das kleine Einmaleins nicht den Computer
bemühen müssen. Dann können wir der :func:`range`-Funktion auch einen Startwert
und eine Schrittweite vorgeben::

  for n in range(20, 26, 2):
      print(n, n**2)

Die zugehörige Ausgabe lautet::

  20 400
  22 484
  24 576

Die Schleife wird also nur so lange ausgeführt, wie die Iterationsvariable kleiner
als das zweite Argument ist. Bereits in dem eingangs betrachteten Beispiel war das
Argument der :func:`range`-Funktion nicht in der Liste enthalten. 

Statt mit der :func:`range`-Funktion eine Zahlenfolge zu erzeugen, können wir eine
Liste mit den gewünschten Objekten vorgeben, wie dieses Beispiel ::

  zahlen = [12, 17, 23]
  for n in zahlen:
      print(n, n**2)

mit der Ausgabe ::

  12 144
  17 289
  23 529

zeigt. Listen werden grundsätzlich durch eckige Klammern begrenzt und können auch
Objekte mit verschiedenen Datentypen enthalten, wie wir im Kapitel :ref:`zusgdatentypen`
sehen werden.

In den obigen Beispielen haben wir die Schleifenvariable mit ``n`` bezeichnet.
Im Allgemeinen ist es aber besser, nach Möglichkeit einen aussagekräftigeren
Namen zu verwenden, der sich aus der konkreten Anwendung ergibt. In dem
speziellen Fall, in dem die Schleifenvariable bei der Abarbeitung der Schleife
nicht verwendet wird, kann zur Verdeutlichung dieses Umstands der Unterstrich
``_`` als Variablenname verwendet werden. Hierbei handelt es sich, wie wir aus
dem Kapitel :ref:`variablen` wissen, um einen erlaubten Bezeichner.

>>> for _ in range(3):
...     print("Python ist toll!")
... 
Python ist toll!
Python ist toll!
Python ist toll!

Es sei jedoch ausdrücklich davon abgeraten, einen Unterstrich für Variablen zu
verwenden, die später noch benötigt werden.

Gerade bei der Entwicklung eines Programms kann es vorkommen, dass man eine
Schleife vorbereitet, den Schleifeninhalt noch nicht geschrieben hat, aber
dennoch ein syntaktisch korrektes Programm haben möchte.  Da der
Schleifeninhalt nicht leer sein darf, verwendet man in einem solchen Fall die
Anweisung ``pass``, die sonst keine weiteren Auswirkungen hat. In dem Beispiel

.. code-block:: python

   for n in range(10):
       pass

gibt es also keinen wirklichen Schleifeninhalt. Allerdings muss man sich
darüber im Klaren sein, dass dennoch die Schleife abgearbeitet wird. Dabei
werden in diesem Beispiel der Variablen ``n`` nacheinander die Werte von ``0``
bis ``9`` zugeordnet. Nach Abarbeitung der Schleife hat ``n`` also den Wert
``9``.

Eine typische Form der Anwendung einer ``for``-Schleife ist im folgenden Beispiel
gezeigt.
 
.. code-block:: python
  :linenos:

  from math import sqrt

  summe = 0
  for n in range(100000):
      summe = summe+1/(n+1)**2
  print(sqrt(6*summe))

Konzentrieren wir uns auf die Zeilen 3-5, deren Ziel es ist, eine unendliche
Summe, die π²/6 ergibt, durch Beschränkung auf die ersten 100000 Terme
näherungsweise auszuwerten. Nachdem uns die Form der Zeilen 4 und 5 inzwischen
schon gut vertraut ist, betrachten wir insbesondere die Zeile 3. Hier wird, wie
dies häufig bei Schleifen erforderlich ist, zunächst eine Variable, hier die
Summationsvariable ``summe``, initialisiert. Vergisst man dies, so ist diese
Variable beim ersten Schleifendurchlauf auf der rechten Seite der Zeile 5
undefiniert, was zu einem ``NameError`` führt. Es ist also keineswegs so, dass
Variablen auf magische Weise mit einer Null vorbelegt werden. Bei der
Verwendung von Schleifen muss man also immer auch an die eventuell
erforderliche Initialisierung von Variablen denken, die in der Schleife
verwendet werden.

``for``-Schleifen können auch ineinander geschachtelt werden, wie folgendes
Beispiel zeigt, das die Wahrheitswerttabelle der logischen UND-Verknüpfung
mit Hilfe des ``&``-Operators erzeugt.

.. code-block:: python

   print(" arg1 arg2    arg1 & arg2 ")
   print("--------------------------")
   for arg1 in [0, 1]:
       for arg2 in [0, 1]:
           print("   {}    {}          {}"
                 .format(arg1, arg2, arg1 & arg2))

Die zugehörige Ausgabe lautet::

    arg1 arg2    arg1 & arg2 
    --------------------------
      0    0          0
      0    1          0
      1    0          0
      1    1          1

Wie man sieht, wird zunächst durch die äußere Schleife die Variable ``arg1`` auf
den Wert 0 gesetzt. Dann wird die innere Schleife abgearbeitet und ``arg2``
durchläuft die Werte 0 und 1. Anschließend schreitet die äußere Schleife einen
Schritt voran, wobei ``arg1`` auf den Wert 1 gesetzt wird. Dann läuft wiederum
die innere Schleife über die Werte 0 und 1, so dass sich insgesamt vier Ausgabezeilen
ergeben. Hinzu kommen die zu Beginn des Codes definierten zwei Ausgabezeilen, die
den Kopf der Ausgabe bilden. Wichtig ist, dass die Einrückungen entsprechend den
Zugehörigkeiten zu den jeweiligen Schleifen korrekt vorgenommen werden. So ist
die innere Schleife Bestandteil des Codeblocks der äußeren Schleife und daher
eingerückt. Die ``print``-Anweisung gehört zum Codeblock der inneren Schleife und
wurde somit entsprechend weiter eingerückt. Die Einrückung in der letzten Zeile, einer
Fortsetzungszeile, ist dagegen willkürlich und vor allem so gewählt, dass die Lesbarkeit
möglichst gut ist.


==============
While-Schleife
==============

Nicht immer kennt man vorab die Zahl der benötigten Schleifendurchläufe,
sondern möchte die Beendigung einer Schleife von der Nichterfüllung einer
Bedingung abhängig machen. Dann ist eine ``while``-Schleife das Mittel der
Wahl. 

Als Beispiel betrachten wir eine physikalische Problemstellung. Beim schiefen
Wurf beginne eine Punktmasse ihre Bahn am Ort ``x=0``, ``y=0`` mit der
Anfangsgeschwindigkeit (``vx0``, ``vy0``). Die Bahn soll für Zeiten in Schritten
von ``dt`` so lange bestimmt werden wie die y-Koordinate nicht negativ ist. In
der Praxis wäre die Problemstellung wahrscheinlich so kompliziert, dass man die
newtonsche Bewegungsgleichung numerisch lösen müsste. In dem vorliegenden Fall 
kennen wir die Lösung analytisch und können sie im Programm verwenden. 

Die Berechnung der Bahnkurve könnte durch folgendes Programm geschehen:

.. code-block:: python
  :linenos:

  t = 0      # Startzeit
  dt = 0.01  # Zeitschritt
  g = 9.81   # Erdbeschleunigung in m/s²
  x0 = 0     # horizontale Ausgangsposition in m
  y0 = 0     # Anfangshöhe in m
  vx0 = 2    # Anfangsgeschwindigkeit in x-Richtung in m/s
  vy0 = 1    # Anfangsgeschwindigkeit in y-Richtung in m/s
  
  x = x0
  y = y0
  print(" t      x      y")
  print("----------------------")
  while y >= 0:
      print("{:4.2f}   {:4.2f}   {:8.6f}".format(t, x, y))
      t = t + dt
      x = x0 + vx0*t
      y = y0 + vy0*t - 0.5*g*t**2

In den Zeilen 1-7 wird zunächst eine Reihe von Parametern festgelegt. Hierzu
gehören die Größen, die auch in einer physikalischen Problemstellung benötigt
werden, nämlich Ort (``x0``, ``y0``) und Geschwindigkeit (``vx0``, ``vy0``) zum
Anfangszeitpunkt. Außerdem benötigen wir den Wert der Erdbeschleunigung ``g``.
Der Anfangszeitpunkt bestimmt den anfänglichen Wert der Zeitvariable ``t``. 

Da uns das Programm die Bahn nicht für eine kontinuierlich verlaufende Zeit 
liefern kann, müssen wir eine diskrete Zeit einführen. Hierfür legen wir den
Abstand ``dt`` zwischen aufeinanderfolgenden Zeitpunkten fest.

In den Zeilen 9 und 10 wird der Ort zur Anfangszeit mit den Anfangsbedingungen
belegt. Damit ist auch beim ersten Test der ``while``-Bedingung die Variable ``y``
definiert. Zudem benötigen wir diese Werte für die Ausgabe in Zeile 14.
Die ``print``-Anweisungen in den Zeilen 11 und 12 dienen dazu, die Ausgabe
selbsterklärend zu machen. 

Der uns hier eigentlich interessierende Programmteil beginnt in Zeile 13 mit
der ``while``-Anweisung. Da wir uns mit der Berechnung der Wurfparabel für 
nicht negative Höhen begnügen wollen, lautet die zu erfüllende Bedingung 
``y>=0``. In Zeile 14 wird der aktuelle Bahnpunkt, für den ja überprüft wurde,
dass der Wert der Variable ``y`` nicht negativ ist, ausgegeben. In Zeile 15
wird die Zeit um den vorgegebenen Zeitschritt erhöht und in den Zeilen 16 und
17 der zugehörige Bahnpunkt bestimmt.

|frage| Wie würde sich die Ausgabe verändern, wenn man die Zeilen 14 und 15 hinter
die Zeile 17 verschiebt, also zunächst den Bahnpunkt berechnet und ausgibt und
anschließend die Zeit inkrementiert?

In den Zeilen 1-7 fällt noch auf, dass nach den Anweisungen ein „Gartenzaun“
(#) und eine Erläuterung folgt. In Python wird das Zeichen # als
Kommentarzeichen interpretiert, so dass der gesamte Text nach diesem Zeichen
ignoriert wird. Welches Zeichen als Kommentarzeichen dient, hängt von der
Programmiersprache ab. In C++ beispielsweise wird diese Funktion von zwei
Zeichen, nämlich //, übernommen.  Kommentare sind eine Möglichkeit um
sicherzustellen, dass die Funktionsweise eines Programms auch nach längerer
Zeit leicht verstanden werden kann. :pep:`8` gibt Hinweise zur Verwendung und
Formatierung von Kommentaren. Es lohnt sich, einen Blick hineinzuwerfen, auch
wenn man nicht alle Regeln immer zwingend befolgen muss. [#hobgoblin]_ Zum
Beispiel sind unsere Kommentare auf deutsch geschrieben, was natürlich nur
sinnvoll ist, wenn alle potentiellen Leser des Programms die deutsche Sprache
beherrschen. Auch die Verwendung von Umlauten ist nicht immer empfehlenswert.
In jedem Fall sollte aber der folgende Hinweis aus dem :pep:`8` beherzigt werden:

  “Comments that contradict the code are worse than no comments.  Always make
  a priority of keeping the comments up-to-date when the code changes!”

Andernfalls besteht die Gefahr, den Leser des Kommentars, also unter Umständen
sich selbst, auf eine falsche Fährte zu setzen.

Als Anmerkung sei noch erwähnt, dass andere Sprachen eventuell ein 
``do...while``-Konstrukt (z.B. C) oder ein ``repeat...until``-Konstrukt
(z.B. Pascal) zur Verfügung stellen. Dort erfolgt der Abbruchtest nicht zu
Beginn, sondern am Ende. Daher wird der Code auf jeden Fall einmal durchlaufen.

Ein Beispiel hierfür könnte in C folgendermaßen aussehen:

.. code-block:: c
  :linenos:

  #include <stdio.h>

  main(){
     int i=-1;
     do {printf("%4i %4i\n", i, i*i);
         i = i-1;
     } while (i>0);
  }

In Zeile 4 wird die Variable ``i`` mit ``-1`` initialisiert. Da der Test auf Positivität
von ``i`` erst am Ende der Schleife erfolgt, wird die Schleife einmal durchlaufen und
somit eine Zeile mit dem Inhalt ``-1  1`` ausgegeben. In Pascal würde man das Gleiche
mit diesem Code erhalten:

.. code-block:: pascal

  program Quadrat;
  var
    i: integer;
  begin
    i := -1;

    repeat
      writeln(i, '   ', i*i);
      i := i-1;
    until i <= 0;

  end.

Abschließend sei betont, dass der Programmierer bei der Verwendung von 
``while``-Schleifen und ähnlichen Konstrukten selbst dafür verantwortlich
ist sicherzustellen, dass die Schleife irgendwann beendet wird. 
Andernfalls liegt eine Endlosschleife vor und das Programm muss von außen
abgebrochen werden. Dieses Szenario kann allerdings gezielt bei Programmen
eingesetzt werden, die durch äußere Ereignisse wie Tastendrucke oder Mausbewegungen
gesteuert werden. In diesem Fall durchläuft das Programm eine Endlosschleife,
um bei Bedarf auf äußere Ereignisse adäquat zu reagieren. Aber auch in diesem
Fall ist darauf zu achten, dass es eine Möglichkeit gibt, das Programm kontrolliert,
beispielsweise durch Drücken der Taste ``q``, zu beenden. Im Python-Code verwendet
man dann den ``break``-Befehl, um die Ausführung des Programmcodes außerhalb der
Schleife fortzusetzen.

.. _ifelse:

=============
Verzweigungen
=============

Eine andere Art von Kontrollstrukturen, bei denen es nicht um die mehrfache
Ausführung von Code geht, sind Verzweigungen. Dabei wird ein Code nur dann
ausgeführt, wenn eine vorgegebene Bedingung erfüllt ist. Im einfachsten Fall
geschieht dies mit der ``if``-Anweisung wie folgendes Beispiel zeigt:

>>> x = 5
>>> if x != 0:
...     print("Der Kehrwert von {} ist {}.".format(x, 1./x))
...
Der Kehrwert von 5 ist 0.2.
>>> x = 0
>>> if x != 0:
...     print("Der Kehrwert von {} ist {}.".format(x, 1./x))
...

Im ersten Fall wird der Code des ``if``-Blocks ausgeführt, im zweiten Fall
dagegen nicht. Wie schon bei den ``for``- und ``while``-Konstrukten ist der
Umfang des Codeblocks, der nur bedingt ausgeführt wird, durch die Einrückung
bestimmt, kann also auch mehr als eine Zeile umfassen. Ist der Code nur eine 
Zeile lang, darf er auch direkt hinter der ``if``-Anweisung stehen.

>>> x = -5
>>> if x < 0: x = -x
...
>>> print("Diese Zahl ist bestimmt nicht negativ:", x)
Diese Zahl ist bestimmt nicht negativ: 5

Die ``print``-Anweisung wird in diesem Fall immer ausgeführt.

In diesen Beispielen ist die Bedeutung der verwendeten Bedingung ziemlich 
offensichtlich. Gelegentlich können aber auch kompliziertere Bedingungen 
auftreten, deren Bedeutung sich nicht ohne Weiteres erschließt. Dann kann es
sinnvoll sein, eine Variable für den entsprechenden Wahrheitswert nach
folgendem Muster einzuführen:

.. code-block:: python
   :linenos:

   x = -5
   zahl_ist_negativ = x<0
   if zahl_ist_negativ:
       x = -x

In Zeile 2 dokumentiert die Bezeichnung der Wahrheitswertvariable die Bedeutung
des logischen Ausdrucks auf der rechten Seite.

Häufig möchte man abhängig von einer Bedingung eine von zwei Alternativen
ausführen lassen. Hierfür verwendet man das ``if`` … ``else`` …-Konstrukt:

>>> x = 0
>>> if x != 0:
...     print("Der Kehrwert von {} ist {}.".format(x, 1/x))
... else:
...     print("Ich weiß nicht wie man durch Null dividiert.")
...
Ich weiß nicht wie man durch Null dividiert.

Verzweigungen lassen sich auch schachteln. 

.. code-block:: python
  :linenos:

  if x < 0:
      print("x ist negativ.")
  else:
      if x == 0:
          print("x ist gleich Null.")
      else:
          print("x ist positiv.")

Wie die Einrückung zeigt, stellen die Zeilen 4-7 den Codeblock der ersten
``else``-Anweisung dar. Da solche Konstruktionen häufig vorkommen, stellt
Python hier eine ``elif``-Anweisung zur Verfügung, mit der sich der Code
folgendermaßen schreiben lässt:

.. code-block:: python
  :linenos:

   if x < 0:
       print("x ist negativ.")
   elif x == 0:
       print("x ist gleich Null.")
   else:
       print("x ist positiv.")

Um die Programmlaufzeit zu optimieren, sollten die Abfragen so formuliert
werden, dass in der Mehrheit der Fälle bereits die erste Bedingung erfüllt 
ist. Muss man davon ausgehen, dass die Variable ``x`` in den meisten Fällen
positiv ist, so wäre es sinnvoll, den obigen Code umzuformulieren.

Man kann sich durchaus mehrere Schachtelungsebenen vorstellen, die mit
entsprechend vielen ``elif``-Anweisungen realisiert werden. Einige
Programmiersprachen stellen hierfür eine so genannte ``case``-Anweisung zur
Verfügung. In Python gibt es eine solche Anweisung allerdings nicht.  Mit Hilfe
des Datentyps ``dictionary``, den wir im Abschnitt :ref:`dictionaries` noch
kennenlernen werden, lässt sich aber ein effizienter Ersatz schaffen, der eine
lange Hierarchie von Abfragen vermeidet.

In Verzweigungen wie im obigen Beispiel, vor allem aber, wenn man mehrere
``elif``-Blöcke vorliegen hat, sollte man beachten, dass nach der Abarbeitung
eines Blockes an das Ende der gesamten ``if``-Konstruktion gesprungen wird.
Dies gilt auch dann, wenn eine später folgende Bedingung erfüllt ist, wie das
folgende Beispiel illustriert.

.. code-block:: python

   x = 2
   if x < 0:
       print("x ist negativ.")
   elif x == 2:
       print("x ist gleich 2.")
   elif x > 0:
       print("x ist größer als Null.")

Hier ist die zweite Bedingung erfüllt, so dass der Text »\ ``x ist gleich 2.``\ «
ausgegeben wird. Im weiteren Programmablauf wird die dritte Bedingung in diesem Fall
überhaupt nicht ausgewertet.
  

.. _tryexcept:

======================
Abfangen von Ausnahmen
======================

In einem der Beispiele des vorigen Abschnitts haben wir sichergestellt, dass
die Variable ungleich Null ist, bevor wir den Kehrwert gebildet haben [#lbyl]_.
In Python verwendet man gerne eine Alternative, die davon ausgeht, dass es
leichter ist, um Verzeihung zu bitten also um Erlaubnis [#eafp]_.  Im Abschnitt
:ref:`float` hatten wir bereits gesehen, dass bei einer Division durch Null
eine ``ZeroDivisionError``-Ausnahme (engl. *Exception*) geworfen wird. Diese
Ausnahme kann folgendermaßen abgefangen werden:

.. code-block:: python
  :linenos:

  from math import sin
  x = 0
  try:
      y = sin(x)/x
  except ZeroDivisionError:
      y = 1.
  print(y)

Als Ausgabe ergibt sich ``1.0``. Zunächst wird versucht, den Codeblock nach der
``try``-Anweisung, also hier den Code in Zeile 4, auszuführen. Wird dabei eine
``ZeroDivisionError``-Ausnahme geworfen, so wird der Programmablauf im
Codeblock der ``except``-Anweisung, also in Zeile 6, fortgesetzt. Dies gilt
jedoch nur für die in der ``except``-Anweisung angegebene(n) Ausnahme(n).  Wäre
z.B. die Variable ``x`` vom Typ *String*, so würde das Programm mit einer
``TypeError``-Ausnahme abbrechen. Gibt man nach der ``except``-Anweisung keine
Ausnahme(n) an, so wird der Programmablauf beim Auftreten einer Ausnahme
unabhängig von deren Typ in Zeile 6 fortgesetzt. Auch wenn ein solches Vorgehen
zunächst als sehr bequem erscheint, ist es aus mehreren Gründen nicht ratsam.
Zum einen würde die Behandlung beispielsweise einer ``TypeError``-Ausnahme
durch den Code in Zeile 6 nicht korrekt sein und somit sehr wahrscheinlich zu
einem fehlerhaften Ergebnis führen. Zum anderen tritt der fehlerhafte Typ der
Variable ``x``, der seinen Ursprung wohl in einem Programmierfehler hat, nicht
mehr in Erscheinung, so dass der Programmierfehler möglicherweise unentdeckt 
bliebe.

|weiterfuehrend| Das ``try…except…``-Konstrukt erlaubt auch noch einen
``finally…``-Block, der unabhängig vom Auftreten einer Ausnahme ausgeführt
wird. Dies ist zum Beispiel wichtig, wenn Dateizugriffe erfolgen und die Datei
am Ende auf jeden Fall geschlossen werden muss.

.. |frage| image:: images/symbols/question.*
           :height: 1em
.. |achtung| image:: images/symbols/attention.*
           :height: 1em
.. |weiterfuehrend| image:: images/symbols/weiterfuehrend.*
           :height: 1em

.. [#pep] PEP steht für »Python Enhancement Proposal«.
.. [#hobgoblin] Siehe hierzu den Abschnitt *A Foolish Consistency is the 
        Hobgoblin of Little Minds* des :pep:`8`. Nebenbemerkung: Dieser Titel
        spielt auf ein `Zitat von Ralph Waldo Emerson <http://en.wikiquote.org/wiki/Ralph_Waldo_Emerson>`_ an.

.. [#lbyl] Diese Strategie wird gelegentlich mit dem Akronym LBYL = “look before
   you leap” belegt.

.. [#eafp] Das Gegenteil zu LBYL ist EAFP = “easier to ask forgiveness than 
   permission”.
