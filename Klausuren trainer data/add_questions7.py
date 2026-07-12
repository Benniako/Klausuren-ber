import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "_data", "questions_validated.json")

with open(PATH, "r", encoding="utf-8") as f:
    QS = json.load(f)

# Hilfsfunktionen zum Hinzufügen
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

def add_fitb(bank, q, correct_str, solution, source, acceptable=None, diagram=None):
    item = {
        "q": q,
        "type": "fitb",
        "o": [],
        "c": correct_str,
        "s": solution,
        "src": source
    }
    if acceptable:
        item["acceptable"] = acceptable
    if diagram:
        item["diagram"] = diagram
    QS[bank].append(item)

# =====================================================================
# 10 Komplexe WPR Sachverhaltsfragen (Multiple Choice)
# =====================================================================
add_mc("wpr",
    "K kauft von V ein gebrauchtes Auto. V weiss, dass das Auto einen schweren, unsichtbaren Getriebeschaden hat, verschweigt dies aber absichtlich. Zwei Wochen nach Uebergabe bemerkt K den Defekt. Kann K den Vertrag wegen arglistiger Taeuschung anfechten?",
    [
        "Ja, nach paragraph 123 I BGB innerhalb der Jahresfrist des paragraph 124 BGB",
        "Nein, Gewaehrleistungsrechte des Kaufrechts sperren die Anfechtung nach paragraph 123 BGB generell",
        "Nein, eine Anfechtung ist nur innerhalb von 2 Wochen nach Uebergabe zulaessig",
        "Ja, aber nur wenn K vorher erfolglos Nacherfuellung vom Verkaeufer verlangt hat"
    ],
    0,
    "Die arglistige Taeuschung (paragraph 123 I BGB) wird nicht durch das Kaufgewaehrleistungsrecht gesperrt, da das Verhalten des taeuschenden Verkaeufers nicht schutzwuerdig ist. K kann daher direkt anfechten, ohne vorher Nacherfuellung zu verlangen.",
    "WPR Schuldrecht / BGB AT"
)

add_mc("wpr",
    "K kauft von V eine originale Statue von unschaetzbarem Wert. Vor der Uebergabe brennt das Lagerhaus von V durch Blitzschlag unverschuldet ab, die Statue wird zerstoert. Was kann K von V verlangen?",
    [
        "Keinen Schadensersatz, da V die Zerstoerung nicht zu vertreten hat (paragraph 275 IV, paragraph 280 I 2 BGB)",
        "Schadensersatz statt der Leistung in Hoehe des vollen Statuenwerts",
        "Die vertragliche Lieferung einer gleichartigen, neuen Statue derselben Kuenstlerin",
        "Minderung des Kaufpreises auf die Haelfte wegen mangelhafter Leistung"
    ],
    0,
    "Wegen Unmoeglichkeit nach paragraph 275 I BGB wird V von der Leistungspflicht frei. Ein Anspruch auf Schadensersatz statt der Leistung scheitert an paragraph 280 I 2 BGB, da Blitzschlag hoehere Gewalt darstellt und V kein Verschulden trifft (kein Vertretenmuessen).",
    "WPR Schuldrecht / Leistungsstoerungsrecht"
)

add_mc("wpr",
    "A hat sein Rennrad an B verliehen. B geraet in Geldnot und verkauft das Rad fuer 800 Euro an C, der B fuer den Eigentuemer haelt. Das Rad wird C uebergeben. Hat C das Eigentum erworben?",
    [
        "Ja, C hat das Eigentum gutglaeubig nach paragraph 929 S. 1, paragraph 932 BGB erworben, da die Sache A nicht abhandengekommen ist",
        "Nein, da B nicht der Eigentuemer war und somit nicht ueber das Eigentum verfuegen durfte",
        "Nein, da die Sache A abhandengekommen ist, weil er die tatsaechliche Sachherrschaft verloren hat",
        "Ja, aber A kann das Rad jederzeit ohne Entschaedigung von C herausverlangen"
    ],
    0,
    "Das Rad ist A nicht abhandengekommen (paragraph 935 BGB), da er den Besitz freiwillig auf B uebertragen hat. B war unberechtigter Besitzer (Nichtberechtigter). Da C gutglaeubig war (paragraph 932 BGB) und Besitz erlangte, hat er das Eigentum wirksam erworben. A hat nur Schadensersatz- oder Bereicherungsansprueche gegen B.",
    "WPR Sachenrecht"
)

