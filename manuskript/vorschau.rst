.. _vorschau:

*************
Eine Vorschau
*************

Um möglichst schnell erste interessante Programme schreiben zu können, beginnen
wir mit einer Vorschau auf einige wenige wichtige Elemente der
Programmiersprache Python. Die dabei auftretenden Fragen werden dann in den
folgenden Kapiteln geklärt. Wir werden vor allem die folgenden Aspekte
ansprechen:

* Umgang mit Variablen
* Ausgabe von Ergebnissen auf dem Bildschirm
* Kontrolle des Programmverlaufs mit Hilfe von Schleifen und Verzweigungen

Da wir nur kurze Codesegmente ausprobieren werden, benutzen wir die Python-
oder IPython-Shell und versuchen zunächst einmal, eine ganz einfache Rechnung
auszuführen.

>>> 1+1
2
>>> 5*7
35

Es wird uns auf Dauer jedoch nicht genügen, Rechnungen mit fest vorgegebenen
Zahlen auszuführen, sondern wir werden auch Variablen benötigen.

>>> x = 3
>>> x**2
9
>>> x = x+1
>>> x
4

Wir können also einer Variable, die hier ``x`` genannt wurde, eine Zahl
zuweisen und anschließend mit dieser Variable Rechnungen ausführen.
Beispielsweise können wir die Zahl quadrieren. Allerdings muss man sich davor
hüten, das Gleichheitszeichen in seiner üblichen mathematischen Bedeutung zu
verstehen, denn dann wäre die Anweisung ``x = x+1`` in der vierten Zeile ein
mathematischer Widerspruch. Python interpretiert das Gleichheitszeichen im
Sinne einer Zuweisung, bei der die rechte Seite ausgewertet und der linken
Seite zugewiesen wird.

Führen wir eine Division aus, so zeigt sich, dass Python nicht nur ganze Zahlen
beherrscht, sondern auch Gleitkommazahlen.

>>> 5/2
2.5

