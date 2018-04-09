.. _scipy:

***********************************************************
Numerische Programmbibliotheken am Beispiel von NumPy/SciPy
***********************************************************

Bei der numerischen Lösung von Problemen aus der Physik oder den
Materialwissenschaften benötigt man häufig Funktionalität, die von Python und
der zugehörigen Standardbibliothek nicht unmittelbar zur Verfügung gestellt
wird. Man denke an spezielle Funktionen, die nicht im ``math``-Modul enthalten
sind, beispielsweise Besselfunktionen, an die numerische Auswertung von
Integralen oder die Lösung von Differentialgleichungen. Auch die Verwendung von
Matrizen ist nicht unmittelbar möglich. Zwar erlauben es Listen, matrizenartige
Objekte darzustellen, aber es ist nicht direkt möglich, Matrizen miteinander zu
multiplizieren. Hier bleibt einem die Möglichkeit, die benötigte Funktionalität
selbst zu implementieren oder auf eines der vielen für die verschiedensten
Problemstellungen zur Verfügung stehenden Module zurückzugreifen.  Letzteres
ist sicherlich bequemer. Zudem handelt es sich häufig um effiziente und
sorgfältige Implementierungen. In diesem Kapitel wollen wir uns beispielhaft
das Numerikmodul NumPy/SciPy ansehen.

============
Installation
============

Nachdem NumPy/SciPy nicht Bestandteil von Pythons Standardbibliothek ist, steht
es standardmäßig noch nicht zur Verfügung. Ob es installiert ist, lässt sich
leicht mit Hilfe eines ``import``-Versuchs feststellen:

.. code-block:: python

   >>> import numpy
   >>> numpy.__version__
   '1.14.0'
   >>> import scipy
   >>> scipy.__version__
   '1.0.0'