add_mc("wpr",
    "Der Prokurist P des Kaufmanns K schliesst mit V einen Grundstueckskaufvertrag ab, obwohl K ihm im Innenverhaeltnis ausdruecklich verboten hatte, Geschaefte ueber 50.000 Euro abzuschliessen. Der Kaufpreis betraegt 120.000 Euro. V wusste nichts von der internen Beschraenkung. Ist der Vertrag fuer K bindend?",
    [
        "Ja, der Vertrag ist bindend, da der Umfang der Prokura im Aussenverhaeltnis unbeschraenkbar ist (paragraph 50 I, II HGB) und V gutglaeubig war",
        "Nein, der Vertrag ist unwirksam, weil P seine gesetzlichen Vertretungsbefugnisse ueberschritten hat",
        "Der Vertrag ist schwebend unwirksam und bedarf der nachtraeglichen Genehmigung durch K persönlich",
        "Der Vertrag ist nur in Hoehe von 50.000 Euro wirksam, im Uebrigen unwirksam"
    ],
    0,
    "Nach paragraph 50 I, II HGB ist der gesetzliche Umfang der Prokura im Aussenverhaeltnis absolut unbeschraenkbar. Interne Einschraenkungen sind Dritten gegenüber unwirksam, ausser es liegt bewusste Kollusion oder evidenter Missbrauch der Vertretungsmacht vor.",
    "WPR Handelsrecht"
)

add_mc("wpr",
    "Verbraucher K kauft online beim Haendler V ein Smartphone. V uebergibt das verpackte Paket an DHL. Auf dem Transportweg geht das Paket unauffindbar verloren. Wer traegt das Risiko (Gefahruebergang)?",
    [
        "Der Haendler V, da beim Verbrauchsgüterkauf die Gefahr erst mit Uebergabe an den Verbraucher uebergeht (paragraph 475 II BGB)",
        "Der Verbraucher K, sobald das Paket an den Transporteur DHL uebergeben wurde (paragraph 447 BGB)",
        "DHL haftet unbegrenzt gegenüber K, weshalb der Kaufvertrag wirksam bleibt und K zahlen muss",
        "Beide Parteien teilen sich den entstandenen Schaden haelfatig auf"
    ],
    0,
    "Beim Verbrauchsgüterkauf (paragraph 474 BGB) gilt die Abweichung in paragraph 475 II BGB: Die Gefahr geht beim Versendungskauf erst auf den Verbraucher ueber, wenn dieser die Sache tatsaechlich erhaelt. Da das Paket auf dem Transportweg verloren ging, traegt V das Risiko und verliert den Zahlungsanspruch (paragraph 326 I BGB).",
    "WPR Kaufrecht / Verbraucherschutz"
)

add_mc("wpr",
    "Die Gesellschafter A und B betreiben eine GbR. A schliesst im Namen der GbR einen Mietvertrag ab. Die GbR zahlt die Miete nicht. Der Vermieter verlangt die Zahlung direkt von B persoenlich. Muss B haften?",
    [
        "Ja, B haftet fuer die Verbindlichkeiten der GbR persoenlich, unbeschraenkt und gesamtschuldnerisch (analog paragraph 128 HGB bzw. paragraph 715 BGB)",
        "Nein, GbR-Gesellschafter haften im Aussenverhaeltnis niemals mit ihrem Privatvermoegen",
        "Ja, aber B haftet nur quotal entsprechend seinem Geschaftsanteil am Gesellschaftsvermoegen",
        "Nein, der Vermieter muss zuerst das Privatvermoegen des handelnden Gesellschafters A vollstaendig pfaenden"
    ],
    0,
    "Gesellschafter einer GbR haften fuer die Gesellschaftsschulden persoenlich, primaer, unbeschraenkt und gesamtschuldnerisch (Akzessoritaetshaftung analog paragraph 128 HGB bzw. seit MoPeG ausdruecklich in paragraph 715 BGB n.F.).",
    "WPR Gesellschaftsrecht"
)

