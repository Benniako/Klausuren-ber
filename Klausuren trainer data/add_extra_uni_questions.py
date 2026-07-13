import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "_data", "questions_validated.json")

with open(PATH, "r", encoding="utf-8") as f:
    QS = json.load(f)

# Helper function
def add_mc(bank, q, opts, correct_idx, solution, source, diagram=None):
    item = {
        "q": q,
        "o": opts,
        "c": correct_idx,
        "s": solution,
        "src": source
    }
    if diagram:
        item["diagram"] = diagram
    QS[bank].append(item)

# 1. BWL 1 (Grundlagen)
add_mc("bwl1",
    "Ein Unternehmen plant eine Investition mit Anschaffungskosten von 100.000 € am Zeitpunkt t=0. In den Perioden t=1 und t=2 werden Netto-Rückflüsse (Cashflows) von jeweils 60.000 € erwartet. Der Kalkulationszinssatz beträgt 10 % p.a. Wie hoch ist der Kapitalwert (NPV) dieser Investition und ist sie vorteilhaft?",
    [
        "-10.000 €; die Investition ist unvorteilhaft",
        "4.132,23 €; die Investition ist vorteilhaft",
        "20.000,00 €; die Investition ist vorteilhaft",
        "-5.123,97 €; die Investition ist unvorteilhaft"
    ],
    1,
    "Der Kapitalwert berechnet sich als: NPV = -C0 + CF1 / (1+r) + CF2 / (1+r)^2. Hier: NPV = -100.000 + 60.000/1.10 + 60.000/1.21 = -100.000 + 54.545,45 + 49.586,78 = 4.132,23 €. Da der NPV > 0 ist, erhöht die Investition den Vermögenswert und ist vorteilhaft.",
    "BWL Investitionsrechnung"
)

add_mc("bwl1",
    "Die Gesamtkapitalrentabilität (GKR) eines Unternehmens beträgt 8 % bei einem Zinssatz für Fremdkapital von 5 % p.a. Wie verändert sich die Eigenkapitalrentabilität (EKR), wenn der Verschuldungsgrad (FK/EK) von 1 auf 2 erhöht wird (unter Annahme eines konstanten Fremdkapitalzinssatzes)?",
    [
        "Die EKR steigt von 11 % auf 14 %",
        "Die EKR steigt von 13 % auf 16 %",
        "Die EKR bleibt unverändert bei 8 %",
        "Die EKR sinkt von 11 % auf 8 %"
    ],
    0,
    "Nach der Leverage-Formel gilt: EKR = GKR + (GKR - i) * (FK/EK). Bei einem Verschuldungsgrad von 1: EKR = 8 % + (8 % - 5 %) * 1 = 11 %. Bei einem Verschuldungsgrad von 2: EKR = 8 % + (8 % - 5 %) * 2 = 14 %. Dies zeigt den positiven Hebeleffekt (Leverage-Effekt) der Verschuldung, da die GKR über dem FK-Zins liegt.",
    "BWL Finanzierung"
)

add_mc("bwl1",
    "Wenn ein Unternehmen seine Umsatzrentabilität von 5 % auf 6 % steigert und gleichzeitig der Kapitalumschlag von 2,0 auf 1,8 sinkt, wie verändert sich der Return on Investment (ROI) im DuPont-System?",
    [
        "Der ROI steigt von 10,0 % auf 10,8 %",
        "Der ROI sinkt von 10,0 % auf 9,0 %",
        "Der ROI steigt von 5,0 % auf 6,0 %",
        "Der ROI bleibt konstant bei 10,0 %"
    ],
    0,
    "Der ROI im DuPont-System berechnet sich als Produkt aus Umsatzrentabilität und Kapitalumschlag. Vorher: 5 % * 2,0 = 10 %. Nachher: 6 % * 1,8 = 10,8 %. Der ROI erhöht sich somit trotz des gesunkenen Kapitalumschlags aufgrund des starken Anstiegs der Umsatzrentabilität.",
    "BWL Controlling"
)

