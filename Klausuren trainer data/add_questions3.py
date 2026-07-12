"""Fuegt 21 neue Fragen fuer schwache Themen hinzu."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "_data", "questions_validated.json")

with open(PATH, "r", encoding="utf-8") as f:
    QS = json.load(f)

def add(bank, q, opts, correct_idx, solution, source):
    QS[bank].append({"q": q, "o": opts, "c": correct_idx, "s": solution, "src": source})

# ============================================================
# BWL1 - Unternehmenstypologie (3)
# ============================================================
add("bwl1",
    "Welches Kriterium wird NICHT als Unterscheidungskriterium fuer Unternehmenstypologien genannt?",
    ["Branche", "Betriebsgroesse", "Guendungsjahr", "Art der Leistungserstellung"],
    2, "Die 5 Kriterien: Branchen, Art der Leistungserstellung, vorherrschender Produktionsfaktor, Betriebsgroesse, Leitungs-/Eigentumsstruktur. Guendungsjahr ist keines davon.", "Folienskript Chwallek Kap. 2.6")

add("bwl1",
    "Was beschreibt der Begriff 'Hidden Champions'?",
    ["Unbekannte aber grosse Unternehmen", "Kleine aber bekannte Unternehmen", "Innovative, auf Marktnische spezialisierte Weltmarktfuehrer", "Unternehmen mit Einheit von Management und Eigentum"],
    2, "Hidden Champions (Simon 2005): besonders innovative Unternehmen, die Weltmarktfuehrer in ihrer Nische sind (z.B. Duerr AG, Kaercher, Recaro).", "Folienskript Chwallek Kap. 2.6")

add("bwl1",
    "In welcher Phase des Phasenmodells liegt der Schwerpunkt der klassischen BWL?",
    ["Gruendung", "Entwicklung", "Krise", "Aufloesung"],
    1, "Die klassische BWL befasst sich hauptsaechlich mit der Entwicklungsphase eines Unternehmens.", "Folienskript Chwallek Kap. 2.6")

# ============================================================
# BWL1 - Unternehmensverbindungen (3)
# ============================================================
add("bwl1",
    "Was ist der Unterschied zwischen horizontalem und vertikalem Zusammenschluss?",
    ["Horizontal: Vereinigung auf gleicher Produktionsstufe; Vertikal: aufeinanderfolgende Stufen", "Horizontal: unterschiedliche Branchen; Vertikal: gleiche Stufe", "Horizontal: kurzfristig; Vertikal: dauerhaft", "Horizontal: freiwillig; Vertikal: erzwungen"],
    0, "Horizontaler Zusammenschluss = Vereinigung auf gleicher Stufe (z.B. Walzwerke). Vertikal = aufeinanderfolgende Stufen (Sicherung Rohstoff/Absatz).", "Folienskript Chwallek Kap. 3.3")

add("bwl1",
    "Welche Beteiligungsquote berechtigt zu Satzungsaeenderungen?",
    ["25-50% (Sperrminoritaet)", "50-75% (einfache Mehrheitsbeteiligung)", "75-100% (qualifizierte Mehrheitsbeteiligung)", "Ueber 95% (Squeeze Out)"],
    2, "Qualifizierte Mehrheitsbeteiligung (75-100%) ermoeglicht Satzungsaeenderungen. Ab 95%: Squeeze Out (Herausdrängung).", "Folienskript Chwallek Kap. 3.3")

add("bwl1",
    "Was gilt beim Kartellverbot nach 1 GWB?",
    ["Alle Kartelle erlaubt", "Verboten, mit Ausnahmen (Mittelstandskartelle)", "Nur verboten wenn Preise erhoeht werden", "Seit 2005 Genehmigungspflicht"],
    1, "Kartelle grundsatzlich verboten. Ausnahmen: Mittelstandskartelle, Rationalisierungskartelle, Normierungskartelle.", "Folienskript Chwallek Kap. 3.3")

# ============================================================
# BWL1 - Entscheidungsmodelle (3)
# ============================================================
add("bwl1",
    "Welches Modell ist ein qualitatives Entscheidungsmodell zur Standortwahl?",
    ["Partialmodell (Transportkosten)", "Totalmodell (Kapitalrentabilitaet)", "Nutzwertanalyse (Scoring-Modell)", "Lineare Programmierung"],
    2, "Nutzwertanalyse = qualitativ. Partialmodell und Totalmodell sind quantitativ.", "Folienskript Chwallek Kap. 2.5")

add("bwl1",
    "Was ist der erste Schritt bei einer Nutzwertanalyse zur Standortwahl?",
    ["Gewichtung der Standortfaktoren", "Bewertung durch Punktzahlen", "Bestimmen der Alternativen (Standorte)", "Bildung des Gesamtnutzenwerts"],
    2, "Reihenfolge: 1. Alternativen bestimmen, 2. Faktoren sammeln, 3. Gewichtung, 4. Bewertung, 5. Gesamtnutzwert.", "Folienskript Chwallek Kap. 2.5")

add("bwl1",
    "Welches Problem hat das Totalmodell zur Standortwahl?",
    ["Beruecksichtigt nur Transportkosten", "Sehr vage, da Kapitalrendite schwer abshaetzbar und zu viele Einflussfaktoren", "Nur fuer Logistikunternehmen", "Erfordert immer Nutzwertanalyse"],
    1, "Totalmodell vergleicht Kapitalrentabilitaet je Standort, ist aber vage weil Rendite (R) schwer abshaetzbar ist.", "Folienskript Chwallek Kap. 2.5")

# ============================================================
# BWL1 - Standortwahl (3)
# ============================================================
add("bwl1",
    "Welcher Standortfaktor ist KEIN inputorientierter Faktor?",
    ["Materialtransportkosten (Lieferantennaehe)", "Co-Working-Space fuer Start-Up", "Nahe zu Entsorgungsunternehmen", "Wahl der Innenstadt fuer Einkaufszentrum (Kundennaehe)"],
    3, "Inputorientiert = Leistungsprozess (Material, Personal, Energie). Innenstadt = outputorientiert (Kundennaehe).", "Folienskript Chwallek Kap. 3.1")

add("bwl1",
    "Was gilt zur Gewerbesteuer als Standortfaktor?",
    ["Hoeherer Hebesatz = profitabler", "Hoeherer Hebesatz = hoeherer Steuerbetrag", "Messbetrag ist jedes Unternehmen gleich", "Hebesatz ist in jeder Kommune gleich"],
    1, "GewSt-Hebesatz wird von Kommunen festgelegt (Bundesdurchschnitt 435%). Hoeherer Hebesatz = hoehere Belastung.", "Folienskript Chwallek Kap. 3.1")

add("bwl1",
    "Welche Kategorien von Standortfaktoren unterscheidet das Folienskript?",
    ["Oekologisch, sozial, oekonomisch", "Inputorientiert, outputorientiert, abgabenbezogen", "Hart und weich", "Kurzfristig und langfristig"],
    1, "3 Hauptkategorien: Inputorientiert (Leistungsprozess), Outputorientiert (Absatz/Verkauf), Abgabenbezogen (gesetzlich).", "Folienskript Chwallek Kap. 3.1")

# ============================================================
# BWL2 - Grundlagen Buchfuehrung (3)
# ============================================================
add("bwl2",
    "Ab welchem Umsatz liegt Buchfuehrungspflicht nach HGB vor?",
    ["200.000 EUR Umsatz + 20.000 EUR Gewinn", "600.000 EUR Umsatz + 60.000 EUR Gewinn", "1.000.000 EUR Umsatz + 100.000 EUR Gewinn", "500.000 EUR Umsatz + 50.000 EUR Gewinn"],
    1, "Nach 240 HGB: Buchfuehrungspflicht ab 600.000 EUR Umsatz ODER 60.000 EUR Gewinn (2 auf 3 Jahre).", "Foliensatz BUF Kap. 1-3, Buchfuehrungspflicht")

add("bwl2",
    "Was ist das Gliederungsprinzip im Kontenrahmen?",
    ["Sortierung nach Kontonummer", "Prozessgliederung (Beschaffung, Produktion, Absatz, Verwaltung)", "Nach Rechtsformen", "Nach Gueterarten"],
    1, "Kontenrahmen nach IKR gliedert nach Prozess: Beschaffung, Produktion, Absatz, allgemeine Verwaltung.", "Foliensatz BUF Kap. 1-3, Kontenrahmen")

add("bwl2",
    "Zu welchen Kontenklassen gehoeren Bestands-, Erfolgs- und Abschlusskonten im IKR?",
    ["0-2 Bestands-, 3-6 Erfolgs-, 7-8 Abschlusskonten", "0-3 Bestands-, 4-7 Erfolgs-, 8 Abschlusskonten", "1-4 Bestands-, 5-7 Erfolgs-, 9 Abschlusskonten", "0-2 Bestands-, 3-5 Erfolgs-, 6-9 Abschlusskonten"],
    1, "IKR: Klasse 0-3 Bestandskonten, Klasse 4-7 Erfolgskonten, Klasse 8 Abschlusskonten (GuV, Eigenkapital).", "Foliensatz BUF Kap. 1-3, IKR")

# ============================================================
# BWL2 - Erfolgskonten & GuV (3)
# ============================================================
add("bwl2",
    "Was bedeutet 'doppelte Buchfuehrung'?",
    ["Jede Buchung wird doppelt getaetigt", "Doppelte Erfolgsermittlung (Saldierungs- und Bruttoprinzip)", "Buchung auf zwei Bankkonten", "Doppelte Inventur"],
    1, "Doppelte Buchfuehrung = doppelte Erfolgsermittlung: Bruttoprinzip (Ertrag/Aufwand) und Saldierungsprinzip (GuV-Ermittlung).", "Foliensatz BUF Kap. 8-9, doppelte Buchfuehrung")

add("bwl2",
    "Was ist die Abschlussbuchung des GuV-Kontos bei Gewinn (Habenueberschuss)?",
    ["Soll GuV / Haben Eigenkapital", "Soll Eigenkapital / Haben GuV", "Soll GuV / Haben Bank", "Soll Aufwand / Haben Ertrag"],
    0, "GuV-Konto wird auf Eigenkapital abgeschlossen: GuV (Soll) an Eigenkapital (Haben) = Gewinn erhoeht Eigenkapital.", "Foliensatz BUF Kap. 8-9, Abschlussbuchung")

add("bwl2",
    "Was besagt der Grundsatz 'Keine Buchung ohne Beleg'?",
    ["Buchungen sind optional", "Jede Buchung muss durch einen Beleg nachweisbar sein", "Nur Bareinzahlungen brauchen Belege", "Belege muessen digital sein"],
    1, "Grundsatz ordnungsmaessiger Buchfuehrung (GOB): Keine Buchung ohne GuV-beachtlichen Beleg (Rechnung, Quittung, Vertrag).", "Foliensatz BUF Kap. 1-3, GOB")

# ============================================================
# WPR - Einfuehrung ins Recht (3)
# ============================================================
add("wpr",
    "Was ist ein Anspruch nach 194 I BGB?",
    ["Ein Wunsch gegenueber einem Dritten", "Das Recht, von einem anderen ein Tun oder Unterlassen zu verlangen", "Eine gesetzliche Pflicht", "Ein vertragliches Versprechen"],
    1, "194 I BGB: Anspruch ist das Recht, von einem anderen ein Tun oder Unterlassen zu verlangen (z.B. Kaufpreisanspruch, Rueckforderungsanspruch).", "WPR Foliensatz Kap. 1, Anspruch")

add("wpr",
    "In welche 5 Buecher ist das BGB gegliedert?",
    ["Allgemeiner Teil, Sachenrecht, Schuldrecht, Familienrecht, Erbrecht", "Allgemeiner Teil, Schuldrecht, Sachenrecht, Familienrecht, Erbrecht", "Schuldrecht, Sachenrecht, Allgemeiner Teil, Familienrecht, Erbrecht", "Allgemeiner Teil, Familienrecht, Sachenrecht, Schuldrecht, Erbrecht"],
    1, "BGB-Aufbau: 1. Allgemeiner Teil (1-240), 2. Schuldrecht (241-853), 3. Sachenrecht (854-1296), 4. Familienrecht (1297-1921), 5. Erbrecht (1922-2385).", "WPR Foliensatz Kap. 1, BGB-Aufbau")

add("wpr",
    "Was ist der Unterschied zwischen oeffentlichem Recht und Privatrecht?",
    ["Kein Unterschied", "Oeffentliches Recht: Staat zu Buerger; Privatrecht: Buerger zu Buerger", "Oeffentliches Recht gilt nur fuer Unternehmen", "Privatrecht gilt nur im Ausland"],
    1, "Oeffentliches Recht = Ueber-/Unterordnungsverhaeltnis (Staat-Buerger). Privatrecht = Gleichordnungsverhaeltnis (Buerger-Buerger). WPR = Privatrecht mit Wirtschaftsbezug.", "WPR Foliensatz Kap. 1, Rechtsgebiete")

# Speichern
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(QS, f, ensure_ascii=False, indent=2)

print("NEUE FRAGEN HINZUGEFUEGT:")
for bank in QS:
    print(f"  {bank}: {len(QS[bank])} Fragen")
total = sum(len(v) for v in QS.values())
print(f"\nTOTAL: {total} Fragen")