add_mc("wpr",
    "In einer extremen Wohnungsnot bietet Vermieter V dem Studenten S ein Zimmer (Marktwert: 300 Euro) fuer 950 Euro an. S unterschreibt zaehneknirschend den Vertrag, weil er sonst obdachlos waere. Ist der Mietvertrag wirksam?",
    [
        "Nein, der Vertrag ist sittenwidrig (Wucher) nach paragraph 138 II BGB und somit von Anfang an nichtig",
        "Ja, im Rahmen der Vertragsfreiheit koennen Parteien Preise voellig frei vereinbaren",
        "Der Vertrag ist wirksam, aber S kann die monatliche Miete einseitig um 80% kuerzen",
        "Der Vertrag ist schwebend unwirksam und bedarf der Genehmigung des zustaendigen AStA"
    ],
    0,
    "Nach paragraph 138 II BGB (Wucher) ist ein Rechtsgeschaeft insbesondere dann nichtig, wenn jemand unter Ausbeutung der Zwangslage, der Unerfahrenheit oder des Mangels an Urteilskraft eines anderen sich Vermögensvorteile versprechen laesst, die in einem auffaelligen Missverhaeltnis zur Leistung stehen.",
    "WPR Schuldrecht / BGB AT"
)

add_mc("wpr",
    "K unterschreibt versehentlich ein Bestellformular fuer 10 statt 1 Kiste Wein, da er die Masseinheit falsch verstanden hat. Er bemerkt den Irrtum am naechsten Tag. Wann muss er die Anfechtung erklaeren?",
    [
        "Unverzueglich (ohne schuldhaftes Zoegern), nachdem er von dem Anfechtungsgrund Kenntnis erlangt hat (paragraph 121 I BGB)",
        "Innerhalb einer gesetzlichen Ausschlussfrist von exakt 2 Wochen",
        "Spaetestens nach Ablauf von 3 Jahren (regelmaessige Verjaehrungsfrist)",
        "Die Anfechtung ist fristfrei moeglich, solange die Lieferung noch nicht erfolgt ist"
    ],
    0,
    "Ein Irrtum nach paragraph 119 BGB (hier Inhaltsirrtum) muss nach paragraph 121 I BGB unverzueglich (ohne schuldhaftes Zoegern) nach Kenntniserlangung des Irrtums erklaert werden. Ein Zoegern von mehreren Wochen schliesst die Anfechtung aus.",
    "WPR BGB AT"
)

add_mc("wpr",
    "K mietet einen Festsaal fuer eine grosse Hochzeitsfeier. Kurz vor der Feier wird durch staatliche Pandemie-Schutzmassnahmen die Durchfuehrung von Grossveranstaltungen komplett verboten. Kann K den Mietvertrag anpassen oder kuedigen?",
    [
        "Ja, es liegt eine schwerwiegende Stoerung der Geschaeftsgrundlage vor (paragraph 313 BGB). K kann Anpassung oder ggf. Ruecktritt verlangen",
        "Nein, das Verwendungsrisiko gemieteter Raeume liegt immer vollumfaenglich beim Mieter",
        "Nein, Vertraege sind stets strikt einzuhalten (pacta sunt servanda), ohne jede Ausnahme",
        "Ja, aber nur wenn der Vermieter grob fahrlaessig gehandelt hat"
    ],
    0,
    "Nach paragraph 313 BGB (Stoerung der Geschaeftsgrundlage) kann ein Vertrag angepasst oder aufgeloest werden, wenn sich wesentliche Umstaende, die zur Grundlage wurden, nach Vertragsschluss schwerwiegend veraendert haben und das Festhalten am unveraenderten Vertrag unzumutbar ist.",
    "WPR Schuldrecht / Stoerung der Geschaeftsgrundlage"
)