Haben Sie beispielsweise die Anaconda-Distribution installiert, so
sollte das Importieren problemlos funktionieren, auch wenn vielleicht eine
andere Versionsnummer angezeigt wird [#version]_. Sind die Bibliotheken nicht vorhanden,
so würde eine ``ImportError``-Ausnahme geworfen. Dann müssen NumPy und
SciPy installiert werden. Informationen hierzu finden Sie für
verschiedene Betriebssysteme unter `www.scipy.org/install.html
<http://www.scipy.org/install.html>`_.

.. _numpy:

======================
Arrays und Anwendungen
======================

Im Folgenden soll anhand von wenigen Beispielen ein kurzer Einblick in die
Möglichkeiten gegeben werden, die NumPy bietet. Das Programm

.. code-block:: python
   :linenos:

   import numpy as np

   matrixA = np.array([[1.3, 2.5], [-1.7, 3.9]])
   matrixB = np.array([[2.1, -4.5], [0.9, -2.1]])
   print(matrixA, end="\n\n")
   print(matrixB, end="\n\n")
   print(np.dot(matrixA, matrixB), end="\n\n")
   anweisung = "{:g}*{:g}+{:g}*{:g}".format(matrixA[0, 0], matrixB[0, 0],
                                            matrixA[0, 1], matrixB[1, 0])
   print("{} = {:g}".format(anweisung, eval(anweisung)))

erzeugt die Ausgabe

.. code-block:: python

   [[ 1.3  2.5]
    [-1.7  3.9]]

   [[ 2.1 -4.5]
    [ 0.9 -2.1]]

   [[  4.98 -11.1 ]
    [ -0.06  -0.54]]

   1.3*2.1+2.5*0.9 = 4.98

In der ersten Zeile des Programmcodes wird das NumPy-Modul geladen, wobei die
Verwendung des kurzen Bezeichners ``np`` eine häufig verwendete Konvention ist,
um im Programmtext auf die Herkunft der verwendeten Methoden hinzuweisen. In
den Zeilen 3 und 4 ist eine Möglichkeit gezeigt, Matrizen mit Hilfe von NumPy
aus einer Liste zu erzeugen. In Zeile 9 wird das Produkt der beiden Matrizen
berechnet und ausgegeben. Die in den Zeilen 11 und 12 erzeugte Ausgabe weist
die Korrektheit anhand des obersten Diagonalelements des Produkts durch
Multiplikation der entsprechenden Zeile von ``matrixA`` und Spalte von
``matrixB`` nach. Zugleich erkennt man aus Zeile 11, dass die Nummerierung der
Matrixelemente, wie die von Python-Listen, mit ``0`` beginnt. Im Gegensatz zu
Listen werden die Matrixelemente jedoch durch Kommas getrennt in einem einzigen
eckigen Klammerpaar angegeben. Daraus wird deutlich, dass im Gegensatz zu der
hierarchischen Konstruktion der Listen von Listen hier die verschiedenen
Dimensionen eines Arrays gleichberechtigt sind.

Multipliziert man zwei Arrays mit Hilfe des Multiplikationsoperators ``*``, so
wird keine Matrixmultiplikation durchgeführt. Vielmehr werden die Elemente an
den jeweils gleichen Positionen der beiden Matrizen miteinander multipliziert.

.. code-block:: python

   >>> matrixA*matrixB
   array([[  2.73 -11.25],
          [ -1.53  -8.19]])

|weiterfuehrend| Ab Python 3.5 und NumPy 1.10 kann die Matrixmultiplikation von
Arrays mit Hilfe des Operators ``@`` ausgeführt werden:

.. code-block:: python

   >>> matrixA @ matrixB
   array([[  4.98, -11.1 ],
          [ -0.06,  -0.54]])

Das folgende Beispiel zeigt die Berechnung von Skalarprodukt, dyadischem
Produkt sowie Kreuzprodukt für zwei Vektoren.

.. code-block:: python

   import numpy as np

   vecA = np.array([2, -3, 0])
   vecB = np.array([5, 4, 0])
   print np.dot(vecA, vecB)
   print
   print np.outer(vecA, vecB)
   print
   print np.cross(vecA, vecB)

Als Ausgabe findet man erwartungsgemäß

.. code-block:: python

   -2

   [[ 10   8   0]
    [-15 -12   0]
    [  0   0   0]]

   [ 0  0 23]

Interessant ist die Möglichkeit, Arrays als Argumente von mathematischen Funktionen zu verwenden:

.. code-block:: python
   :linenos:

   >>> import numpy as np
   >>> import math
   >>> x = np.linspace(0, 1, 11)
   >>> x
   array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1. ])
   >>> np.exp(x)
   array([ 1.        ,  1.10517092,  1.22140276,  1.34985881,  1.4918247 ,
           1.64872127,  1.8221188 ,  2.01375271,  2.22554093,  2.45960311,
           2.71828183])
   >>> math.exp(x)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: only length-1 arrays can be converted to Python scalars

Eine praktische Methode, um ein Array mit äquidistanten Werten zwischen zwei
Grenzen zu erzeugen, ist die :func:`linspace`-Funktion, die in Zeile 3 zur
Erzeugung der Argumente benutzt wird. Der Aufruf der Exponentialfunktion aus
NumPy gibt in den Zeilen 6-9 ein ganzes Array der entsprechenden Ergebnisse
zurück. Zeilen 10-13 zeigen, dass dies mit der Exponentialfunktion aus dem
``math``-Modul nicht möglich wäre.  Bei umfangreichen Arrays spart die
Verwendung der NumPy-Funktion Rechenzeit gegenüber einer Schleife, die die
Funktion nacheinander auf jedes Element einzeln anwendet. Als Faustregel gilt
bei der Verwendung von NumPy, dass im Hinblick auf die Effizienz eines Programms
``for``-Schleifen nach Möglichkeit durch geeignete ``array``-Operationen
ersetzt werden sollten.

Zum Abschluss kehren wir noch einmal zu den Matrizen zurück und sehen uns
einige Funktionen aus dem Bereich der Linearen Algebra an.