In der Shell wird das Ergebnis einer Anweisung auf dem Bildschirm ausgegeben, sofern
das Ergebnis nicht einer Variable zugewiesen wird. Weiter oben hatten wir schon
gesehen, dass der Inhalt einer Variable ausgegeben werden kann, indem man den
Namen der Variable in der Shell eingibt. Speichert man ein Skript in einer Datei
ab und führt diese aus, so erhält man auf diese Weise jedoch keine Ausgabe. Wir
speichern die folgenden Anweisungen in einer Datei namens ``foo.py`` ab [#foo]_:

.. code-block:: python

  x = 5*8
  x = x+2
  x

Führen wir diese Datei im Python-Interpreter aus, so erhalten wir keine Ausgabe::

  $ python foo.py
  $

In den meisten Fällen möchte man jedoch das Ergebnis eines Programms wissen. Dazu
verwendet man die ``print``-Anweisung. Im einfachsten Fall kann dies folgendermaßen
aussehen:

.. code-block:: python

  x = 5*8
  x = x+2
  print(x)

Speichern wir diese Anweisungen wiederum in der Datei ``foo.py`` ab und führen sie
im Python-Interpreter aus, so erhalten wir eine Ausgabe::

  $ python foo.py
  42
  $

Eine etwas informativere Ausgabe kann man folgendermaßen erhalten. Das Programm
``foo.py``

.. code-block:: python

  x = 5*8
  x = x+2
  print("Das Ergebnis lautet:", x)

führt zu folgender Ausgabe::

  $ python foo.py
  Das Ergebnis lautet: 42
  $

Dabei wurden Anführungszeichen benutzt, um dem Python-Interpreter anzuzeigen,
dass sich dazwischen auszugebender Text befindet. Die Darstellung der Ausgabe
lässt sich sehr viel genauer spezifizieren. Wie das geht, werden wir im Kapitel
:ref:`strings` sehen.

Ein großer Vorteil von Computern liegt unter anderem darin, dass auch vielfache
Wiederholungen der gleichen Aufgabe zuverlässig ausgeführt werden. Dazu kann man
Schleifen verwenden. Betrachten wir ein einfaches Beispiel, das wir in einer Datei
``summe.py`` abspeichern:

.. code-block:: python
   :linenos:

   summe = 0
   for n in range(5):
       print("Schleifendurchgang", n)
       summe = summe+1
   print("Summe =", summe)

Bevor wir dieses Skript genauer ansehen, wollen wir uns davon überzeugen, dass es
vernünftig funktioniert::

  $ python summe.py
  Schleifendurchgang 0
  Schleifendurchgang 1
  Schleifendurchgang 2
  Schleifendurchgang 3
  Schleifendurchgang 4
  Summe = 5
  $

Wie entsteht diese Ausgabe? In Zeile 1 belegen wir zunächst die Variable ``summe``
mit dem Wert ``0``. Später wird dieser Wert beim Durchlaufen der Schleife jeweils
um Eins erhöht. In Zeile 2 beginnt die eigentliche Schleife. Wie der Wert der
``range``-Anweisung angibt, soll die Schleife fünfmal durchlaufen werden. Dabei nimmt
die Variable ``n`` nacheinander die Werte ``0``, ``1``, ``2``, ``3`` und ``4`` an.
Anschließend folgt in den Zeilen 3 und 4 ein eingerückter Bereich. Die Einrückung
gibt den Teil des Codes an, der im Rahmen der Schleife wiederholt ausgeführt wird.
Dabei muss immer gleich weit eingerückt werden. Es empfiehlt sich, immer vier
Leerzeichen zur Einrückung zu verwenden. Beim Schleifendurchlauf wird nun zunächst
angegeben, der wievielte Durchlauf gerade stattfindet. Anschließend wird in Zeile 4
die Variable ``summe`` inkrementiert. In Zeile 5 wurde die Schleife bereits wieder
verlassen und es wird das Ergebnis der fünffachen Inkrementierung ausgegeben.

|frage| Rücken Sie im Skript ``summe.py`` Zeile 5 ebenfalls ein. Überlegen Sie
sich zunächst, welche Ausgabe Sie erwarten, und überprüfen Sie Ihre Überlegung,
indem Sie das Skript anschließend ausführen.

Sehen wir uns noch an, wie die Eingabe der Schleife in der Python-Shell ablaufen
würde:

>>> summe = 0
>>> for n in range(5):
...     print("Schleifendurchgang", n)
...     summe = summe+1
... 
Schleifendurchgang 0
Schleifendurchgang 1
Schleifendurchgang 2
Schleifendurchgang 3
Schleifendurchgang 4
>>> print("Summe", summe)
Summe 5

Nach der Eingabe der zweiten Zeile erkennt der Python-Interpreter, dass gerade
eine Schleife begonnen wurde. Dies wird durch Änderung der Eingabeaufforderung von
``>>>`` nach ``...`` angedeutet. Will man die Schleife beenden, so verzichtet man
auf eine Eingabe und drückt direkt die Eingabetaste.

Bei der Eingabe können verschiedene Dinge schieflaufen. Betrachten wir zwei Beispiele.

>>> summe = 0
>>> for n in range(5) # doctest: +SKIP
      File "<stdin>", line 1
        for n in range(5)
                        ^
    SyntaxError: invalid syntax

Der ``SyntaxError`` weist darauf hin, dass die Eingabe nicht die Form hat, die der
Python-Interpreter erwartet. In diesem Fall fehlt der Doppelpunkt am Ende der Zeile
– ein beliebter Fehler. Kein Problem, man nimmt einfach einen zweiten Anlauf.

>>> for n in range(5): # doctest: +SKIP
... print("Schleifendurchgang", n)
      File "<stdin>", line 2
        print("Schleifendurchgang", n)
            ^
    IndentationError: expected an indented block

Hier wurde der Doppelpunkt eingegeben, aber in der nächsten Zeile fehlt die
Einrückung, worauf die Fehlermeldung ``expected an indented block`` deutlich
hinweist.

Abschließend wollen wir noch Verzweigungen ansprechen, die es erlauben, abhängig
davon, ob eine bestimmte Bedingung erfüllt ist, unterschiedlichen Programmcode
auszuführen. Betrachten wir wieder ein Beispiel:

.. code-block:: python
   :linenos:

   temperatur = 25
   if temperatur < 28:
       print("Ich rechne meine Übungsaufgaben.")
   else:
       print("Ich gehe lieber in's Freibad.")
   print("Das war's.")

Liest man das Programm und übersetzt die einzelnen Befehle ins Deutsche, so hat
man eigentlich schon eine gute Vorstellung davon, was dieses Programm machen
wird. Wenn (»if«) die Temperatur unter 28 Grad ist, rechne ich meine Übungsaufgaben
oder genauer: Das Programm gibt aus, dass ich meine Übungsaufgaben rechnen werde.
Andernfalls (»else«) ist es zu warm, und ich gehe lieber in's Freibad. 

Um zu testen, ob wir den Code richtig interpretiert haben, führen wir das
Programm aus und erhalten die folgende Ausgabe::

   Ich rechne meine Übungsaufgaben.
   Das war's.

Setzt man dagegen die Variable ``temperatur`` auf einen Wert von 28 oder größer,
so lautet die Ausgabe::

   Ich gehe lieber in's Freibad.
   Das war's.

Der wichtige Teil dieses Programm befindet sich in den Zeilen 2 bis 5. Ist die
Bedingung in der Zeile 2 erfüllt, so wird der danach befindliche, eingerückte
Block ausgeführt. Dieser kann durchaus auch mehr als eine Zeile umfassen. Ist
die Bedingung in Zeile 2 dagegen nicht erfüllt, so wird der Block nach der
``else:``-Zeile ausgeführt. Wichtig sind hier, wie schon bei der Schleife, die
Doppelpunkte nach der ``if``-Bedingung und nach ``else`` sowie die Einrückung
der zugehörigen Codeblöcke. Die nicht mehr eingerückte Anweisung in Zeile 6 wird
unabhängig davon ausgeführt, ob die Bedingung in Zeile 2 erfüllt ist oder nicht.

.. |frage| image:: images/symbols/question.*
           :height: 1em

.. [#foo] Der Name ``foo`` wird häufig als Platzhalter in Beispielprogrammen 
   verwendet. Im Normalfall sollten natürlich aussagekräftigere Bezeichnungen
   gewählt werden.