add_mc("wpr",
    "Die Kaufleute A und B vereinbaren telefonisch die Lieferung von Holz. A schickt B am selben Tag ein Bestaetigungsschreiben, das jedoch abweichend eine zusaetzliche Vertragsstrafe bei Lieferverzug enthaelt. B legt das Schreiben ungelenkt ab und widerspricht nicht. Hat die Vertragsstrafe Gueltigkeit?",
    [
        "Ja, durch das Schweigen auf das kaufmaennische Bestaetigungsschreiben gilt dessen Inhalt als genehmigt, sofern die Abweichung nicht unredlich war",
        "Nein, da B der Klausel am Telefon nicht zugestimmt hatte",
        "Nein, Schweigen hat im Handelsrecht niemals Erklaerungscharakter",
        "Ja, aber nur wenn das Bestaetigungsschreiben notariell beglaubigt wurde"
    ],
    0,
    "Das kaufmaennische Bestaetigungsschreiben ist Gewohnheitsrecht des HGB. Wenn ein Kaufmann auf ein solches Schreiben nicht unverzueglich reagiert, gilt das Schweigen als Zustimmung zu dem Inhalt des Schreibens, ausser das Schreiben wich so stark ab, dass der Absender nicht mit einer Billigung rechnen durfte.",
    "WPR Handelsrecht"
)

# =====================================================================
# 5 WPR Lückentext-Fragen (Fill-in-the-Blank)
# =====================================================================
add_fitb("wpr",
    "Das Trennungsprinzip besagt, dass das Verpflichtungsgeschäft (z.B. Kaufvertrag) und das Verfügungsgeschäft (z.B. Übereignung) rechtlich strikt getrennt sind. Das darauf aufbauende ...prinzip besagt, dass die Unwirksamkeit des Verpflichtungsgeschäfts die Wirksamkeit des Verfügungsgeschäfts unberührt lässt.",
    "Abstraktionsprinzip",
    "Das Abstraktionsprinzip trennt die Wirksamkeit des Verfuegungsgeschaefts (Vollzug) von der Wirksamkeit des Verpflichtungsgeschaefts (Kaufvertrag).",
    "WPR Grundlagen",
    acceptable=["Abstraktions-Prinzip"]
)

add_fitb("wpr",
    "Nach paragraph 194 I BGB ist das Recht, von einem anderen ein Tun oder Unterlassen zu verlangen, ein ...",
    "Anspruch",
    "Der Anspruch ist in paragraph 194 I BGB legaldefiniert als das Recht, von einem anderen ein Tun oder Unterlassen zu verlangen.",
    "WPR Grundlagen",
    acceptable=["Anspruche", "Ansprüche"]
)

add_fitb("wpr",
    "Die tatsächliche Sachherrschaft über eine Sache nennt man nach paragraph 854 BGB ...",
    "Besitz",
    "Besitz ist die tatsaechliche Herrschaftsmacht ueber eine Sache (paragraph 854 BGB), waehrend Eigentum die rechtliche Herrschaftsmacht darstellt (paragraph 903 BGB).",
    "WPR Grundlagen",
    acceptable=["unmittelbarer Besitz"]
)

add_fitb("wpr",
    "Die rechtliche Herrschaftsmacht über eine Sache nennt man nach paragraph 903 BGB ...",
    "Eigentum",
    "Eigentum ist die rechtliche Sachherrschaft (paragraph 903 BGB), Besitz dagegen die tatsaechliche Sachherrschaft (paragraph 854 BGB).",
    "WPR Grundlagen"
)

add_fitb("wpr",
    "Ein wirksamer Vertrag kommt durch zwei übereinstimmende Willenserklärungen zustande, nämlich Angebot und ...",
    "Annahme",
    "Ein Vertrag setzt zwei korrespondierende Willenserklaerungen voraus: Das Angebot (oder Antrag, paragraph 145 BGB) und die Annahme (paragraph 147 BGB).",
    "WPR Grundlagen"
)