# 2. BWL 2 (Buchführung)
add_mc("bwl2",
    "Ein Unternehmen hat folgenden Lagerbestand für einen Rohstoff: Anfangsbestand 100 Stk. zu je 10 €. Zukauf 1: 150 Stk. zu je 12 €. Zukauf 2: 50 Stk. zu je 15 €. Es werden 120 Stk. verbraucht. Wie hoch ist der verbleibende Endbestand (180 Stk.) bewertet nach dem FIFO-Verfahren?",
    [
        "2.310 €",
        "2.100 €",
        "2.550 €",
        "1.980 €"
    ],
    0,
    "Die 180 verbleibenden Einheiten unter FIFO sind die am spätesten beschafften Einheiten. Diese setzen sich zusammen aus: 50 Einheiten aus Zukauf 2 (50 * 15 € = 750 €) und 130 Einheiten aus Zukauf 1 (130 * 12 € = 1.560 €). Der bewertete Endbestand beträgt somit: 750 € + 1.560 € = 2.310 €.",
    "Buchführung Vorratsbewertung"
)

add_mc("bwl2",
    "Ein Unternehmen überweist am 01.11.2026 die Miete für die Büroräume im Voraus für 6 Monate (Nov 2026 bis April 2027) in Höhe von insgesamt 12.000 €. Welche Buchung ist zum Abschlussstichtag am 31.12.2026 für den Jahresabschluss 2026 vorzunehmen, wenn im November die gesamte Überweisung als Mietaufwand gebucht wurde?",
    [
        "Aktive Rechnungsabgrenzung (ARAP) an Mietaufwand 8.000 €",
        "Mietaufwand an Passive Rechnungsabgrenzung (PRAP) 4.000 €",
        "Mietaufwand an Sonstige Verbindlichkeiten 8.000 €",
        "Aktive Rechnungsabgrenzung (ARAP) an Mietaufwand 4.000 €"
    ],
    0,
    "Der Gesamtaufwand beträgt 12.000 € für 6 Monate, also 2.000 € pro Monat. Auf das Geschäftsjahr 2026 entfallen 2 Monate (Nov, Dez) = 4.000 €. Auf das Folgejahr 2027 entfallen 4 Monate (Jan bis Apr) = 8.000 €. Da der volle Betrag im Voraus gezahlt und als Aufwand gebucht wurde, müssen 8.000 € als Aktiver Rechnungsabgrenzungsposten (ARAP) abgegrenzt werden, um den Aufwand in 2026 zu reduzieren: Buchung 'ARAP an Mietaufwand 8.000 €'.",
    "Buchführung Rechnungsabgrenzung"
)

add_mc("bwl2",
    "Eine Maschine (historische Anschaffungskosten: 50.000 €, Buchwert zu Jahresbeginn: 10.000 €) wird am 01.07. für 12.000 € netto bar verkauft. Die reguläre jährliche lineare Abschreibung beträgt 4.000 € pro Jahr. Wie hoch ist der im Geschäftsjahr realisierte Gewinn oder Verlust aus dem Anlagenabgang (unter Berücksichtigung der zeitanteiligen Abschreibung)?",
    [
        "Gewinn aus Anlagenabgang von 4.000 €",
        "Gewinn aus Anlagenabgang von 2.000 €",
        "Verlust aus Anlagenabgang von 2.000 €",
        "Gewinn aus Anlagenabgang von 12.000 €"
    ],
    0,
    "Zunächst ist die zeitanteilige Abschreibung bis zum Verkaufszeitpunkt (01.07., d.h. 6 Monate) nachzubuchen: 4.000 € * (6/12) = 2.000 €. Dadurch sinkt der Buchwert der Maschine auf 8.000 € (10.000 € - 2.000 €). Der Nettoverkaufserlös beträgt 12.000 €. Der Gewinn aus dem Abgang ergibt sich als Differenz zwischen Verkaufserlös und Buchwert: 12.000 € - 8.000 € = 4.000 €.",
    "Buchführung Anlagenabgang"
)

# 3. MAWI 1 (Mathe)
add_mc("mawi1",
    "Ein Konsument maximiert seine Nutzenfunktion U(x, y) = x^0.5 * y^0.5 unter der Budgetrestriktion 2x + 4y = 80. Wie lautet die optimale Nachfragemenge x* im Nutzenmaximum unter Verwendung des Lagrange-Verfahrens?",
    [
        "x* = 20",
        "x* = 10",
        "x* = 40",
        "x* = 15"
    ],
    0,
    "Dies ist ein klassisches Optimierungsproblem unter Nebenbedingungen. Bei einer symmetrischen Cobb-Douglas-Nutzenfunktion U = x^0.5 * y^0.5 teilt der Konsument sein Einkommen zu gleichen Teilen auf beide Güter auf. Einkommensanteil für x = 40 €. Bei einem Preis von px = 2 € beträgt die optimale Nachfragemenge x* = 40 € / 2 € = 20 Einheiten.",
    "Wirtschaftsmathematik Lagrange-Optimierung"
)

