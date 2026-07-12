"""Fuegt 40 neue BWL Fragen hinzu."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "_data", "questions_validated.json")

with open(PATH, "r", encoding="utf-8") as f:
    QS = json.load(f)

def add(bank, q, opts, correct_idx, solution, source):
    QS[bank].append({"q": q, "o": opts, "c": correct_idx, "s": solution, "src": source})

# ============================================================
# BWL1 (28 Fragen)
# ============================================================
add("bwl1",
    "Was ist der zentrale Ausgangspunkt der Betriebswirtschaftslehre?",
    ["Gewinnmaximierung", "Tatbestand der Gueterknappheit", "Globalisierung der Maerkte", "Digitalisierung"],
    1, "BWL hat Gueterknappheit als Ausgangspunkt: Wirtschaften = Disponieren ueber knappe Gueter.", "Folienskript Chwallek Kap. 1.1")

add("bwl1",
    "Wie unterscheiden sich knappe von freien Guetern?",
    ["Knappe Gueter von der Natur in ausreichender Menge", "Freie Gueter muessen bewirtschaftet werden", "Knappe Gueter stehen nicht in erforderlicher Qualitaet/Menge/Ort/Zeit zur Verfuegung", "Freie Gueter sind immateriell"],
    2, "Knappe Gueter (Wirtschaftsgueter) stehen nicht ausreichend zur Verfuegung. Freie Gueter: unbegrenzt.", "Folienskript Chwallek Kap. 1.1")

add("bwl1",
    "Nach welchem Kriterium werden Gueter in Produktions- und Konsumgueter unterteilt?",
    ["Dauer der Nutzung", "Art der Beduerfnisbefriedigung (Verwendungszweck)", "Stellung im Produktionsprozess", "Materielle Substanz"],
    1, "Produktionsgueter (Werkzeuge) = indirekt, Konsumgueter (Schuhe) = direkt fuer Beduerfnisbefriedigung.", "Folienskript Chwallek Kap. 1.1")

add("bwl1",
    "Was besagt das Maximalprinzip?",
    ["Eingesetzte Mittel fuer bestimmtes Ertragsniveau gering halten", "Mit vorgegebenen Mitteln maximalen Ertrag erzielen", "Menschen in den Mittelpunkt stellen", "Umweltbelastungen minimieren"],
    1, "Maximalprinzip: Bei gegebenem Input maximalen Output erreichen. Minimalprinzip: Input bei gegebenem Output minimieren.", "Folienskript Chwallek Kap. 1.1.1")

add("bwl1",
    "Welche drei Prinzipien bilden das 'Magische Dreieck der BWL'?",
    ["Gewinn, Umsatz, Marktanteil", "Wirtschaftlichkeit, Humanitaet, Ressourcenschonung", "Effizienz, Effektivitaet, Innovation", "Kosten, Qualitaet, Zeit"],
    1, "Magisches Dreieck: Wirtschaftlichkeit, Humanitaet, Ressourcenschonung - teilweise gegenlaeufig.", "Folienskript Chwallek Kap. 1.1.2")

add("bwl1",
    "Was ist das Hauptmerkmal von CSR?",
    ["Schnelle Umsatzsteigerung", "Gleichbehandlung von Oekonomie, Oekologie und Sozialem", "Maximierung des Shareholder Value", "Ausschliessliche Profitfokussierung"],
    1, "CSR = Oekonomie, Oekologie, Soziales gleich behandeln. Kein Greenwashing.", "Folienskript Chwallek Kap. 1.1.3")

add("bwl1",
    "Was ist das zentrale Merkmal eines Betriebs?",
    ["Gewinnmaximierung", "Fremdbedarfsdeckung", "Oertliche Gebundenheit", "Unbeschraenkte Haftung"],
    1, "Betrieb = planvoll organisierte Wirtschaftseinheit. Zentral: Fremdbedarfsdeckung.", "Folienskript Chwallek Kap. 1.2")

add("bwl1",
    "Was ist der Unterschied zwischen Unternehmen und Betrieb?",
    ["Unternehmen oertlich gebunden, Betrieb nicht", "Betrieb ist rechtliche Einheit", "Unternehmen = wirtschaftlich-finanzielle und rechtliche Einheit, Betrieb = planvoll organisierte Wirtschaftseinheit", "Synonyme Begriffe"],
    2, "Unternehmung: erwerbswirtschaftlich, oertlich nicht gebunden, rechtlich. Betrieb: planvoll organisiert.", "Folienskript Chwallek Kap. 2.1")

add("bwl1",
    "Zu welcher Gruppe gehoeren Lieferanten?",
    ["Interne Anspruchsgruppen", "Externe Anspruchsgruppen", "Keine Anspruchsgruppen", "Weder intern noch extern"],
    1, "Lieferanten = extern. Intern: Eigentuemer, Management, Mitarbeiter.", "Folienskript Chwallek Kap. 2.3")

add("bwl1",
    "Welche Produktionsfaktoren sind 'Elementarfaktoren'?",
    ["Leitung, Planung, Organisation, Kontrolle", "Ausfuehrende Arbeit, Betriebsmittel, Werkstoffe", "Eigenkapital und Fremdkapital", "Personal-, Material-, Maschinenkosten"],
    1, "Elementarfaktoren: ausfuehrende Arbeit (Leistungsfaehigkeit + -wille), Betriebsmittel, Werkstoffe.", "Folienskript Chwallek Kap. 2.4")

add("bwl1",
    "Wie berechnet sich die Arbeitsproduktivitaet?",
    ["Einsatzmenge / Ausbringungsmenge", "Ausbringungsmenge / Arbeitsstunden", "Gewinn / Eingesetztes Kapital", "Ausbringungsmenge in GE / Einsatzmenge in GE"],
    1, "Arbeitsproduktivitaet = Ausbringungsmenge / Arbeitsstunden (bzw. Ma als VZA).", "Folienskript Chwallek Kap. 2.5.1")

add("bwl1",
    "Unterschied Produktivitaet und Wirtschaftlichkeit?",
    ["Produktivitaet wertmaeessig, Wirtschaftlichkeit mengenmaeessig", "Produktivitaet mengenmaeessig, Wirtschaftlichkeit wertmaeessig", "Produktivitaet beruecksichtigt Kosten, Wirtschaftlichkeit nicht", "Gleiche Begriffe"],
    1, "Produktivitaet = mengenmaeessig (Output/Input). Wirtschaftlichkeit = wertmaeessig (GE).", "Folienskript Chwallek Kap. 2.5")

add("bwl1",
    "Was ist die Rentabilitaetsformel?",
    ["Ausbringungsmenge / Einsatzmenge", "Gewinn / Umsatz", "Gewinn / Eingesetztes Kapital", "Umsatz / Eingesetztes Kapital"],
    2, "Rentabilitaet = Gewinn / Eingesetztes Kapital. Misst Verhaeltnis von Gewinn zu Kapital.", "Folienskript Chwallek Kap. 2.5.3")

add("bwl1",
    "EU-Definition 'Kleinunternehmen'?",
    ["Bis 9 MA, bis 2 Mio EUR Bilanz/Umsatz", "Bis 49 MA, bis 10 Mio EUR", "Bis 249 MA, bis 43/50 Mio EUR", "Bis 250 MA, bis 43/50 Mio EUR"],
    0, "EU: Kleinst bis 9 MA/2 Mio. Klein bis 49 MA/10 Mio. Mittel bis 249 MA/43-50 Mio.", "Folienskript Chwallek Kap. 2.6.2")

add("bwl1",
    "Qualitative Kriterien des deutschen Mittelstands?",
    ["Hoher Umsatz, viele MA, international taetig", "Einheit Eigentum/Fuehrung, langfristige Ausrichtung, praegt durch Unternehmer", "Niedrige Kosten, hohe Produktivitaet", "Oeffentliche Rechtsform, staatliche Foerderung"],
    1, "Mittelstand: Einheit Eigentum+Fuehrung, langfristig, staerke Praegung durch Unternehmer.", "Folienskript Chwallek Kap. 2.6.3")

add("bwl1",
    "Was sind 'Hidden Champions'?",
    ["Grosse Konzerne mit hohem Marktanteil", "Weltmarktfuehrer, innovativ, Marktnische spezialisiert", "Unternehmen die Marktstrategie geheim halten", "KMU nicht an Boerse notiert"],
    1, "Hidden Champions (Simon 2005): innovative Marktnischen-Weltmarktfuehrer (Duerr, Kaercher).", "Folienskript Chwallek Kap. 2.6.3")

add("bwl1",
    "Phasenmodell eines Unternehmens?",
    ["Planung, Durchfuehrung, Kontrolle", "Gruendung, Entwicklung, Krise, Aufloesung", "Idee, Planung, Aufbau, Sanierung", "Wachstum, Stabilitaet, Schrumpfung"],
    1, "Klassisches Phasenmodell: Gruendung, Entwicklung, Krise, Aufloesung.", "Folienskript Chwallek Kap. 2.7")

add("bwl1",
    "Was ist Insolvenz im rechtlichen Sinne?",
    ["Freiwilliger Konkurs", "Bei Zahlungsunfaehigkeit muss beim Amtsgericht angemeldet werden", "Automatische Aufloesung", "GF haftet nicht persoenlich"],
    1, "Zahlungsunfaehigkeit -> Insolvenzanmeldung beim AG. Sonst: Insolvenzverschleppung.", "Folienskript Chwallek Kap. 2.7")

add("bwl1",
    "Was ist der Materialindex und was bedeutet >1?",
    ["Verhaeltnis Gewicht Eingang/Endprodukt; Materialverlust", "Verhaeltnis Materialkosten/Arbeitskosten", "Verhaeltnis Rohstoffpreise/Endproduktpreise", "Verhaeltnis Vorraete/Produktionsmenge"],
    0, "Materialindex = Gewicht Eingang / Gewicht Endprodukt. >1 = Materialverlust bei Verarbeitung.", "Folienskript Chwallek Kap. 3.1.1")

add("bwl1",
    "Kategorien von Standortfaktoren?",
    ["Oekologisch, sozial, oekonomisch", "Inputorientiert, outputorientiert, abgabenbezogen", "Hart und weich", "Regional, national, international"],
    1, "3 Kategorien: Inputorientiert (Leistungsprozess), Outputorientiert (Absatz), Abgabenbezogen (gesetzlich).", "Folienskript Chwallek Kap. 3.1")

add("bwl1",
    "Konkurrenzsuchend vs. konkurrenzmeidend?",
    ["Suchend: tagesbedarf; meidend: aperiodisch", "Suchend: aperiodisch; meidend: tagesbedarf", "Suchend: periodisch; meidend: tagesbedarf", "Kein Unterschied"],
    1, "Konk. suchend: aperiodisch (Mbelhaeuser). Konk. meidend: taeglicher Bedarf (Supermaerkte).", "Folienskript Chwallek Kap. 3.1.2")

add("bwl1",
    "Was ist eine stille Gesellschaft?",
    ["Keine Gescfaefte duerfen getaetigt werden", "Innengesellschaft, stille Gesellschafter beteiligt, Einlage geht in Vermoegen des Inhabers ueber", "Gesellschaft ohne HR-Eintrag, unbeschraenkte Haftung", "Kapitalgesellschaft mit 25.000 EUR"],
    1, "Stille Gesellschaft = Innengesellschaft. Keine Haftung mit Privatvermoegen, kein Geschaeftsfuehrungsrecht.", "Folienskript Chwallek Kap. 3.2.2.1.5")

add("bwl1",
    "Mindestkapital einer GmbH?",
    ["25.000 EUR (je Gesellschafter mind. 100 EUR)", "50.000 EUR", "100.000 EUR", "1 EUR"],
    0, "GmbH: Stammkapital mind. 25.000 EUR, je Gesellschafter mind. 100 EUR.", "Folienskript Chwallek Kap. 3.2.2.2.1")

add("bwl1",
    "Organe einer GmbH?",
    ["Vorstand, Aufsichtsrat, Hauptversammlung", "Geschaeftsfuehrung, Aufsichtsrat (ab MA>500), Gesellschafterversammlung", "Geschaeftsfuehrung, Aufsichtsrat, Gesellschafterversammlung", "Alleiniger GF ohne Ueberwachung"],
    1, "GmbH: GF (Leitung), Aufsichtsrat (ab >500 MA), Gesellschafterversammlung.", "Folienskript Chwallek Kap. 3.2.2.2.1")

add("bwl1",
    "Unterschied Kooperation vs. Konzentration?",
    ["Kooperation: Selbstaendigkeit bleibt; Konzentration: geht verloren", "Kooperation: wirtschaftlich verloren; Konzentration: nicht", "Kooperation nur Kleinunternehmen", "Kein Unterschied"],
    0, "Kooperation: rechtlich+wirtschaftlich selbstaendig. Konzentration: wirtschaftliche Selbst. verloren.", "Folienskript Chwallek Kap. 3.3.4")

add("bwl1",
    "Was ist ein horizontaler Zusammenschluss?",
    ["Aufeinander folgende Produktionsstufen", "Gleiche Produktions-/Handelsstufe", "Unterschiedliche Branchen", "Unterschiedliche Laender"],
    1, "Horizontal: Vereinigung auf gleicher Stufe (z.B. Walzwerke). Vertikal: aufeinander folgende.", "Folienskript Chwallek Kap. 3.3.3")

add("bwl1",
    "Was ist ein Konzern?",
    ["Rechtlich nicht selbstaendiges Unternehmen", "Zusammenschluss rechtlich selbstaendiger Unternehmen unter einheitlicher Leitung (nicht rechtsfaehig)", "Kooperation zwischen Kleinunternehmen", "Joint Venture"],
    1, "Konzern (18 AktG): rechtlich selbstaendig, einheitliche Leitung. Vertrags- oder faktischer Konzern.", "Folienskript Chwallek Kap. 3.3.4.2.2")

add("bwl1",
    "Ab welcher Beteiligungsquote qualifizierte Mehrheitsbeteiligung?",
    ["25%", "50%", "75%", "95%"],
    2, "75-100% = qualifizierte Mehrheit (Satzungsaeenderungen). Squeeze Out ab 95%.", "Folienskript Chwallek Kap. 3.3.4.2")

add("bwl1",
    "Was ist eine strategische Allianz?",
    ["Voruebergehender Verkaufsvertrag", "Kooperationsform die strategische Ausrichtung betrifft, auf Dauer ausgelegt", "Fusion zur Marktdominanz", "Kartell zur Preisabsprache"],
    1, "Strategische Allianz: Kooperation (Selbstaendigkeit bleibt), strategisch, auf Dauer.", "Folienskript Chwallek Kap. 3.3.5")

add("bwl1",
    "Was ist die Nutzwertanalyse?",
    ["Quantitativ exakte Loesung", "Quantitatives Entscheidungsmodell", "Qualitatives Entscheidungsmodell (Scoring-Modell)", "Nur fuer Standortentscheidungen"],
    2, "Nutzwertanalyse = qualitativ (Scoring). Keine exakte Loesung, aber wertvolle Entscheidungshilfe.", "Folienskript Chwallek Kap. 3.1.4")

add("bwl1",
    "Was unterscheidet Freiberufler von Gewerbetreibenden?",
    ["Freiberufler zahlen Gewerbesteuer", "Freiberufler von GewSt befreit, wissenschaftlich/kuenstlerisch/beratend taetig", "Freiberufler muessen beim Gewerbeamt anmelden", "Freiberufler unterliegen Buchfuehrungspflicht nach HGB"],
    1, "Freiberufler (18 EStG): wissenschaftlich/kuenstlerisch, von GewSt befreit.", "Folienskript Chwallek Kap. 3.2.1.1")

add("bwl1",
    "Gewinnaufteilung bei OHG ohne abweichende Vereinbarung?",
    ["Gleichmaessig auf alle Gesellschafter", "Nach Gesellschafteranteilen", "Komplett beim Geschaeftsfuehrer", "Nach Koepfen"],
    1, "OHG: Gewinn nach Gesellschafteranteilen. Abweichend im Gesellschaftervertrag moeglich.", "Folienskript Chwallek Kap. 3.2.2.1.3")

add("bwl1",
    "Was charakterisiert eine KG?",
    ["Alle haften unbeschränkt", "Komplementär (unbeschränkt) + Kommanditist (beschränkt)", "Nur Kommanditisten leiten", "Keine Haftungsunterschiede"],
    1, "KG: Komplementäre (unbeschr. Haftung, GF) + Kommanditisten (keine Privathaftung, kein GF-Recht).", "Folienskript Chwallek Kap. 3.2.2.1.4")

add("bwl1",
    "Unterschied Ist-Kaufmann und Kann-Kaufmann?",
    ["Ist freiwillig im HR, Kann muss es", "Ist buchfuehrungspflichtig wegen kaufmaennischer Einrichtung, Kann kann sich freiwillig eintragen", "Ist immer Freiberufler", "Kein Unterschied"],
    1, "Ist-Kaufmann: kaufmaennische Organisation noetig (1 HGB). Kann-Kaufmann: freiwillige HR-Eintragung.", "Folienskript Chwallek Kap. 3.2.1.2")

# ============================================================
# BWL2 (12 Fragen)
# ============================================================
add("bwl2",
    "Nach welchem Gliederungsprinzip ist der IKR aufgebaut?",
    ["Prozessgliederungsprinzip", "Abschlussgliederungsprinzip", "Grundsätze ordnungsmäessiger Buchführung", "Keines davon"],
    1, "IKR = Abschlussgliederungsprinzip: Kontenklassen spiegeln Bilanz und GuV wider.", "Reading-Week 4 - Uebungsaufgaben Kontenrahmen")

add("bwl2",
    "Was gilt fuer Kontenklasse 8 des IKR NICHT?",
    ["Nimmt Abschlussbuchungen aktiver Bestandskonten auf", "Bucht Gewinn/Verlust", "Nimmt Abschlussbuchungen der Erfolgskonten auf", "Werden Eröffnungsbuchungen vorgenommen"],
    3, "Klasse 8 = Abschlussklasse. Eröffnungsbuchungen werden NICHT in Klasse 8 vorgenommen.", "Reading-Week 4")

add("bwl2",
    "Welche Kontenklassen enthalten Bestandskonten?",
    ["Klassen 0-3", "Klassen 0-4", "Klassen 5-7", "Klassen 0-9"],
    0, "Klassen 0-3: Anlagevermoegen, Umlaufvermoegen, Eigenkapital, Fremdkapital.", "Reading-Week 4")

add("bwl2",
    "Buchfuehrungspflicht nach Steuerrecht?",
    ["Ueber 1 Mio EUR Umsatz", "Ueber 600.000 EUR Umsatz ODER 60.000 EUR Gewinn", "Nur Kapitalgesellschaften", "Nur Kaufleute im HR"],
    1, "600.000 EUR Umsatz ODER 60.000 EUR Gewinn (einmalige Ueberschreitung reicht).", "Aufgabensammlung Buchfuehrung")

add("bwl2",
    "Unterschied Inventur und Inventar?",
    ["Inventur = Bestandsnachweis, Inventar = Bestandsaufnahme", "Inventar = Bestandsaufnahme (physisch), Inventur = Aufstellung des Inventars", "Dasselbe", "Inventur = Dokumentation, Inventar = Durchfuehrung"],
    1, "Inventar = physische Zaehlung. Inventur = Aufstellung des Inventars (Bilanzgrundlage).", "Aufgabensammlung Buchfuehrung")

add("bwl2",
    "Vier Bestandteile des gesamten Rechnungswesens?",
    ["FiBu, KiL, Betriebsstatistik, Planungsrechnung", "Grundbuch, Hauptbuch, Nebenbuch, Abschlussbuch", "Bilanz, GuV, Anhang, Lagebericht", "Kasse, Bank, Forderungen, Verbindlichkeiten"],
    0, "FiBu (extern), KiL (intern), Betriebsstatistik, Planungsrechnung.", "Aufgabensammlung Buchfuehrung")

add("bwl2",
    "Buchung: Privatentnahme 300 EUR aus der Kasse?",
    ["Bank an Privat", "Privat an Kasse", "Kasse an Privat", "Privat an Eigenkapital"],
    1, "Entnahme: Privat (Soll) an Kasse (Haben) = Minderung Eigenkapital.", "Reading-Week 5")

add("bwl2",
    "Privatentnahme von Gegenstaenden: Umsatzsteuerpflichtig?",
    ["Keine Buchung noetig", "Ja, umsatzsteuerpflichtig", "Nur Vorsteuer abfuehren", "Gewinn automatisch erhoeht"],
    1, "Entnahme von Gegenstaenden = umsatzsteuerpflichtig. Privat an Entnahme + USt.", "Reading-Week 5")

add("bwl2",
    "Abschluss des Privatkontos zum Bilanzstichtag?",
    ["Eigenkapital an Privat (bei positivem Saldo)", "Privat an Eigenkapital (bei positivem Saldo)", "GuV an Privat", "Privat an GuV"],
    1, "Privat wird ueber Eigenkapital abgeschlossen: Privat (Soll) an Eigenkapital (Haben).", "Reading-Week 5")

add("bwl2",
    "Aufgabe der Finanzbuchhaltung im Rechnungswesen?",
    ["Unabhaengig von anderen", "Liefert Grundlage fuer Kosten- und Leistungsrechnung", "Untergeordnet der Kostenrechnung", "Nur fuer Steuereerklaerung"],
    1, "FiBu = externe Grundlage fuer KiL = internes Rechnungswesen.", "Aufgabensammlung Buchfuehrung")

add("bwl2",
    "Was ist eine Einzelwertberichtigung (EWB)?",
    ["Vollstaendige Abschreibung aller Forderungen", "Abschreibung auf einzelne Forderung bei drohendem Ausfall", "Umwandlung Forderungen in Verbindlichkeiten", "Pauschalabschreibung aller Forderungen"],
    1, "EWB: Einzelne Forderung wird auf niedrigeren Wert abgeschrieben (z.B. Insolvenz 70% Verlust).", "Aufgabensammlung Buchfuehrung")

add("bwl2",
    "Unterschied Regelinsolvenz vs. Eigenverwaltung?",
    ["Regelinsolvenz: GF bleibt", "Eigenverwaltung: Insolvenzverwalter uebernimmt", "Regelinsolvenz: Verwalter uebernimmt; Eigenverwaltung: GF bleibt", "Kein Unterschied"],
    2, "Regelinsolvenz: Verwalter. Eigenverwaltung: GF bleibt, Sachwalter ueberwacht.", "Folienskript Chwallek Kap. 2.7")

add("bwl2",
    "Was ist eine Fusion durch Aufnahme?",
    ["Unternehmen wird neu gegründet", "Unternehmen wird eingegliedert und verliert Rechtspersoenlichkeit", "Zwei Unternehmen gruenden ein drittes", "Minderheitsbeteiligung"],
    1, "Aufnahme: Aufnehmendes Unternehmen behaelt Rechtspersoenlichkeit, uebernommenes verliert sie.", "Folienskript Chwallek Kap. 3.3.4.2.3")

add("bwl2",
    "Was ist der Zweck der Konzernrechnungslegung?",
    ["Steuervermeidung", "Abbildung wirtschaftlicher Lage des gesamten Konzerns ueber rechtliche Grenzen hinaus", "Buchfuehrungspflicht fuer Einzelunternehmen", "Kartellkontrolle"],
    1, "Konzernrechnungslegung: Wirtschaftliche Gesamtsituation ueber rechtliche Grenzen einzelner Unternehmen.", "Folienskript Chwallek Kap. 3.3.4.2.2")

# Speichern
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(QS, f, ensure_ascii=False, indent=2)

print("NEUE FRAGEN HINZUGEFUEGT:")
for bank in QS:
    print(f"  {bank}: {len(QS[bank])} Fragen")
total = sum(len(v) for v in QS.values())
print(f"\nTOTAL: {total} Fragen")