# =====================================================================
# 5 VWL Lückentext-Fragen (Fill-in-the-Blank)
# =====================================================================
add_fitb("vwl",
    "Eine staatliche Steuer auf einen produzierten Schadstoff, die erhoben wird, um negative Externalitäten zu internalisieren, nennt man ...-Steuer.",
    "Pigou",
    "Eine Pigou-Steuer (oder Pigousteuer) internalisiert negative Externalitaeten, indem sie die privaten Grenzkosten an die sozialen Grenzkosten angleicht.",
    "VWL Kap. F - Oeffentliche Gueter",
    acceptable=["Pigou-Steuer", "Pigousteuer"]
)

add_fitb("vwl",
    "Wenn die Erhöhung des Preises eines Gutes die Nachfrage nach einem anderen Gut erhöht, nennt man diese Güter ...",
    "Substitute",
    "Substitute (oder Substitutionsgueter) sind Gueter, die dieselben oder aehnliche Beduerfnisse befriedigen und sich gegenseitig ersetzen koennen.",
    "VWL Kap. C - Angebot und Nachfrage",
    acceptable=["Substitutionsgüter", "Substitutionsgut"]
)

add_fitb("vwl",
    "Das Bruttoinlandsprodukt (BIP) berechnet nach der Verwendungsrechnung lautet: BIP = C + I + G + NX. NX steht dabei für die ...",
    "Nettoexporte",
    "NX steht fuer die Nettoexporte, also den Unterschiedsbetrag zwischen Exporten und Importen (NX = Exporte - Importe).",
    "VWL Kap. H - BIP",
    acceptable=["Aussenbeitrag", "Außenbeitrag", "Netto-Exporte"]
)

add_fitb("vwl",
    "Die makroökonomische Theorie, dass ein überproportionales Wachstum der Geldmenge langfristig zu einer Erhöhung des allgemeinen Preisniveaus (Inflation) führt, heißt ...theorie des Geldes.",
    "Quantitätstheorie",
    "Die Quantitaetstheorie des Geldes (M * V = P * Y) besagt, dass eine Ausweitung der Geldmenge proportional auf das Preisniveau wirkt.",
    "VWL Kap. I - Inflation",
    acceptable=["Quantitaetstheorie", "Quantitaetstheorie des Geldes", "Quantitätstheorie des Geldes"]
)

add_fitb("vwl",
    "Der Nettowohlfahrtsverlust (Deadweight Loss) einer Steuer ist umso größer, je ... Angebot und Nachfrage auf Preisänderungen reagieren.",
    "elastischer",
    "Je elastischer die Marktteilnehmer (Angebot/Nachfrage) reagieren, desto groesser ist der Rueckgang der gehandelten Menge und desto groesser der DWL.",
    "VWL Kap. E - Preiskontrollen und Steuern",
    acceptable=["staerker", "stärker", "empfindlicher"]
)

# =====================================================================
# 5 Weitere fortgeschrittene VWL-Fragen (Multiple Choice)
# =====================================================================
add_mc("vwl",
    "Im Vergleich zu einer Pigou-Steuer: Welchen entscheidenden Vorteil hat der Zertifikatehandel (Cap-and-Trade) bei der Regulierung von Schadstoffen?",
    [
        "Der Zertifikatehandel sichert die exakte Einhaltung einer vorgegebenen Emissionsmenge (Mengensicherheit), selbst wenn die Vermeidungskosten unbekannt sind",
        "Der Zertifikatehandel ist fuer Unternehmen immer kostenguenstiger als eine Steuer",
        "Beim Zertifikatehandel fallen fuer den Staat keinerlei Administrationskosten an",
        "Der Zertifikatehandel verhindert, dass reiche Unternehmen weiterhin Schadstoffe ausstossen duerfen"
    ],
    0,
    "Der wesentliche Vorteil des Zertifikatehandels liegt in der Mengensicherheit: Der Staat legt das Limit ('Cap') fest. Bei einer Pigou-Steuer hingegen haengt die resultierende Emissionsmenge von den Vermeidungskosten der Unternehmen ab, die dem Staat oft unbekannt sind.",
    "VWL Kap. F - Externalitaeten",
    diagram="externality"
)