add_mc("mawi1",
    "Die Nachfragefunktion nach einem Gut lautet q(P) = 300 - 3P. Bei welchem Preis P ist die Preiselastizität der Nachfrage genau elastisch mit Einheitselastizität (Elastizität = -1)?",
    [
        "P = 50",
        "P = 100",
        "P = 30",
        "P = 150"
    ],
    0,
    "Die Preiselastizität der Nachfrage berechnet sich als eta = q'(P) * (P / q(P)). Hier ist q'(P) = -3. Setzt man eta = -1 ein: -3 * (P / (300 - 3P)) = -1 => 3P = 300 - 3P => 6P = 300 => P = 50. Bei einem Preis von P = 50 € beträgt die Elastizität genau -1.",
    "Wirtschaftsmathematik Elastizitäten"
)

add_mc("mawi1",
    "Jemand spart jährlich nachschüssig einen Betrag von 2.000 € bei einem Zinssatz von 4 % p.a. an. Welchen Endwert hat dieses Rentensparen nach genau 10 Jahren? (Formel für Rentenendwertfaktor: ((1+i)^n - 1) / i)",
    [
        "24.012,21 €",
        "20.000,00 €",
        "21.648,32 €",
        "24.972,70 €"
    ],
    0,
    "Der Endwert einer nachschüssigen Jahresrente berechnet sich mit der Formel: RE = R * ((1+i)^n - 1) / i. Hier ist R = 2.000 €, i = 0,04 und n = 10. Rentenendwertfaktor = (1,04^10 - 1) / 0,04 = 0,480244 / 0,04 = 12,0061. RE = 2.000 € * 12,0061 = 24.012,21 €.",
    "Wirtschaftsmathematik Finanzmathematik"
)

# 4. MAWI 2 (Statistik)
add_mc("mawi2",
    "Eine medizinische Studie zeigt: 1 % der Bevölkerung leidet an einer Krankheit X. Ein Diagnosetest ist zu 95 % sensitiv (schlägt bei Kranken an) und weist eine Spezifität von 90 % auf (schlägt bei Gesunden fälschlicherweise zu 10 % an). Wenn ein Patient positiv getestet wird, wie hoch ist die Wahrscheinlichkeit, dass er tatsächlich krank ist?",
    [
        "ca. 8,76 %",
        "ca. 95,00 %",
        "ca. 1,00 %",
        "ca. 50,00 %"
    ],
    0,
    "Nach dem Satz von Bayes gilt: P(Krank|Positiv) = P(Positiv|Krank) * P(Krank) / P(Positiv). Der Nenner P(Positiv) berechnet sich über die totale Wahrscheinlichkeit: P(Positiv) = P(+|K)*P(K) + P(+|Gesund)*P(Gesund) = 0,95 * 0,01 + 0,10 * 0,99 = 0,0095 + 0,099 = 0,1085. Eingesetzt ergibt sich: P(Krank|Positiv) = 0,0095 / 0,1085 ≈ 0,0876 bzw. 8,76 %. Trotz eines sensitiven Tests ist die Wahrscheinlichkeit bei geringer Prävalenz relativ niedrig.",
    "Statistik Wahrscheinlichkeitsrechnung"
)

add_mc("mawi2",
    "Um den Mittelwert einer normalverteilten Grundgesamtheit mit bekannter Standardabweichung sigma = 10 bei einer Stichprobengröße n = 100 im Konfidenzniveau von 95 % zu schätzen, wird der z-Wert z_0.975 = 1,96 verwendet. Wie breit ist der Schwankungsbereich (die maximale Fehlerbreite E, d.h. der Abstand zwischen Unter- und Obergrenze des Konfidenzintervalls)?",
    [
        "3,92",
        "1,96",
        "0,39",
        "7,84"
    ],
    0,
    "Das Konfidenzintervall lautet [X_bar - E, X_bar + E] mit dem halben Konfidenzintervall E = z * (sigma / sqrt(n)) = 1,96 * (10 / sqrt(100)) = 1,96 * 1 = 1,96. Die Gesamtbreite des Intervalls (Abstand zwischen Unter- und Obergrenze) beträgt somit 2 * E = 2 * 1,96 = 3,92.",
    "Statistik Intervallschätzung"
)

