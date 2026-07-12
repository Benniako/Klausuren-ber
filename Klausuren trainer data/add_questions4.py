"""Fuegt 50 neue Perso+Mathe Fragen hinzu."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "_data", "questions_validated.json")

with open(PATH, "r", encoding="utf-8") as f:
    QS = json.load(f)

def add(bank, q, opts, correct_idx, solution, source):
    QS[bank].append({"q": q, "o": opts, "c": correct_idx, "s": solution, "src": source})

# ============================================================
# PERSO (25 Fragen)
# ============================================================
add("perso",
    "Im Blake/Mouton-Grid beschreibt 'Ideales Team-Management' (9,9) welche Eigenschaft?",
    ["Hohe Menschenorientierung, geringe Aufgabenorientierung", "Geringe Menschenorientierung, hohe Aufgabenorientierung", "Hohe Menschenorientierung, hohe Aufgabenorientierung", "Geringe Menschenorientierung, geringe Aufgabenorientierung"],
    2, "Blake/Mouton-Grid: Ideales Team-Management (9,9) = maximale Aufgaben- UND Menschenorientierung.", "Perso Folie 04 Fuehrung")

add("perso",
    "Was ist der Unterschied zwischen Effektivitaet und Effizienz?",
    ["Effektivitaet = Was (Zielerreichung), Effizienz = Wie (Ressourceneinsatz)", "Effektivitaet = Kosten, Effizienz = Umsatz", "Gleiche Begriffe", "Effektivitaet ist messbar, Effizienz nicht"],
    0, "Effektivitaet = 'Die richtigen Dinge tun' (Zielerreichung). Effizienz = 'Die Dinge richtig tun' (optimales Input/Output).", "Perso Folie 09 Grundlagen Organisation")

add("perso",
    "Die Nationalmannschaft hat 76% Ballbesitz und scheidet aus. Das ist ein Beispiel fuer:",
    ["Effizienzproblem", "Effektivitaetsproblem", "Motivationsproblem", "Kommunikationsproblem"],
    1, "Ballbesitz (Input) war hoch, aber Ziel (Sieg) wurde nicht erreicht = Effektivitaetsproblem.", "Perso Menti 09 Grundlagen")

add("perso",
    "Welche Organisationsform maximiert Synergien im Einkauf?",
    ["Divisionale Organisation", "Funktionale Organisation", "Matrixorganisation", "Projektorganisation"],
    1, "Funktionale Organisation buendelt identische Funktionen (z.B. Einkauf) und maximiert Synergien.", "Perso Menti 10 Orgaformen")

add("perso",
    "Welche Organisationsform maximiert Transparenz ueber Geschaeftsfelder?",
    ["Funktionale Organisation", "Divisionale Organisation", "Matrixorganisation", "Netzwerkorganisation"],
    1, "Divisionale Organisation organisiert nach Geschaeftsfeldern und ermoeglicht transparente Ergebnisse pro Bereich.", "Perso Menti 10 Orgaformen")

add("perso",
    "Welches Fuehrungsprinzip erfordert eine kleinere Fuehrungsspanne?",
    ["Demokratische Fuehrung", "Autoritaere Fuehrung (Weisung und Kontrolle)", "Laissez-faire-Fuehrung", "Transaktionale Fuehrung"],
    1, "Autoritaere Fuehrung erfordert mehr Kontrolle und Weisung = kleinere Fuehrungsspanne noetig.", "Perso Menti 10 Fuehrungsspanne")

add("perso",
    "Welche Faktoren ermoeglichen eine hohe Fuehrungsspanne?",
    ["Steigende Komplexitaet", "Hohe Aenderungshaeufigkeit", "Zunehmende Gleichartigkeit und gute Ueberwachbarkeit", "Hohe Spezialisierung"],
    2, "Gleichartige Aufgaben und gute Ueberwachbarkeit ermoeglichen mehr Mitarbeiter pro Vorgesetzten.", "Perso Menti 10 Fuehrungsspanne")

add("perso",
    "Was beschreibt der 'Blinde Fleck' im Johari-Fenster?",
    ["Bereich den ich kenne und andere auch", "Bereich den ich nicht kenne, aber andere kennen", "Bereich den ich kenne, aber andere nicht", "Bereich den weder ich noch andere kennen"],
    1, "Blinder Fleck = Verhaltensweisen die anderen auffallen, aber dem eigenen Bewusstsein fehlen.", "Perso Klausur 71007")

add("perso",
    "Wie verkleinert eine Fuehrungskraft den Blinden Fleck einer Mitarbeiterin?",
    ["Mehr Feedback einholen", "Mehr Informationen preisgeben", "Delegation", "Training"],
    0, "Blinder Fleck wird verkleinert durch Feedback von anderen (Johari-Fenster).", "Perso Klausur 71007")

add("perso",
    "Was sind die 5 Dysfunktionen in Teams nach Lencioni (unten nach oben)?",
    ["Fehlende Kommunikation, schlechte Planung, mangelnde Motivation, schlechte Fuehrung, fehlende Ressourcen", "Abwesenheit von Vertrauen, Furcht vor Konflikt, Mangel an Verpflichtung, Vermeidung von Verantwortlichkeit, Unaufmerksamkeit gegenueber Resultaten", "Zu hohe Kosten, zu wenig Zeit, zu wenige Mitarbeiter, schlechte Technik, mangelnde Bildung", "Keine Vision, keine Strategie, keine Ziele, keine Kontrolle, keine Belohnung"],
    1, "Lencionis Pyramide: 1) Abwesenheit von Vertrauen, 2) Furcht vor Konflikt, 3) Mangel an Verpflichtung, 4) Vermeidung von Verantwortlichkeit, 5) Unaufmerksamkeit.", "Perso Folie 05 TeamKonflikt")

add("perso",
    "Was ist der 'Ringelmann-Effekt' (Social Loafing)?",
    ["Einzelne arbeiten im Team weniger als allein", "Teams sind kreativer als Einzelne", "Gruppen treffen mutigere Entscheidungen", "Konflikte verbessern die Leistung"],
    0, "Ringelmann-Effekt: Einzelne reduzieren Anstrengung weil individuelle Leistung weniger sichtbar ist.", "Perso Folie 05 TeamKonflikt")

add("perso",
    "Welche Massnahme reduziert den Trittbrettfahren-Effekt am besten?",
    ["Groessere Teams", "Identifizierbaren Leistungsbeitrag jedes Einzelnen sicherstellen", "Weniger Kontrolle", "Meetings abschaffen"],
    1, "Wenn jeder individuellen Beitrag sichtbar leisten muss, sinkt Tendenz zum Trittbrettfahren.", "Perso Folie 05 TeamKonflikt")

add("perso",
    "Was ist ein typisches Merkmal eines Hochleistungs-Teams?",
    ["Impersonale Kommunikation", "Teammitglieder kennen ihre Staerken und Schwaechen", "Konflikte werden vermieden", "Fuehrung basiert auf Weisungen"],
    1, "Hochleistungsteams: Mitglieder kennen Staerken/Schwaechen und ihre Lieblingsrolle im Team.", "Perso Folie 05 TeamKonflikt")

add("perso",
    "Bei personenbedingter Kuedigung wurde die Interessensabwaegung nicht eingehalten, wenn:",
    ["Arbeitnehmer Abmahnung erhalten hat", "Arbeitnehmer fuer andere Taetigkeiten haette eingesetzt werden koennen", "Betriebsrat zugestimmt hat", "Kuendigungsfrist eingehalten wurde"],
    1, "Interessensabwaegung: Pruefung ob interne Weiterbeschaftigung (andere Stelle) moeglich waere.", "Perso Klausur 71007")

add("perso",
    "Was muss bei ordentlicher verhaltensbedingter Kuendigung vorausgegangen sein?",
    ["Schriftliche Abmahnung", "Muendliche Ermahnung", "Fristlose Kuendigung", "Abfindungszahlung"],
    0, "Verhaltensbedingt: vorherige Abmahnung erforderlich (Ultima-ratio-Prinzip).", "Perso Klausur 71007")

add("perso",
    "Was beschreibt die Leistungsbereitschaft eines Mitarbeiters?",
    ["Koennen (Faehigkeiten)", "Wollen (Motivation)", "Duermen (Moeglichkeiten)", "Muessen (Pflichten)"],
    1, "Leistungsbereitschaft = Wollen (Motivation). Leistungsfahigkeit = Koennen. Leistungsmoeglichkeit = Duermen.", "Perso Folie 04 Fuehrung")

add("perso",
    "Was kostet die Fluktuation eines Mitarbeiters durchschnittlich?",
    ["15.000 EUR", "25.000 EUR", "45.000 EUR", "75.000 EUR"],
    2, "Austrittskosten (5k) + Rekrutierung (13k) + Einarbeitung (10k) + Opportunitaetskosten (17k) = ~45.000 EUR.", "Perso Folie 06 Arbeitsrecht")

add("perso",
    "In der Normenhierarchie des Arbeitsrechts steht am hoechsten:",
    ["Betriebsvereinbarungen", "Gesetze", "Grundgesetz und Laenderverfassungen", "Tarifvertraege"],
    2, "Normenhierarchie: 1) GG/LV, 2) Gesetze, 3) Tarifvertraege, 4) Betriebsvereinbarungen, 5) Arbeitsvertraege.", "Perso Folie 06 Arbeitsrecht")

add("perso",
    "Was ist der Unterschied zwischen Leiharbeitnehmer und Werkvertrag?",
    ["Kein Unterschied", "Leiharbeitnehmer werden beim Entleiher eingegliedert, Werkvertragsarbeitnehmer bleiben beim Auftragnehmer", "Werkvertragsarbeitnehmer erhalten kein Gehalt", "Leiharbeitnehmer haben mehr Rechte"],
    1, "Leasing: Arbeitnehmer wird ins Unternehmen des Entleiher eingegliedert. Werkvertrag: bleibt beim Auftragnehmer.", "Perso Folie 06 Arbeitsrecht")

add("perso",
    "Was ist ein Merkmal der divisionalen Organisation?",
    ["Maximale Synergien durch Bündelung gleicher Funktionen", "Maximale Transparenz ueber Geschaeftsfelder", "Matrixstruktur mit doppelter Berichtslinie", "Flache Hierarchien ohne Abteilungen"],
    1, "Divisionale Organisation: nach Produkten/Geschaeftsfeldern = transparente Ergebnisse pro Bereich.", "Perso Menti 10 Orgaformen")

add("perso",
    "Was ist der Hauptvorteil der Matrixorganisation?",
    ["Maximale Synergien", "Maximale Transparenz", "Kraft des Dialogs zur Problemlösung", "Maximale Flexibilität"],
    2, "Matrixorganisation foerdert Dialog und Zusammenarbeit zwischen verschiedenen Funktionsbereichen.", "Perso Menti 10 Orgaformen")

add("perso",
    "In welchem Fall ist demokratische Fuehrung sinnvoller als autoritaere?",
    ["Einfache, routinierte Aufgaben", "Komplexe, kreative Aufgaben", "Akute Krisensituationen", "Unerfahrene Mitarbeiter"],
    1, "Demokratische Fuehrung: komplex/kreativ (Mitdenken noetig). Autoritaer: Krisen/einfach.", "Perso Folie 04 Fuehrung")

add("perso",
    "Was ist ein Bewertungsfehler bei der Personalbeurteilung?",
    ["Halo-Effekt", "SWOT-Analyse", "Balanced Scorecard", "Porters Five Forces"],
    0, "Halo-Effekt: einzelnes Merkmal beeinflusst Gesamteinschaetzung ueberproportional.", "Perso Folie 08-2 Performance Management")

add("perso",
    "Unterschied zwischen ergebnisorientierter und verhaltensorientierter Bewertung?",
    ["Ergebnis = Output (Erreichtes), Verhalten = Input (Verhalten)", "Kein Unterschied", "Ergebnis ist fairer", "Verhalten misst nur Erfolg"],
    0, "Ergebnisorientiert = messbare Ergebnisse (Output). Verhaltensorientiert = beobachtbares Verhalten (Input).", "Perso Folie 08-2 Performance Management")

add("perso",
    "Was ist der Unterschied zwischen Headcount und FTE?",
    ["Headcount = Stellen, FTE = Mitarbeiter", "Headcount = Koepfe (Mitarbeiter), FTE = Vollzeitaequivalente", "Kein Unterschied", "FTE immer groesser als Headcount"],
    1, "Headcount = Personenanzahl. FTE (Full-Time Equivalent) = Umrechnung auf Vollzeitaequivalente.", "Perso Folie 08 Personalbeschaffung")

add("perso",
    "Was ist der 'Nettopersonalbedarf'?",
    ["Gesamtbedarf", "Bruttopersonalbedarf minus interne Verfuegbarkeit", "Anzahl auszubildender Mitarbeiter", "Anzahl zu entlassender Mitarbeiter"],
    1, "Netto = Bruttopersonalbedarf - (Bestand + Interne Verfuegbarkeit). Tatsaechlich durch externe Beschaffung zu decken.", "Perso Folie 08 Personalbeschaffung")

# ============================================================
# MATHE (25 Fragen)
# ============================================================
add("mawi1",
    "Was ist die Grenzkostenfunktion wenn K(x) = 2x + 1000?",
    ["K'(x) = 2x", "K'(x) = 2", "K'(x) = 1000", "K'(x) = 2 + 1000/x"],
    1, "Grenzkosten = Ableitung: K'(x) = d/dx(2x + 1000) = 2. Bei linearer Kostenfunktion konstant.", "WiMa 1 Kap. 1")

add("mawi1",
    "Was sind 'stueckfixe Kosten'?",
    ["Kosten pro Einheit", "Fixkosten dividiert durch Produktionsmenge", "Kosten die mit Produktion steigen", "Kosten fuer das Lager"],
    1, "Stueckfixe Kosten = FK / Produktionsmenge (z.B. FK(x) = FK/x). Sinken mit steigender Menge.", "WiMa 1 Kap. 1")

add("mawi1",
    "Break-Even-Point bedeutet:",
    ["Punkt maximaler Kosten", "Punkt wo Umsatz = Kosten (Gewinn = 0)", "Punkt minimaler Produktion", "Punkt maximaler Effizienz"],
    1, "Break-Even = Gewinnschwell: Erloes exakt deckt Kosten. Kein Gewinn, kein Verlust.", "WiMa 1 Kap. 1")

add("mawi1",
    "Was ist der Grenzerloes?",
    ["Umsatz pro verkaufter Einheit", "Aenderung des Erloes bei einer zusaetzlichen Einheit", "Durchschnittliche Eroese", "Maximaler Eroes"],
    1, "Grenzerloes = Ableitung der Eroesfunktion E'(x). Zeigt Veraenderung bei einer zusaetzlichen Einheit.", "WiMa 1 Kap. 1")

add("mawi1",
    "Was ist eine 'ertragsgesetzliche Kostenfunktion'?",
    ["Quadratischer Term", "Grenzkosten erst steigen dann fallen", "Lineare Kostenfunktion", "Kostenfunktion ohne Fixkosten"],
    0, "Ertragsgesetzlich: K(x) = ax^3 + bx^2 + cx + d. Beschreibt Kostenverhalten nach Ertragsgesetzen.", "WiMa 1 Kap. 2")

add("mawi1",
    "Was ist der Grenzgewinn?",
    ["Gewinn pro verkaufter Einheit", "Aenderung des Gewinns bei einer zusaetzlichen Einheit", "Maximaler Gewinn", "Durchschnittlicher Gewinn"],
    1, "Grenzgewinn = G'(x) = E'(x) - K'(x). Zeigt wie sich Gewinn bei einer zusaetzlichen Einheit aendert.", "WiMa 1 Kap. 1")

add("mawi1",
    "Was ist eine Nachfragefunktion?",
    ["Kosten pro Einheit", "Menge die bei einem bestimmten Preis nachgefragt wird", "Umsatz pro Monat", "Produktionsmenge"],
    1, "Nachfragefunktion q(p): wie viel von einem Gut nachgefragt wird bei Preis p. Typisch: p(x) = a - bx.", "WiMa 1 Kap. 1")

add("mawi1",
    "Bei welcher Produktionsmenge wird Gewinn maximal wenn E(x)=3x und K(x)=1,5x+900?",
    ["x=300", "x=600", "x=150", "x=900"],
    1, "G(x) = 3x - 1,5x - 900 = 1,5x - 900. Break-Even bei x=600 (G(600)=0).", "WiMa 1 Kap. 1")

add("mawi2",
    "Was besagt das 'Gesetz vom Gegenteil' in der Statistik?",
    ["h(X in B) = h(X nicht in B)", "h(X in B) = 1 - h(X nicht in B)", "h(X in B) = h(X in B)^2", "h(X in B) = N / h(X nicht in B)"],
    1, "Regel vom Gegenteil: h(X in B) = 1 - h(X nicht in B). Z.B. 70% juenger als 42 = 30% mindestens 42.", "Statistik Kap. 2")

add("mawi2",
    "Was ist die Additionsregel?",
    ["h(A U B) = h(A) + h(B)", "h(A U B) = h(A) + h(B) - h(A n B)", "h(A U B) = h(A) * h(B)", "h(A U B) = max(h(A), h(B))"],
    1, "Addition: h(A U B) = h(A) + h(B) - h(A n B). Schnitt abziehen gegen Doppelzaehlung.", "Statistik Kap. 2")

add("mawi2",
    "Was ist der optimale Lageparameter bei quadrierten Abweichungen?",
    ["Median", "Modus", "Arithmetisches Mittel", "Spannweite"],
    2, "Arithmetisches Mittel minimiert Summe der quadrierten Abweichungen. Median minimiert absolute Abweichungen.", "Statistik Kap. 4")

add("mawi2",
    "Was ist der optimale Lageparameter bei absoluten Abweichungen?",
    ["Arithmetisches Mittel", "Geometrisches Mittel", "Harmonisches Mittel", "Median"],
    3, "Median minimiert Summe der absoluten Abweichungen |xi - c|.", "Statistik Kap. 4")

add("mawi2",
    "Unterschied zwischen diskreten und stetigen Variablen?",
    ["Diskrete = unendlich viele Werte, stetige = endlich", "Diskrete = abzaehlbare Werte (Anzahl), stetige = unendlich in Intervall", "Kein Unterschied", "Diskrete immer groesser"],
    1, "Diskret: abzaehlbare Werte (0,1,2,...). Stetig: beliebige Werte in Intervall (z.B. 1,23 kg).", "Statistik Kap. 2")

add("mawi2",
    "Was ist 'Normierung' in der Statistik?",
    ["h(X in B) = 0", "h(X in B) = 1", "Summe aller h(x) = 1", "h(X in B) = N"],
    2, "Normierung: Summe aller Haeufigkeiten ueber alle moeglichen Werte muss immer 1 ergeben (100%).", "Statistik Kap. 2")

add("mawi2",
    "Was ist der 'Preisindex nach Laspeyres'?",
    ["Wert Berichtsmengen zu Basispreisen / Wert Basismengen zu Basispreisen", "Wert Basismengen zu Berichtspreisen / Wert Basismengen zu Basispreisen", "Wert Berichtsmengen zu Berichtspreisen / Wert Basismengen zu Berichtspreisen", "Wert Basismengen zu Berichtspreisen / Wert Berichtsmengen zu Basispreisen"],
    1, "Laspeyres: PL = Summe(p(t)*q(t0)) / Summe(p(t0)*q(t0)). Mengen der Basisperiode bleiben konstant.", "Statistik Kap. 6")

add("mawi2",
    "Was ist 'Deflationierung'?",
    ["Preissteigerung berechnen", "Nominalen Wert durch Preisindex teilen fuer realen Wert", "Mengen indexieren", "Umsatz berechnen"],
    1, "Realer Wert = Nominaler Wert / Preisindex. Nominal gemessene Groessen auf einheitliches Preisniveau.", "Statistik Kap. 6")

add("mawi2",
    "Was beschreibt die 'Varianz'?",
    ["Durchschnittliches Merkmal", "Ausmass der Streuung um den Mittelwert", "Haeufigster Wert", "Mittlerer Wert"],
    1, "Varianz = sigma^2 = (1/N)*Summe(xi - x_bar)^2. Misst mittlere quadratische Abweichung = Streuung.", "Statistik Kap. 5")

add("mawi2",
    "Unterschied zwischen absoluter und relativer Streuung?",
    ["Absolute in Euro, relative in Prozent", "Absolute in Maßeinheit, relative dimensionslos (z.B. VK)", "Kein Unterschied", "Relative immer groesser"],
    1, "Absolute (Varianz, StdAbw) = Einheit des Merkmals. Relative (VK = sigma/mu) = dimensionslos, vergleichbar.", "Statistik Kap. 5")

add("mawi2",
    "Was ist der Laspeyres-Mengenindex?",
    ["Wert Basismengen zu Berichtspreisen / Wert Basismengen zu Basispreisen", "Wert Berichtsmengen zu Basispreisen / Wert Basismengen zu Basispreisen", "Wert Berichtsmengen zu Berichtspreisen / Wert Basismengen zu Berichtspreisen", "Wert Basismengen zu Berichtspreisen / Wert Berichtsmengen zu Basispreisen"],
    1, "Laspeyres-Mengenindex: QL = Summe(p(t0)*q(t)) / Summe(p(t0)*q(t0)). Preise der Basisperiode bleiben konstant.", "Statistik Kap. 6")

add("mawi2",
    "Was ist der 'Variationskoeffizient' (VK)?",
    ["Varianz / Mittelwert", "Standardabweichung / Mittelwert", "Mittlere Abweichung / Varianz", "Spannweite / Standardabweichung"],
    1, "VK = sigma / x_bar (dimensionslos). Erlaubt Vergleich der Streuung bei unterschiedlichen Skalen.", "Statistik Kap. 5")

add("mawi2",
    "Was ist ein 'Histogramm'?",
    ["Saeulendiagramm fuer diskrete Merkmale", "Flaechendiagramm fuer stetige Merkmale mit Klassenbreite", "Kreisdiagramm", "Liniendiagramm"],
    1, "Histogramm: Flaeche = Haeufigkeit (Flaechenprinzip). Klassenbreite kann variieren.", "Statistik Kap. 2")

add("mawi2",
    "Was ist die 'Dichtefunktion' f(x)?",
    ["Relative Haeufigkeit", "Hoehe des Rechtecks im Histogramm", "Kumulierte Haeufigkeit", "Summe aller Haeufigkeiten"],
    1, "Dichte = Hoehe des Rechtecks. kann Werte > 1 annehmen. Flaeche = Haeufigkeit.", "Statistik Kap. 2")

add("mawi2",
    "Was ist ein 'Quantil'?",
    ["Haeufigster Wert", "Wert der ein bestimmtes Prozent der Daten teilt", "Mittelwert", "Spannweite"],
    1, "p-Quantil xp: h(X <= xp) >= p und h(X >= xp) >= 1-p. Median = 0.5-Quantil.", "Statistik Kap. 4")

# Speichern
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(QS, f, ensure_ascii=False, indent=2)

print("NEUE FRAGEN HINZUGEFUEGT:")
for bank in QS:
    print(f"  {bank}: {len(QS[bank])} Fragen")
total = sum(len(v) for v in QS.values())
print(f"\nTOTAL: {total} Fragen")