.. code-block:: python
   :linenos:

   >>> import numpy as np
   >>> from numpy import linalg as LA
   >>> a = np.array([[1, 3], [2, 5]])
   >>> LA.det(a)
   -1.0
   >>> LA.inv(a)
   array([[-5.,  3.],
          [ 2., -1.]])
   >>> np.dot(a, LA.inv(a))
   array([[ 1.,  0.],
          [ 0.,  1.]])
   >>> LA.eig(a)
   (array([-0.16227766,  6.16227766]), array([[-0.93246475, -0.50245469],
          [ 0.36126098, -0.86460354]]))
   >>> eigenwerte, eigenvektoren = LA.eig(a)
   >>> for i in range(len(eigenwerte)):
   ...     print(np.dot(a, eigenvektoren[:, i]), eigenwerte[i]*eigenvektoren[:, i])
   ... 
   [ 0.1513182  -0.05862459] [ 0.1513182  -0.05862459]
   [-3.09626531 -5.32792709] [-3.09626531 -5.32792709]

In den Zeilen 1 und 2 werden zunächst die weiter unten benötigten Funktionen
importiert.  Dabei bezieht sich Zeile 2 auf die Funktionen, die im Modul zur
Linearen Algebra von NumPy enthalten sind. Nachdem in Zeile 3 eine Matrix
definiert wurde, wird in Zeile 4 die zugehörige Determinante bestimmt. In Zeile
6 wird die inverse Matrix berechnet und die Korrektheit des Ergebnisses durch
Multiplikation mit der ursprünglichen Matrix nachgewiesen. In Zeile 9 werden
die Eigenwerte und Eigenvektoren der Matrix ``a`` berechnet. Um auf das Tupel
nicht über die entsprechenden Indizes zugreifen zu müssen, kann man das
Ergebnis wie in Zeile 12 gezeigt gleich in die Eigenwerte und die Eigenvektoren
aufteilen. In den Zeilen 13-17 wird schließlich nachgewiesen, dass die
Eigenwerte und Eigenvektoren korrekt sind. Dabei wird verwendet, dass die
Spalten der Eigenvektormatrix den Eigenvektoren entsprechen. Der erste
Eigenvektor wird mit ``eigenvektor[:, 0]`` angegeben. Wie bei Listen bedeutet
der einzelne Doppelpunkt, dass der erste Index von seinem Minimalwert ``0`` bis
zu seinem Maximalwert, hier ``1``, läuft.

======================
Numerische Integration
======================

Als Anwendung von SciPy betrachten wir die numerische Auswertung des Integrals

.. math:: 

   J_0(1) = \frac{1}{\pi}\int_0^\pi\cos(\cos(x))\mathrm{d}x.

Hierbei ist :math:`J_0(z)` die Besselfunktion erster Gattung und nullter
Ordnung, deren Wert wir probehalber ebenfalls mit Hilfe von SciPy berechnen
lassen können. Das folgende Programm führt die notwendigen Berechnungen durch:

.. code-block:: python
   :linenos:

   from math import cos, pi
   from scipy import integrate, special

   resultat, fehler = integrate.quad(lambda x: cos(cos(x)), 0, pi)
   print(resultat/pi, fehler/pi)
   print(special.j0(1))

Die zugehörige Ausgabe lautet

.. code-block:: python

   0.7651976865579664 7.610964456309953e-11
   0.765197686558

In den ersten beiden Programmzeilen werden zunächst die benötigten Unterpakete
von SciPy, :mod:`integrate` für die Integration und :mod:`special` für
spezielle Funktionen, sowie der Kosinus und die Kreiszahl aus dem
:mod:`math`-Modul importiert. In Zeile 4 wird zur Integration die Funktion
:func:`quad` (von »Quadratur« oder Englisch »quadrature«) aus dem
:mod:`integrate`-Modul verwendet. :func:`quad` verlangt zwingend eine Funktion,
die den Integranden beschreibt und hier als Lambdafunktion angegeben ist, sowie
die Integrationsgrenzen. Ausgegeben werden das Resultat der numerischen
Integration und eine Abschätzung des absoluten Fehlers. Zur Beurteilung der
Qualität des Resultats verwenden wir in Zeile 6 die Besselfunktion :func:`j0`
aus dem :mod:`special`-Modul von SciPy.  Der Vergleich des Ergebnisses der
numerischen Integration mit :math:`J_0(1)`, für das SciPy einen ebenfalls im
Prinzip mit Fehlern behafteten numerischen Wert bestimmt, ergibt perfekte
Übereinstimmung. 