add_mc("mawi2",
    "In einer einfachen linearen Regression zur Erklärung des Umsatzes durch Marketing-Ausgaben beträgt die Gesamtabweichungsquadratsumme (SST) 500 und die Residualquadratsumme (SSE) 150. Wie hoch ist das Bestimmtheitsmaß R² und wie ist es zu interpretieren?",
    [
        "0,70 (70 % der Varianz des Umsatzes werden durch Marketing-Ausgaben erklärt)",
        "0,30 (30 % der Varianz des Umsatzes werden durch Marketing-Ausgaben erklärt)",
        "0,70 (Marketing-Ausgaben korrelieren schwach negativ mit dem Umsatz)",
        "0,45 (Die Modellqualität ist ungenügend)"
    ],
    0,
    "Das Bestimmtheitsmaß R² berechnet sich nach der Formel: R² = 1 - (SSE / SST), wobei SSE die unerklärte Abweichungsquadratsumme (Residuals) und SST die Gesamtabweichungsquadratsumme darstellt. Hier gilt: R² = 1 - (150 / 500) = 1 - 0,3 = 0,70 bzw. 70 %. Das bedeutet, dass 70 % der Varianz der abhängigen Variable (Umsatz) durch die unabhängige Variable (Marketing-Ausgaben) erklärt werden.",
    "Statistik Regressionsanalyse"
)

# 5. VWL
add_mc("vwl",
    "Zwei identische Firmen im Cournot-Duopol stehen einer linearen Marktnachfrage P = 120 - Q gegenüber. Die Grenzkosten beider Firmen sind konstant bei MC = 30. Wie hoch ist die Gleichgewichtsmenge q* pro Firma?",
    [
        "q* = 30",
        "q* = 45",
        "q* = 15",
        "q* = 20"
    ],
    0,
    "Im Cournot-Wettbewerb bestimmen Duopolisten ihre Reaktionsfunktionen. Für Firma 1 gilt die Gewinnfunktion pi1 = (120 - q1 - q2) * q1 - 30*q1. Ableiten nach q1 und Nullsetzen ergibt die Reaktionsfunktion: q1*(q2) = (90 - q2) / 2. Wegen Symmetrie (q1 = q2 = q*) gilt: q* = (90 - q*) / 2 => 2q* = 90 - q* => 3q* = 90 => q* = 30. Jedes Unternehmen bietet im Gleichgewicht 30 Einheiten an (Gesamtmenge Q = 60, Preis P = 60).",
    "VWL Mikroökonomie - Oligopole"
)

add_mc("vwl",
    "Im IS-LM-Modell einer geschlossenen Volkswirtschaft führt eine restriktive Geldpolitik der Zentralbank (Senkung der nominalen Geldmenge) zu welchen kurzfristigen Anpassungen bei Zinssatz und Realeinkommen?",
    [
        "Der Zinssatz steigt, das Realeinkommen sinkt",
        "Der Zinssatz sinkt, das Realeinkommen steigt",
        "Sowohl der Zinssatz als auch das Realeinkommen steigen",
        "Der Zinssatz bleibt unverändert, das Realeinkommen sinkt"
    ],
    0,
    "Eine restriktive Geldpolitik (Senkung der nominalen Geldmenge) verschiebt die LM-Kurve nach links/oben. Am Geldmarkt entsteht eine Übernachfrage nach Geld, weshalb der Zinssatz steigt. Der höhere Zinssatz dämpft die zinssensitiven Investitionen der Unternehmen, was über den Multiplikatoreffekt zu einem Rückgang des Realeinkommens (BIP) führt.",
    "VWL Makroökonomie - IS-LM"
)

add_mc("vwl",
    "Was beschreibt die 'Golden Rule' der Akkumulation im Solow-Wachstumsmodell einer Volkswirtschaft?",
    [
        "Diejenige Sparquote, die den langfristigen Pro-Kopf-Konsum im Steady State maximiert",
        "Diejenige Sparquote, die das Wirtschaftswachstum unendlich beschleunigt",
        "Den Punkt, an dem die Sparquote genau der Abschreibungsrate der Maschinen entspricht",
        "Die optimale staatliche Verschuldungsquote für Schwellenländer"
    ],
    0,
    "Die 'Golden Rule' der Kapitalakkumulation bezeichnet im Solow-Modell den Zustand im langfristigen Gleichgewicht (Steady State), in dem die Sparquote so gewählt wird, dass der Pro-Kopf-Konsum der Bevölkerung maximiert wird. An diesem Punkt entspricht die Grenzproduktivität des Kapitals der Summe aus Abschreibungsrate, Bevölkerungswachstum und technologischem Fortschritt.",
    "VWL Makroökonomie - Wachstumstheorie"
)

