"""Fuegt 84 neue VWL+WPR Fragen aus MC_Fragen_Extra.md hinzu (47 VWL + 37 WPR)."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "_data", "questions_validated.json")

with open(PATH, "r", encoding="utf-8") as f:
    QS = json.load(f)

def add(bank, q, opts, correct_idx, solution, source):
    QS[bank].append({"q": q, "o": opts, "c": correct_idx, "s": solution, "src": source})

# ============================================================
# VWL Fragen (47 Fragen)
# ============================================================

# VWL Kap. C - Angebot und Nachfrage
add("vwl",
    "Drei Aachener Baeckereien moechten Printen vom Grosshandel beziehen. Welche Nachfragekurve gehoert zu Baeckerei 1?",
    ["Kurve A", "Kurve B", "Kurve C", "Kurve D"],
    1, "Baeckerei 1 hat die steilste Nachfragekurve, da sie die groesste Abhaengigkeit von Printen aufweist.", "VWL Kap. C")

add("vwl",
    "Wie viele Printen wuerde Baeckerei 2 bei einem Preis von 1,20 Euro nachfragen?",
    ["0", "20", "5", "100"],
    2, "Bei 1,20 Euro liegt Baeckerei 2 genau auf dem Punkt ihrer Nachfragekurve mit 5 Einheiten.", "VWL Kap. C")

add("vwl",
    "Aggregieren Sie die Nachfragekurven zur Marktnachfragekurve. Welches Marktgleichgewicht ergibt sich?",
    ["p=0,6 Euro/q=60", "p=0,4 Euro/q=30", "p=0,8 Euro/q=10", "p=1,2 Euro/q=25"],
    0, "Das Marktgleichgewicht ergibt sich am Schnittpunkt der aggregierten Marktnachfrage mit dem Marktangebot.", "VWL Kap. C")

add("vwl",
    "Die Bauern hatten eine ertragreichere Zuckerruebenernte, wodurch der Zuckerpreis sinkt. Was passiert im Angebots-Nachfrage-Diagramm fuer Printen?",
    ["Nachfragekurve verschiebt sich nach links", "Nachfragekurve verschiebt sich nach rechts", "Angebotskurve verschiebt sich nach links", "Angebotskurve verschiebt sich nach rechts"],
    3, "Niedrigere Zuckerpreise senken die Produktionskosten fuer Printen, wodurch sich die Angebotskurve nach rechts verschiebt (Angebotszunahme).", "VWL Kap. C")

add("vwl",
    "Bei sinkendem Zuckerpreis: Was geschieht mit Marktgleichgewichtsmenge und Marktgleichgewichtspreis?",
    ["Groessere GGW-Menge, kleinerer GGW-Preis", "Groessere GGW-Menzaepp, groesserer GGW-Preis", "Kleinere GGW-Menge, kleinerer GGW-Preis", "Kleinere GGW-Menge, groesserer GGW-Preis"],
    0, "Eine Angebotszunahme (Rechtsschiebung) fuehrt zu hoeherer Gleichgewichtsmenge und niedrigerem Gleichgewichtspreis.", "VWL Kap. C")

add("vwl",
    "Der Preis von Lebkuchen (Substitut) sinkt deutlich. Was passiert im Angebots-Nachfrage-Diagramm fuer Printen?",
    ["Nachfrage verschiebt sich nach links", "Nachfrage verschiebt sich nach rechts", "Angebotskurve verschiebt sich nach links", "Angebotskurve verschiebt sich nach rechts"],
    0, "Lebkuchen und Printen sind Substitute. Sinkt der Preis eines Substituts, sinkt die Nachfrage nach dem anderen Gut.", "VWL Kap. C")

add("vwl",
    "Bei sinkendem Lebkuchenpreis: Was geschieht mit Marktgleichgewichtsmenge und -preis?",
    ["Kleinere GGW-Menge, kleinerer GGW-Preis", "Kleinere GGW-Menge, groesserer GGW-Preis", "Groessere GGW-Menge, kleinerer GGW-Preis", "Groessere GGW-Menge, groesserer GGW-Preis"],
    0, "Eine Nachfrageabnahme (Linksschiebung) fuehrt sowohl zu niedrigerer Menge als auch zu niedrigerem Preis.", "VWL Kap. C")

# VWL Kap. D - Effizienz von Maerkten
add("vwl",
    "Fuer den Markt fuer Schokolade mit QD = 5 - 0,5*P und QS = (1/2)*P - 1: Welches ist das Gleichgewicht?",
    ["P*=6 Euro; Q*=2000 Pkg.", "P*=8 Euro; Q*=3000 Pkg.", "P*=2 Euro; Q*=4000 Pkg.", "Keine der anderen Antwortoptionen ist korrekt"],
    0, "Setzt man QD = QS, ergibt sich 5 - 0,5P = 0,5P - 1, also P=6 und Q=2 (in Tausend Pkg.).", "VWL Kap. D")

add("vwl",
    "Wie hoch sind Produzenten- und Konsumentenrente im Gleichgewicht (in Tsd. Euro)?",
    ["PR=KR=4", "PR=KR=8", "PR=KR=9", "Keine der anderen Antwortoptionen ist korrekt"],
    0, "Im linearen Modell ergibt sich jede Rente als Dreiecksflaeche: 0,5 * Basis * Hoehe = 0,5 * 2 * 4 = 4.", "VWL Kap. D")

add("vwl",
    "Kann durch einen Staatseingriff die Gesamtrente im Vergleich zum Marktgleichgewicht erhoht werden?",
    ["Ja, durch Umverteilung der produzierten Schokolade zu anderen Konsumenten", "Ja, durch Produktion einer kleineren Menge", "Ja, durch Produktion einer groesseren Menge", "Nein"],
    3, "Im Marktgleichgewicht ohne Externalitaeten ist die Gesamtrente bereits maximal (First Welfare Theorem).", "VWL Kap. D")

add("vwl",
    "Sehr viele Kaeufer konsumieren Schokolade zusammen mit Marshmallows als S'Mores. Was passiert, wenn der Preis fuer Marshmallows sinkt?",
    ["Nachfrage nach Schokolade steigt, Kurve verschiebt sich nach rechts, Preis steigt", "Nachfrage nach Schokolade sinkt, Kurve verschiebt sich nach links, Preis sinkt", "Marshmallows-Preis hat keinerlei Auswirkung auf den Schokoladenmarkt", "Keine der anderen Antwortoptionen ist korrekt"],
    0, "Marshmallows und Schokolade sind Komplemetaergueter. Sinkt der Preis des einen, steigt die Nachfrage nach dem anderen.", "VWL Kap. D")

add("vwl",
    "Wie veraendern sich Konsumentenrente und Produzentenrente bei sinkendem Marshmallows-Preis?",
    ["P*=5 Euro; Q*=2500 Pkg.; KR und PR steigen", "P*=4 Euro; Q*=2000 Pkg.; KR und PR steigen", "P*=5 Euro; Q*=2500 Pkg.; KR und PR sinken", "P*=4 Euro; Q*=2000 Pkg.; KR und PR sinken"],
    0, "Die Nachfrageschiebung nach rechts erhoeht sowohl Gleichgewichtspreis als auch -menge, wodurch beide Renten steigen.", "VWL Kap. D")

# VWL Kap. E - Preiskontrollen und Steuern
add("vwl",
    "Ein bindender Mindestpreis...",
    ["bewirkt einen Nachfrageueberschuss", "verteilt Wohlfahrt von Produzenten zu Konsumenten um", "ist zum Beispiel der Mindestlohn", "erzeugt keinen Nettowohlfahrtsverlust"],
    2, "Ein bindender Mindestpreis liegt ueber dem Gleichgewichtspreis, z.B. der Mindestlohn am Arbeitsmarkt.", "VWL Kap. E")

add("vwl",
    "Fuer einen Hoechstpreis gilt immer:",
    ["Er bewirkt Nachfrageueberschuss", "Er fuehrt zu anderen Rationierungsmechanismen als dem Preis", "Er erzeugt einen Nettowohlfahrtsverlust", "Er bindet nur, wenn er unter dem Gleichgewichtspreis liegt"],
    3, "Ein Hoechstpreis ist nur dann bindend (wirksam), wenn er unter dem Marktgleichgewichtspreis liegt.", "VWL Kap. E")

add("vwl",
    "Was ist kein Beispiel fuer einen alternativen Rationierungsmechanismus bei Hoechstmiete?",
    ["Wohnung fuer denjenigen, der am meisten Zeit mit Suche verbringt", "Wohnung fuer denjenigen, der am meisten fuer die Kueche zahlt", "Wohnung fuer denjenigen, der keine Kinder mitbringt", "Wohnung fuer denjenigen mit der hoechsten Zahlungsbereitschaft im Markt"],
    3, "Hoechste Zahlungsbereitschaft ist ein Preismechanismus, kein alternativer Rationierungsmechanismus. Bei Hoechstmieten werden z.B. Wartelisten, Beziehungen oder Qualitaetskriterien als Rationierung herangezogen.", "VWL Kap. E")

add("vwl",
    "Was ist falsch: Eine Mengensteuer...",
    ["reduziert die gehandelte Menge", "ist zum Beispiel die Mehrwertsteuer", "bewirkt, dass bestimmte Handelsvorteile nicht mehr realisiert werden", "erzeugt Ineffizienzen"],
    1, "Die Mehrwertsteuer ist eine Wertsteuer (Prozent vom Preis), keine Mengensteuer (Betrag pro Mengeneinheit).", "VWL Kap. E")

add("vwl",
    "Eine Mengensteuer, die beim Verkaeufer erhoben wird:",
    ["wird hauptsaechlich von der elastischeren Marktseite getragen", "wird hauptsaechlich von der unelastischeren Marktseite getragen", "wird zu 100% vom Verkaeufer getragen", "wird zu 100% vom Kaeufer getragen"],
    1, "Die Steuerlast verteilt sich umso staerker auf die unelastischere Marktseite, da diese weniger auf Preisänderungen reagieren kann.", "VWL Kap. E")

add("vwl",
    "Was gilt fuer eine Mengensteuer, die beim Kaeufer erhoben wird?",
    ["Die Steuerlastverteilung aendert sich gegenueber Erhebung beim Verkaeufer", "Die Steuerlastverteilung bleibt identisch zur Erhebung beim Verkaeufer", "Der Verkaeufer traegt immer 100% der Last", "Es entsteht kein Nettowohlfahrtsverlust"],
    1, "Steuerinzidenz ist unabhaengig davon, bei wem die Steuer rechtlich erhoben wird (Inzidenztheorem).", "VWL Kap. E")

# VWL Kap. F - Oeffentliche Gueter und Externalitaeten
add("vwl",
    "In einer Abbildung zur Ausstosznachfrage Deutschlands: Wie viele Mio. Tonnen wuerde Deutschland pro Jahr ausstossen, wenn es umsonst waere CO2 auszustossen?",
    ["80", "1000", "0", "Andere Zahl"],
    1, "Bei Preis null (kostenloser CO2-Ausstoss) wird die gesamte Nachfrage nach CO2-Kapazitaet befriedigt, in diesem Fall 1000 Mio. Tonnen.", "VWL Kap. F")

add("vwl",
    "Wird der Markt ohne Staatseingriff dafuer sorgen, dass die gesellschaftlich optimale Menge an CO2 ausgestossen wird?",
    ["Ja, da eine negative Externalitaet vorliegt", "Ja, da eine positive Externalitaet vorliegt", "Nein, da eine negative Externalitaet vorliegt", "Nein, da eine positive Externalitaet vorliegt"],
    2, "Negative Externalitaeten fuehren zu Uebernutzung (Market Failure), da private Kosten unter sozialen Kosten liegen.", "VWL Kap. F")

add("vwl",
    "Eine Pigousteuer in Hoehe von 20 EUR/Tonne CO2: Handelt es sich um eine Wert- oder Mengensteuer und wie hoch wird der resultierende CO2-Ausstoss?",
    ["Wertsteuer, 250 Mio. Tonnen", "Mengensteuer, 250 Mio. Tonnen", "Wertsteuer, 1000 Mio. Tonnen", "Mengensteuer, 80 Mio. Tonnen"],
    0, "Eine Pigousteuer ist eine Wertsteuer (Betrag pro Einheit). Bei 20 EUR/Tonne ergibt sich ein Ausstoss von 250 Mio. Tonnen.", "VWL Kap. F")

add("vwl",
    "Welche Aussage zur Alternative der Mengenregulierung gegenueber der Pigousteuer ist korrekt?",
    ["Mit Pigousteuer laesst sich leichter eine bestimmte fixe Ausstossmenge erreichen", "Bei Mengenregulierung entstehen Anreize, die Ausstossmenge noch weiter zu reduzieren", "Mengenregulierung ist in der Regel effizienter als Pigousteuer", "Keine der anderen Antwortoptionen ist korrekt"],
    3, "Weder A noch B noch C sind korrekt. Der Zertifikatehandel ist in der Regel effizienter als beide Alternativen.", "VWL Kap. F")

add("vwl",
    "Auf europaeischer Ebene gibt es ein Handelssystem mit Umweltzertifikaten. Welche Aussage ist richtig?",
    ["Mit Mengenregulierung laesst sich leichter eine bestimmte fixe Ausstossmenge erreichen", "Ein Zertifikatesystem ist in der Regel noch effizienter als eine Pigousteuer", "Mit Pigousteuer laesst sich leichter eine bestimmte fixe Ausstossmenge erreichen", "Das europaeische Zertifikatesystem deckt alle Industrien in der EU ab"],
    1, "Zertifikatehandel kombiniert Mengensicherheit (wie Mengenregulierung) mit Kosteneffizienz (wie Pigousteuer).", "VWL Kap. F")

# VWL Kap. G - Handel und Handelsbeschraenkungen
add("vwl",
    "Elfriede braucht 2 Stunden fuer eine Torte und 1 Stunde fuer Eierlikoer. Hartmut braucht 3 Stunden fuer eine Torte und 2 Stunden fuer Eierlikoer. Wer hat einen absoluten Vorteil in der Tortenherstellung?",
    ["Elfriede, da 2 Stunden > 1 Stunde", "Elfriede, da 2 Stunden < 3 Stunden", "Hartmut, da 3 Stunden > 2 Stunden", "Elfriede, da 1 Stunde < 2 Stunden"],
    1, "Absoluter Vorteil bedeutet geringerer Ressourcenverbrauch. Elfriede braucht weniger Zeit (2h < 3h) fuer eine Torte.", "VWL Kap. G")

add("vwl",
    "Was sind Hartmuts Opportunitaetskosten fuer eine Torte?",
    ["3/2 Flaschen Eierlikoer pro Torte", "3/2 Torten pro Flasche Eierlikoer", "2/3 Flaschen Eierlikoer pro Torte", "2/3 Torten pro Flasche Eierlikoer"],
    0, "Hartmut gibt pro Torte 3/2 Flaschen Eierlikoer auf (3h fuer Torte geteilt durch 2h pro Flasche = 3/2).", "VWL Kap. G")

add("vwl",
    "Was sind Elfriedes Opportunitaetskosten fuer Eierlikoer?",
    ["1/2 Torten pro Flasche Eierlikoer", "1/2 Flasche Eierlikoer pro Torte", "2/1 Torten pro Flasche Eierlikoer", "2/1 Flaschen Eierlikoer pro Torte"],
    0, "Elfriede gibt pro Flasche Eierlikoer 1/2 Torte auf (1h fuer Eierlikoer geteilt durch 2h pro Torte = 1/2).", "VWL Kap. G")

add("vwl",
    "Kann Hartmut durch Spezialisierung und Tausch mit Elfriede mehr produzieren? Konkret: Er spezialisiert sich auf Torte und Elfriede produziert eine halbe Torte plus 5 Flaschen Eierlikoer.",
    ["Nein, weil Elfriede nicht genug Torte schafft", "Ja, weil sie in Summe genauso viele Torten, aber eine halbe Flasche Eierlikoer mehr produzieren", "Nein, sie koennen sogar eine ganze Flasche mehr produzieren", "Das kann ohne weitere Informationen nicht beantwortet werden"],
    1, "Bei Spezialisierung auf komparative Vorteile steigt die Gesamtproduktion um eine halbe Flasche Eierlikoer.", "VWL Kap. G")

add("vwl",
    "Was muss fuer den Handelspreis p in Torten pro Flasche Eierlikoer gelten, damit sich Handel fuer beide lohnt?",
    ["1/2 < p < 2/3", "2/3 < p < 1", "p < 1/2", "p > 2/3"],
    0, "Der Preis muss zwischen den Opportunitaetskosten beider Handelspartner liegen: Elfriede (1/2 Torte) < p < Hartmut (3/2 Torte, bzw. 2/3 invers).", "VWL Kap. G")

add("vwl",
    "Punkt A auf der Produktionsmoeglichkeitenkurve (PPK) ist effizient, Punkt B nicht. Punkt C liegt auf der Kurve. Was bedeutet das?",
    ["A ist effizient, B nicht", "B ist effizient, A nicht", "Alle drei Punkte sind effizient", "Kein Punkt ist effizient"],
    0, "Punkte auf der PPK sind effizient (volle Ressourcennutzung), Punkte innerhalb sind nicht effizient.", "VWL Kap. G")

# VWL Kap. H - Bruttoinlandsprodukt
add("vwl",
    "Wie lautet die Gleichung fuer das BIP nach Verwendungsrechnung?",
    ["BIP = C+I+G+Ex-Im", "BIP = C+I+G-Ex+Im", "BIP = C+G+F-Ex+Im", "BIP = C+G+Ex-Im"],
    0, "Verwendungsrechnung: Konsum (C) + Investitionen (I) + Staatsausgaben (G) + Exporte (Ex) - Importe (Im).", "VWL Kap. H")

add("vwl",
    "Wie hoch war das BIP laut Verwendungsrechnung in Deutschland 2019?",
    ["3449,1 Mrd. Euro", "3249,1 Mrd. Euro", "3949,9 Mrd. Euro", "Keine der anderen Antwortoptionen ist korrekt"],
    0, "BIP = 737,4 + 1617,4 - 1417,4 + 1806,9 + 704,5 = 3449,1 Mrd. Euro.", "VWL Kap. H")

add("vwl",
    "Geht die Position 'Handel, Verkehr und Gastgewerbe' (500,8 Mrd. Euro) in die Berechnung des BIP nach Verwendungsrechnung ein?",
    ["Nein, da diese Position zur Entstehungsrechnung gehoert", "Nein, da Handel, Verkehr und Gastgewerbe immer gesondert betrachtet werden", "Ja, da diese Sektoren relevante Teile der Volkswirtschaft sind", "Ja, als eigene Komponente in der Verwendungsrechnung"],
    0, "Die Entstehungsrechnung (Produktionswerte nach Sektoren) ist eine andere Perspektive auf das BIP.", "VWL Kap. H")

add("vwl",
    "Warum werden Importe beim BIP nach Verwendungsrechnung abgezogen?",
    ["Weil Importe zur Entstehungsrechnung gehoeren", "Weil Importe in C+G+I enthalten werden, aber nicht im Inland produziert wurden", "Weil Importe addiert werden muessen, da sie im BIP beruecksichtigt werden", "Weil Exporte abgezogen werden, da diese nicht in Deutschland verwendet werden"],
    1, "Importe sind bereits in C, G und I enthalten, aber da sie nicht inlandische Produktion sind, werden sie herausgerechnet.", "VWL Kap. H")

add("vwl",
    "Die Nettoexporte Deutschlands sind im Vergleich zum Vorjahr gestiegen. Welche der folgenden Aussagen ist falsch?",
    ["Der Aussenbeitrag von Deutschland ist gestiegen", "Hoehere Nettoexporte fuehren immer zu einem hoeheren BIP", "Bei konstanten Exporten koennte dies durch eine Abnahme der Importe verursacht worden sein", "Der Mengenunterschied zwischen Importen und Exporten ist groesser geworden"],
    1, "Nettoexporte koennten aufgrund eines Importrueckgangs gestiegen sein, ohne dass sich das BIP veraendert.", "VWL Kap. H")

add("vwl",
    "Das BIP pro Kopf in Deutschland hat in etwa den Wert...",
    ["eines Einkaufs im Supermarkt", "eines Smartphones", "eines Neuwagens", "eines Kreuzfahrtschiffes"],
    2, "Das deutsche BIP pro Kopf liegt bei ca. 45.000-50.000 Euro, was in etwa dem Wert eines Neuwagens entspricht.", "VWL Kap. H")

add("vwl",
    "Welches ist keine der aequivalenten Perspektiven auf das BIP?",
    ["Entstehungsrechnung", "Verwertungsrechnung", "Verteilungsrechnung", "Verwendungsrechnung"],
    1, "Die drei aequivalenten Perspektiven sind: Entstehungs-, Verteilungs- und Verwendungsrechnung.", "VWL Kap. H")

add("vwl",
    "Bei Beruecksichtigung welcher Position wuerde es zu Doppelzaehlungen in der BIP-Berechnung kommen?",
    ["Produktionsinputs", "Transaktionen auf dem Schwarzmarkt", "Abschreibung", "Produktion in Haushalten"],
    0, "Produktionsinputs (z.B. Stahl fuer Autos) sind bereits im Endprodukt enthalten und wuerden bei erneuter Erfassung doppelt gezählt.", "VWL Kap. H")

# VWL Kap. I - Inflation
add("vwl",
    "Der Verbraucherpreisindex wird verwendet, um...",
    ["die Kaufkraft von Geld ueber Zeit zu vergleichen", "die Kaufkraft von Geld ueber Laender zu vergleichen", "das reale BIP so umzurechnen, dass es ueber Zeit vergleichbar wird", "das nominale BIP so umzurechnen, dass es ueber Laender vergleichbar wird"],
    0, "Der VPI zeigt, wie sich das allgemeine Preisniveau und damit die Kaufkraft des Geldes ueber die Zeit veraendert.", "VWL Kap. I")

add("vwl",
    "Der Verbraucherpreisindex fuers Zieljahr ist...",
    ["Warenkorbpreis Basisjahr / Warenkorbpreis Zieljahr", "Warenkorbpreis Zieljahr / Warenkorbpreis Basisjahr", "Warenkorbpreis Basisjahr / Warenkorbpreis Zieljahr * 100", "Warenkorbpreis Zieljahr / Warenkorbpreis Basisjahr * 100"],
    3, "VPI = (Warenkorbpreis Zieljahr / Warenkorbpreis Basisjahr) * 100. Das Basisjahr hat VPI = 100.", "VWL Kap. I")

add("vwl",
    "Um wie viel Prozent ist das Verbraucherpreisniveau zwischen 2014 (VPI=99,5) und 2019 (VPI=105,3) gestiegen?",
    ["5,8%", "5,3%", "10,53%", "Andere Zahl"],
    0, "(105,3 - 99,5) / 99,5 = 5,8%.", "VWL Kap. I")

add("vwl",
    "Wie hoch war die Inflationsrate im Jahr 2018 (VPI 2017=102; VPI 2018=103,8)?",
    ["3,80%", "1,76%", "1,45%", "Andere Zahl"],
    1, "Inflationsrate = (103,8 - 102) / 102 = 1,76%.", "VWL Kap. I")

add("vwl",
    "Um wie viel Prozent ist der nominale Bierpreis zwischen 2014 (9,90 Euro) und 2019 (11,30 Euro) gestiegen?",
    ["7,85%", "14,14%", "8,40%", "13,57%"],
    1, "(11,30 - 9,90) / 9,90 = 14,14%.", "VWL Kap. I")

add("vwl",
    "Um wie viel Prozent ist der reale Bierpreis (inflationsbereinigt) zwischen 2014 und 2019 gestiegen?",
    ["7,85%", "14,14%", "8,40%", "13,57%"],
    0, "Realer Preis 2014 = 9,90/99,5*100 = 9,9497; Realer Preis 2019 = 11,30/105,3*100 = 10,7312. Steigerung = 10,7312/9,9497 = 1,0785 = 7,85%.", "VWL Kap. I")

add("vwl",
    "In welchem Jahr war der Bierpreis real am niedrigsten (VPI-Basisjahr = 2015)?",
    ["2014", "2016", "2017", "Anderes Jahr"],
    0, "2014 hatte mit 9,9497 Euro den niedrigsten realen Bierpreis.", "VWL Kap. I")

add("vwl",
    "Welche Aussage ueber den Bierpreis ist falsch?",
    ["Der reale Bierpreis ist von Jahr zu Jahr gestiegen", "Die Kaufkraft des Euros sinkt von Jahr zu Jahr", "Der Preisanstieg des Bieres ist nur zum Teil durch Inflation erkaerbar", "Der Verbraucherpreisindex 2014 laesst auf eine Deflation schliessen, da er <100 liegt"],
    3, "VPI < 100 bedeutet nicht Deflation. Es bedeutet nur, dass die Preise im Jahr 2014 unter dem Basisjahr 2015 lagen.", "VWL Kap. I")

add("vwl",
    "Wenn die Geldmenge schneller waechst als das reale BIP, resultiert Inflation. Wie heisst diese Theorie?",
    ["Qualitaetstheorie des Geldes", "Quantitaetstheorie des Geldes", "Qualitaetstheorie der Inflation", "Quantitaetstheorie der Inflation"],
    1, "Die Quantitaetstheorie des Geldes (MV = PY) besagt, dass ein ueberproportionales Geldmengenwachstum Inflation erzeugt.", "VWL Kap. I")

add("vwl",
    "Wie berechnet sich der Realzins?",
    ["Nominalzins + Inflationsrate", "Nominalzins - Inflationsrate", "Nominalzins * Inflationsrate", "Nominalzins / Inflationsrate"],
    1, "Die Fisher-Gleichung: Realzins = Nominalzins - Inflationsrate.", "VWL Kap. I")

# ============================================================
# WPR Fragen (37 Fragen)
# ============================================================

# WPR - Grundlagen und Einfuehrung
add("wpr",
    "Was versteht man unter dem Trennungs- und Abstraktionsprinzip beim Kaufvertrag?",
    ["Kaufvertrag (Verpflichtung) und Uebereignung (Verfuegung) sind rechtlich streng voneinander zu trennen; Fehler des einen beeinflussen die Wirksamkeit des anderen nicht",
     "Kaufvertrag und Uebereignung sind ein einziges Rechtsgeschaeft; ein Fehler macht beides unwirksam",
     "Kaufvertrag bedarf immer der notariellen Beurkundung",
     "Uebereignung erfolgt automatisch mit Vertragsschluss"],
    0, "Trennungsprinzip: Verpflichtungs- und Verfuegungsgeschaeft sind getrennt. Abstraktionsprinzip: Maengel des einen wirken sich nicht auf das andere aus.", "WPR Grundlagen")

add("wpr",
    "Was ist ein 'Anspruch' im Sinne des paragraph 194 I BGB?",
    ["Ein Recht, von einem anderen ein Tun oder Unterlassen zu verlangen", "Eine Verpflichtung, etwas zu tun", "Eine Erlaubnis, etwas zu unterlassen", "Eine Regelung in den AGB"],
    0, "paragraph 194 I BGB definiert einen Anspruch als das Recht, von einem anderen ein Tun oder Unterlassen zu verlangen.", "WPR Grundlagen")

add("wpr",
    "Zu welchen Rechtsgebieten gehoert das Wirtschaftsprivatrecht?",
    ["Oeffentliches Recht", "Privatrecht", "Prozessrecht", "Verfassungsrecht"],
    1, "WPR gehoert zum Privatrecht (neben Arbeitsrecht, Gesellschaftsrecht, Wettbewerbsrecht etc.).", "WPR Grundlagen")

add("wpr",
    "Was sind die drei aequivalenten Rechtsnormen des WPR?",
    ["BGB, HGB, GmbHG", "StGB, AO, VwGO", "GG, EUV, AEUV", "ArbGG, SGB, AsylG"],
    0, "BGB (seit 1900), HGB (seit 1900) und GmbHG (seit 1892) sind die zentralen Rechtsquellen des WPR.", "WPR Grundlagen")

add("wpr",
    "Was ist der Unterschied zwischen Eigentum und Besitz?",
    ["Eigentum ist rechtliche Herrschaftsmacht ueber eine Sache, Besitz ist tatsaechliche Herrschaftsmacht",
     "Eigentum und Besitz sind dasselbe",
     "Besitz ist rechtlicher als Eigentum",
     "Nur bei Grundstuecken gibt es diesen Unterschied"],
    0, "paragraph 903 BGB (Eigentum) vs. paragraph 854 BGB (Besitz): Rechtliche vs. tatsaechliche Herrschaftsmacht ueber eine Sache.", "WPR Grundlagen")

# WPR - Rechtsgeschaeftslehre
add("wpr",
    "Was ist eine Willenserklaerung?",
    ["Die Aeusserung eines privaten Willens, die unmittelbar auf die Herbeifuehrung einer Rechtswirkung gerichtet ist",
     "Ein gerichtlicher Beschluss",
     "Oeffentlich-rechtliche Verordnung",
     "Ein Vertrag zwischen zwei Parteien"],
    0, "Eine Willenserklaerung ist die private Willensaeusserung zur Herbeifuehrung einer Rechtsfolge.", "WPR Rechtsgeschaeftslehre")

add("wpr",
    "K bestellt bei V einen HighPerformance-Verstaerker fuer 1.200 Euro. V hat sich verschrieben und verlangt 2.100 Euro. Wie ist die Rechtslage?",
    ["V ist an sein Angebot zu 1.200 Euro gebunden",
     "V kann sich auf einen unbeachtlichen Irrtum berufen",
     "V kann den Vertrag anfechten wegen Irrtums ueber den Preis",
     "Der Vertrag ist automatisch unwirksam"],
    2, "V kann den Vertrag nach paragraph 119 BGB anfechten, da er sich ueber den wesentlichen Vertragsgegenstand (Preis) geirrt hat.", "WPR Rechtsgeschaeftslehre")

add("wpr",
    "Was ist die 'Sachverhaltsgrafik' in der Fallloesungsskizze?",
    ["Eine graphische Darstellung der Parteien und ihrer Beziehungen",
     "Ein schriftlicher Text ueber den Sachverhalt",
     "Ein Urteil des Gerichts",
     "Ein Formular fuer die Klage"],
    0, "Die Sachverhaltsgrafik stellt die beteiligten Parteien und deren Beziehungen graphisch dar.", "WPR Rechtsgeschaeftslehre")

# WPR - Zugang von Willenserklaerungen
add("wpr",
    "A schickt B einen Kaufvertrag per Brief, den B am selben Abend liest. Am naechsten Tag schickt A einen Widerruf. Wann ist der Widerruf zugegangen?",
    ["Am Tag des Einwurfs",
     "Am Folgetag um 11 Uhr (wenn die Zustellung im Bezirk beendet ist)",
     "Sofort beim Einwurf",
     "Erst wenn B den Brief liest"],
    1, "Zugang setzt voraus, dass der Brief derart in den Machtbereich des Empfaengers gelangt ist, dass unter normalen Umstaenden mit der Kenntnisnahme gerechnet werden kann.", "WPR Willenserkl.")

add("wpr",
    "M wirft sein Kuendigungsschreiben am 30.12. in den Briefkasten des V. Kinder werfen einen Kanonenschlag in den Briefkasten, der den Brief verbrennt. V erfährt erst im neuen Jahr davon. Ist die Kueendigung zugegangen?",
    ["Ja, denn M hat den Brief in den Briefkasten geworfen",
     "Nein, denn der Zugang setzt voraus, dass der Brief nicht untergeht",
     "Ja, aber erst am 01.01.",
     "Nein, Kuendigungen koennen nie per Brief erfolgen"],
    1, "Kein Zugang, da der Brief vollstaendig vernichtet wurde und V keine Kenntnis nehmen konnte.", "WPR Willenserkl.")

# WPR - Auslegung von Willenserklaerungen
add("wpr",
    "G bestellt ein 'Wiener Schnitzel' im Restaurant. G und W gehen davon aus, es sei Schweineschnitzel. Ein Gast weist darauf hin, dass Wiener Schnitzel aus Kalbfleisch sein muesse. Was gilt?",
    ["Massgeblich ist der Erklaerungswortlaut",
     "Massgeblich ist der uebereinstimmende Wille beider Parteien",
     "Der Vertrag ist unwirksam",
     "G kann nur Kalbfleisch verlangen"],
    1, "Bei uebereinstimmendem Wille beider Parteien (beide gingen von Schweinefleisch aus) ist dieser massgeblich, nicht der Erklaerungswortlaut.", "WPR Auslegung")

# WPR - Vertragsschluss
add("wpr",
    "V bietet K ein Buch fuer 15 Euro an. K will annehmen, sendet die Annahme aber erst 4 Wochen spaeter. V hat inzwischen den Preis um 10 Euro erhoeht. Kann K das Buch fuer 15 Euro verlangen?",
    ["Ja, denn V war an sein Angebot gebunden",
     "Nein, denn V hat das Angebot rechtzeitig zurueckgezogen",
     "Nein, denn 4 Wochen ist zu lang fuer eine Annahme",
     "Ja, aber nur wenn K sofort annimmt"],
    2, "Ohne Festlegung einer Annahmefrist gilt die Annahme nur wenn sie 'zeitgerecht' erfolgt. 4 Wochen ist in der Regel zu lang.", "WPR Vertragsschluss")

add("wpr",
    "Was sind die 'essentialia negotii' eines Kaufvertrages?",
    ["Alle Vertragsbestandteile",
     "Die wesentlichen Vertragsbestandteile, die fuer die Bestimmtheit erforderlich sind",
     "Die Nebenabreden",
     "Die AGB"],
    1, "Essentialia negotii sind die wesentlichen Vertragsbestandteile (z.B. Kaufsache und Preis), die fuer die Bestimmtheit erforderlich sind.", "WPR Vertragsschluss")

# WPR - Geschaeftsfuehigkeit
add("wpr",
    "Ein erkennbar 14-jaehriger kauft ohne elterliche Zustimmung ein Rennrad fuer 3.000 Euro. V hat das Rad nicht vorraetig. Die Eltern widersprechen nachtraeglich nicht. Wie ist die Rechtslage?",
    ["Der Vertrag ist wirksam",
     "Der Vertrag ist unwirksam wegen fehlender Geschaeftsfuehigkeit",
     "Der Vertrag ist schwebend unwirksam",
     "Die Eltern koennen den Vertrag genehmigen"],
    2, "Bei beschraenkter Geschaeftsfuehigkeit (paragraph 106 BGB) ist ein Kaufvertrag, der nicht als beneficial einzustufen ist, schwebend unwirksam und bedarf der Genehmigung.", "WPR Geschaeftsf.")

# WPR - AGB-Kontrolle
add("wpr",
    "In den AGB eines Fitnessstudios heisst es: 'Das Mitglied stimmt einer dauerhaften Kameraueberwachung zur Sicherheitserhoehung zu.' Kann diese Klausel nach paragraph 307 BGB unwirksam sein?",
    ["Ja, weil sie vom gesetzlichen Standard abweicht",
     "Nein, weil Sicherheit immer Vorrang hat",
     "Nein, weil es sich um eine freiwillige Zustimmung handelt",
     "Ja, aber nur bei Verbrauchervertraegen"],
    0, "Die Klausel koennte eine unangemessene Benachteiligung nach paragraph 307 BGB darstellen, da sie vom gesetzlichen Datenschutzstandard abweicht.", "WPR AGB")

add("wpr",
    "In den AGB eines Vermieters heisst es: 'Kosten fuer noetige Reparaturen hat der Mieter bis 100 Euro im Einzelfall auf sich zu nehmen.' Ist diese Klausel wirksam?",
    ["Ja, der Vermieter darf Reparaturkosten auf den Mieter abwaeltzen",
     "Nein, denn nach paragraph 535 Abs. 2 BGB ist der Vermieter zur Instandhaltung verpflichtet",
     "Ja, aber nur bei Gewerbemietern",
     "Nein, Mietnebenkosten sind immer unzulaessig"],
    1, "paragraph 535 Abs. 2 BGB: Der Vermieter hat die Mietsache in einem zum vertragsgemaessen Gebrauch geeigneten Zustand zu erhalten. Reparaturen sind seine Pflicht.", "WPR AGB")

add("wpr",
    "In den AGB einer Brauerei heisst es: 'Verletzt der Gastwirt den Bierlieferungsvertrag, kann die Brauerei die Rueckgabe des ueberlassenen Inventars verlangen. Die Bezugsverpflichtung besteht fort.' Ist diese Klausel wirksam?",
    ["Ja, denn die Brauerei hat ein berechtigtes Interesse",
     "Nein, denn sie benachteiligt den Gastwirt unangemessen",
     "Ja, aber nur bei Ausschliesslichkeitsklauseln",
     "Nein, denn Inventar ist immer unentgeltlich"],
    1, "Die Bezugsverpflichtung fortbestehen zu lassen, obwohl das Inventar zurueckgefordert wird, stellt eine unangemessene Benachteiligung nach paragraph 307 BGB dar.", "WPR AGB")

# WPR - Formvorschriften beim Mietvertrag
add("wpr",
    "paragraph 550 BGB bestimmt die Schriftform fuer bestimmte Mietvertraege. Welche Aussage trifft zu?",
    ["Es ist besser fuer den Mieter, einen Vertrag auf bestimmte Zeit abzuschliessen, weil er diesen jederzeit beenden kann",
     "Es ist besser fuer den Mieter, einen Vertrag auf unbestimmte Zeit abzuschliessen, weil er diesen jederzeit beenden kann",
     "Formvorschriften gibt es nur fuer Gewerbemietvertraege",
     "Mietvertraege beduerfen immer der notariellen Beurkundung"],
    1, "Bei unbefristeten Mietvertraegen hat der Mieter das Sonderkuendigungsrecht nach paragraph 580a BGB.", "WPR Formvorschr.")

add("wpr",
    "Wird in den Faellen des paragraph 550 BGB die Schriftform nicht eingehalten:",
    ["Ist der Vertrag nichtig",
     "Ist der Vertrag auf die unbestimmte Zeit geschlossen",
     "Ist der Vertrag auf die bestimmte Zeit von einem Jahr geschlossen",
     "Ist der Vertrag wirksam, aber anfechtbar"],
    1, "paragraph 550 S. 2 BGB: Wird die Form nicht eingehalten, gilt der Vertrag auf unbestimmte Zeit als geschlossen.", "WPR Formvorschr.")

add("wpr",
    "Welche Aussage zum Thema Form bei Mietvertraegen ist korrekt?",
    ["Die Einhaltung der Form ist bei allen Mietvertraegen erforderlich",
     "Die Einhaltung der Form ist bei befristeten Mietverhaeltnissen ueber Bueroeraeume erforderlich",
     "Die Einhaltung der Form ist bei allen Mietverhaeltnissen ueber Grundstuecke erforderlich",
     "Die Einhaltung der Form ist bei unbefristeten Mietverhaeltnissen ueber Wohnraum erforderlich"],
    3, "paragraph 550 BGB: Schriftform ist bei Mietverhaeltnissen ueber mehr als ein Jahr erforderlich, insbesondere bei Wohnraum.", "WPR Formvorschr.")

# WPR - Formvorschriften beim Darlehen
add("wpr",
    "Donald D. benoetigt ein Darlehen von 50.000 Euro. Mickey M. faxt der Bank: 'Uebernehme Buergschaft fuer das Darlehen meines Freundes D in Hoehe von 50.000 Euro.' Das Fax ist handschriftlich verfasst und unterschrieben. M. weigert sich spaeter zu zahlen. Kann die Bank von M. Zahlung verlangen?",
    ["Ja, die Buergschaft ist wirksam zustande gekommen",
     "Nein, denn eine Buergschaft bedarf der Schriftform (paragraph 766 BGB) und ein Telefax genuegt nicht",
     "Ja, denn handschriftliche Form reicht aus",
     "Nein, denn Buergschaften sind immer unwirksam"],
    0, "Eine handschriftlich verfasste und unterschriebene Erklaerung, die per Telefax uebermittelt wird, genuegt der Schriftform des paragraph 766 BGB.", "WPR Formvorschr.")

# WPR - Anfechtung
add("wpr",
    "X tippt bei eBay in Hektik ein Gebot von 14.000 Euro statt 1.400 Euro ein. Das zweithoechste Gebot sind 1.700 Euro. X lehnt Zahlung ab. Zu Recht?",
    ["Ja, denn X hat sich geirrt und kann anfechten",
     "Nein, denn bei eBay ist jedes Gebot bindend",
     "Ja, aber nur wenn er sofort widerspricht",
     "Nein, denn eBay-Gebote sind immer verbindlich"],
    0, "X kann nach paragraph 119 BGB anfechten, da ein wesentlicher Irrtum ueber die Erklaerungshaltung vorliegt.", "WPR Anfechtung")

add("wpr",
    "E raeumt seinen Keller aus und stellt ein altes Bild zum Sperrmuell auf die Strasse ('Aufgabe des Eigentums'). Das Bild ist von der Malerin Karla Klecks, nicht von seiner Tante. A nimmt das Bild mit. Kann E das Bild nach Aufklaerung herausverlangen?",
    ["Ja, denn E hat das Bild nicht aufgeben wollen",
     "Nein, denn E hat das Bild bewusst aufgegeben",
     "Ja, aber nur gegen Schadensersatz",
     "Nein, denn A hat das Bild rechtmaeessig erworben"],
    0, "E kann nach paragraph 119 BGB anfechten, da er sich ueber die Identitaet des Gegenstandes geirrt hat.", "WPR Anfechtung")

add("wpr",
    "V hat bei X eine Buddha-Skulptur fuer 10.000 Euro gekauft und fuer 18.000 Euro an K weiterverkauft. K ficht wegen Irrtums nach paragraph 119 wirksam an. Was kann V als Schadensersatz verlangen?",
    ["Nur die Kosten fuer das Hinbringen (100 Euro)",
     "Die Kosten fuer Hinbringen (100 Euro) und Abholen (50 Euro) = 150 Euro",
     "Den entgangenen Gewinn von 8.000 Euro",
     "Nichts, denn die Anfechtung war wirksam"],
    1, "Bei wirksamer Anfechtung kann V Ersatz der Aufwendungen (negatives Interesse) verlangen: 100 Euro Hinbringen + 50 Euro Abholen.", "WPR Anfechtung")

# WPR - Stellvertretung
add("wpr",
    "K beauftragt X per Email, einen Ford Mustang bis 50.000 Euro zu kaufen. K ruft X an und sagt 'Der Auftrag ist ungueltig', erreicht aber nur die Mailbox. X hoert die Nachricht nicht und kauft einen Mustang fuer 20.000 Euro. K weigert sich zu zahlen. Wie ist die Rechtslage?",
    ["K ist an den Kauf gebunden, da die Vollmacht nicht wirksam widerrufen wurde",
     "K ist nicht gebunden, da er den Widerruf erklaert hat",
     "K ist nur teilweise gebunden",
     "X muss selbst zahlen"],
    0, "Der Widerruf muss zugehen, um wirksam zu werden. Da X die Nachricht nicht gehoert hat, ist die Vollmacht noch wirksam.", "WPR Stellvertretung")

add("wpr",
    "V hat einen Ford Mustang III Turbo (Wert: 12.000 Euro) fuer 20.000 Euro an X (im Namen des K) verkauft. V verlangt von X 8.000 Euro (Differenz Kaufpreis - Wert) bzw. 4.000 Euro (entgangener Gewinn). Zu Recht?",
    ["V kann von X 8.000 Euro verlangen",
     "V kann von X 4.000 Euro verlangen",
     "V kann von X weder 8.000 noch 4.000 Euro verlangen, da X nur Vertreter war",
     "V kann von K 8.000 Euro verlangen"],
    2, "Als Vertreter haftet X nicht persoehnlich, es sei denn, er hat die Vertretung nicht offengelegt (paragraph 164 Abs. 2 BGB).", "WPR Stellvertretung")

# WPR - Verjaehrung
add("wpr",
    "K kauft am 13.12.2020 ein Rennrad fuer 1.500 Euro mit Zahlungsfrist bis 31.01.2021. V vergisst die Rechnung, erinnert sich erst im Dezember 2024. Ist der Anspruch auf Kaufpreiszahlung verjaehrt?",
    ["Ja, die 3-jaehrige Verjaehrungsfrist ist abgelaufen",
     "Nein, denn die Verjaehrung hat erst 2024 begonnen",
     "Nein, denn Verjaehrung gibt es nicht beim Kaufpreis",
     "Ja, aber V kann das Rad zurueckverlangen"],
    0, "Die Verjaehrungsfrist von 3 Jahren (paragraph 195 BGB) begann mit Ablauf des 31.12.2020 und endete am 31.12.2023.", "WPR Verjaehrung")

add("wpr",
    "Wie lang ist die regelmaessige Verjaehrungsfrist nach paragraph 195 BGB?",
    ["1 Jahr", "2 Jahre", "3 Jahre", "5 Jahre"],
    2, "paragraph 195 BGB: Die regelmaessige Verjaehrungsfrist betraegt drei Jahre.", "WPR Verjaehrung")

add("wpr",
    "Wann beginnt die Verjaehrungsfrist nach paragraph 199 BGB?",
    ["Mit Entstehung des Anspruchs",
     "Mit Ablauf des Jahres, in dem der Anspruch entstanden ist und der Glaeubiger Kenntnis erlangt",
     "Mit der ersten Mahnung",
     "Mit der Klageerhebung"],
    1, "paragraph 199 BGB: Verjaehrung beginnt mit Ablauf des Jahres, in dem der Anspruch entstanden ist und der Glaeubiger von den Anspruchsgruenden Kenntnis erlangt.", "WPR Verjaehrung")

add("wpr",
    "K hat den Kaufpreis bezahlt. Die Kettenschaltung zeigt ab Frueling 2022 Maengel. K bringt das Rad am 03.01.2023 zur Nacherfuellung. V meint, der Anspruch sei verjaehrt. Wer hat Recht?",
    ["V hat Recht, die Verjaehrungsfrist von 2 Jahren ist abgelaufen",
     "K hat Recht, die Verjaehrungsfrist von 3 Jahren ist noch nicht abgelaufen",
     "V hat Recht, aber nur bei Gebrauchtwagen",
     "K hat Recht, denn Maengel verjaehren nie"],
    1, "Die Verjaehrungsfrist betraegt 3 Jahre. Bei Maengelbemerkung im Frueling 2022 beginnt die Verjaehrung mit Ablauf des 31.12.2022 und endet am 31.12.2025.", "WPR Verjaehrung")

add("wpr",
    "Bei einem Schadensersatzanspruch wegen beschaedigter Doppelhaushaelfte: Die Verjaehrung des Anspruchs des Y gegen S begann mit Ablauf des... und die Frist betraegt... Jahre.",
    ["31.12.1987; 3 Jahre", "31.12.1985; 3 Jahre", "31.12.1987; 30 Jahre", "23.05.1987; 3 Jahre"],
    0, "Die Verjaehrung begann mit Ablauf des Jahres 1987 (Kenntnis des Schadens), Frist: 3 Jahre.", "WPR Verjaehrung")

# WPR - Sachenrecht
add("wpr",
    "A moechte nach Kanada auswandern und seine Habe an B verkaufen. B verkauft ein Triathlonrad weiter an C fuer 4.000 Euro. A verlangt den Kaufpreis nach paragraph 816 I 1 BGB heraus. Zu Recht?",
    ["Ja, denn B hat ohne Berechtigung ueber eine Sache des A verfuegt",
     "Nein, denn A hat die Sache wirksam uebereignet",
     "Ja, aber nur den Unterschiedsbetrag",
     "Nein, denn B war Besitzer"],
    1, "Durch die wirksame Uebereignung an B (paragraph 929 S. 1 BGB) ist B Eigentuemer geworden und darf frei verfuegen.", "WPR Sachenrecht")

add("wpr",
    "Wie wird Eigentum an einer beweglichen Sache uebertragen?",
    ["Durch Vertrag allein", "Durch Einigung und Uebergabe (paragraph 929 S. 1 BGB)", "Durch notarielle Beurkundung", "Durch Registereintragung"],
    1, "paragraph 929 S. 1 BGB: Zur Eigentumsuebertragung ist Einigung und Uebergabe der Sache erforderlich.", "WPR Sachenrecht")

add("wpr",
    "Was ist eine 'Verfuegung' im Sinne des Sachenrechts?",
    ["Ein Vertrag ueber den Kauf einer Sache",
     "Ein Rechtsgeschaeft, durch das ein Recht uebertragen, inhaltlich geaendert, belastet oder aufgehoben wird",
     "Eine gerichtliche Entscheidung",
     "Eine Verwaltungsanordnung"],
    1, "Eine Verfuegung ist ein Rechtsgeschaeft, das unmittelbar ein Recht an einer Sache veraendert (z.B. Eigentumsuebertragung, Pfandrechtsbestellung).", "WPR Sachenrecht")

# WPR - Gesellschaftsrecht
add("wpr",
    "Welche Gesellschaftsform hat kein Mindesthaftkapital?",
    ["GmbH", "AG", "UG (haftungsbeschraenkt)", "Keine der genannten"],
    2, "Die UG (haftungsbeschraenkt) kann mit nur 1 Euro Stammkapital gegrueendet werden, im Gegensatz zur GmbH (25.000 Euro) und AG (50.000 Euro).", "WPR Gesellschaftsrecht")

add("wpr",
    "Wer haftet bei einer GbR im Aussenverhaeltnis?",
    ["Nur die Gesellschaft", "Gesellschaft und Gesellschafter", "Nur die Gesellschafter", "Niemand"],
    1, "Bei der GbR haften sowohl die Gesellschaft als auch die einzelnen Gesellschafter im Aussenverhaeltnis.", "WPR Gesellschaftsrecht")

add("wpr",
    "Wer ist der gesetzliche Vertreter bei einer GmbH?",
    ["Der Vorstand", "Der Geschaeftsfuehrer", "Der Aufsichtsrat", "Die Gesellschafterversammlung"],
    1, "Bei der GmbH vertritt der Geschaeftsfuehrer die Gesellschaft nach aussen.", "WPR Gesellschaftsrecht")

# ============================================================
# Speichern
# ============================================================
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(QS, f, ensure_ascii=False, indent=2)

print("TOTAL:", sum(len(v) for v in QS.values()))
