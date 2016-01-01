.. _einausgabe:

****************
Ein- und Ausgabe
****************

Das Ergebnis der Abarbeitung eines Programms wird in den meisten Fällen die
Ausgabe des Ergebnisses zur Folge haben. In den bisherigen Kapiteln haben wir
die Ausgabe auf dem Bildschirm mit Hilfe der ``print``-Funktion kennengelernt.
Insbesondere bei umfangreicheren Ausgaben wird man das Ergebnis in eine Datei
schreiben wollen, um es zu speichern oder später weiter zu verarbeiten,
beispielsweise mittels eines Grafikprogramms. Häufig ist es auch notwendig, dem
Programm Parameter zu übergeben, entweder beim Programmaufruf über Argumente
auf der Kommandozeile, auf Anfrage des Programms über die Tastatur oder durch
Einlesen aus einer Datei. Im Folgenden werden wir uns zunächst die Eingabe über
die Kommandozeile und die Tastatur ansehen und uns anschließend mit der Ein-
und Ausgabe von Daten mit Hilfe von Dateien beschäftigen.

===============================================
Eingabe über die Kommandozeile und die Tastatur
===============================================

Ein Python-Programm, nennen wir es ``foo.py`` [#foo]_, lässt sich von der Kommandozeile
mit Hilfe des Aufrufs 

   ``python3 foo.py`` 
   
starten. An diesen Aufruf kann man jedoch auch weitere Argumente anhängen, die
innerhalb des Programms verfügbar sind.  Ein solcher Aufruf könnte
beispielsweise lauten

   ``python3 foo.py Hallo 3``

Es könnte sich dabei um den Aufruf eines Programms handeln, das den angegebenen
String so oft ausgibt wie es durch das letzte Argument des Aufrufs vorgegeben
ist.  Der Zugriff auf die Argumente erfolgt dabei über die ``argv``-Variable
des ``sys``-Moduls, wobei ``argv`` für »argument vector« steht. Eine
Realisierung des Programms könnte also folgendermaßen aussehen:

.. code-block:: python
   :linenos:

   import sys

   print(sys.argv)
   for n in range(int(sys.argv[2])):
       print(sys.argv[1])

Dieser Code ergibt die folgende Ausgabe

.. code-block:: python

   ['foo.py', 'Hallo', '3']
   Hallo
   Hallo
   Hallo

Aus der ersten Zeile der Ausgabe wird deutlich, dass die Variable ``sys.argv``
die Kommandozeilenargumente in Form einer Liste enthält. Dabei gibt das erste
Element den Namen des aufgerufenen Programms an. Dies ist unter anderem dann
von Interesse, wenn man das Programm unter verschiedenen Namen aufrufen kann
und dabei ein unterschiedliches Verhalten erreichen möchte. Des Weiteren zeigt
die erste Zeile der Ausgabe, dass alle Argumente in der Liste ``sys.argv`` als
Strings auftreten. Daher musste das letzte Argument des Programmaufrufs in
Zeile 4 des Programmcodes erst mit Hilfe der :func:`int`-Funktion in einen
Integer umgewandelt werden.

Will man für ein Programm eine flexible oder umfangreiche Übergabe von Optionen
auf der Kommandozeile vorsehen, so lohnt sich ein Blick auf das
``argparse``-Modul [#argparse]_. Dieses stellt einige nützliche
Funktionalitäten zur Verfügung, unter anderem auch die automatisierte
Erstellung einer Hilfeausgabe.

Eingaben können auch während des Programmablaufs erfolgen. Dies geschieht mit
Hilfe der :func:`input`-Funktion, die in dem folgenden Beispiel illustriert
wird.

.. code-block:: python
   :linenos:

   while 1:
       try:
           x = input("Aufgabe: ")
           print(eval(x))
       except SyntaxError:
           break

Uns kommt es zunächst auf die Zeile 3 an. Die :func:`input`-Funktion gibt das
Stringargument aus und gibt die Eingabe als String, hier an die Variable ``x``,
zurück. Diese Funktionalität wird in dem Beispiel verwendet, um vom Benutzer
eingegebene Rechenaufgaben zu lösen. Hierzu wird mit der Zeile 1 eine
Dauerschleife eingeleitet, in der in Zeile 3 versucht wird, eine Aufgabe
einzulesen. In Zeile 4 wird die :func:`eval`-Funktion verwendet, um den String
als Anweisung zu interpretieren und auszuführen. Tritt dabei ein
``SyntaxError`` auf, so wird die Dauerschleife in den Zeilen 5 und 6 beendet.

Die Eingabe kann aber auch einfach in einem Tupel bestehen, dessen Bestandteile
an mehrere Variablen übergeben werden:

.. code-block:: python

   x = y = 1
   while x*y:
       x, y = eval(input("Multiplikanden: "))
       print("Produkt = {}".format(x*y))

Dabei muss die Eingabe das erforderliche Komma enthalten:

.. code-block:: python

   Multiplikanden: 4, 5
   Produkt = 20
   Multiplikanden: 3, 0
   Produkt = 0

In diesem Beispiel wird die Schleife beendet, sobald das Produkt gleich Null ist, was
dem Wahrheitswert ``False`` entspricht. In einem anderen Beispiel wird eine Liste 
eingegeben, die in einer Schleife abgearbeitet wird.

.. code-block:: python

   zahlen = eval(input("Geben Sie eine Liste ein: "))
   for n in zahlen:
           print("{:6}\t{:10}".format(n, n**2))

Die Eingabe einer Liste gibt die Listenelemente und die zugehörigen Quadrate aus:

.. code-block:: python

   Geben Sie eine Liste ein: [-17, 5, 247]
      -17         289
        5          25
      247       61009

===============================
Lesen und Schreiben von Dateien
===============================

Häufig wird man statt der manuellen Eingabe von Daten und der Ausgabe von
Ergebnissen auf dem Bildschirm das Einlesen aus einer Datei und das Schreiben
in eine Datei vorziehen.  Wir betrachten zunächst den Fall, dass eine Datei
vorliegt, auf deren Inhalt wir in einem Programm zugreifen wollen. Für die
folgenden Beispiele nehmen wir an, dass eine Datei namens ``foo_utf8.dat`` mit
dem Inhalt

.. code-block:: python

   Einführung in das
   Programmieren für
   Physiker und
   Materialwissenschaftler

existiert. Dabei liege diese Datei in der UTF-8-Kodierung vor. Zur Illustration
sei noch eine Datei ``foo_latin1.dat`` vorhanden, die die ISO-8859-1-Kodierung,
auch als Latin-1-Kodierung bekannt, verwendet. Während in der ersten Datei der
Umlaut »ü« hexadezimal durch ``C3BC`` kodiert ist, ist er in der zweiten Datei
hexadezimal als ``FC`` dargestellt.

Bevor Daten aus dieser Datei gelesen werden können, muss die Datei geöffnet werden.
Dies könnte wie in der ersten Zeile gezeigt geschehen:

.. code-block:: python
   :linenos:

   >>> datei = open("foo_utf8.dat")
   >>> datei
   <_io.TextIOWrapper name='foo.dat' encoding='UTF-8'>

Damit haben wir ein Dateiobjekt erhalten, das den Zugriff auf die Datei mit dem
in der ersten Zeile als Argument angegebenen Namen ermöglicht. Falls nichts
anderes beim Öffnen der Datei angegeben wird, ist die Datei lediglich zum Lesen
geöffnet. Die Datei kann also nicht überschrieben werden, und es kann auch
nichts angefügt werden.

Standardmäßig erwartet wird die auf dem jeweiligen System bevorzugte Kodierung.
In unserem Fall ist dies UTF-8.

.. code-block:: python

   >>> import locale
   >>> locale.getpreferredencoding()
   'UTF-8'

Der Versuch, auf eine nicht existierende Datei lesend zuzugreifen, wird mit
einem ``IOError`` beantwortet:

.. code-block:: python

   >>> datei = open("foo.txt")
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IOError: [Errno 2] No such file or directory: 'foo.txt'

Nachdem die Datei geöffnet wurde, gibt es verschiedene Möglichkeiten, auf ihren Inhalt
zuzugreifen. Mit der :func:`read`-Funktion wird, sofern kein Argument eingegeben wurde,
die gesamte Datei in einen String eingelesen:

.. code-block:: python

   >>> datei.read()
   'Einführung in das\nProgrammieren für\nPhysiker und\nMaterialwissenschaftler\n'

Die in dem String auftretenden ``\n`` geben Zeilenumbrüche an [#unicode]_. Die
Datei besteht also aus vier Zeilen. Versucht man auf die gleiche Weise, die
Datei ``foo_latin1.dat`` einzulesen, erhält man einen ``UnicodeDecodeError``
weil die den Umlauten entsprechenden Bytes in dieser Datei nicht im Rahmen der
UTF-8-Kodierung interpretiert werden können.

.. code-block:: python

   >>> datei = open("foo_latin1.dat")
   >>> datei.read()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "/usr/lib/python3.1/codecs.py", line 300, in decode
       (result, consumed) = self._buffer_decode(data, self.errors, final)
   UnicodeDecodeError: 'utf8' codec can't decode byte 0xfc in position 4: invalid start byte

Dagegen funktioniert das Einlesen problemlos, wenn man die richtige Kodierung
angibt.

.. code-block:: python

   >>> datei = open("foo_latin1.dat", encoding="latin1")
   >>> datei.read()
   'Einführung in das\nProgrammieren für\nPhysiker und\nMaterialwissenschaftler\n'

Nach dem Lesen einer gesamten Datei mit der :func:`read`-Funktion steht der
Zeiger, der die aktuelle Position in der Datei angibt, am Dateiende. Ein
weiteres Lesen ergibt daher nur einen leeren String wie Zeile 7 in dem
folgenden Beispiel zeigt.

.. code-block:: python
   :linenos:

   >>> datei = open("foo_utf8.dat")
   >>> datei.read()
   'Einführung in das\nProgrammieren für\nPhysiker und\nMaterialwissenschaftler\n'
   >>> datei.tell()
   75
   >>> datei.read()
   ''

In den Zeilen 4 und 5 haben wir mit Hilfe der :func:`tell`-Methode die
aktuelle Position des Dateizeigers abgefragt. Dabei zählen die Zeilenumbrüche
mit. Man muss allerdings beachten, dass das Resultat der :func:`tell`-Methode
auf der Bytedarstellung beruht und das UTF8-kodierte ``ü`` als zwei Bytes zählt.

Mit Hilfe der :func:`seek`-Funktion kann man gezielt an bestimmte Stellen der
Datei springen, wobei allerdings wieder die Bytedarstellung relevant ist. Es
besteht also potentiell die Gefahr, mitten in einem Mehrbyte-Code zu
landen. Daher ist es sinnvoll, :func:`seek` auf der Basis von Positionen zu
verwenden, die mit :func:`tell` bestimmt wurden.

Eindeutig ist jedoch der Dateianfang, der der Zeigerposition ``0`` entspricht.
Nach einem ``seek(0)`` liest der zweite Aufruf der :func:`read`-Funktion im
folgenden Beispiel nochmals die gesamte Datei ein:

.. code-block:: python
   :linenos:

   >>> datei = open("foo_utf8.dat")
   >>> datei.read()
   'Einführung in das\nProgrammieren für\nPhysiker und\nMaterialwissenschaftler\n'
   >>> datei.seek(0)
   >>> datei.read(10)
   'Einführung'
   >>> datei.read(10)
   ' in das\nPr'

Man kann sich die Funktionsweise wie bei einem Magnetband vorstellen, bei dem
die Position des Lesekopfes durch die :func:`tell`-Funktion angegeben wird,
während die :func:`seek`-Funktion den Lesekopf neu positioniert. Im gerade
gezeigten Beispiel wird der Lesekopf an den Anfang, d.h. auf die absolute
Position ``0`` zurückgesetzt. Anschließend werden zweimal je zehn Zeichen
eingelesen.

Nicht immer möchte man die ganze Datei auf einmal einlesen, sei es weil die
Datei sehr groß ist oder weil man den Inhalt zum Beispiel zeilenweise
verarbeiten möchte. Hierzu stellt Python verschiedene Möglichkeiten zur
Verfügung. Mit Hilfe der :func:`readlines`-Funktion lassen sich die einzelnen
Zeile für die weitere Verarbeitung in eine Liste aufnehmen:

.. code-block:: python

   >>> datei = open("foo_utf8.dat")
   >>> inhalt = datei.readlines()
   >>> print(inhalt)
   ['Einführung in das\n', 'Programmieren für\n', 'Physiker und\n',
   'Materialwissenschaftler\n']

Bei der Verarbeitung der einzelnen Zeilen ist zu beachten, dass die
Zeichenketten am Ende noch die Zeilenumbruchkennzeichnung ``\n`` enthalten.

Zeilen lassen sich auch einzeln einlesen.

.. code-block:: python

   >>> datei = open("foo_utf8.dat")
   >>> datei.readline()
   'Einführung in das\n'
   >>> datei.readline()
   'Programmieren für\n'
   >>> datei.readline()
   'Physiker und\n'
   >>> datei.readline()
   'Materialwissenschaftler\n'
   >>> datei.readline()
   ''

Nachdem alle Zeilen eingelesen wurden, steht der Dateizeiger am Dateiende, so
dass bei weiteren Aufrufen der :func:`readline`-Funktion nur ein leerer String
zurückgegeben wird.

Eine elegante Methode, die Zeilen einer Datei in einer Schleife abzuarbeiten,
zeigt das folgende Beispiel.

.. code-block:: python

   >>> datei = open("foo_utf8.dat")
   >>> for zeile in datei:
   ...     print(zeile.upper())
   ... 
   EINFÜHRUNG IN DAS

   PROGRAMMIEREN FÜR

   PHYSIKER UND

   MATERIALWISSENSCHAFTLER

Will man die zusätzlichen Leerzeilen vermeiden, so muss man das ``\n`` am Ende
der Zeilen entfernen, entweder unter Verwendung der :func:`rstrip`-Methode oder
durch Verwendung eines Slices.

.. code-block:: python

   >>> datei = open("foo_utf8.dat")
   >>> for zeile in datei:
   ...     print(zeile.upper().rstrip("\n"))
   ... 
   EINFÜHRUNG IN DAS
   PROGRAMMIEREN FÜR
   PHYSIKER UND
   MATERIALWISSENSCHAFTLER

Die gleiche Ausgabe erhält man mit

.. code-block:: python

   >>> datei = open("foo_utf8.dat")
   >>> for zeile in datei:
   ...     print(zeile[:-1].upper())
   ... 

In allen bisherigen Beispielen haben wir eine Anweisung unterschlagen, die man
am Ende der Arbeit mit einer Datei immer ausführen lassen sollte. Nachdem man
eine Datei zunächst geöffnet hat, sollte man sie am Ende auch wieder schließen.

.. code-block:: python

   >>> datei = open("foo_utf8.dat")
   >>> inhalt = datei.read()
   >>> datei.closed
   False
   >>> datei.close()
   >>> datei.closed
   True

Das Schließen einer Datei gibt die im Zusammenhang mit der geöffneten Datei
benötigten Ressourcen wieder frei und bewahrt einen unter Umständen auch vor
einem teilweisen oder vollständigen Verlust der geschriebenen Daten.

Bevor wir uns mit dem Schreiben von Dateien beschäftigen, müssen wir uns
zunächst noch ansehen, wie man Zahlen aus einer Datei liest, eine bei
numerischen Arbeiten sehr häufige Situation. Als Eingabedatei sei eine Datei
namens ``spam.dat`` [#spam]_ mit dem Inhalt

.. code-block:: python

    1.37  2.59
   10.3  -1.3
    5.8   2.0

gegeben. Das folgende Programm berechnet zeilenweise das Produkt des jeweiligen
Zahlenpaares.

.. code-block:: python
   :linenos:

   daten = open("spam.dat")
   for zeile in daten:
       x, y = zeile.split()
       print(float(x)*float(y))
   daten.close()

In Zeile 3 wird jede eingelesene Zeile an Leerräumen wie zum Beispiel
Leerstellen oder Tabulatorzeichen, aufgeteilt. Damit ergeben sich je zwei
Strings, die die Information über die jeweilige Zahl enthalten. Allerdings kann
man Strings nicht miteinander multiplizieren. Daher muss in Zeile 4 vor der
Multiplikation mit Hilfe der :func:`float`-Funktion eine Umwandlung in
Gleitkommazahlen erfolgen. Das Schließen der Datei erfolgt in Zeile 5 außerhalb
der ``for``-Schleife, da sonst die Datei bereits nach dem Einlesen der ersten
Zeile geschlossen würde.

Als Alternative zu der im vorigen Beispiel gezeigten expliziten Umwandlung kann
es sinnvoll sein, die von Python zur Verfügung gestellte :func:`map`-Funktion
zu verwenden. Dies ist insbesondere bei mehreren Zahlen oder wenn deren Anzahl
nicht bekannt ist, nützlich. Das Beispiel lautet dann

.. code-block:: python
   :linenos:

   daten = open("spam.dat")
   for zeile in daten:
       x, y = map(float, zeile.split())
       print(x*y)
   daten.close()

Dabei wird in Zeile 3 die :func:`float`-Funktion zur Umwandlung aller Elemente
der Liste ``zeile.split()`` in Gleitkommazahlen angewandt.

In einem Programm möchte man nicht nur Daten aus einer Datei einlesen, sondern
vor allem auch die Ergebnisse in einer Datei speichern. Wie beim Lesen aus
Dateien muss man beim Schreiben in Dateien zunächst eine Datei öffnen. Dies
kann auf verschiedene Weise geschehen. Betrachten wir zunächst das folgende
Beispiel:

.. code-block:: python
   :linenos:

   datei = open("foo.dat", "w")
   for n in range(5):
       datei.write("{:4}{:4}\n".format(n, n*n))
   datei.close()

Die Anweisung in Zeile 1 kennen wir im Prinzip schon, nur dass jetzt das zweite
Argument explizit auf ``w``, also »write« gesetzt ist. Damit wird die Datei
``foo.dat`` zum Schreiben geöffnet. Ob die Datei schon existiert, ist dabei
unerheblich. Existiert sie nicht, so wird eine neue Datei angelegt. Existiert
die Datei dagegen schon, so wird ihre Länge vor dem Schreiben auf Null gesetzt.
Damit wird die zuvor existierende Datei effektiv überschrieben. In der dritten
Zeile erfolgt das Schreiben in die Datei mit Hilfe der :func:`write`-Methode.
Wie bei dem uns bereits bekannten ``print``-Befehl muss als Argument ein String
angegeben werden. Dabei können natürlich die im Abschnitt :ref:`formatierung`
besprochenen Formatspezifikationen verwendet werden. Zu beachten ist, dass im
Gegensatz zur ``print``-Anweisung bei Bedarf ein Zeilenumbruch explizit mit
``\n`` zu verlangen ist.  Die :func:`read`- und die :func:`write`-Methode sind
also insofern symmetrisch als in beiden Fällen der Zeilenumbruch in den
jeweiligen Zeichenketten explizit auftritt. Nicht vergessen werden sollte das
Schließen der Datei in Zeile 4, da ansonsten die Gefahr bestehen könnte, dass
Daten verloren gehen.

Öffnet man eine existierende Datei im Modus ``r+``, so kann man von ihr lesen
und in sie schreiben.  Ähnliches geschieht bei ``w+``, wobei bei Bedarf jedoch
eine neue Datei angelegt wird.  Gelegentlich möchte man Daten an eine Datei
anhängen. In diesem Falle verwendet man den Modus ``a`` für »append« oder
``a+`` falls man aus der Datei auch lesen möchte. 

|weiterfuehrend| Ab Python 3.3 gibt es auch noch die Option ``"x"``, die nur
dann eine Datei erfolgreich öffnet, falls diese Datei noch nicht existiert.

Bei numerischen Rechnungen ist es oft sinnvoll, die verwendeten Parameter im
Dateinamen aufzuführen wie es im folgenden Beispiel gezeigt ist. Dazu wird in
der Zeile 2 beim Öffnen der Datei ein geeigneter Konvertierungsspezifikator
verwendet.

.. code-block:: python
   :linenos:

    parameter = 12
    datei = open("resultate_{:05}.dat".format(parameter), "w")
    for n in range(parameter):
        datei.write("{:10}\n".format(n*n))
    datei.close()

Entsprechend dem Wert der Variable ``parameter`` erfolgt die Ausgabe in die
Datei ``resultate_00012.dat``. Die Formatiervorgabe, den Integer bis zur
geforderten Feldbreite von links mit Nullen aufzufüllen, ist hier nützlich, um
bei einer großen Anzahl von Parameterwerten eine ordentlich sortierte Übersicht
über die vorhandenen Dateien bekommen zu können.

Da das Überschreiben von Dateien unangenehme Folgen haben kann, ist es nützlich
zu wissen, wie man die Existenz einer Datei überprüfen kann. Mit einer Methode
aus dem ``os.path``-Modul geht das wie im Folgenden gezeigt, 

.. code-block:: python

   import os

   datei = "foo.dat"
   if os.path.exists(datei):
       print("Achtung! {} existiert bereits.".format(datei))
   else:
       print("Die Datei {} existiert noch nicht.".format(datei))

Existiert die Datei bereits, so würde man in einer echten Anwendung dem
Benutzer wohl die Möglichkeit geben, das Programm an dieser Stelle geordnet zu
beenden oder einen alternativen Dateinamen anzugeben.

Abschließend sei noch erwähnt, dass Python für bestimmte Dateiformate spezielle
Module zum Lesen und Schreiben zur Verfügung stellt. Hierzu gehört zum Beispiel
das ``csv``-Modul, das den Zugriff auf Dateien im ``csv``-Format [#csv]_
erlaubt. Dieses Format wird häufig von Tabellenkalkulationsprogrammen wie zum
Beispiel ``Microsoft Excel`` oder ``Calc`` aus ``OpenOffice`` bzw.
``LibreOffice`` benutzt. Hat man solche Programme bei der Erfassung der Daten
verwendet, so ist es sinnvoll, sich das ``csv``-Modul [#csvdoc]_ anzusehen.

Bei einer aufwendigen Übergabe von Parametern an ein Programm kann auch das
``ConfigParser``-Modul [#cpdoc]_ von Interesse sein, das mit Dateien im
``INI``-Format umgehen kann. Dabei werden Parameter in Name-Wert-Paaren
beschrieben, wobei eine Unterteilung in Abschnitte möglich ist.

.. |weiterfuehrend| image:: images/symbols/weiterfuehrend.*
           :height: 1em

.. rubric:: Footnotes
.. [#foo] Zum Ursprung dieses Namens siehe `RFC 3092 <http://www.ietf.org/rfc/rfc3092.txt>`_.
.. [#optparse] Dieses Modul ist unter dem Titel `optparse – Parser for command line options
   <http://docs.python.org/library/optparse.html>`_ in der Python-Dokumentation beschrieben.
.. [#argparse] Dieses Modul ist unter dem Titel `argparse – Parser for command-line options,
   arguments and sub-commands <http://docs.python.org/library/argparse.html>`_ in der 
   Python-Dokumentation beschrieben.
.. [#unicode] Hierzu und zu den folgenden Überlegungen zur Zeichenkodierung sei auf den 
   Anhang :ref:`appendixunicode` hingewiesen.
.. [#spam] Die Verwendung von ``spam`` in Python-Beispielen als Name ohne spezifische Bedeutung ist
   ein Verweis auf einen Sketch der Komikergruppe Monty Python (siehe `Wikipedia: Spam-Sketch
   <http://de.wikipedia.org/wiki/Spam-Sketch>`_).
.. [#csv] ``csv`` steht für *comma separated values*, wobei allerdings kein verbindlicher Standard
   existiert. Beispielsweise können Felder genauso gut durch Kommas wie durch Strichpunkte getrennt
   sein.
.. [#csvdoc] Dieses Modul ist unter dem Titel `csv — CSV File Reading and Writing 
   <http://docs.python.org/library/csv.html>`_ in der Python-Dokumentation beschrieben.
.. [#cpdoc] Dieses Modul ist unter dem Titel `ConfigParser — Configuration file parser
   <http://docs.python.org/library/configparser.html>`_ in der Python-Dokumentation beschrieben.