# 6. WPR
add_mc("wpr",
    "A kauft im Namen seines Freundes B bei C ein edles Gemälde. Er macht jedoch weder beim Verkaufsgespräch noch beim Vertragsabschluss deutlich, dass er für B handelt. C geht davon aus, dass A für sich selbst kauft. Wer wird Vertragspartner des C?",
    [
        "A wird Vertragspartner (Eigengeschäft nach dem Offenkundigkeitsprinzip, paragraph 164 II BGB)",
        "B wird Vertragspartner, da A Vertretungsmacht besaß und im Innenverhältnis für B handeln sollte",
        "Der Vertrag ist schwebend unwirksam, da C getäuscht wurde",
        "Es kommt überhaupt kein wirksamer Vertrag zustande, da der Wille nicht mit der Erklärung übereinstimmt"
    ],
    0,
    "Nach dem Offenkundigkeitsprinzip (paragraph 164 I BGB) muss ein Vertreter im Namen des Vertretenen handeln, damit die Wirkungen unmittelbar für diesen eintreten. Tritt dieser Wille nicht erkennbar hervor, so kommt das Geschäft mangels Offenkundigkeit mit dem Vertreter selbst zustande (Eigengeschäft des Vertreters, paragraph 164 II BGB). Ein Anfechtungsrecht wegen Irrtums ist nach paragraph 164 II BGB ausgeschlossen.",
    "WPR BGB AT - Vertretung"
)

add_mc("wpr",
    "K kauft von Händler V einen neuen Fernseher. Nach 2 Wochen zeigt das Bild heftige Streifen (Sachmangel). K verlangt von V sofort ein fabrikneues Ersatzgerät. V weigert sich und will das Gerät stattdessen zunächst zweimal reparieren. Wer ist im Recht?",
    [
        "K ist im Recht, da der Käufer die Art der Nacherfüllung (Reparatur oder Neulieferung) grundsätzlich frei wählen darf (paragraph 439 I BGB)",
        "V ist im Recht, da der Verkäufer immer das Recht auf zwei Nachbesserungsversuche hat, bevor eine Neulieferung verlangt werden kann",
        "V ist im Recht, da eine Neulieferung bei Vorliegen eines Mangels gesetzlich generell erst nach Fehlschlagen der Reparatur zulässig ist",
        "Niemand, das Gesetz verlangt bei Mängeln im ersten Monat zwingend eine gütliche Einigung"
    ],
    0,
    "Gemäß paragraph 439 I BGB kann der Käufer als Nacherfüllung nach seiner Wahl die Beseitigung des Mangels (Reparatur) oder die Lieferung einer mangelfreien Sache (Neulieferung) verlangen. Der Verkäufer kann die gewählte Art der Nacherfüllung nur verweigern, wenn sie unmöglich ist oder für ihn mit unverhältnismäßigen Kosten verbunden wäre (paragraph 439 IV BGB). Das angebliche Recht des Verkäufers auf 'zwei Reparaturversuche' betrifft nur das Fehlschlagen der Nachbesserung für einen anschließenden Rücktritt oder Schadensersatz, schränkt aber das primäre Wahlrecht des Käufers nicht ein.",
    "WPR Schuldrecht - Kaufrecht"
)

add_mc("wpr",
    "Zwei Jugendliche A und B werfen aus Übermut gemeinsam Kieselsteine auf parkende Autos. Ein Stein zertrümmert die Windschutzscheibe eines PKWs im Wert von 1.500 €. Es lässt sich im Nachhinein absolut nicht feststellen, wessen Stein die Scheibe getroffen hat. Müssen A und B haften?",
    [
        "Ja, beide haften als Gesamtschuldner für den vollen Schaden in Höhe von 1.500 € nach paragraph 830 I 2 BGB",
        "Nein, da im Zweifel für den Angeklagten gilt und keinem die Tat individuell nachgewiesen werden kann",
        "Sie haften jeweils nur für die Hälfte des Schadens (750 €), da der Verursacher unklar ist",
        "Es haftet nur die Haftpflichtversicherung der Eltern im Rahmen der Aufsichtspflichtverletzung"
    ],
    0,
    "Kann nachgewiesen werden, dass mehrere Beteiligte eine rechtswidrige Tat begangen haben, lässt sich aber nicht ermitteln, wer von ihnen den konkreten Schaden verursacht hat, haftet jeder für den Schaden (paragraph 830 I S. 2 BGB). Dies dient dem Schutz des Geschädigten vor Gefährdungssituationen. A und B haften als Gesamtschuldner für den gesamten Schaden (paragraph 840 BGB).",
    "WPR Deliktsrecht - paragraph 830 BGB"
)