add_mc("vwl",
    "Wie verändert sich die Wohlfahrt eines Landes, wenn es von einer geschlossenen Volkswirtschaft zu einem Importeur von Weizen wird?",
    [
        "Die Konsumentenrente steigt stark, die Produzentenrente sinkt, und die Gesamtwohlfahrt im Inland steigt",
        "Sowohl Konsumenten- als auch Produzentenrente steigen durch den Freihandel",
        "Die Produzentenrente steigt, die Konsumentenrente sinkt, und die Gesamtwohlfahrt bleibt konstant",
        "Die Gesamtwohlfahrt sinkt, da inlndische Produktion ver draengt wird"
    ],
    0,
    "Beim Uebergang zum Import sinkt der Inlandspreis auf das Weltmarktniveau. Die Konsumentenrente steigt (groessere Menge, niedrigerer Preis), die Produzentenrente sinkt. Der Zuwachs an Konsumentenrente uebersteigt den Verlust an Produzentenrente, sodass die Gesamtwohlfahrt steigt.",
    "VWL Kap. G - Internationaler Handel"
)

add_mc("vwl",
    "Was versteht man unter dem Begriff 'Wertschöpfung' (Value Added) in der Entstehungsrechnung des BIP?",
    [
        "Der Produktionswert eines Gutes abzueglich des Werts aller eingesetzten Vorleistungen",
        "Der reine Gewinn eines Unternehmens vor Zinsen und Steuern (EBIT)",
        "Die Summe aller Loehne, Gehaelter und Gewinnausschuettungen in einem Jahr",
        "Der Marktwert aller exportierten Fertiggüter"
    ],
    0,
    "Die Wertschoepfung ist der Produktionswert abzueglich der Vorleistungen. Dies verhindert Doppelzaehlungen in der BIP-Berechnung, da Vorleistungen bereits erfasst wurden.",
    "VWL Kap. H - BIP"
)

add_mc("vwl",
    "Welche Kosten der Inflation beschreiben den Ressourcenaufwand, den Menschen betreiben, um ihre Bargeldbestände aufgrund der Entwertung zu minimieren (z.B. häufige Bankgänge)?",
    [
        "Schuhlederkosten (Shoeleather costs)",
        "Speisekartenkosten (Menu costs)",
        "Relative Preisschwankungen",
        "Steuerliche Verzerrungen"
    ],
    0,
    "Schuhlederkosten bezeichnen den Aufwand und die Zeit, die Menschen aufwenden, um Bargeldbestaende zu verringern (z.B. haeufigeres Abheben kleinerer Betraege), da die Inflation Bargeld entwertet.",
    "VWL Kap. I - Inflation"
)

add_mc("vwl",
    "Welches Wohlfahrtsmaß sinkt im Vergleich zum perfekten Marktgleichgewicht, wenn der Staat eine Preissubvention für ein Gut einführt?",
    [
        "Die Gesamtwohlfahrt sinkt, da die Subventionskosten des Staates den Zuwachs an Konsumenten- und Produzentenrente übersteigen (Nettowohlfahrtsverlust)",
        "Die Konsumentenrente sinkt, da der Preis kuenstlich erhoeht wird",
        "Die Produzentenrente sinkt, da Unternehmen weniger anbieten duerfen",
        "Nichts sinkt – eine staatliche Subvention erhoeht die Wohlfahrt in jedem Fall"
    ],
    0,
    "Eine Subvention verschiebt die gehandelte Menge ueber das effiziente Marktgleichgewicht hinaus. Fuer die zusaetzlichen Einheiten liegen die Produktionskosten ueber der Zahlungsbereitschaft der Konsumenten. Dies erzeugt einen Nettowohlfahrtsverlust (DWL), da die Ausgaben des Staates groesser sind als die Zunahme an KR und PR.",
    "VWL Kap. D / E - Wohlfahrt und Staatseingriffe",
    diagram="konsumenten-produzenten-rente"
)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(QS, f, ensure_ascii=False, indent=2)

print("TOTAL NEW QUESTIONS:", sum(len(v) for v in QS.values()))
print("✅ Fragen erfolgreich hinzugefügt!")