Wenn man die Konstante ``inf`` aus NumPy importiert, kann man auch
uneigentliche Integrale berechnen:

.. code-block:: python

   from scipy import integrate
   import numpy as np

   resultat, fehler = integrate.quad(lambda x: 1/(x*x+1), -np.inf, np.inf)
   print(resultat/np.pi, fehler)

Der erste Wert der Ausgabe 

.. code-block:: python

   1.0 5.155583905474508e-10

zeigt, dass der Wert des Integrals

.. math::

   \int_{-\infty}^\infty\frac{1}{x^2+1}\mathrm{d}x = \pi

korrekt bestimmt wird. Man sollte sich von der Qualität dieses Ergebnisses jedoch nicht täuschen lassen.
Nicht immer kann ein numerisches Resultat mit einer solchen Genauigkeit erhalten werden. Manchmal muss
das Integrationsproblem auch zunächst geeignet formuliert werden, zum Beispiel in der Nähe von Singularitäten 
oder wenn der Integrand schnell oszilliert.

.. _ode:

================================================
Integration gewöhnlicher Differentialgleichungen
================================================

Häufig steht man in der Physik und den Materialwissenschaften vor der Aufgabe,
Differentialgleichungen zu lösen.  Wir beschränken uns hier auf gewöhnliche
Differentialgleichungen, die als Anfangswertproblem gelöst werden sollen. Wir
beginnen mit einer Differentialgleichung erster Ordnung

.. math:: 
   
   \dot x = -x^2,

die sich durch Trennung der Variablen lösen lässt. Will man nicht selbst ein
Lösungsverfahren, zum Beispiel das Euler- oder Runge-Kutta-Verfahren
implementieren, so kann man wiederum auf das SciPy-Paket zurückgreifen. Dort
wird unter anderem die Funktion ``odeint`` zur Verfügung gestellt, die wir im
Folgenden benutzen wollen. Der Name der Funktion enthält das englische
»ordinary differential equation« in abgekürzter Form. 

Da der Funktionsaufruf in einem solchen Fall durchaus komplexer sein kann, muss
man sich zunächst über die von der Funktion erwarteten Argumente informieren.
In Python kann man das leicht mit der :func:`help`-Funktion tun, aber auch im
Internet unter http://docs.scipy.org/doc/ finden sich Dokumentationen.

.. code-block:: python

   >>> from scipy import integrate
   >>> help(integrate.odeint)

   Help on function odeint in module scipy.integrate.odepack:

   odeint(func, y0, t, args=(), Dfun=None, col_deriv=0, full_output=0, ml=None,
   mu=None, rtol=None, atol=None, tcrit=None, h0=0.0, hmax=0.0, hmin=0.0, ixpr=0,
   mxstep=0, mxhnil=0, mxordn=12, mxords=5, printmessg=0)
       Integrate a system of ordinary differential equations.
    
       Solve a system of ordinary differential equations using lsoda from the
       FORTRAN library odepack.
    
       Solves the initial value problem for stiff or non-stiff systems
       of first order ode-s::
    
           dy/dt = func(y,t0,...)
    
       where y can be a vector.
    
       Parameters
       ----------
       func : callable(y, t0, ...)
           Computes the derivative of y at t0.
       y0 : array
           Initial condition on y (can be a vector).
       t : array
           A sequence of time points for which to solve for y.  The initial
           value point should be the first element of this sequence.
   […]  
    
       Returns
       -------
       y : array, shape (len(t), len(y0))
           Array containing the value of y for each desired time in t,
           with the initial value y0 in the first row.
   […]  