# 7. Perso
add_mc("perso",
    "Nach der Zwei-Faktoren-Theorie von Frederick Herzberg: Welcher der folgenden Faktoren zählt zu den 'Motivatoren' (die tatsächliche Zufriedenheit erzeugen) und nicht bloß zu den 'Hygienefaktoren' (die lediglich Unzufriedenheit verhindern)?",
    [
        "Die Anerkennung der eigenen Leistung",
        "Die Höhe des Grundgehalts",
        "Die physischen Arbeitsbedingungen im Büro",
        "Das Verhältnis zu den Kollegen und Vorgesetzten"
    ],
    0,
    "Nach Herzbergs Zwei-Faktoren-Theorie sind Hygienefaktoren (wie Gehalt, Arbeitsbedingungen, Unternehmenspolitik und kollegiale Beziehungen) notwendig, um Unzufriedenheit zu verhindern, können aber keine echte, intrinsische Motivation erzeugen. Echte Motivatoren sind Faktoren, die sich auf den Arbeitsinhalt und das Erreichen von Zielen beziehen, wie z.B. Anerkennung, Verantwortung, persönliche Weiterentwicklung und die Arbeit selbst.",
    "Perso Motivationstheorien"
)

add_mc("perso",
    "Welches ist ein wesentlicher struktureller Nachteil einer Matrixorganisation im Vergleich zu einer rein funktionalen Einlinienorganisation?",
    [
        "Gefahr von Kompetenzkonflikten und unklaren Weisungsrechten durch das Mehrlinienprinzip",
        "Geringe Flexibilität bei Marktveränderungen",
        "Mangelnde Spezialisierungsmöglichkeiten für Führungskräfte",
        "Extrem lange, starre Dienstwege über mehrere Hierarchieebenen"
    ],
    0,
    "In einer Matrixorganisation überschneiden sich funktionale (z. B. Beschaffung, Vertrieb) und objektbezogene (z. B. Produkte, Regionen) Verantwortungsbereiche. Da Mitarbeiter zwei Vorgesetzten unterstellt sind (Mehrlinienprinzip), führt dies häufig zu Kompetenzkonflikten, doppelten Priorisierungen, Abstimmungsaufwand und Rollenkonflikten.",
    "Perso Organisationsformen"
)

add_mc("perso",
    "In einem qualifizierten Arbeitszeugnis steht der Satz: 'Er zeigte stets großes Einfühlungsvermögen für die Belange der Belegschaft.' Was bedeutet diese Formulierung im sogenannten 'Zeugnis-Geheimcode' übersetzt für zukünftige Arbeitgeber?",
    [
        "Der Mitarbeiter hatte sexuelle Kontakte im Betrieb oder neigte zu indiskretem Verhalten",
        "Der Mitarbeiter war besonders teamfähig und sozial engagiert",
        "Der Mitarbeiter hatte exzellente Führungsqualitäten und war allseits geschätzt",
        "Der Mitarbeiter war gewerkschaftlich aktiv und suchte Konfrontation mit der Leitung"
    ],
    0,
    "Einige Formulierungen in Arbeitszeugnissen haben eine codierte Bedeutung. Sätze, die ein 'großes Einfühlungsvermögen für die Belegschaft' oder 'Interesse an den Kollegen' betonen, deuten im Geheimcode oft verschlüsselt auf intime Kontakte im Betrieb oder mangelnde professionelle Distanz hin. Ein wohlwollend klingendes Zeugnis kann so erhebliche negative Kritik transportieren.",
    "Perso Personalentwicklung & Zeugnisse"
)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(QS, f, ensure_ascii=False, indent=2)

print("✅ Added extra complex uni-level questions successfully!")
print("TOTAL QUESTIONS NOW:", sum(len(v) for v in QS.values()))
