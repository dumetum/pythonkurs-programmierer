# Pythonkurs für Programmierer

Das Repository enthält Unterlagen für einen Pythonkurs für Programmierer<sup>1</sup>. Diese beinhalten:

* Folien (Asciidoc und PDF)<sup>2</sup>
* Beispiele
* Übungen (Vorlagen zur Bearbeitung und Lösungsvorschläge)

Die Unterlagen sind für ein Sebststudium nur bedingt geeignet. 
Sie sind als begleitende Unterlagen zu einer Präsenzveranstaltung gedacht.


## Zielgruppe

Der vorliegende Kurs ist für Menschen mit Programmierkenntnisse gedacht. Die Teilnehmer sollten mit den folgenden Konzepten vertraut sein:
* Variablen und Zuweisungen
* Bedingte Anweisung und Schleifen
* Funktionen
* Datentypen: Zahlen, Zeichenketten, Listen
* Objektorientierung (bedingt - es wird eine kurze Einführung geboten)


## Inhalt

Ziel des Kurses ist eine kompakte Einführung in die Grundlagen von Python auf Basis der vorhandenen Programmierkenntnisse, so dass sich die Teilnehmer danach weitergehende Themen selbständig erarbeiten können.

Behandelt werden die folgenden Themen:
* Das Laufzeitmodell von Python
* Eingebaute Datentypen
* Kontrollstrukturen (Verzweigungen, Schleifen)
* Funktionen, Module und Pakete
* Einführung in die Objektorientierung und Vererbung


## Zeitlicher Rahmen

Ich habe den Kurs bisher im Rahmen von 3 Terminen à 4 (Schul-) Stunden (3 Zeitstunden) gehalten. 
* Tag 1: Laufzeitmodell, Datentypen, Kontrollstrukturen
* Tag 2: Funktionen, Module
* Tag 3: Objektorientierung

Zu jedem der Teile gibt es am Ende Übungsvorschläge, die die Teilnehmer nach dem theoretischen Teil bearbeiten sollen.


## Verwendete Werkzeuge

Eine erste Version der Folien wurde mit einem der gängigen Präsentationsprogramme erstellt. Für einen Programmierkurs als geeigneter hat sich dann aber ein textbasiertes Format erwiesen - in dem Fall asciidoc unter Verwendung von asciidoctor-pdf.js (https://github.com/Mogztter/asciidoctor-web-pdf). 

Die Graphiken wurden mit yEd (https://www.yworks.com/products/yed) erstellt.


### Erstellung der PDF-Folien

Um die PDF-Folien aus den Asciidoc-Quellen zu erzeugen, ist zunächst asciidoctor-pdf-js zu installieren wie unter https://github.com/Mogztter/asciidoctor-web-pdf beschrieben.

Die Folien in PDF kann man dann durch einen Befehl der folgenden Art erzeugen (im Build-Verzeichnis, andernfalls sind die Pfade entsprechend zu anzupassen):

`asciidoctor-pdf --template-require ./../Build/template.js ../FolienAsciidoc/01-Datentypen.adoc -o ../FolienPDF/01-Datentypen.pdf`


## Quellen

Ein solcher Kurs entsteht nicht im luftleeren Raum, sondern basiert neben eigenen Ideen und Konzepten auf verschiedenen Büchern und Kursen. Einige Referenzen seien hier beispielhaft genannt. Wo ich eine Idee oder ein Beispiel explizit übernommen habe, habe ich das in den Unterlagen entsprechend kenntlich gemacht. Sollte sich jemand trotzdem in seinen Rechten verletzt fühlen, setze er / sie sich bitte mit mir in Verbindung (s. unten).

* Bernd Klein, Einführung in Python 3, Hanser-Verlag
* Web-Seite zu diesem Buch: https://www.python-kurs.eu/
* Kofler: Python – Der Grundkurs, Rheinwerk Computing
* Johannes Ernesti, Peter Kaiser: Python 3 – Das umfassende Handbuch, Rheinwerk Computing
* Eric Matthes: Python Crashkurs – Eine praktische, projektbasierte Programmiereinführung, dpunkt.verlag
* Sweigart: Eigene Spiele programmieren: Python lernen


## Lizenz

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Lizenzvertrag" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Pythonkurs für Programmierer</span> von <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Christian Heckler</span> ist lizenziert unter einer <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Namensnennung - Nicht kommerziell - Keine Bearbeitungen 4.0 International Lizenz</a>.

Wer weitergehende Rechte möchte, wende sich gerne an mich.

## Kontakt
Fragen und Anregungen gerne an pythonkurs@ch-heckler.de.

<sup>1</sup>Im Deutschen sind hier alle Geschlechter eingeschlossen. So ist es natürlich auch in den gesamten Unterlagen zu verstehen.

<sup>2</sup>In dem Ordner Unterlagen liegen PDF-Dateien, in denen die Folien nicht als Folien formatiert sind. Die Dateien sind nicht besonders schön formatiert und eigenen sich nur für einen schnellen Überblick bzw. zum papiersparendem Ausdrucken.