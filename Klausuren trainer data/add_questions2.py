"""Fügt 22 neue Fragen aus Statistik-Vorlesungen und WPR-Sachenrecht hinzu."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "_data", "questions_validated.json")

with open(PATH, "r", encoding="utf-8") as f:
    QS = json.load(f)

def add(bank, q, opts, correct_idx, solution, source):
    QS[bank].append({"q": q, "o": opts, "c": correct_idx, "s": solution, "src": source})

# ============================================================
# MAWI2 - Verteilungen (6 Fragen)
# ============================================================
add("mawi2",
    "Welches Darstellungsprinzip gilt für die Verteilung einer diskreten Variablen im Säulendiagramm?",
    ["Die Säulenbreite entspricht der relativen Häufigkeit", "Die Säulenhöhe entspricht der relativen Häufigkeit", "Die Säulenfläche entspricht der relativen Häufigkeit", "Die Anzahl der Säulen entspricht der relativen Häufigkeit"],
    1, "Bei diskreten Variablen gilt im Säulendiagramm: Säulenhöhe = relative Häufigkeit. Flächenprinzip gilt erst bei Histogrammen stetiger Merkmale.", "Statistik Kap. 2")

add("mawi2",
    "Bei einem Histogramm (klassifiziertes Merkmal) entspricht die relative Häufigkeit welcher Größe?",
    ["Der Höhe der Säule", "Der Breite der Säule", "Der Fläche des Rechtecks", "Der Anzahl der Klassen"],
    2, "Beim Histogramm gilt das FLÄCHENprinzip: Fläche = relative Häufigkeit. Die Höhe wird als Dichtefunktion f(x) bezeichnet.", "Statistik Kap. 2")

add("mawi2",
    "Was gilt für die Dichtefunktion f(x) eines klassifizierten Merkmals?",
    ["Kann höchstens den Wert 1 annehmen", "Ist identisch mit H(x)", "Kann auch Werte über 1 annehmen", "Ist stets konstant über alle Klassen"],
    2, "Eine Dichte kann Werte über 1 annehmen, da sie als Höhe definiert ist. Die FLÄCHE (nicht Höhe) summiert sich zur Häufigkeit.", "Statistik Kap. 2")

add("mawi2",
    "Welche mathematische Beziehung besteht zwischen kumulierter Verteilung H(x) und Dichtefunktion f(x)?",
    ["f(x) = H(x) · x", "H'(x) = f(x)", "f(x) = H(x)²", "f(x) = H(x) + x"],
    1, "Die Steigung der kumulierten Verteilung ist die Dichtefunktion: H'(x) = f(x). H(x) ist stetig, monoton wachsend, stückweise linear.", "Statistik Kap. 2")

add("mawi2",
    "20 Pendler: Klasse 0-5 km hat 5 Personen. Wie groß ist die relative Häufigkeit?",
    ["0,05", "0,20", "0,25", "0,50"],
    2, "h = Anzahl in Klasse / Gesamtanzahl = 5/20 = 0,25. Die Klassenbreite spielt für die relative Häufigkeit keine Rolle.", "Statistik Kap. 2")

add("mawi2",
    "Welche Eigenschaft hat die kumulierte Verteilungsfunktion H(x) bei einem Histogramm?",
    ["Stückweise konstant mit Sprüngen", "Stetig, monoton wachsend, stückweise linear", "Stets fallende Funktion", "Identisch mit f(x)"],
    1, "H(x) beschreibt den Anteil der Objekte mit Merkmal ≤ x. Im Histogramm ergibt sich ein ansteigender Polygonzug ohne Sprünge.", "Statistik Kap. 2")

# ============================================================
# MAWI2 - Streuungsmaße (4 Fragen)
# ============================================================
add("mawi2",
    "Welche Eigenschaft hat die Varianz σ² bezüglich der Einheit?",
    ["Gleiche Einheit wie X", "Wurzel aus der Standardabweichung", "Quadrierte Einheit von X", "Stets kleiner als δ"],
    2, "Da Abstände quadratisch gemessen werden, hat die Varianz die QUADRIERTE Einheit (z.B. Liter²). σ = �√σ² hat wieder die Einheit von X.", "Statistik Kap. 5")

add("mawi2",
    "Urliste 150, 180, 230, 240 (Mittelwert 200). Wie groß ist die Varianz?",
    ["35", "36,74", "1350", "5400"],
    2, "σ² = [(−50)²+(−20)²+30²+40²]/4 = (2500+400+900+1600)/4 = 5400/4 = 1350. σ ≈ 36,74.", "Statistik Kap. 5")

add("mawi2",
    "Welcher Lageparameter minimiert die mittlere absolute Abweichung, welcher die quadratische?",
    ["Beide: Median", "Median (absolut) / arithm. Mittel (quadratisch)", "Arithm. Mittel (absolut) / Median (quadratisch)", "Beide: arithm. Mittel"],
    1, "Bei absoluten Abweichungen optimiert der Median, bei quadratischen Abweichungen das arithmetische Mittel.", "Statistik Kap. 5")

add("mawi2",
    "Wie unterscheidet sich die Standardabweichung σ von der mittleren Abweichung δ?",
    ["σ = δ immer", "σ < δ immer", "σ ≠ δ (unterschiedliche Formeln)", "σ = 2δ"],
    2, "Wurzel aus mittlerer Quadratsumme ≠ mittlere Betragssumme. Im Beispiel: σ ≈ 36,74, δ = 35.", "Statistik Kap. 5")

# ============================================================
# MAWI2 - Indexzahlen (3 Fragen)
# ============================================================
add("mawi2",
    "Beim Laspeyres-Preisindex bleiben welche Größen konstant?",
    ["Preise der Berichtsperiode", "Mengen der Basisperiode", "Mengen der Berichtsperiode", "Umsätze der Basisperiode"],
    1, "Laspeyres vergleicht Basismengen zu Berichts-/Basispreisen – die Mengen der Basisperiode bleiben konstant (Ceteris paribus).", "Statistik Kap. 6")

add("mawi2",
    "Ein Umsatzindex ergibt 0,7297. Was bedeutet das?",
    ["Umsatz stieg um 72,97%", "Umsatz blieb konstant", "Umsatz ging um ca. 27,03% zurück", "Umsatz stieg um 27,03%"],
    2, "Index unter 1 = Rückgang. 1 − 0,7297 = 0,2703, also Umsatzrückgang um ca. 27,03%.", "Statistik Kap. 6")

add("mawi2",
    "Warum gibt es bei 'Wie stark haben sich Preise veraendert?' keine eindeutige Antwort?",
    ["Preise sind gesetzlich festgelegt", "Verschiedene Modelle (Laspeyres vs. Paasche) liefern unterschiedliche Ergebnisse", "Preise sind nicht vergleichbar", "Es gibt nur den Umsatzindex"],
    1, "Der Preisindex hängt vom Warenkorb ab (Basis- vs. Berichtsmengen). Laspeyres und Paasche liefern unterschiedliche Werte.", "Statistik Kap. 6")

# ============================================================
# MAWI2 - Lageparameter (2 Fragen)
# ============================================================
add("mawi2",
    "Wie ist der Median formal definiert?",
    ["h(X = xme) ≥ 0,50", "h(X ≤ xme) ≥ 0,50 UND h(X ≥ xme) ≥ 0,50", "xme = Summe aller Werte / N", "xme ist der häufigste Wert"],
    1, "Der Median teilt die Grundgesamtheit in der Mitte: h(X ≤ xme) ≥ 0,50 UND h(X ≥ xme) ≥ 0,50.", "Statistik Kap. 4")

add("mawi2",
    "Wie lautet die formale Definition eines p-Quantils xp?",
    ["h(X = xp) ≥ p", "h(X ≤ xp) ≥ p UND h(X ≥ xp) ≥ 1−p", "xp = p · x̄", "h(X ≤ xp) = 1−p"],
    1, "Ein p-Quantil teilt im Verhältnis p:(1−p): h(X ≤ xp) ≥ p und h(X ≥ xp) ≥ 1−p. Für p=0,5 → Median.", "Statistik Kap. 4")

# ============================================================
# WPR - Sachenrecht (6 Fragen)
# ============================================================
add("wpr",
    "Woraus wird Besitz nach § 854 Abs. 1 BGB erworben?",
    ["Durch bloßen Vertrag", "Durch bewusste Erlangung der tatsächlichen Sachherrschaft", "Durch Eintragung im Grundbuch", "Durch Verfügungsberechtigung"],
    1, "§ 854 I BGB: Besitz = Erlangung der tatsächlichen Sachherrschaft. Besitz ist rein faktisch, nicht rechtlich.", "WPR Foliensatz Kap. 8, § 854 BGB")

add("wpr",
    "Wer ist Besitzdiener nach § 855 BGB?",
    ["Der Eigentümer der Sache", "Übt Sachherrschaft kraft Weisung eines anderen aus, ist selbst kein Besitzer", "Stets mittelbarer Besitzer", "Muss im Handelsregister stehen"],
    1, "Besitzdiener übt die Sachherrschaft in sozialer Abhängigkeitsverhältnis (kraft Weisung) aus. Er ist kein mittelbarer Besitzer.", "WPR Foliensatz Kap. 8, § 855 BGB")

add("wpr",
    "Was regelt § 903 BGB (Inhalt des Eigentums)?",
    ["Erwerb des mittelbaren Besitzes", "Übertragung durch Einigung und Übergabe", "Befugnis des Eigentümers, nach Belieben zu verfügen und andere auszuschließen", "Pflicht zur Herausgabe"],
    2, "§ 903 BGB: Eigentümer darf mit der Sache nach Belieben verfahren und andere von jeder Einwirkung ausschließen (soweit nicht Gesetz/Rechte Dritter).", "WPR Foliensatz Kap. 8, § 903 BGB")

add("wpr",
    "Welche Voraussetzungen braucht die Übereignung beweglicher Sachen (§ 929 BGB)?",
    ["Nur notarieller Kaufvertrag", "Einigung, Übergabe, Einigsein, Verfügungsberechtigung", "Grundbuch-Eintragung", "Besitzkonstitut zwingend"],
    1, "§ 929: Einigung (dinglicher Vertrag) + Übergabe + dass Einigung bei Übergabe noch besteht + Verfügungsberechtigung.", "WPR Foliensatz Kap. 8, § 929 BGB")

add("wpr",
    "Wann kann ein Gutgläubiger Eigentum erwerben, obwohl Veräußerer NICHT Eigentümer ist (§§ 932 ff. BGB)?",
    ["Nur bei notariellem Vertrag", "Verkehrsgeschäft, guter Glaube (vermutet, § 932 II), Sache nicht abhandengekommen (§ 935)", "Ausschließlich bei gestohlenen Sachen", "Nur bei Handelsregister-Eintragung"],
    1, "Gutgläubiger Erwerb: Verkehrsgeschäft + guter Glaube (vermutet) + Sache nicht abhandengekommen (§ 935). Bei Abhandenkommen: kein Schutz.", "WPR Foliensatz Kap. 8, §§ 932-935 BGB")

add("wpr",
    "Was ist ein Eigentumsvorbehalt rechtlich?",
    ["Unverbindliches Zahlungsversprechen", "Bedingtes Rechtsgeschäft: Eigentumsübertragung nach § 158 I bis zur vollständigen Zahlung bedingt", "Grundbuch-Eintragung nach § 873", "Sofortiger Eigentumsübergang"],
    1, "Eigentumsvorbehalt: Eigentumsübertragung (§§ 929, 158 I BGB) unter aufschiebender Bedingung = vollständige Kaufpreiszahlung.", "WPR Foliensatz Kap. 8, § 158 I BGB")

# Speichern
with open(PATH, "w", encoding="utf-8") as f:
    json.dump(QS, f, ensure_ascii=False, indent=2)

print("✅ Neue Fragen hinzugefügt:")
for bank in QS:
    print(f"  {bank}: {len(QS[bank])} Fragen")
total = sum(len(v) for v in QS.values())
print(f"\nTOTAL: {total} Fragen")
