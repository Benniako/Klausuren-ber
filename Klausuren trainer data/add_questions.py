"""
Fügt ~90 neue Fragen aus den Vorlesungsmaterialien zu questions_validated.json hinzu.
Quellen: VWL Quizzes, Probeklausuren, WPR Folien, Perso PDFs, Mathe Blaetter.
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "_data", "questions_validated.json")

with open(PATH, "r", encoding="utf-8") as f:
    QS = json.load(f)

# Helper: Konvertiere Listenformat in das JSON-Format
# (q, o, c, s, src) oder (q, o, c, s, src, diagram)
def add(bank, q, opts, correct_idx, solution, source, diagram=None):
    entry = {"q": q, "o": opts, "c": correct_idx, "s": solution, "src": source}
    if diagram:
        entry["diagram"] = diagram
    QS[bank].append(entry)

# ============================================================
# VWL - Kapitel B (Denken wie ein Volkswirt) - 10 neue Fragen
# ============================================================
vwl_b = [
    ("Was ist FALSCH: Ein gutes ökonomisches Modell...",
     ["liefert Vorhersagen und Hypothesen", "vereinfacht ein komplexes Problem", "trifft plausible Annahmen", "ist unabhängig von der Empirie"],
     3, "Ein gutes Modell MUSS empirisch überprüfbar sein. Unabhängigkeit von der Empirie ist falsch – Modelle müssen an der Realität getestet werden.", "VWL Kap. B 'Denken wie ein Volkswirt', Folie 20-25; Quiz B"),
    ("Was will die Ökonomin letztlich finden?",
     ["Positive Korrelation", "Negative Korrelation", "Ausgelassene Variablen", "Kausalität"],
     3, "Das letztliche Ziel der empirischen Ökonomie ist die Feststellung von KAUSALITÄT, nicht bloßer Korrelation. Korrelation ist nur ein Hinweis auf mögliche Kausalität.", "VWL Kap. B 'Denken wie ein Volkswirt', Folie 20-25; Quiz B"),
    ("Empirisch zu testen bedeutet NICHT...",
     ["Historische Daten zu analysieren", "100 Ökonomen nach ihrer Meinung zu fragen", "Kontrollierte Experimente durchzuführen", "Natürliche Experimente auszuwerten"],
     1, "Meinungen zu erfragen ist KEINE empirische Überprüfung. Empirie nutzt Daten, Experimente oder natürliche Experimente – nicht subjektive Einschätzungen.", "VWL Kap. B, Folie 22; Quiz B"),
    ("Schokoladeneisverkäufe und Todesfälle durch Ertrinken sind stark positiv korreliert. Was ist die wahrscheinlichste Erklärung?",
     ["Es liegt ein Messfehler vor", "Eisverkäufe sind kausal für Ertrinken", "Es gibt eine ausgelassene Variable (Sommerwetter/Temperatur)", "Es liegt umgekehrte Kausalität vor"],
     2, "Klassisches Beispiel einer AUSGELASSENEN VARIABLEN: Sommerwetter treibt sowohl Eisverkäufe als auch Badbesuche (und damit Ertrinkungsfälle) nach oben.", "VWL Kap. B, Folie 23; Quiz B"),
    ("Was trifft auf natürliche Experimente NICHT zu?",
     ["Quasi-zufällige Einteilung in mindestens zwei Gruppen", "Gruppen bekommen unterschiedliche Behandlung", "Vom Ökonomen selbst durchführbar bei ethischer Unbedenklichkeit", "Entstehen durch natürliche/historische Ereignisse"],
     2, "Natürliche Experimente entstehen durch natürliche/historische Ereignisse, sie werden NICHT vom Ökonomen selbst durchgeführt (das wäre ein kontrolliertes Experiment).", "VWL Kap. B, Folie 24; Quiz B"),
    ("Studierende mit mehr Klausurvorbereitungs-Stunden (X) erreichen mehr Punkte (Y). Was liegt vor?",
     ["Positive Korrelation, X ist wahrscheinlich kausal für Y", "Positive Korrelation, Y ist wahrscheinlich kausal für X", "Negative Korrelation, X ist wahrscheinlich kausal für Y", "Negative Korrelation, Y ist wahrscheinlich kausal für X"],
     0, "Mehr Vorbereitung (X) geht mit mehr Punkten (Y) einher = positive Korrelation. X ist plausibel kausal für Y (Lernen führt zu besseren Noten).", "VWL Kap. B; Probeklausur EVWL, Aufgabe 3"),
    ("Mehr Übungsveranstaltungen (X) gehen mit mehr Durchfallern (Y) einher. Was ist eine wahrscheinliche Erklärung?",
     ["X ist kausal für Y", "Eine ausgelassene Variable (Modulschwierigkeit) ist kausal für X und Y", "Es liegt ein Messfehler vor", "Es gibt keinen statistischen Zusammenhang"],
     1, "Ein schwieriges Modul (ausgelassene Variable) führt sowohl zu mehr Übungsveranstaltungen als auch zu mehr Durchfallern. Scheinkorrelation!", "VWL Kap. B; Probeklausur EVWL, Aufgabe 3"),
    ("Ein Krankenhaus mit weniger Ärzten (X) hat weniger Todesfälle (Y). Welche ausgelassene Variable erklärt das?",
     ["Die Qualität der Ärzte", "Die Bettenzahl (Größe des Krankenhauses)", "Die Adresse des Krankenhauses", "Die Farbe der Krankenhauswände"],
     1, "Die Bettenzahl (Größe des Krankenhauses) bestimmt sowohl die Ärztezahl als auch die Todesfälle. Größere Krankenhäuser haben mehr Ärzte UND mehr Todesfälle.", "VWL Kap. B; Probeklausur EVWL, Aufgabe 3"),
    ("Schlechte Klausurergebnisse (Y) gehen mit hohem Bierkonsum (X) einher. Was liegt vor?",
     ["Positive Korrelation", "Negative Korrelation", "Ein statistischer Zusammenhang, aber keine Korrelation", "Kein Zusammenhang"],
     1, "Hoher Bierkonsum geht mit niedriger Punktzahl einher = NEGATIVE Korrelation (je mehr X, desto weniger Y).", "VWL Kap. B; Probeklausur EVWL, Aufgabe 3"),
    ("Welche Frage ist am ehesten eine Frage der MAKROÖKONOMIE?",
     ["Soll in Aachen die Mietpreisbremse verschärft werden?", "Soll die Bundesregierung an der schwarzen Null im Bundeshaushalt festhalten?", "Soll eine CO2-Steuer für Pkw eingeführt werden?", "Wie wirkt eine Erhöhung des Butterpreises auf den Margarinemarkt?"],
     1, "Bundeshaushalt/Staatsfinanzen sind ein gesamtwirtschaftliches (makroökonomisches) Thema. Die anderen sind mikroökonomisch (einzelne Märkte).", "VWL Kap. A 'Was ist VWL'; Probeklausur EVWL, Aufgabe 1"),
]
for q, o, c, s, src in vwl_b:
    add("vwl", q, o, c, s, src)

# ============================================================
# VWL - Kapitel D (Effizienz/Wohlfahrt) - 5 neue Fragen
# ============================================================
vwl_d = [
    ("Die Konsumentenrente...",
     ["aller Konsumenten ergibt die Wohlfahrt der Gesellschaft", "ist in der Regel negativ beim Kauf", "ist die Fläche zwischen Angebotskurve und Preis", "bildet einen Kernbaustein der Wohlfahrtsbestimmung"],
     3, "Die Konsumentenrente (KR) ist ein Kernbaustein der Wohlfahrtsbestimmung. Wohlfahrt = KR + PR. KR ist die Fläche unter der Nachfragekurve und über dem Preis.", "VWL Kap. D 'Effizienz', Folie 35-42; Quiz D"),
    ("Die Produzentenrente...",
     ["entspricht der Fläche zwischen Nachfrage- und Angebotskurve", "= Gesamtrente minus Konsumentenrente", "steigt, wenn der Preis ceteris paribus sinkt", "errechnet sich als Kosten minus Preis"],
     1, "Gesamtrente = KR + PR, daher gilt PR = Gesamtrente - KR. Die PR ist die Fläche über der Angebotskurve und unter dem Preis.", "VWL Kap. D, Folie 38-42; Quiz D"),
    ("Was ist im Gleichgewicht eines effizienten Wettbewerbsmarkts NICHT unbedingt richtig?",
     ["Durch Umverteilung kann die Gesamtrente nicht erhöht werden", "Eine größere Produktionsmenge erhöht die Gesamtrente nicht", "Alle bekommen ihren gerechten Anteil", "Eine kleinere Produktionsmenge erhöht die Gesamtrente nicht"],
     2, "Effizienz bedeutet nicht Verteilungsgerechtigkeit. Der Markt kann effizient sein, aber die Verteilung kann als ungerecht empfunden werden.", "VWL Kap. D, Folie 40; Quiz D"),
    ("Was ist KEINE geeignete Rechtfertigung für einen Staatseingriff?",
     ["Umverteilung erhöht die Effizienz", "Marktmacht liegt vor", "Es gibt externe Effekte", "Verteilungsgerechtigkeit"],
     0, "Umverteilung dient der GERECHTIGKEIT, erhöht aber nicht die Effizienz. Marktmacht, externe Effekte und Verteilungsgerechtigkeit sind legitime Eingriffsgründe.", "VWL Kap. D, Folie 42; Quiz D"),
    ("Ein Höchstpreis wird eingeführt. Welche wohlfahrtsökonomische Aussage ist korrekt?",
     ["Die Produzentenrente schrumpft, es entsteht ein Nettowohlfahrtsverlust", "Die Produzentenrente schrumpft, kein Wohlfahrtsverlust", "Die Konsumentenrente schrumpft, Produzentenrente steigt", "Keine Änderung"],
     0, "Bei bindendem Höchstpreis sinkt die gehandelte Menge, die Produzentenrente sinkt, und es entsteht ein Nettowohlfahrtsverlust (DWL).", "VWL Kap. D/E; Probeklausur EVWL, Aufgabe 4"),
]
for q, o, c, s, src in vwl_d:
    add("vwl", q, o, c, s, src)

# ============================================================
# VWL - Kapitel G (Handel) - 5 neue Fragen
# ============================================================
vwl_g = [
    ("Welche Aussage zur Produktionsmöglichkeitenkurve (PMK) ist FALSCH?",
     ["PMK zeigt mögliche Outputkombinationen", "Punkte auf der PMK sind effizient", "Bei Wirtschaftswachstum verschiebt sich die PMK nach innen", "Opportunitätskosten entsprechen der Steigung der PMK"],
     2, "Bei Wirtschaftswachstum verschiebt sich die PMK nach AUSSEN (mehr Produktion möglich), nicht nach innen.", "VWL Kap. G 'Handel', Folie 50-60; Quiz G"),
    ("Wer kleinere Opportunitätskosten bei einem Gut hat, hat einen...",
     ["Absoluten Vorteil", "Komparativen Vorteil", "Komparativen Nachteil", "Keinen Vorteil"],
     1, "Kleinere Opportunitätskosten = komparativer VORTEIL (nach Ricardo). Das ist die Grundlage für Spezialisierung und Handel.", "VWL Kap. G, Folie 52; Quiz G"),
    ("Ein kleines Land öffnet seinen Stahlmarkt. Inlandspreis > Weltmarktpreis. Was passiert?",
     ["Das Inland wird Stahl-Importeur", "Im Inland wird weniger Stahl konsumiert", "Die Produzentenrente im Inland steigt", "Die Wohlfahrt im Inland sinkt"],
     0, "Da der Inlandspreis über dem Weltmarktpreis liegt, importiert das Land billigeren Stahl. Konsumenten profitieren, Produzenten verlieren, aber die Gesamtwohlfahrt STEIGT.", "VWL Kap. G, Folie 55; Quiz G"),
    ("Was wäre ein Beispiel für eine tarifäre Handelsbeschränkung?",
     ["Ein Zoll auf deutsche Autos in den USA", "Eine Krümmungsvorschrift für Salatgurken in der EU", "Eine russische Mengenbeschränkung für Fleischimporte", "Umfangreicher Papierkram bei Exporten"],
     0, "Tarifär = ZOLL (Steuer auf Importe). Die anderen sind nicht-tarifäre Handelsbeschränkungen (Quoten, Bürokratie, Standards).", "VWL Kap. G, Folie 58; Quiz G"),
    ("Ein Importzoll auf Stahl erhöht den Inlandspreis. Was passiert mit der Produzentenrente?",
     ["Sie steigt", "Sie sinkt", "Sie bleibt gleich", "Sie verschwindet"],
     0, "Ein Zoll erhöht den Inlandspreis → inländische Produzenten profitieren (PR steigt). Konsumentenrente sinkt, Gesamtwohlfahrt sinkt (DWL).", "VWL Kap. G, Folie 56; Quiz G"),
]
for q, o, c, s, src in vwl_g:
    add("vwl", q, o, c, s, src)

# ============================================================
# VWL - Probeklausur (Kreuzfahrten, Pigou-Steuer etc.) - 8 Fragen
# ============================================================
vwl_pk = [
    ("Was besagt das Coase-Theorem?",
     ["Umweltverschmutzung erhöht immer den Wohlstand", "Umweltverschmutzung senkt immer den Wohlstand", "Bei klaren Eigentumsrechten und fehlenden Transaktionskosten führt private Verhandlung zum effizienten Ergebnis", "Der Staat muss Umweltverschmutzung regulieren"],
     2, "Coase-Theorem: Bei klaren Eigentumsrechten und vernachlässigbaren Transaktionskosten führen private Verhandlungen zu einem effizienten Ergebnis – unabhängig von der Eigentumsverteilung.", "VWL Kap. F; Probeklausur EVWL, Aufgabe 1.5", "externality"),
    ("Eine Kreuzfahrt verursacht 1000 € externen Schaden pro Passagier. Wie hoch muss die Pigou-Steuer sein?",
     ["800 €", "1000 €", "1200 €", "1800 €"],
     1, "Die Pigou-Steuer wird in Höhe der marginalen externen Kosten erhoben = 1000 € pro Passagier. Dadurch wird die private Angebotskurve zur sozialen Grenzkostenkurve.", "VWL Kap. F; Probeklausur EVWL, Aufgabe 2.5", "externality"),
    ("Der Nettowohlfahrtsverlust einer Steuer ist umso GRÖSSER, je...",
     ["elastischer die Angebotskurve ist", "unelastischer die Nachfragekurve ist", "niedriger der Steuersatz ist", "weniger Handelsmöglichkeiten unterbunden werden"],
     0, "Der DWL ist umso größer, je ELASTISCHER Angebot und Nachfrage sind (weil mehr Transaktionen unterbunden werden). Bei unelastischer Nachfrage reagieren Konsumenten kaum → kleiner DWL.", "VWL Kap. E; Probeklausur EVWL, Aufgabe 1.6"),
    ("Ein Streaming-Film (z.B. Netflix) ist am ehesten...",
     ["Ein privates Gut", "Ein Clubgut (ausschließbar, nicht rivalisierend)", "Ein öffentliches Gut", "Ein Allmendegut"],
     1, "Clubgut = AUSSCHLIEẞBAR (Paywall) aber NICHT RIVALISIEREND (Nutzung durch eine Person schadet nicht anderen). Netflix ist ein klassisches Clubgut.", "VWL Kap. F; Probeklausur EVWL, Aufgabe 1.4", "wirtschaftskreislauf"),
    ("Die Kreuzfahrtbranche hat negative Externalitäten. Die sozialen Grenzkosten liegen...",
     ["Unter der privaten Angebotskurve", "Über der privaten Angebotskurve (um den externen Schaden)", "Auf der Nachfragekurve", "Gleich hoch wie die Nachfrage"],
     1, "SK = PK + externer Schaden. Die sozialen Grenzkostenkurve liegt ÜBER der privaten Angebotskurve. Markt produziert zu viel.", "VWL Kap. F; Probeklausur EVWL, Aufgabe 2.2", "externality"),
    ("Welche Maßnahme kann eine negative Externalität korrigieren?",
     ["Subventionierung der Verschmutzer", "Pigou-Steuer in Höhe des externen Schadens", "Verbot allen Handels", "Nichts, Externalitäten sind unlösbar"],
     1, "Die Pigou-Steuer internalisiert die externen Kosten. Sie wird in Höhe des Grenzschadens erhoben und verschiebt die private Angebotskurve nach oben → effiziente Menge.", "VWL Kap. F; Probeklausur EVWL, Aufgabe 2.7"),
    ("Bei erheblichen Transaktionskosten greift das Coase-Theorem...",
     ["Besonders gut", "Gar nicht – privates Verhandeln führt nicht zum effizienten Ergebnis", "Nur bei klaren Eigentumsrechten", "Nur beim Staat"],
     1, "Bei hohen Transaktionskosten (viele Beteiligte) scheitert private Verhandlung. Das Marktgleichgewicht bleibt ineffizient → Staatseingriff nötig.", "VWL Kap. F; Probeklausur EVWL, Aufgabe 2.8"),
    ("Ein bindender Höchstpreis von 4 € (bei Gleichgewichtspreis 8 €) führt zu...",
     ["Nachfrageüberschuss (Knappheit)", "Angebotsüberschuss", "Markt im Gleichgewicht", "Steigendem Angebot"],
     0, "Bei Preis unter dem Gleichgewicht: Nachfrage > Angebot → Nachfrageüberschuss (Knappheit). Konsumenten wollen mehr kaufen, als angeboten wird.", "VWL Kap. E; Probeklausur EVWL, Aufgabe 4.4", "preiskontrolle"),
]
for q, o, c, s, src, *rest in vwl_pk:
    add("vwl", q, o, c, s, src, rest[0] if rest else None)

# ============================================================
# WPR - Kaufrecht (Kap 7) - 5 neue Fragen
# ============================================================
wpr_k = [
    ("Welche Pflichten hat der Verkäufer gemäß § 433 Abs. 1 BGB?",
     ["Nur die Übergabe der Sache", "Übergabe der Sache und Verschaffung des Eigentums", "Zahlung des Kaufpreises", "Nur Verschaffung des Besitzes"],
     1, "§ 433 I 1 BGB: Verkäufer muss die Sache ÜBERGEBEN und das EIGENTUM verschaffen. Die Kaufpreiszahlung trifft den Käufer (§ 433 II).", "WPR Foliensatz Kap. 7, § 433 BGB"),
    ("Was bedeutet der Eigentumsvorbehalt rechtlich?",
     ["Käufer darf die Sache nicht nutzen", "Eigentumsübertragung unter aufschiebender Bedingung (§ 158 I): erst bei voller Zahlung", "Verkäufer behält das Nutzungsrecht", "Kaufvertrag wird erst bei Zahlung geschlossen"],
     1, "Beim Eigentumsvorbehalt wird die Eigentumsübertragung bedingt (§ 158 I): Der Käufer erhält Besitz/Nutzung, wird aber erst mit voller Kaufpreiszahlung Eigentümer.", "WPR Foliensatz Kap. 7, Eigentumsvorbehalt"),
    ("Wann verjährt der Kaufpreisanspruch (§ 433 II) regelmäßig?",
     ["Nach 10 Jahren", "Nach 30 Jahren", "Nach 3 Jahren ab Jahresende, bei Kenntnis", "Nach 6 Monaten"],
     2, "Der Zahlungsanspruch unterliegt der regelmäßigen Verjährung (§ 195 = 3 Jahre). Beginn: Jahresende, wenn Anspruch entstand und Gläubiger Kenntnis erlangte (§ 199).", "WPR Foliensatz Kap. 7, § 195 BGB"),
    ("Was bedeutet das Trennungs- und Abstraktionsprinzip?",
     ["Verpflichtungs- und Verfügungsgeschäft sind getrennt, Wirksamkeit unabhängig", "Verträge müssen schriftlich getrennt sein", "Käufer und Verkäufer verhandeln räumlich getrennt", "Schuldrecht und Sachenrecht gelten in verschiedenen Ländern"],
     0, "Verpflichtungsgeschäft (Kaufvertrag) und Verfügungsgeschäft (Übereignung) sind rechtlich getrennt. Nach dem Abstraktionsprinzip bleibt die Übereignung wirksam, auch wenn der Kaufvertrag nichtig ist.", "WPR Foliensatz Kap. 3, Trennungs-/Abstraktionsprinzip"),
    ("Im Schaufenster steht versehentlich 1.200 € statt 2.100 €. Was gilt?",
     ["Verkäufer muss für 1.200 € liefern", "Schaufensterauslage ist nur invitatio ad offerendum (Aufforderung zum Angebot)", "Käufer bekommt den Artikel gratis", "Vertrag ist nichtig wegen Irrtum"],
     1, "Eine Schaufensterauslage ist eine invitatio ad offerendum, kein verbindliches Angebot. Ein Vertrag erfordert Angebot + Annahme mit übereinstimmendem Willen.", "WPR Foliensatz – Fallbeispiel, invitatio ad offerendum"),
]
for q, o, c, s, src in wpr_k:
    add("wpr", q, o, c, s, src)

# ============================================================
# WPR - Handelsrecht (Kap 6) - 4 neue Fragen
# ============================================================
wpr_h = [
    ("Was ist die Prokura gemäß § 48 HGB?",
     ["Vollmacht für Familienangehörige", "Besondere Handlungsvollmacht, nur von Kaufmann (§ 1 HGB) erteilbar, gesetzlich nicht einschränkbar", "Automatische Vollmacht für alle Arbeitnehmer", "Vollmacht nur für interne Angelegenheiten"],
     1, "Prokura = stärkste Handlungsvollmacht. Nur von Kaufmann (§§ 1 ff. HGB) erteilbar. Umfang gesetzlich festgelegt (§§ 49 f. HGB) und NICHT einschränkbar.", "WPR Foliensatz Kap. 6, § 48 HGB"),
    ("Wann trat das HGB in Kraft?",
     ["01.01.1900", "01.01.2000", "26.04.1892", "01.01.1950"],
     0, "HGB trat am 01.01.1900 (gleichzeitig mit dem BGB) in Kraft. Es regelt die Sonderrechte der Kaufleute und ergänzt das BGB im Handelsverkehr.", "WPR Foliensatz Kap. 6, HGB"),
    ("Wie ist das Verhältnis von BGB und HGB?",
     ["HGB verdrängt BGB vollständig in der Wirtschaft", "BGB = allgemeines Privatrecht; HGB = Sonderprivatrecht der Kaufleute, ergänzt das BGB", "HGB gilt nur für Staatsangehörige", "Beide gelten nur für juristische Personen"],
     1, "BGB = allgemeines Privatrecht. HGB = Sonderprivatrecht der Kaufleute, ergänzt/modifiziert das BGB im Handelsverkehr. Beide gelten nebeneinander.", "WPR Foliensatz Kap. 6, BGB/HGB"),
    ("Welche Aussage zur Prokura ist richtig?",
     ["Kann beliebig eingeschränkt werden", "Umfang gesetzlich festgelegt, nicht einschränkbar (§§ 49 f. HGB)", "Darf nur von Privatpersonen erteilt werden", "Erlischt automatisch nach einem Jahr"],
     1, "Die Prokura ist gesetzlich nicht einschränkbar (§§ 49 f. HGB). Eine inhaltliche Beschränkung gegenüber Dritten ist unwirksam – gerade um den Rechtsverkehr zu schützen.", "WPR Foliensatz Kap. 6, §§ 49 f. HGB"),
]
for q, o, c, s, src in wpr_h:
    add("wpr", q, o, c, s, src)

# ============================================================
# Perso - Organisationsentwicklung - 5 neue Fragen
# ============================================================
perso_oe = [
    ("Was versteht man unter 'organisatorischer Beidhändigkeit'?",
     ["Mitarbeiter müssen beidhändig arbeiten", "Unternehmen muss operatives Geschäft UND geplanten Wandel gleichzeitig gestalten", "Jede Abteilung braucht zwei Leiter", "Change-Prozesse brauchen zwei Beratungsfirmen"],
     1, "Beidhändigkeit = Unternehmen muss一方面 das Tagesgeschäft effizient betreiben und andererseits geplanten Wandel umsetzen. Beides ist für langfristigen Erfolg unverzichtbar.", "Perso Folie 11 Organisationsentwicklung, S. 1-15"),
    ("Welche vier Handlungsfelder muss ganzheitliches Change Management einbeziehen?",
     ["Produktion, Vertrieb, Marketing, Personal", "Strategie, Organisation, Kultur und Technologie", "Einkauf, Logistik, Rechnungswesen, Controlling", "Forschung, Entwicklung, Finanzen, Recht"],
     1, "Vahs: Change Management erfordert Strategie, Organisation, Kultur und Technologie gleichzeitig. Beschränkung auf einzelne Bereiche ist nicht ganzheitlich.", "Perso Folie 11 Organisationsentwicklung, S. 5-10"),
    ("In welche drei Arten lassen sich Widerstände gegen Veränderungen einteilen?",
     ["Finanzielle, zeitliche, personelle", "Rational (Logik), politisch (Macht), emotional (Angst)", "Aktive, passive, schlafende", "Interne, externe, staatliche"],
     1, "Widerstände: rational (unterschiedliche Perspektiven), politisch (Angst vor Machtverlust), emotional (Angst). Sie äußern sich in aktiver oder passiver Ablehnung.", "Perso Folie 11 Organisationsentwicklung, S. 10-15"),
    ("Wie setzt sich der typische 'Akzeptanzmix' bei Veränderungen zusammen?",
     ["50% Promotoren, 30% Skeptiker, 20% Gegner", "5% Promotoren, 40% Skeptiker, 40% Bremser, 15% Gegner", "90% Promotoren, 10% Gegner", "50% Promotoren, 50% Gegner"],
     1, "Typisch: ~5% Promotoren, ~40% Skeptiker, ~40% Bremser, ~15% Gegner. Die Mehrheit ist zunächst zurückhaltend bis ablehnend.", "Perso Folie 11 Organisationsentwicklung, S. 15-20"),
    ("Was ist die 'Realitätslücke' in der Organisationsentwicklung?",
     ["Differenz zwischen Berater-Versprechen und Umsetzbarkeit", "Diskrepanz zwischen struktureller und Verhaltensebene; kann zu Desorientierung führen", "Unterschied zwischen Theorie und Praxis", "Gehaltslücke zwischen Top- und Lower-Management"],
     1, "Realitätslücke entsteht, wenn sachliche/strukturelle und Verhaltensebene nicht synchron verlaufen. Zu schneller Wandel: alte Muster treffen neue Realität. Zu langsamer: neue Verhaltensweisen auf veralteten Strukturen.", "Perso Folie 11 Organisationsentwicklung, S. 20-25"),
]
for q, o, c, s, src in perso_oe:
    add("perso", q, o, c, s, src)

# ============================================================
# Perso - Cross-Cultural - 6 neue Fragen
# ============================================================
perso_cc = [
    ("Welche 6 Kulturdimensionen unterscheidet Hofstede?",
     ["Sprache, Religion, Geschichte, Geografie, Klima, Bevölkerung", "Machtdistanz, Individualismus, Maskulinität, Unsicherheitsvermeidung, Langzeitorientierung, Genussorientierung", "Zeit, Geld, Macht, Bildung, Gesundheit, Freizeit", "Hierarchie, Konsens, Feedback, Vertrauen, Pünktlichkeit, Emotion"],
     1, "Hofstedes 6 Dimensionen: Machtdistanz, Individualismus/Kollektivismus, Maskulinität/Feminität, Unsicherheitsvermeidung, Langzeit-/Kurzzeitorientierung, Indulgence/Restraint (Genussorientierung).", "Perso Folie 02 CrossCultural, S. 1-20"),
    ("Was beschreibt die Dimension 'Machtdistanz'?",
     ["Geografischer Abstand zwischen Management und Produktion", "Ausmaß der Akzeptanz ungleicher Machtverteilung in einer Gesellschaft", "Höhe der Gehaltsdifferenz", "Anzahl der Hierarchieebenen"],
     1, "Machtdistanz = Ausmaß, in dem Mitglieder einer Gesellschaft ungleiche Machtverteilung akzeptieren. Hoch (Malaysia): Orientierung an Autoritäten. Niedrig (Dänemark): Orientierung an Argumenten.", "Perso Folie 02 CrossCultural, S. 5-15"),
    ("In welche 5 Stufen lässt sich der interkulturelle Entwicklungsprozess einteilen?",
     ["Ankommen, Arbeiten, Heiraten, Kinder, Rente", "Honeymoon, Desorientierung, Befremden/Feindlichkeit, Toleranz/Integration, Bi-Kulturalität", "Planung, Umsetzung, Kontrolle, Auswertung, Verbesserung", "Ignoranz, Wissen, Verständnis, Akzeptanz, Liebe"],
     1, "5 Stufen: (1) Honeymoon – anfängliche Begeisterung, (2) Desorientierung, (3) Befremden/Feindlichkeit – Kulturschock, (4) Toleranz/Integration, (5) Bi-Kulturalität – Zu-Hause-Gefühl in zwei Kulturen.", "Perso Folie 02 CrossCultural, S. 30-50"),
    ("Was ist der Unterschied zwischen kontextarmer und kontextreicher Kommunikation (Erin Meyer)?",
     ["Kontextarm = laut, kontextreich = leise", "Kontextarm = präzise/wörtlich; kontextreich = nuanciert, zwischen den Zeilen", "Kontextarm nur für E-Mails, kontextreich nur für Gespräche", "Kein Unterschied"],
     1, "Kontextarm (Deutschland, USA): Botschaften wortwörtlich, explizit. Kontextreich (Japan, China): Botschaften impliziert, zwischen den Zeilen. Missverständnisse bei unterschiedlicher Kontexterwartung.", "Perso Folie 02 CrossCultural, S. 15-30"),
    ("Worin unterscheiden sich aufgabenbasiertes und beziehungsbasiertes Vertrauen?",
     ["Kein Unterschied", "Aufgabenbasiert: durch Arbeitsleistung. Beziehungsbasiert: durch gemeinsame Zeit/Mahlzeiten", "Aufgabenbasiert nur privat, beziehungsbasiert nur beruflich", "Beziehungsbasiert ist immer schwächer"],
     1, "Aufgabenbasiert (USA, Deutschland): Vertrauen durch gute, zuverlässige Arbeit. Beziehungsbasiert (China, Brasilien): Vertrauen durch gemeinsame Zeit, Mahlzeiten, persönliche Begegnungen.", "Perso Folie 02 CrossCultural, S. 20-35"),
    ("Wie unterscheiden sich zeitlich lineare und zeitlich flexible Kulturen?",
     ["Linear = Schritt für Schritt, Fokus auf Pünktlichkeit. Flexibel = parallel, Unterbrechungen akzeptabel", "Linear = alle pünktlich, flexibel = alle zu spät", "Unterschied betrifft nur Arbeitszeiten", "Linear arbeitet langsamer"],
     0, "Linear (Deutschland, Japan, USA): seriell, fokussiert auf Pünktlichkeit/Planeinhaltung. Flexibel (Brasilien, China, Indien): parallel, Unterbrechungen akzeptabel, Anpassungsfähigkeit über Organisation.", "Perso Folie 02 CrossCultural, S. 25-40"),
]
for q, o, c, s, src in perso_cc:
    add("perso", q, o, c, s, src)

# ============================================================
# Perso - Team & Konflikt - 4 neue Fragen
# ============================================================
perso_tk = [
    ("Wie lauten die 4 Phasen der Teamentwicklung nach Tuckman?",
     ["Performing, Norming, Storming, Forming", "Forming, Storming, Norming, Performing", "Storming, Forming, Performing, Norming", "Norming, Performing, Forming, Storming"],
     1, "Tuckman: (1) Forming – Kennenlernen, (2) Storming – Konflikte/Spannungen, (3) Norming – Spielregeln, Rollen, (4) Performing – effizientes Arbeiten.", "Perso Folie 05 TeamKonflikt, S. 1-10"),
    ("Welche 5 Konfliktstile unterscheidet Thomas/Kilman?",
     ["Flucht, Kampf, Verhandlung, Schlichtung, Klage", "Vermeiden, Nachgeben, Kompromiss, Durchsetzen, Kooperieren", "Aggressiv, passiv, manipulativ, diplomatisch, ignorant", "Win, Lose, Draw, Fold, Raise"],
     1, "Thomas/Kilman im Koordinatensystem Eigene Ziele/Fremde Ziele: Vermeiden (Schildkröte), Nachgeben (Teddybär), Kompromiss (Fuchs), Durchsetzen (Haifisch), Kooperieren (Eule = Win-Win).", "Perso Folie 05 TeamKonflikt, S. 10-20"),
    ("Was ist der 'Ringelmann-Effekt' (Social Loafing)?",
     ["Leistungssteigerung durch Gruppendynamik", "Einzelne leisten im Team weniger als allein; bekämpfbar durch kleine Gruppen (max. 5-7)", "Teams arbeiten immer schneller als Einzelne", "Teams werden kreativer als Individuen"],
     1, "Beim Ringelmann-Effekt ('Trittbrettfahren') reduzieren Einzelne ihre Leistung in der Gruppe, da ihr Beitrag weniger sichtbar ist. Gegenmaßnahmen: kleine Gruppen, identifizierbare Beiträge.", "Perso Folie 05 TeamKonflikt, S. 15-25"),
    ("Für welche Konfliktstile ist das Harvard-Verhandlungsmodell besonders geeignet?",
     ["Für alle fünf Stile", "Für Kompromiss und Kooperation (beide Seiten wollen Win-Win)", "Nur für Vermeiden", "Nur für Durchsetzen"],
     1, "Harvard-Modell (Menschen/Probleme trennen, Interessen statt Positionen, Alternativen, neutrale Kriterien) erfordert Kooperationsbereitschaft. Funktioniert bei Kompromiss/Kooperation (5.5 und 9.9).", "Perso Folie 05 TeamKonflikt, S. 20-25"),
]
for q, o, c, s, src in perso_tk:
    add("perso", q, o, c, s, src)

# ============================================================
# Perso - Arbeitsrecht - 4 neue Fragen
# ============================================================
perso_ar = [
    ("Wann kann ein Betriebsrat gewählt werden?",
     ["Ab 50 Arbeitnehmern", "Ab 5 ständigen wahlberechtigten Arbeitnehmern, davon 3 wählbar; Amtszeit 4 Jahre", "Ab 100 Arbeitnehmern mit Zustimmung des Arbeitgebers", "Automatisch in jedem Unternehmen"],
     1, "Nach BetrVG: Betriebsrat wählbar ab 5 ständigen wahlberechtigten Arbeitnehmern, davon 3 wählbar. Amtsperiode: 4 Jahre.", "Perso Folie 06 Arbeitsrecht, S. 1-15"),
    ("Was ist der Unterschied zwischen Mitwirkung und Mitbestimmung des Betriebsrats?",
     ["Kein Unterschied", "Mitwirkung = schwächer (Information/Anhörung). Mitbestimmung = stärker (Widerspruchsrecht/Veto)", "Mitwirkung nur für Arbeitgeber", "Mitbestimmung ist freiwillig"],
     1, "Mitwirkung = schwächer (Informations-, Anhörungs-, Beratungsrecht). Mitbestimmung = stärker (Widerspruchsrecht, Vetorecht, Initiativrecht).", "Perso Folie 06 Arbeitsrecht, S. 10-20"),
    ("Was muss bei verhaltensbedingter Kündigung VORHER erfolgt sein?",
     ["Schriftliche Abmahnung wegen gleicher Pflichtverletzung", "Abfindungszahlung", "Zustimmung aller Kollegen", "Nichts, Kündigung immer ohne Vorwarnung"],
     0, "Bei verhaltensbedingter Kündigung ist eine Abmahnung erforderlich (Ultima-ratio-Prinzip), da der Arbeitnehmer sein Verhalten ändern kann. Erst nach erneuter Pflichtverletzung: Kündigung.", "Perso Folie 06 Arbeitsrecht, S. 15-25"),
    ("Was regelt § 99 BetrVG (personelle Einzelmaßnahmen)?",
     ["Urlaubstage", "Einstellung/Eingruppierung/Versetzung: Betriebsrat hat Widerspruchsrecht, 1 Woche Frist", "Gehaltshöhe", "Nur Kündigungen"],
     1, "§ 99 BetrVG: Bei Einstellung, Ein-/Umgruppierung, Versetzung hat der Betriebsrat Widerspruchsrechte. Frist: 1 Woche, sonst gilt Zustimmung als erteilt.", "Perso Folie 06 Arbeitsrecht, S. 10-20"),
]
for q, o, c, s, src in perso_ar:
    add("perso", q, o, c, s, src)

# ============================================================
# Mathe - Grenzwerte und Stetigkeit - 6 neue Fragen
# ============================================================
mawi1_g = [
    ("Für B(y) = 60·e^(−1500/y): Wie groß ist lim_{y→∞} B(y) (Sättigungswert)?",
     ["0", "60", "∞", "1"],
     1, "Für y→∞ geht −1500/y gegen 0, also e^0 = 1 und B(y) → 60·1 = 60. Das ist der Sättigungswert des Butterverbrauchs.", "WiMa 1 Kap. 3 Grenzwerte und Stetigkeit, Folie 15-18"),
    ("Wie groß ist lim_{y→0+} 60·e^(−1500/y)?",
     ["60", "+∞", "0", "−∞"],
     2, "Für y→0+ strebt −1500/y gegen −∞; da e^(−∞)=0, ergibt sich der Grenzwert 0. Bei keinem Einkommen wird keine Butter konsumiert.", "WiMa 1 Kap. 3, Folie 15-18"),
    ("Mit Regel von l'Hospital: lim_{x→2} (3x²+3x−18)/(x−2) = ? (Typ 0/0)",
     ["0", "9", "15", "nicht auflösbar"],
     2, "Typ 0/0. Ableiten: (6x+3)/1, an x=2: 12+3 = 15. L'Hospital erlaubt das Ableiten von Zähler und Nenner separat.", "WiMa 1 Kap. 3, Folie 22-28; Blatt 9 Loesungen"),
    ("Bei einer rationalen Funktion im Unendlichen (∞/∞) empfiehlt sich:",
     ["Die kleinste Potenz ausklammern", "Die größte Potenz im Zähler und Nenner ausklammern, dann kürzen", "Sofort l'Hospital anwenden", "Zähler gleich null setzen"],
     1, "Bei ∞/∞ kürzt man die höchste Potenz; bei 0/0 (x→0) die kleinste Potenz. So lässt sich der Grenzwert direkt ablesen.", "WiMa 1 Kap. 3, Folie 20-25"),
    ("Die Funktion f(x) = 1/x hat an x₀ = 0 eine Polstelle. Was stimmt?",
     ["lim_{x→0+} f(x) = 0", "lim_{x→0+} = +∞ und lim_{x→0−} = −∞; Grenzwert existiert nicht", "Grenzwert existiert und ist 1", "f ist bei x=0 stetig"],
     1, "Von rechts → +∞, von links → −∞. Da links- und rechtseitiger Grenzwert verschieden sind, existiert der zweiseitige Grenzwert nicht. y-Achse ist senkrechte Asymptote.", "WiMa 1 Kap. 3, Folie 18-22"),
    ("Welche Aussage zum Verhältnis Stetigkeit und Differenzierbarkeit ist richtig?",
     ["Jede differenzierbare Funktion ist stetig und umgekehrt", "Stetigkeit ist nötig für Differenzierbarkeit; nicht jede stetige Funktion ist differenzierbar", "Beides völlig unabhängig", "Differenzierbarkeit ist Voraussetzung für Stetigkeit"],
     1, "Stetigkeit ist notwendig für Differenzierbarkeit. Die Betragsfunktion f(x)=|x| ist in x=0 stetig, aber NICHT differenzierbar (verschiedene links/rechts Steigungen).", "WiMa 1 Kap. 3, Folie 25-28"),
]
for q, o, c, s, src in mawi1_g:
    add("mawi1", q, o, c, s, src)

# ============================================================
# BWL - Buchführung Grundlagen - 6 neue Fragen
# ============================================================
bwl2_g = [
    ("Welcher Zweck erfüllt der Jahresabschluss?",
     ["Information der Konkurrenz über Strategien", "Information der Unternehmensführung + Bemessung von Steuer/Ausschüttungen", "Nur materielle Vermögensgegenstände", "Ersetzt die Inventur"],
     1, "Jahresabschluss: Informationsfunktion (Führung über Erfolg/Finanzlage) und Bemessungsfunktion (Steuern, Anteilseigner). Grundlage: Inventur und Bilanz.", "Foliensatz BUF Kap. 1-3, Zweck Jahresabschluss"),
    ("Was zeigt die Bilanz?",
     ["Aktivseite: Kapital, Passivseite: Vermögen", "Aktivseite: Vermögen, Passivseite: Kapital (Eigen + Fremd)", "Nur Erträge/Aufwendungen", "Nur flüssige Mittel"],
     1, "Aktiv = Vermögen (Mittelverwendung), Passiv = Kapital (Mittelherkunft). Anlage- + Umlaufvermögen = Eigenkapital + Fremdkapital.", "Foliensatz BUF Kap. 4, Bilanzaufbau"),
    ("Welche Position gehört zum Anlagevermögen?",
     ["Forderungen an Kunden", "Erworbene Softwarelizenzen und Geschäftsausstattung", "Spekulative Wertpapiere", "Handelswaren für Weiterverkauf"],
     1, "Anlagevermögen dient dauerhaft dem Geschäftsbetrieb (Software, BGA). Forderungen, spekulative Wertpapiere, Handelswaren = Umlaufvermögen.", "Foliensatz BUF Kap. 4, Anlagevermögen"),
    ("Was gehört zum Eigenkapital einer GmbH?",
     ["Rückstellungen", "Rücklagen und Stammeinlagen der Eigentümer", "Langfristige Forderungen", "Verbindlichkeiten aus Lieferungen"],
     1, "Eigenkapital = gezeichnetes Kapital (Stammeinlagen) + Rücklagen. Rückstellungen und Verbindlichkeiten = Fremdkapital. Forderungen = Vermögen.", "Foliensatz BUF Kap. 4, Eigenkapital"),
    ("Was ist die 'verlegte Inventur'?",
     ["Beliebig vor- oder zurückverlegbar", "Körperliche Aufnahme innerhalb von 3 Monaten vor/nach dem Stichtag; bei bestimmten Gütern unzulässig", "Nur an Wochenenden", "Nur für Anlagevermögen"],
     1, "Verlegte Inventur: Aufnahme kann innerhalb von 3 Monaten vor/nach Bilanzstichtag verlegt werden. Für leicht verderbliche Ware etc. unzulässig.", "Foliensatz BUF Kap. 4; Beispielklausur, Aufgabe 8"),
    ("Was gehört zu den flüssigen Mitteln?",
     ["Nur Kassenbestand", "Kassenbestand, Bankguthaben, Schecks", "Forderungen und Fuhrpark", "Rohstoffe und Grundstücke"],
     1, "Flüssige Mittel = Kasse, Bankguthaben, Schecks. Forderungen und Vorräte sind Umlaufvermögen, aber keine flüssigen Mittel.", "Foliensatz BUF Kap. 4; Beispielklausur, Aufgabe 1"),
]
for q, o, c, s, src in bwl2_g:
    add("bwl2", q, o, c, s, src)

# ============================================================
# BWL - Umsatzsteuer - 6 neue Fragen
# ============================================================
bwl2_u = [
    ("Beim Einkauf von Rohstoffen mit 19% MWSt entsteht:",
     ["Umsatzsteuer im Soll", "Vorsteuer im Soll und (später) Umsatzsteuer im Haben beim Verkauf", "Nur Aufwand ohne Steuerkonto", "Vorsteuer und Umsatzsteuer beide im Soll"],
     1, "Beim Einkauf: Vorsteuer (Aktivkonto, im Soll). Umsatzsteuer (Passivkonto, im Haben) entsteht erst beim VERKAUF/Ausgangsrechnung.", "Foliensatz BUF Kap. 10.2, Vorsteuer/Umsatzsteuer"),
    ("Wann entsteht ein Vorsteuerüberhang?",
     ["Wenn USt > VSt; Verbindlichkeit", "Wenn VSt > USt; Forderung gegenüber Finanzamt", "Nur bei steuerfreien Umsätzen", "Wird direkt mit Eigenkapital verrechnet"],
     1, "Überwiegt die Vorsteuer, schuldet das Finanzamt dem Unternehmen. Das ist eine Forderung (Aktivposten). Bei USt > VSt: Zahllast (Verbindlichkeit).", "Foliensatz BUF Kap. 10.2; Beispielklausur, Aufgabe 8"),
    ("Skonto von 2% auf 15.000 € netto. Wie hoch ist die Vorsteuerkorrektur?",
     ["300 €", "570 €", "57 €", "2.850 €"],
     2, "Skonto = 2% von 15.000 € = 300 € netto. Steuerkorrektur = 19% von 300 € = 57 €. Der steuerpflichtige Warenwert verringert sich um den Skontobetrag.", "Foliensatz BUF Kap. 10.2; Beispielklausur, Aufgabe 2"),
    ("Welche Kontonummern gelten im Standard-Kontenplan für Vorsteuer/Umsatzsteuer?",
     ["Vorsteuer 2600, Umsatzsteuer 4800", "Vorsteuer 4800, Umsatzsteuer 2600", "Beide unter 4800", "Vorsteuer 2400, Umsatzsteuer 4400"],
     0, "2600 = Vorsteuer (VOS, Aktivkonto). 4800 = Umsatzsteuer (UMS, Passivkonto). 2400/4400 sind Forderungen/Verbindlichkeiten.", "Foliensatz BUF; Kontenplan Klausur"),
    ("Welche Umsatzsteuersätze gelten in Deutschland?",
     ["19% regulär, 7% ermäßigt", "16% regulär, 5% ermäßigt", "20% regulär, 10% ermäßigt", "19% regulär, 0% ermäßigt"],
     0, "Regulärer Steuersatz 19%, ermäßigter 7% (z.B. Lebensmittel, Bücher). Beide können in Klausuraufgaben relevant sein.", "Foliensatz BUF Kap. 10.2, Steuersätze"),
    ("Produktionsanlage für 30.000 € netto + 19% MWSt auf Ziel. Wie wird gebucht?",
     ["Anlage 30.000 €, Vorsteuer 5.700 €", "Anlage 35.700 €, Vorsteuer 5.700 €", "Anlage 30.000 €, Vorsteuer 0 €", "Anlage 35.700 €, Vorsteuer 0 €"],
     0, "Anlage wird netto (30.000 €) aktiviert, Vorsteuer (19% von 30.000 = 5.700 €) ist separater Aktivposten. Zu zahlen: 35.700 €.", "Foliensatz BUF Kap. 10.2; Beispielklausur, Aufgabe 2"),
]
for q, o, c, s, src in bwl2_u:
    add("bwl2", q, o, c, s, src)

# ============================================================
# BWL - Privatkonten - 6 neue Fragen
# ============================================================
bwl2_p = [
    ("Bei welchen Rechtsformen wird ein Privatkonto geführt?",
     ["Bei allen, auch GmbH und AG", "Nur bei Personenunternehmen (Einzelunternehmen, Personengesellschaften)", "Nur bei Kapitalgesellschaften", "Nur bei Vereinen"],
     1, "Privatentnahmen/-einlagen gibt es nur bei Personenunternehmen. Kapitalgesellschaften haben keine Privatkonten (Trennung von Rechts- und Vermögenspersönlichkeit).", "Foliensatz BUF Kap. 12-13, Privatkonto"),
    ("Einzelunternehmer entnimmt 400 € aus der Kasse. Buchungssatz?",
     ["Soll Kasse / Haben Priv", "Soll Priv / Haben Kasse", "Soll Priv / Haben Eigenkapital", "Soll Kasse / Haben Eigenkapital"],
     1, "Entnahmen stehen im SOLL des Privatkontos, Kasse wird im HABEN gemindert. Buchungssatz: Priv (Soll) an Kasse (Haben).", "Foliensatz BUF Kap. 12-13; Beispielklausur, Aufgabe 3"),
    ("Überweisung von 10.000 € privater Ersparnisse auf Betriebsbankkonto. Buchungssatz?",
     ["Soll Bank / Haben Priv", "Soll Priv / Haben Bank", "Soll Bank / Haben Eigenkapital", "Soll Eigenkapital / Haben Bank"],
     0, "Einlagen stehen im HABEN des Privatkontos. Bank wird im SOLL erhöht: Bank (Soll) an Priv (Haben).", "Foliensatz BUF Kap. 12-13; Beispielklausur, Aufgabe 3"),
    ("Jahresabschluss Privatkonto: Entnahmen (Soll) > Einlagen (Haben). Wie wird abgeschlossen?",
     ["Soll GuV / Haben Priv", "Soll Priv / Haben GuV", "Soll Eigenkapital / Haben Priv", "Soll Priv / Haben Eigenkapital"],
     2, "Bei Sollüberschuss (mehr Entnahmen als Einlagen) mindert das Eigenkapital. Abschluss: Eigenkapital (Soll) an Priv (Haben).", "Foliensatz BUF Kap. 12-13; Beispielklausur, Aufgabe 3"),
    ("GuV-Konto zeigt Habenüberschuss (Erlöse > Aufwendungen = Gewinn). Abschluss?",
     ["Soll Eigenkapital / Haben GuV", "Soll GuV / Haben Eigenkapital", "Soll GuV / Haben Priv", "Soll Bank / Haben GuV"],
     1, "Habenüberschuss im GuV = Gewinn, der das Eigenkapital ERHÖHT. Abschluss: GuV (Soll) an Eigenkapital (Haben).", "Foliensatz BUF Kap. 12-13; Beispielklausur, Aufgabe 3"),
    ("GuV: 470.000 € Soll, 525.000 € Haben. Wie hoch ist der Gewinn?",
     ["Verlust 55.000 €", "Gewinn 55.000 €", "Gewinn 5.000 €", "Gewinn 0 €"],
     1, "Habenüberschuss = 525.000 - 470.000 = 55.000 € = Gewinn. GuV (Soll) an Eigenkapital (Haben) 55.000 €.", "Foliensatz BUF Kap. 12-13; Beispielklausur, Aufgabe 3"),
]
for q, o, c, s, src in bwl2_p:
    add("bwl2", q, o, c, s, src)

# ============================================================
# Speichern
# ============================================================
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(QS, f, ensure_ascii=False, indent=2)

# Statistik
print("✅ Fragen hinzugefügt:")
for bank in QS:
    print(f"  {bank}: {len(QS[bank])} Fragen")
total = sum(len(v) for v in QS.values())
print(f"\nTOTAL: {total} Fragen")