Wir haben an den mit ``[…]`` markierten Stellen einigen Text ausgelassen. Bereits der
gleich zu Beginn angegebene Funktionsaufruf zeigt, dass eine Vielzahl an Parametern übergeben
werden können. Die meisten sind jedoch mit Defaultwerten belegt, so dass wir nicht gezwungen
sind, sie zu spezifizieren. Sollte es jedoch zum Beispiel nötig sein, den relativen oder absoluten
Fehler besser zu kontrollieren, so kann man dies tun. Beim Aufruf der Funktion :func:`odeint`
müssen wir aber auf jeden Fall eine aufrufbare Funktion übergeben, die es erlaubt, die Ableitung
zu berechnen. Diese Funktion muss zumindest zwei Argumente besitzen, nämlich die aktuellen Werte
der abhängigen und der unabhängigen Variablen. Ferner benötigen wir einen Anfangswert und 
einen Vektor, der die Werte der unabhängigen Variablen enthält, zu der die gesuchte Lösung der
Differentialgleichung bestimmt werden soll. Das folgende Programm berechnet eine numerische
Lösung für die oben genannte Differentialgleichung.

.. code-block:: python
   :linenos:

   import numpy as np
   from scipy import integrate
   
   pts = np.linspace(0, 100, 101)
   ergebnis = integrate.odeint(lambda x, t: -x**2, 1, pts)[:, 0]
   for n in range(len(pts)):
       exakt = 1/(1+pts[n])
       print("{:3.0f}  {:10.8f}  {:11.5g}".format(
                         pts[n], 
                         ergebnis[n], 
                         (ergebnis[n]-exakt)/exakt))

In Zeile 1 importieren wir zunächst das :mod:`numpy`-Modul, das wir benötigen,
um in Zeile 4 ein Array mit äquidistanten Zeitpunkten zu erzeugen. Außerdem
wird in Zeile 2 das :mod:`integrate`-Unterpaket aus SciPy importiert, aus dem
wir die Funktion :func:`odeint` zum Lösen der Differentialgleichung verwenden
wollen.  Dies geschieht in Zeile 5. Dabei haben wir die Ableitung der
Einfachheit halber als Lambda-Funktion in den Aufruf geschrieben.  Der
Anfangswert ist im zweiten Argument gleich ``1`` gesetzt und das dritte
Argument enthält das NumPy-Array mit den Punkten, für die die Lösung bestimmt
werden soll. :func:`odeint` gibt ein zweidimensionales Array zurück, das bei
Differentialgleichungssystemen in jeder Spalte den Zeitverlauf für eine
Komponente enthält. Da wir in unserem Beispiel nur eine einzige
Differentialgleichung erster Ordnung vorliegen haben, wählen wir explizit die
Spalte 0 aus. Ab Zeile 6 wird das exakte Ergebnis an den vorgegebenen Punkten
ausgewertet und die Lösung samt den Werten der unabhängigen Variablen und des
relativen Fehlers ausgegeben. Führt man das Programm aus, so erhält man etwa
die folgende Ausgabe

.. code-block:: python

    0  1.00000000            0
    1  0.50000000   1.1693e-09
    2  0.33333332  -5.1641e-08
    3  0.24999998   -8.066e-08
    4  0.19999998  -1.0617e-07
  […]
   95  0.01041665  -1.1279e-06
   96  0.01030927   -1.126e-06
   97  0.01020407  -1.1343e-06
   98  0.01010100   -1.146e-06
   99  0.00999999  -1.1439e-06
  100  0.00990098   -1.135e-06

Wir verzichten darauf, die gesamte Ausgabe zu reproduzieren. Man sieht aber bereits an 
diesen Zeilen, dass das erhaltene Ergebnis nicht exakt ist und der relative Fehler mit zunehmendem
Abstand vom Startwert zunimmt. Dennoch ist der relative Fehler gut kontrolliert, so dass hier
eine brauchbare Lösung erzeugt wurde.

