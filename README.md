# Learn To Fly

Copyright (C) 2023 Frank Abelbeck <frank@abelbeck.info>

Lizenz: GLP 3

## Überblick

Dieses Repository enthält Hilfsprogramme für den
Theorieteil der PPL-A.

## BZF-Trainer

Der BZF-Trainer ist eine einzelne, für sich stehende
HTML5-Datei. Bei Betrachtung in einem Browser zeigt
der Trainer alle Fragen des offiziellen Fragenkatalogs
der Bundesnetzagentur in zufälliger Reihenfolge. Die
zugehörigen Antworten werden ebenfalls in zufälliger
Reihenfolge dargestellt.

Die User können eine Antwort auswählen und dann mit
der Schaltfläche "Prüfen" die korrekte Antwort aufdecken
lassen. Danach können sie mit der Schaltfläche "Weiter"
die nächste Frage abrufen.

Ein Fortschrittsbalken im Kopfbereich zeigt den Anteil
bearbeiteter Fragen. Sind alle Fragen abgerufen,
beginnt das Programm mit neu gemischten Fragen von vorn.

## PartFLC-Übersicht

Der Themenkatalog der Easy Access Rules for Flight Crew Licencing (Part-FCL),
Subpart PPL ist in einzeln anklick-/ausklappbarer Form als für sich stehende
HTML5-Datei abrufbar.

Quelle: https://www.easa.europa.eu/en/easy-access-rules-flight-crew-licencing-part-fcl

## PFCLAug20_make_html.py

Die Datei `PFCLAug20_make_html.py` enthält Python-Code, um aus einer
Markdown-Version des Part-FCL die o.a. alleinstehende HTML5-Datei zu erzeugen.

## Base64-Encoder

Dieses ist ein kleines Hilfsprogramm, um den Inhalt
einer Datei in Base64 auszugeben. Der BZF-Trainer
benötigt Dateiinhalte als Base64, wenn Abbildungen
zu Fragen darzustellen sind (hier: Meldepunkte).

## Changelog

 * **2023-03-23** initial version
    * late evening hack parallel to Hellboy II
 * **2023-03-26** enhanced version
    * better GUI
    * support for question-related images
    * disclaimer for Copyright Frank Abelbeck/Bundesnetzagentur
    * fixed shuffling algo
 * **2023-03-27** optimised version
    * simplified shuffle algo
 * **2023-04-06** initial release
    * asked BNetzA for permission due to integrated
      QA catalogue
    * removed official questions until permission
      is granted 
 * **2023-07-13**
    * added updated QA catalogue (no answer yet from BNetzA :shrugs:)
    * added PartFCL files