Wenn wir uns die Dokumentation der :func:`odeint`-Funktion noch einmal ansehen, stellen wir
fest, dass die Funktion zunächst für Differentialgleichungen erster Ordnung gedacht ist.
Allerdings kann es sich bei der Variablen ``y`` um einen Vektor handeln. Dies gibt uns die
Möglichkeit, auch Differentialgleichungen höherer Ordnung numerisch zu behandeln. Wir müssen
sie nur in ein System von Differentialgleichungen erster Ordnung umformulieren. Betrachten wir
als Beispiel die Differentialgleichung eines gedämpften harmonischen Oszillators

.. math:: 

   \ddot x+\gamma\dot x+x=0,

wobei γ die Dämpfungskonstante ist. Diese Differentialgleichung ist zu dem Satz
zweier Differentialgleichungen erster Ordnung

.. math::

   \dot p=-x-\gamma p

.. math::

   \dot x=p

äquivalent, den wir nun mit den Anfangsbedingungen :math:`x(0)=0,\,p(0)=1`
numerisch lösen wollen.

.. code-block:: python
   :linenos:

   from scipy import integrate
   import numpy as np
   from math import exp, sin, sqrt
   
   def ableitung(y, t, gamma):
       x, p = y
       return np.array([p, -x-gamma*p])
   
   pts = np.linspace(0, 10, 101)
   anfangsbedingungen = np.array([0, 1])
   gamma = 0.3
   omega = sqrt(1-0.25*gamma**2)
   
   ergebnis = integrate.odeint(ableitung, anfangsbedingungen, pts, (gamma,))
   ort = ergebnis[:, 0]
   
   for n in range(len(pts)):
       exakt = exp(-0.5*gamma*pts[n])*sin(omega*pts[n])/omega
       print("{:4.1f}  {:8.5f}  {:11.5g}".format(
                           pts[n], ort[n], ort[n]-exakt))

Nachdem wir bereits ein Beispiel besprochen haben, können wir uns hier auf die
neuen Aspekte beschränken. In den Zeilen 5-7 wurde diesmal eine Funktion
definiert, die einen Vektor mit den benötigten ersten Ableitungen zurückgibt.
Die in Zeile 10 definierten Anfangsbedingungen müssen jetzt ebenfalls aus einem
Vektor bestehen. Außerdem enthält die Funktion :func:`ableitung` ein
zusätzliches Argument, nämlich ``gamma``, das übergeben werden muss. Dazu sieht
:func:`odeint` ein viertes Argument vor, das ein Tupel sein muss und dessen
Elemente dem dritten und eventuell weiteren Argumenten der Ableitungsfunktion
zugeordnet werden.  Es ist zu beachten, dass ein einzelner eingeklammerter
Variablenname nur dann als Tupel interpretiert wird, wenn dieser von einem
Komma gefolgt wird.

|frage| Warum wird hier im Gegensatz zum ersten Beispiel nicht der relative sondern
der absolute Fehler ausgegeben?

Auch wenn der hier vorgestellte Programmcode nur die Position des Oszillators
als Funktion der Zeit ausgibt, könnte man genauso seine Geschwindigkeit
ausgeben. Nachdem wir zwei Differentialgleichungen erster Ordnung gelöst haben,
ist die Geschwindigkeit bei der von uns gewählten Reihenfolge als zweite Spalte 
``ergebnis[:, 1]`` in der Ergebnismatrix zugänglich.

|frage| Wie ändert sich die Trajektorie, wenn in der Bewegungsgleichung
:math:`\dot x` durch :math:`\dot x^2` ersetzt wird, so dass die Bewegungsgleichung
nichtlinear wird? Mit den in Kapitel :ref:`grafik` dargestellten Techniken können
Sie die berechneten Trajektorien leicht vergleichen.

.. |frage| image:: images/symbols/question.*
           :height: 1em
.. |weiterfuehrend| image:: images/symbols/weiterfuehrend.*
           :height: 1em

.. rubric:: Footnotes
.. [#version] Man beachte, dass vor und nach ``version`` jeweils *zwei* Unterstriche einzugeben sind.
