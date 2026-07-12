"""
Erstellt _data/topics.json mit themenbasierten Lern-Einheiten.
Filter-Strategie: Array von String-Prefixen, first-match-wins.
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

TOPICS = {
    # ===================== VWL =====================
    "vwl": [
        {
            "id": "vwl_B", "name": "Was ist VWL & Denken wie ein Volkswirt", "icon": "🧠",
            "filter": ["VWL Kap. B", "VWL Kap. A"],
            "explanation": """## Denken wie ein Volkswirt

### Methodische Grundlagen
VWL untersucht, wie Gesellschaften knappe Ressourcen allozieren. Im Gegensatz zu Naturwissenschaften sind **kontrollierte Experimente** oft nicht durchführbar (ethisch, praktisch).

### Zentrale Herausforderungen
1. **Ausgelassene Variablen** (omitted variable bias): Ein scheinbarer Zusammenhang verschwindet, wenn eine dritte Variable berücksichtigt wird.
2. **Umgekehrte Kausalität** (reverse causality): Ursache und Wirkung sind unklar.
3. **Ethische Grenzen**: Viele Experimente wären unmoralisch.

### Lösung: Natürliche Experimente
Ökonomen nutzen „natürliche Experimente" (z.B. Gesetzesänderungen, Naturkatastrophen), um kausale Schlüsse zu ziehen.

### Positiv vs. Normativ
- **Positive Ökonomik**: Beschreibt, was IST (objektiv prüfbar)
- **Normative Ökonomik**: Beschreibt, was SEIN SOLLTE (Werturteil)"""
        },
        {
            "id": "vwl_C", "name": "Angebot und Nachfrage", "icon": "📈",
            "filter": ["VWL Kap. C"],
            "explanation": """## Angebot und Nachfrage

### Das Gesetz der Nachfrage
**Ceteris paribus**: Steigt der Preis, sinkt die nachgefragte Menge (negative Steigung der Nachfragekurve D).
- **Substitutionseffekt**: Konsumenten weichen auf billigere Alternativen aus
- **Einkommenseffekt**: Höherer Preis = weniger Kaufkraft

### Das Gesetz des Angebots
Steigt der Preis, steigt die angebotene Menge (positive Steigung der Angebotskurve S).

### Marktgleichgewicht
Schnittpunkt von Angebot und Angebot: **Gleichgewichtspreis P\\*** und **Gleichgewichtsmenge Q\\***.

- Preis **über** P\\* → **Angebotsüberschuss** (Überschuss): Angebot > Nachfrage
- Preis **unter** P\\* → **Nachfrageüberschuss** (Knappheit): Nachfrage > Angebot

### Güterarten
| Güterart | Eigenschaft | Beispiel |
|----------|-------------|----------|
| **Komplemente** | Werden gemeinsam konsumiert | Auto & Benzin |
| **Substitute** | Ersetzen einander | Butter & Margarine |
| **Normal** | Bei Einkommen↑ → Nachfrage↑ | Bio-Lebensmittel |
| **Inferior** | Bei Einkommen↑ → Nachfrage↓ | Billigprodukte |

**Komplemente**: Steigt Preis von Gut A → sinkt Nachfrage nach Gut B
**Substitute**: Steigt Preis von Gut A → STEIGT Nachfrage nach Gut B"""
        },
        {
            "id": "vwl_D", "name": "Effizienz und Wohlfahrt", "icon": "⚖️",
            "filter": ["VWL Kap. D"],
            "explanation": """## Konsumenten- und Produzentenrente

### Konsumentenrente (KR)
Differenz zwischen dem, was Konsumenten **maximal zahlen würden** (Fläche unter D-Kurve), und dem, was sie **tatsächlich zahlen** (Marktpreis).

> KR = Fläche unter der Nachfragekurve und über dem Marktpreis

### Produzentenrente (PR)
Differenz zwischen dem Marktpreis und den minimalen Grenzkosten (Bereitschaft zu verkaufen).

> PR = Fläche über der Angebotskurve und unter dem Marktpreis

### Gesamtrente (Wohlfahrt)
**W = KR + PR** ist im Wettbewerbsgleichgewicht maximal. Das ist dasEffizienztheorem: Freie Märkte allozieren Ressourcen effizient."""
        },
        {
            "id": "vwl_E", "name": "Preiskontrollen und Steuern", "icon": "🏛️",
            "filter": ["VWL Kap. E"],
            "explanation": """## Preiskontrollen und Steuern

### Preisobergrenze (Höchstpreis / Price Ceiling)
Staatlicher Maximalpreis **unterhalb** des Gleichgewichtspreises → **Knappheit** (Nachfrage > Angebot).
Beispiel: Mietpreisbremse.

### Preisuntergrenze (Mindestpreis / Price Floor)
Staatlicher Minimalpreis **oberhalb** des Gleichgewichts → **Überschuss** (Angebot > Nachfrage).
Beispiel: Mindestlohn, agrarische Garantiepreise.

### Steuern
Eine **Mengensteuer** verschiebt die Angebotskurve um den Steuerbetrag nach oben.

**Nettowohlfahrtsverlust (Deadweight Loss, DWL)**: Dreieck zwischen alter und neuer Menge. Er entsteht, weil die Steuer Transaktionen verhindert, die ohne Steuer vorteilhaft gewesen wären.

> DWL ist umso GRÖSSER, je **elastischer** Angebot und Nachfrage sind (mehr Transaktionen fallen weg).

### Steuerlast
Die Seite mit der **geringeren Elastizität** trägt den größeren Teil der Steuerlast (kann weniger ausweichen)."""
        },
        {
            "id": "vwl_F", "name": "Externalitäten und öffentliche Güter", "icon": "🌱",
            "filter": ["VWL Kap. F"],
            "explanation": """## Externalitäten und öffentliche Güter

### Externalitäten
Wirkungen auf Dritte, die nicht über den Preis abgerechnet werden.

**Negative Externalität** (z.B. Umweltverschmutzung):
- Soziale Grenzkosten (SK) = private Grenzkosten (PK) + externer Schaden
- SK-Kurve liegt **über** der privaten Angebotskurve
- Markt produziert **zu viel** (Mengen Q_Markt > Q_optimal)

### Pigou-Steuer
Steuer in Höhe des externen Grenzschadens verschiebt PK-Kurve nach oben → entspricht SK-Kurve → effiziente Menge.

### Coase-Theorem
Bei **klaren Eigentumsrechten** und **vernachlässigbaren Transaktionskosten** führen private Verhandlungen zu effizientem Ergebnis (unabhängig von Eigentumsverteilung). Grenzen: viele Beteiligte, hohe Transaktionskosten.

### Güterklassifikation
| Typ | Ausschließbar? | Rivalisierend? | Beispiel |
|-----|----------------|----------------|----------|
| **Privat** | Ja | Ja | Brot |
| **Club** | Ja | Nein | Netflix |
| **Allmende** | Nein | Ja | Fischgründe |
| **Öffentlich** | Nein | Nein | Landesverteidigung |

**Trittbrettfahrerproblem**: Bei öffentlichen Gütern will niemand zahlen → Marktversagen."""
        },
        {
            "id": "vwl_G", "name": "Handel und Handelsbeschränkungen", "icon": "🌍",
            "filter": ["VWL Kap. G"],
            "explanation": """## Internationaler Handel

### Komparativer Vorteil (Ricardo)
Ein Land soll sich auf die Güter spezialisieren, bei denen es die **geringsten Opportunitätskosten** hat (nicht zwingend die absolut niedrigsten Kosten).

Durch Spezialisierung und Handel können BEIDE Länder über das Autarkie-Niveau hinaus konsumieren.

### Argumente für Freihandel
- Niedrigere Preise, mehr Produktvielfalt
- Skaleneffekte, Innovation

### Argumente gegen Freihandel
- **Infant-Industry-Argument**: Junge Industrien brauchen Schutz
- Beschäftigung, nationale Sicherheit, Umweltschutz

### Handelsbeschränkungen
**Zölle** verteuern Importe → Preis steigt → inländische Produktion steigt, Importe sinken. Entspricht einer Steuer → erzeugt Wohlfahrtsverlust."""
        },
        {
            "id": "vwl_H", "name": "BIP, Inflation und Messgrößen", "icon": "📊",
            "filter": ["VWL Kap. H", "VWL Kap. I"],
            "explanation": """## BIP und Inflation

### Bruttoinlandsprodukt (BIP)
Gesamtwert aller **endgültigen** in einer Volkswirtschaft innerhalb einer Periode produzierten Güter und Dienstleistungen.

> BIP = Konsum (C) + Investitionen (I) + Staatsausgaben (G) + Nettoexporte (NX = Ex - Im)

### BIP vs. BNE
- **BIP** = **Inlandsprinzip**: Produktion INNERHALB der Landesgrenzen
- **BNE** (Bruttonationaleinkommen) = **Inländerprinzip**: Produktion von Inländern weltweit

### Inflation
Anhaltender **Anstieg** des allgemeinen Preisniveaus.

| Begriff | Bedeutung |
|---------|-----------|
| **Deflation** | Sinkendes Preisniveau |
| **Disinflation** | Verlangsamung der Inflationsrate |
| **Stagflation** | Inflation + stagnierendes Wachstum |
| **Realzins** | Nominalzins minus Inflationsrate |

### Verbraucherpreisindex (VPI)
Misst Preisentwicklung eines repräsentativen Warenkorbs. Wichtigstes Inflationsmaß (Basisjahr = 100%)."""
        },
    ],

    # ===================== PERSO =====================
    "perso": [
        {
            "id": "perso_02", "name": "Cross-Cultural Management", "icon": "🌏",
            "filter": ["Perso Folie 02 CrossCultural"],
            "explanation": """## Cross-Cultural Management

### Kulturelle Dimensionen (Hofstede)
Geert Hofstede unterscheidet 6 Kulturdimensionen:

1. **Machtdistanz** (Power Distance): Akzeptanz ungleicher Machtverteilung
2. **Individualismus vs. Kollektivismus**
3. **Maskulinität vs. Feminität** (Leistung vs. Fürsorge)
4. **Unsicherheitsvermeidung** (Uncertainty Avoidance)
5. **Langfrist- vs. Kurzfristorientierung**
6. **Indulgence vs. Restraint** (Genuss vs. Kontrolle)

### Kulturschock-Phasen
1. Euphorie (Honeymoon)
2. Frustration / Kulturschock
3. Anpassung
4. Akzeptanz / Biculturalism

### Cross-Cultural Training
Sensibilisierung für kulturelle Unterschiede, um Missverständnisse in internationalen Teams zu vermeiden."""
        },
        {
            "id": "perso_03", "name": "Kommunikation", "icon": "💬",
            "filter": ["Perso Folie 03 Kommunikation"],
            "explanation": """## Kommunikation

### Kommunikationsmodelle
**Sender-Empfänger-Modell**: Sender → Kodierung → Kanal → Dekodierung → Empfänger. Störquellen (Rauschen) können überall auftreten.

### 4 Seiten einer Nachricht (Schulz von Thun)
1. **Sachinhalt**: Was wird faktisch mitgeteilt?
2. **Selbstoffenbarung**: Was sagt der Sender über sich selbst?
3. **Beziehung**: Wie steht der Sender zum Empfänger?
4. **Appell**: Was will der Sender erreichen?

### Aktives Zuhören
- Paraphrasieren (Inhalt wiedergeben)
- Verbalisieren (Gefühle ansprechen)
- Nachfragen

### Barrieren
Selektive Wahrnehmung, Werturteile, semantische Störungen, kulturelle Unterschiede."""
        },
        {
            "id": "perso_04", "name": "Führung", "icon": "👤",
            "filter": ["Perso Folie 04 Führung", "Perso Menti 10 Fuehrungsspanne"],
            "explanation": """## Führung

### Führungstheorien
1. **Eigenschaftstheorie** (Trait): Führer haben bestimmte Persönlichkeitsmerkmale
2. **Verhaltenstheorie**: Aufgaben- vs. personenorientiert
3. **Situationstheorie**: Führung muss zur Situation passen

### Situative Führung (Hersey/Blanchard)
Abhängig vom **Reifegrad** der Mitarbeiter:

| Reifegrad | Stil |
|-----------|------|
| Niedrig (R1) | Anweisen (directing) |
| Mittel (R2) | Überzeugen (selling) |
| Hoch (R3) | Partizipieren (participating) |
| Sehr hoch (R4) | Delegieren (delegating) |

### Management vs. Führung
- **Management**: Dinge richtig tun (Prozesse, Effizienz)
- **Führung**: Die richtigen Dinge tun (Vision, Strategie)

### Transformationale vs. transaktionale Führung
- **Transaktional**: Tausch „Leistung gegen Belohnung"
- **Transformational**: Inspiration, Vision, Entwicklung"""
        },
        {
            "id": "perso_05", "name": "Team und Konflikt", "icon": "👥",
            "filter": ["Perso Folie 05 TeamKonflikt", "Perso Klausur 71007", "Perso Menti 09 Grundlagen"],
            "explanation": """## Teams und Konflikte

### Teamentwicklung (Tuckman)
1. **Forming**: Kennenlernen, Höflichkeit
2. **Storming**: Konflikte, Machtkämpfe
3. **Norming**: Regeln, Konsens
4. **Performing**: Leistung, Zusammenarbeit
5. **Adjourning**: Auflösung

### Konfliktarten
- **Sachkonflikt**: Verschiedene Meinungen zur Aufgabe
- **Beziehungskonflikt**: Persönliche Spannungen
- **Wertkonflikt**: Unterschiedliche Werte/Normen
- **Verteilungskonflikt**: Kampf um Ressourcen

### Konfliktstile (Thomas-Kilmann)
| Stil | Durchsetzungsgrad | Kooperationsgrad |
|------|-------------------|------------------|
| Konkurrenz | Hoch | Niedrig |
| Nachgeben | Niedrig | Hoch |
| Vermeiden | Niedrig | Niedrig |
| Kompromiss | Mittel | Mittel |
| Kooperation | Hoch | Hoch (Win-Win) |

### Vorteile von Teams
Synergieeffekte,互补 skills, bessere Entscheidungen (vielfältige Perspektiven)."""
        },
        {
            "id": "perso_06", "name": "Arbeitsrecht", "icon": "⚖️",
            "filter": ["Perso Folie 06 Arbeitsrecht"],
            "explanation": """## Arbeitsrecht

### Quellen
- **BGB** (Dienstvertrag § 611 ff.)
- **HGB** (für Handlungsgehilfen)
- **Tarifverträge**, **Betriebsvereinbarungen**
- **Einzelarbeitsvertrag**

### Allgemeines Gleichbehandlungsgesetz (AGG)
Diskriminierung wegen Rasse, ethnischer Herkunft, Geschlecht, Religion, Weltanschauung, Behinderung, Alter oder sexueller Identität ist verboten.

### Grundpflichten
- Arbeitgeber: Vergütung, Fürsorge
- Arbeitnehmer: Arbeitsleistung, Treue

### Kündigung
- **Fristen**: Probezeit 2 Wochen, danach nach Betriebszugehörigkeit (steigend)
- **Kündigungsschutz** (KSchG) ab 6 Monaten + 10 Mitarbeiter
- **Arten**: ordentlich, außerordentlich (fristlos), Änderungskündigung"""
        },
        {
            "id": "perso_07", "name": "Motivation", "icon": "🔥",
            "filter": ["Perso Folie 07 Motivation"],
            "explanation": """## Motivation

### Inhaltstheorien (Was motiviert?)

**Maslow** – Bedürfnispyramide:
1. Physische Bedürfnisse
2. Sicherheit
3. Soziale Bedürfnisse
4. Wertschätzung
5. Selbstverwirklichung

**Herzberg** – Zweifaktorentheorie:
- **Hygienefaktoren** (verhindern Unzufriedenheit): Gehalt, Bedingungen, Sicherheit
- **Motivatoren** (erzeugen Zufriedenheit): Anerkennung, Verantwortung, Sinn

### Prozesstheorien (Wie entsteht Motivation?)

**Vroom – VIE-Theorie**:
> Motivation = Valenz × Instrumentalität × Erwartung

**Equity-Theorie** (Adams): Vergleiche Input/Output mit anderen (Gerechtigkeit).

### intrinsisch vs. extrinsisch
- **Intrinsisch**: Aus der Tätigkeit selbst (Freude, Sinn)
- **Extrinsisch**: Äußere Anreize (Geld, Status)"""
        },
        {
            "id": "perso_08", "name": "Personalmanagement", "icon": "🎯",
            "filter": ["Perso Folie 08 Personalbeschaffung", "Perso Folie 08 Personalentwicklung", "Perso Folie 08-2 Performance"],
            "explanation": """## Personalmanagement

### Personalbeschaffung (Recruitment)
- **Intern**: Beförderung, Versetzung, Stellenanzeigen im Intranet
- **Extern**: Jobbörsen, Headhunter, Hochschulmarketing

**Schritte**: Personalbedarf → Anzeige → Auswahl → Einstellung

### Auswahlverfahren
- Bewerbungsunterlagen
- Interviews (strukturiert > unstrukturiert)
- Assessment Center
- Tests (kognitiv, Persönlichkeit)

### Personalentwicklung
Qualifizierung durch Schulung, Coaching, Job Rotation. Ziel: Kompetenzaufbau, Bindung.

### Performance Management
Systematische Beurteilung der Mitarbeiterleistung.
- **Ziele**: leistungsbezogene Vergütung, Entwicklung, Feedback
- **Kritik**: Subjektivität, Einfluss des Vorgesetzten

### New Work Konzepte
Agile Arbeit, Remote Work, 4-Tage-Woche, Sinnorientierung."""
        },
        {
            "id": "perso_09_10", "name": "Organisation und Aufbauorganisation", "icon": "🏢",
            "filter": ["Perso Folie 09 Grundlagen", "Perso Folie 09-10", "Perso Folie 10 Aufbauorganisation"],
            "explanation": """## Organisation

### Grundlagen
Organisation = dauerhafte Regelung der Aufgabenerfüllung. Unterschieden:
- **Aufbauorganisation**: Wer macht was? (Struktur)
- **Ablauforganisation**: Wie/Wann wird es gemacht? (Prozesse)

### Einlinienorganisation
Jeder Mitarbeiter hat EINEN Vorgesetzten. Klarheit, aber Überlastung bei Spitze.

### Mehrlinienorganisation
Mehrere Weisungsbefugnisse (Funktionsspezialisten). Gefahr: widersprüchliche Anweisungen.

### Matrixorganisation
Schnittstelle von Funktion und Produkt/Projekt. Doppelte Unterstellung → Konflikte, aber Flexibilität.

### Divisionale Organisation (Sparten)
Gliederung nach Produkten, Regionen oder Kundengruppen. Dezentral, marktnah.

### Stäbe
Beratende Einheiten ohne Weisungsbefugnis (z.B. Rechtsabteilung, Controlling).

### Vor-/Nachteile
- **Zentralisation**: Standardisierung, Skaleneffekte
- **Dezentralisation**: Marktnähe, Flexibilität"""
        },
        {
            "id": "perso_11", "name": "Organisationsentwicklung", "icon": "🔄",
            "filter": ["Perso Folie 11 Organisationsentwicklung"],
            "explanation": """## Organisationsentwicklung (OE)

### Definition
Geplanter, systematischer Wandel von Organisationen zur Steigerung der Problemlösungsfähigkeit.

### Phasen des Wandels (Lewin)
1. **Auftauen** (Unfreezing): Alte Strukturen hinterfragen
2. **Verändern** (Changing): Neue Lösungen implementieren
3. **Einfrieren** (Refreezing): Neue Strukturen verankern

### Widerstand gegen Veränderung
- Rational (Aufwand, Risiko)
- Emotional (Angst, Gewohnheit)
- Sozial (Gruppendruck)

### Change Management Ansätze
- Top-Down (Führung getrieben)
- Bottom-Up (Mitarbeiter beteiligt)
- Partizipativ (gemeinsam)"""
        },
    ],

    # ===================== BWL1 =====================
    "bwl1": [
        {
            "id": "bwl1_1_1", "name": "Ökonomisches Prinzip & Güter", "icon": "💡",
            "filter": ["Folienskript Chwallek Kap. 1.1"],
            "explanation": """## Ökonomisches Prinzip & Güter

### Ökonomisches Prinzip
Knappheit der Ressourcen zwingt zu wirtschaftlichem Handeln:

- **Minimalprinzip**: Bestimmter Erfolg mit **minimalen** Mitteln
- **Maximalprinzip**: Gegebene Mittel → **maximaler** Erfolg

### Güterklassifikation
| Güterart | Eigenschaft | Beispiel |
|----------|-------------|----------|
| **Freie Güter** | Unbegrenzt, kein Preis | Luft, Sonnenlicht |
| **Wirtschaftliche Güter** | Knapp, mit Preis | Brot, Auto |
| **Sachgüter** | Materiell | Maschine |
| **Dienstleistungen** | Immateriell | Beratung |
| **Rechte** | Z.B. Patente | Lizenz |

### Corporate Social Responsibility (CSR)
Verantwortung von Unternehmen über die rechtlichen Pflichten hinaus: ökologisch, sozial, ökonomisch.

### Sustainable Development Goals (SDGs)
17 UN-Ziele für nachhaltige Entwicklung (z.B. kein Armut, Klimaschutz)."""
        },
        {
            "id": "bwl1_1_2", "name": "Betrieb und Bestimmungsfaktoren", "icon": "🏭",
            "filter": ["Folienskript Chwallek Kap. 1.2", "Folienskript Chwallek Kap. 2.1"],
            "explanation": """## Definition Betrieb

### Betrieb
Wirtschaftliche Einheit, die Güter erstellt und absetzt. Planvoll und dauerhaft.

### Bestimmungsfaktoren eines Betriebs
1. **Art** der Leistung (Produkt/Dienstleistung)
2. **Menge** der Leistung
3. **Ort** der Leistungserstellung
4. **Zeit** der Leistungserstellung

### Phasenmodell des Unternehmens
1. Gründung
2. Wachstum
3. Reife
4. Schrumpfung / Transformation"""
        },
        {
            "id": "bwl1_2_2", "name": "Anspruchsgruppen", "icon": "🤝",
            "filter": ["Folienskript Chwallek Kap. 2.2"],
            "explanation": """## Anspruchsgruppen (Stakeholder)

### Stakeholder-Modell
Gruppen, die ein berechtigtes Interesse am Unternehmen haben.

**Intern**:
- Eigentümer / Gesellschafter
- Management
- Mitarbeiter

**Extern**:
- Kunden
- Lieferanten
- Staat (Steuern, Regulierung)
- Gesellschaft
- Banken / Kapitalgeber

### Stakeholder-Interessen (konfliktär)
- **Eigentümer**: Rendite, Wertsteigerung
- **Mitarbeiter**: Gehalt, Sicherheit
- **Kunden**: Qualität, günstiger Preis
- **Lieferanten**: pünktliche Zahlung
- **Staat**: Steuern, Arbeitsplätze

### Stakeholder-Management
Ausbalancieren der Interessen, um langfristigen Erfolg zu sichern."""
        },
        {
            "id": "bwl1_2_4", "name": "Kennzahlen", "icon": "📐",
            "filter": ["Folienskript Chwallek Kap. 2.4"],
            "explanation": """## Kennzahlen

### Arten
- **Absolute Kennzahlen**: Stückzahlen, Umsatz
- **Verhältniszahlen**: Quotient aus zwei Größen
  - Gliederungszahlen (Anteil am Ganzen)
  - Beziehungszahlen (verschiedene Basen)
  - Indexzahlen (Zeitvergleich)

### Wichtige Kennzahlen

**Liquidität**:
- Liquiditätsgrad 1 = Umlaufvermögen / kurzfristiges Fremdkapital
- **Goldene Bilanzregel**: Anlagevermögen sollte durch Eigenkapital gedeckt sein

**Rentabilität**:
- Eigenkapitalrentabilität = Gewinn / Eigenkapital
- Gesamtkapitalrentabilität = (Gewinn + Zinsen) / Gesamtkapital
- Umsatzrentabilität = Gewinn / Umsatz

### ROI (Return on Investment)
> ROI = Umsatzrentabilität × Kapitalumschlag

### Phasenmodell des Unternehmenslebenszyklus
Gründung → Wachstum → Reife → Sättigung → Schrumpfung."""
        },
        {
            "id": "bwl1_2_5", "name": "Entscheidungsmodelle", "icon": "🧭",
            "filter": ["Folienskript Chwallek Kap. 2.5"],
            "explanation": """## Entscheidungsmodelle

### Entscheidungen unter...
1. **Sicherheit**: Alle Daten bekannt
2. **Risiko**: Wahrscheinlichkeiten bekannt
3. **Unsicherheit**: Wahrscheinlichkeiten unbekannt

### Entscheidungsregeln unter Unsicherheit
- **Maximax**: Maximum der Maxima (optimistisch)
- **Maximin**: Maximum der Minima (pessimistisch, Wald)
- **Hurwicz**: Gewichtung von Optimum und Pessimismus
- **Laplace**: Gleichverteilung der Wahrscheinlichkeiten
- **Savage-Niehaus**: Minimierung des Bedauerns (Opportunitätskosten)"""
        },
        {
            "id": "bwl1_2_6", "name": "Unternehmenstypologie", "icon": "📋",
            "filter": ["Folienskript Chwallek Kap. 2.6", "Folienskript Chwallek Kap. 2.7", "Folienskript Chwallek Kap. 2.1"],
            "explanation": """## Unternehmenstypologie

Klassifikation nach verschiedenen Merkmalen:

- **Rechtsform**: Einzelunternehmen, GmbH, AG, etc.
- **Größe**: Klein, mittel, groß (Mitarbeiter, Umsatz)
- **Branche**: Industrie, Handel, Dienstleistung
- **Eigentum**: Privat, öffentlich, genossenschaftlich
- **Region**: lokal, national, international"""
        },
        {
            "id": "bwl1_3_1", "name": "Standortwahl", "icon": "📍",
            "filter": ["Folienskript Chwallek Kap. 3.1"],
            "explanation": """## Standortwahl

### Standortfaktoren
**Harte Faktoren** (quantifizierbar):
- Lohnkosten
- Grundstückspreise
- Steuern
- Verkehrsanbindung

**Weiche Faktoren** (qualitativ):
- Qualifikation der Arbeitskräfte
- Lebensqualität
- Image der Region
- Cluster / Netzwerke

### Internationalisierung
Auslagerung von Produktion (Offshoring) an günstigere Standorte."""
        },
        {
            "id": "bwl1_3_2", "name": "Rechtsformen", "icon": "📜",
            "filter": ["Folienskript Chwallek Kap. 3.2"],
            "explanation": """## Rechtsformen

### Personengesellschaften
**Einzelunternehmen**: Eine Person, unbeschränkte Haftung, volle Gewinne.

**OHG** (Offene Handelsgesellschaft): ≥ 2 Gesellschafter, persönliche Haftung, rechtliche Selbständigkeit.

**KG** (Kommanditgesellschaft): Vollhafter (unbeschränkt) + Kommanditist (beschränkt auf Einlage).

### Kapitalgesellschaften
**GmbH**: Haftungsbeschränkung auf Gesellschaftsvermögen, Mindeststammkapital 25.000 €.

**AG** (Aktiengesellschaft): Aktien als Anteile, Mindestkapital 50.000 €, börsenfähig, strenge Publizität.

### Vergleichskriterien
| Kriterium | Einzel | GmbH | AG |
|-----------|--------|------|-----|
| Haftung | Unbeschränkt | Beschränkt | Beschränkt |
| Kapital | Selbst | 25.000 € | 50.000 € |
| Mitbestimmung | – | Gering | Hoch |
| Publizität | Keine | Mittel | Hoch |
| Flexibilität | Hoch | Mittel | Niedrig |"""
        },
        {
            "id": "bwl1_3_3", "name": "Unternehmensverbindungen", "icon": "🔗",
            "filter": ["Folienskript Chwallek Kap. 3.3", "Folienskript Chwallek Kap. 3.3.4.2"],
            "explanation": """## Unternehmensverbindungen

### Kartell
Zusammenschluss rechtlich selbständiger Unternehmen (Wettbewerbsbeschränkung). Meist verboten (Kartellverbot § 1 GWB), Ausnahmen zulässig.

### Konzern
Muttergesellschaft beherrscht Tochtergesellschaft(en). rechtlich selbständig, wirtschaftlich einheitlich geführt.

### Trust
Vollständige Verschmelzung, rechtliche Einheit.

### Syndikat
Gemeinsame Vertriebsstelle.

### Joint Venture
Zwei oder mehr Unternehmen gründen gemeinsame Gesellschaft (Risikoteilung, Marktentry)."""
        },
        {
            "id": "bwl1_other", "name": "Weitere Themen", "icon": "📚",
            "filter": ["VWL Kap. C", "Zusatzübung 1", "Folienskript Chwallek Kap. 2.3"],
            "explanation": """## Weitere BWL-Themen

Hier findest du Cross-Listing-Fragen aus VWL und weitere Zusatzthemen:
- Güterklassifikation
- Querverbindungen zur VWL (Angebot & Nachfrage)"""
        },
    ],

    # ===================== BWL2 =====================
    "bwl2": [
        {
            "id": "bwl2_grundlagen", "name": "Grundlagen Buchführung", "icon": "📚",
            "filter": ["Foliensatz BUF Kap. 1-3", "Aufgabensammlung Buchfuehrung", "Reading-Week 4", "Reading-Week 5"],
            "explanation": """## Grundlagen Buchführung

### Aufgabe der Buchführung
- Dokumentation aller Geschäftsvorfälle
- Grundlage für Jahresabschluss (Bilanz, GuV)
- Information von Eigentümern, Staat, Gläubigern

### Buchungspflicht (§ 238 HGB)
Jeder Kaufmann ist zur Buchführung verpflichtet. Grundsätze:
- **Vollständigkeit**, **Richtigkeit**, **Klarheit**
- **Vorsicht** (Gläubigerschutz)
- **Stetigkeit** (gleiche Methoden)

### Inventur
Körperliche und bookmäßige Bestandsaufnahme aller Vermögenswerte und Schulden zu einem Stichtag."""
        },
        {
            "id": "bwl2_inventur", "name": "Inventur und Bilanz", "icon": "📋",
            "filter": ["Foliensatz BUF Kap. 4"],
            "explanation": """## Inventur → Bilanz

### Inventur
Physische Bestandsaufnahme aller Vermögenswerte und Schulden.

### Inventar
Detaillierte Auflistung (in Geld bewertet). Drei Teile:
1. **Vermögen** (Anlage- + Umlaufvermögen)
2. **Schulden** (langfristig + kurzfristig)
3. **Eigenkapital** = Vermögen − Schulden

### Bilanz
Zusammenfassung in **Staffelform**:

```
        AKTIVA          =          PASSIVA
   (Mittelverwendung)       (Mittelherkunft)
Anlagevermögen              Eigenkapital
+ Umlaufvermögen            + Fremdkapital
```

### Bilanzgleichung
> **Aktiva = Passiva** (immer!)
> Eigenkapital = Vermögen − Schulden

### Erfolgsbilanz
Gewinn ↑ Eigenkapital, Verlust ↓ Eigenkapital."""
        },
        {
            "id": "bwl2_konten", "name": "Konten und Kontenarten", "icon": "📂",
            "filter": ["Foliensatz BUF Kap. 5-9", "Foliensatz BUF Kap. 5.1-5.3"],
            "explanation": """## Konten und Kontenarten

### T-Konto (Kontenrahmen)
```
    Soll  |  Haben
----------+----------
   Mehrung|  Minderung
```

### Bestandskonten
- **Aktivkonten** (Vermögen): Soll = Mehrung (Zugang), Haben = Minderung (Abgang)
  - Anfangsbestand im SOLL
- **Passivkonten** (Schulden): Haben = Mehrung (Zugang), Soll = Minderung (Abgang)
  - Anfangsbestand im HABEN

### Erfolgskonten
- **Aufwandskonten**: Soll = Aufwand (z.B. Lohnaufwand)
- **Ertragskonten**: Haben = Ertrag (z.B. Umsatzerlös)

### Soll-Wen-Prinzip
„Soll wissen, wen es angeht" – jedes Konto hat einen klaren Funktionstyp:
- Aktiv: Bestandsmehrung im **Soll**, Minderung im **Haben**
- Passiv: Bestandsmehrung im **Haben**, Minderung im **Soll**"""
        },
        {
            "id": "bwl2_sollwen", "name": "Soll-Wen-Prinzip & Buchungssatz", "icon": "✍️",
            "filter": ["Foliensatz BUF Kap. 5.4-7", "Foliensatz BUF Kap. 5-7", "Foliensatz BUF Kap. 5-6"],
            "explanation": """## Buchungssatz und Soll-Wen-Prinzip

### Buchungssatz-Logik
**„Soll an Haben"** – erster Konto: Soll, zweiter Konto: Haben.

Beispiel: *Barzahlung einer Rechnung*
> Bank (Aktivzunahme) an Kasse (Aktivabnahme)

### Regeln
1. **Aktivkonto** im **Soll** = **Mehrung** des Vermögens
2. **Aktivkonto** im **Haben** = **Minderung** des Vermögens
3. **Passivkonto** im **Haben** = **Mehrung** der Schulden
4. **Passivkonto** im **Soll** = **Minderung** der Schulden
5. **Aufwand** immer im **Soll**
6. **Ertrag** immer im **Haben**

### Tausch-Prinzip
Jeder Buchungssatz tauscht: **etwas kommt, etwas geht** (oder beides).

**Beispiel Kauf auf Ziel**:
> Wareneingang (Aktiv+) an Verbindlichkeiten (Passiv+)"""
        },
        {
            "id": "bwl2_erfolgskonten", "name": "Erfolgskonten & GuV", "icon": "💰",
            "filter": ["Foliensatz BUF Kap. 8-9"],
            "explanation": """## Erfolgskonten und GuV

### Aufwandskonten (Soll)
- Lohnaufwand, Mietaufwand, Zinsaufwand, Abschreibungen
- Erhöhen Aufwand → mindern Gewinn → mindern Eigenkapital

### Ertragskonten (Haben)
- Umsatzerlös, Zinsertrag, Mietertrag
- Erhöhen Ertrag → erhöhen Gewinn → erhöhen Eigenkapital

### Gewinn- und Verlustrechnung (GuV)
```
   Erträge
-  Aufwendungen
=  Gewinn / Verlust
```

### Schlussbilanz
Nach GuV: Erfolgskonten werden auf das Eigenkapital abgeschlossen."""
        },
        {
            "id": "bwl2_abschreibung", "name": "Abschreibungen", "icon": "📉",
            "filter": ["Foliensatz BUF Kap. 9.2"],
            "explanation": """## Abschreibungen

### Begriff
Wertminderung von Anlagevermögen durch Verschleiß, Alterung, technischen Fortschritt.

### Methoden
**Lineare Abschreibung** (gleichmäßig):
> Abschreibung = Anschaffungskosten / Nutzungsdauer

**Degressive Abschreibung** (fallend): Höherer Betrag in frühen Jahren.

### Buchwert
Anschaffungskosten − kumulierte Abschreibungen.

### Poolmethode
Vereinfachte Sammelabschreibung für geringwertige Wirtschaftsgüter (GWG ≤ 800 €)."""
        },
        {
            "id": "bwl2_umsatzsteuer", "name": "Umsatzsteuer", "icon": "🧾",
            "filter": ["Foliensatz BUF Kap. 10.2"],
            "explanation": """## Umsatzsteuer / Vorsteuer

### Umsatzsteuer (USt)
Mehrwertsteuer auf Verkäufe. **Verbindlichkeit** gegenüber dem Finanzamt.

> Buchung: Forderung an Umsatzerlös + Umsatzsteuer (Passiv+)

### Vorsteuer (VSt)
Umsatzsteuer, die das Unternehmen selbst beim Einkauf bezahlt. **Forderung** gegen das Finanzamt.

> Buchung: Wareneingang (Aktiv+) + Vorsteuer (Aktiv+) an Verbindlichkeit

### Zahllast
> Umsatzsteuer − Vorsteuer = an Finanzamt zu zahlen"""
        },
        {
            "id": "bwl2_privat", "name": "Privatkonten", "icon": "🏠",
            "filter": ["Foliensatz BUF Kap. 12-13"],
            "explanation": """## Privatkonten

### Privatentnahme
Entnahmen des Inhabers für private Zwecke (Geld, Waren). Eigenkapitalminderung.

> Buchung: Privat an Kasse (oder Ware)

### Privateinlage
Einlagen des Inhabers in den Betrieb. Eigenkapitalmehrung.

> Buchung: Kasse an Privat

### Schlussbilanz
Privatkonto wird auf das Eigenkapital abgeschlossen."""
        },
        {
            "id": "bwl2_beschaffung", "name": "Beschaffungsbereich", "icon": "🚚",
            "filter": ["Foliensatz BUF Kap. 15 ", "Foliensatz BUF Kap. 15-16"],
            "explanation": """## Beschaffungsbereich

### Einkauf
Wareneingang + Vorsteuer (Aktiv+) an Verbindlichkeiten (Passiv+)

### Bezugsnebenkosten
Transport, Versicherung, Zoll → erhöhen Anschaffungskosten.

### Skonto
Preisnachlass bei vorzeitiger Zahlung:
> Buchung: Verbindlichkeiten an Kasse + Wareneingang (Rabatt Minderung)

### Rabatt
Nachlass auf den Listenpreis (vorab)."""
        },
        {
            "id": "bwl2_absatz", "name": "Absatzbereich", "icon": "🛒",
            "filter": ["Foliensatz BUF Kap. 16 "],
            "explanation": """## Absatzbereich

### Verkauf
Forderungen (Aktiv+) an Umsatzerlös (Ertrag) + Umsatzsteuer (Passiv+)

### Erlösschmälerungen
- **Rabatt**: vorab auf Preis
- **Skonto**: bei vorzeitiger Zahlung
- **Bonus**: nachträglich
- **Umsatzboni**: Bonus für Umsatzvolumen

### Forderungsverlust
**Einzelfallwertberichtigung**: Konkrete Forderung uneinbringbar → direkter Abgang.

**Pauschalwertberichtigung**: Allgemeines Risiko, statistisch geschätzt."""
        },
        {
            "id": "bwl2_jahresabgrenzung", "name": "Jahresabgrenzung", "icon": "📅",
            "filter": ["Foliensatz BUF Kap. 17.4"],
            "explanation": """## Jahresabgrenzung

### Transitorische Posten
**Aktiver Rechnungsabgrenzungsposten (ARAP)**: Bereits bezahlt, gehört ins nächste Jahr (z.B. Miete vorausgezahlt).

**Passiver Rechnungsabgrenzungsposten (PRAP)**: Bereits vereinnahmt, Ertrag gehört ins nächste Jahr.

### Antizipative Posten
Noch nicht bezahlt/vereinnahmt, aber Aufwand/Ertrag schon in diesem Jahr:
- **Antizipativer Aufwand** (z.B. noch offene Stromrechnung)
- **Antizipativer Ertrag** (z.B. noch offene Zinsforderung)

### Rückstellungen
Für ungewisse Verbindlichkeiten (z.B. Prozessrisiko, Urlaubsrückstellung)."""
        },
        {
            "id": "bwl2_other", "name": "Sonstiges (Beispielklausur/Kontenplan)", "icon": "📑",
            "filter": ["Beispielklausur Buchführung", "Foliensatz BUF; Kontenplan"],
            "explanation": """## Sonstige Buchführungsthemen

Hier findest du übergreifende Fragen aus Beispielklausuren und Kontenplan."""
        },
    ],

    # ===================== MAWI1 =====================
    "mawi1": [
        {
            "id": "mawi1_1_1", "name": "Funktionen und Grundlagen", "icon": "📈",
            "filter": ["WiMa 1 Kap. 1.1", "WiMa 1 Kap. 1"],
            "explanation": """## Funktionen einer Variablen

### Funktionsbegriff
Eine Funktion f ordnet jedem x aus der Definitionsmenge D genau ein y zu.

> y = f(x)

### Wichtige Begriffe
- **Definitionsmenge D**: zulässige x-Werte
- **Wertemenge W**: erreichbare y-Werte
- **Nullstelle**: f(x) = 0
- **Schnittpunkt mit y-Achse**: f(0)

### Kostenfunktion
> K(x) = K_f + K_v(x)
>   Fixkosten + variable Kosten

- **Stückkosten**: k(x) = K(x) / x
- **Stückvariable Kosten**: k_v(x) = K_v(x) / x
- **Grenzkosten**: K'(x) = dK/dx

### Erlösfunktion
> E(x) = p · x  (Preis · Menge)

### Gewinnfunktion
> G(x) = E(x) − K(x) = Umsatz − Kosten

Gewinnmaximum: G'(x) = 0  →  E'(x) = K'(x) (Grenzerlös = Grenzkosten)"""
        },
        {
            "id": "mawi1_1_2", "name": "Wichtige Funktionstypen", "icon": "🔣",
            "filter": ["WiMa 1 Kap. 1.2", "WiMa 1 Kap. 1.3"],
            "explanation": """## Wichtige Funktionstypen

### Lineare Funktion
> f(x) = m·x + b
- Steigung m = Δy/Δx
- y-Achsenabschnitt b

### Quadratische Funktion
> f(x) = ax² + bx + c
- Parabel, Scheitelpunkt bei x = -b/(2a)
- Nullstellen: Mitternachtsformel

### Polynomfunktion
> f(x) = a_n·x^n + ... + a_1·x + a_0

### Gebrochen-rationale Funktion
> f(x) = p(x) / q(x)
- Polstellen: Nenner = 0
- Asymptoten

### Exponentialfunktion
> f(x) = a·e^(kx)
- Wachstum (k>0) / Zerfall (k<0)

### Logarithmusfunktion
> ln(x), log(x)
- Inverse zur Exponentialfunktion"""
        },
        {
            "id": "mawi1_2", "name": "Differentialrechnung", "icon": "∫",
            "filter": ["WiMa 1 Kap. 2"],
            "explanation": """## Differentialrechnung

### Ableitung
Die Ableitung f'(x) ist die Steigung der Tangente an einem Punkt.

### Ableitungsregeln
**Potenzregel**: f(x) = x^n → f'(x) = n·x^(n-1)

**Summenregel**: (f+g)' = f' + g'

**Produktregel**: (f·g)' = f'·g + f·g'

**Quotientenregel**: (f/g)' = (f'·g − f·g') / g²

**Kettenregel**: f(g(x)) → f'(g(x))·g'(x)

### Extremwerte
- **Notwendige Bedingung**: f'(x) = 0
- **Hinreichende Bedingung**: f''(x) < 0 (Maximum) bzw. f''(x) > 0 (Minimum)

### Wendepunkt
f''(x) = 0 und f'''(x) ≠ 0"""
        },
        {
            "id": "mawi1_3", "name": "Grenzwerte und Stetigkeit", "icon": "∞",
            "filter": ["WiMa 1 Kap. 3"],
            "explanation": """## Grenzwerte und Stetigkeit

### Grenzwert
> lim_(x→a) f(x) = L

f nähert sich L, wenn x gegen a geht.

### Stetigkeit
Eine Funktion ist stetig an x=a, wenn:
1. f(a) definiert ist
2. lim_(x→a) f(x) existiert
3. lim_(x→a) f(x) = f(a)

### Unstetigkeiten
- **Sprung**: links/rechts verschieden
- **Lücke**: Definitionslücke
- **Pol**: Grenzwert geht gegen ±∞

### Regel von L'Hôpital
Bei 0/0 oder ∞/∞:
> lim f(x)/g(x) = lim f'(x)/g'(x)"""
        },
        {
            "id": "mawi1_4", "name": "Matrizenrechnung", "icon": "🔲",
            "filter": ["WiMa 1 Kap. 4"],
            "explanation": """## Matrizenrechnung

### Matrix
Rechteckiges Zahlenschema mit m Zeilen und n Spalten.

### Operationen
**Addition**: A + B (gleiche Dimensionen)
**Multiplikation mit Skalar**: k·A
**Matrixmultiplikation**: A·B
- Zeile × Spalte
- Bedingung: Spalten von A = Zeilen von B

### Einheitsmatrix I
Diagonal 1, sonst 0. A·I = A.

### Inverse
A^(-1)·A = I
- Nur für quadratische, reguläre Matrizen (Det ≠ 0)

### Determinante
Skalar, der einer quadratischen Matrix zugeordnet ist.
- 2×2: |A| = ad − bc
- Wichtig für Invertierbarkeit und Lösung von Gleichungssystemen"""
        },
    ],

    # ===================== MAWI2 =====================
    "mawi2": [
        {
            "id": "mawi2_1", "name": "Grundlagen Statistik", "icon": "📊",
            "filter": ["Statistik Kap. 1"],
            "explanation": """## Grundlagen Statistik

### Grundbegriffe
- **Grundgesamtheit** (Population, N): alle relevanten Objekte
- **Stichprobe** (sample, n): Teilmenge der Grundgesamtheit
- **Merkmal** (Variable, X): Eigenschaft, die beobachtet wird
- **Ausprägung**: konkreter Wert eines Merkmals

### Merkmalsarten
**Skalenniveaus** (vom niedrigen zum hohen):
1. **Nominal**: nur Gleichheit (Augenfarbe)
2. **Ordinal**: Reihenfolge (Schulnote)
3. **Interval**: Abstände (Temperatur °C)
4. **Verhältnis**: natürlicher Nullpunkt (Körpergröße)

### Häufigkeit
- **Absolute Häufigkeit** h_i: Anzahl
- **Relative Häufigkeit** f_i = h_i / n

### Verteilung
Tabellarische oder grafische Darstellung der Häufigkeiten."""
        },
        {
            "id": "mawi2_3", "name": "Verteilungen", "icon": "📊",
            "filter": ["Statistik Kap. 2", "Statistik Kap. 3"],
            "explanation": """## Verteilungen

### Häufigkeitsverteilung
Tabelle mit Merkmalsausprägungen und Häufigkeiten.

### Grafische Darstellung
- **Histogramm**: Säulendiagramm (kategorial/intervallskaliert)
- **Kreisdiagramm**: Anteile (nominal)
- **Stabdiagramm**: diskret

### Kumulierte Häufigkeit
F(x) = Anzahl der Werte ≤ x."""
        },
        {
            "id": "mawi2_4", "name": "Lageparameter", "icon": "📍",
            "filter": ["Statistik Kap. 4"],
            "explanation": """## Lageparameter (Maße der zentralen Tendenz)

### Modus (Modalwert)
Häufigster Wert. Für alle Skalenniveaus.

### Median (Zentralwert)
Wert in der Mitte der sortierten Reihe. Bei gerader Anzahl: Mittel der beiden mittleren.

### Arithmetisches Mittel (Mittelwert)
> x̄ = (1/n) · Σx_i

Empfindlich gegenüber Ausreißern.

### Quartile
- Q1 (25%-Quantil)
- Q2 = Median
- Q3 (75%-Quantil)

### Zusammenhang
Bei symmetrischer Verteilung: Modus ≈ Median ≈ Mittelwert.
Bei linkssteil: Mittel < Median < Modus."""
        },
        {
            "id": "mawi2_5", "name": "Streuungsmaße", "icon": "📡",
            "filter": ["Statistik Kap. 5"],
            "explanation": """## Streuungsmaße (Dispersion)

### Spannweite (Range)
> R = max − min

### Varianz
Durchschnittliche quadratische Abweichung vom Mittelwert:

> σ² = (1/n) · Σ(x_i − x̄)²  (Population)
> s² = (1/(n-1)) · Σ(x_i − x̄)²  (Stichprobe, korrigiert)

### Standardabweichung
> σ = √σ²  bzw.  s = √s²

Selbe Einheit wie die Daten.

### Interquartilsabstand (IQR)
> IQR = Q3 − Q1

Robust gegenüber Ausreißern.

### Variationskoeffizient
> CV = σ / x̄

Vergleich von Streuung unterschiedlicher Skalen."""
        },
        {
            "id": "mawi2_6", "name": "Indexzahlen", "icon": "🔢",
            "filter": ["Statistik Kap. 6"],
            "explanation": """## Indexzahlen

### Preisindex
Misst die zeitliche Entwicklung von Preisen oder Mengen.

### Laspeyres-Index
Gewichtung mit Basisjahr-Mengen:
> I_L = (Σ p_1·q_0) / (Σ p_0·q_0) · 100

Vorteil: stabile Gewichte. Nachteil: veraltetes Konsumverhalten.

### Paasche-Index
Gewichtung mit Berichtsjahr-Mengen:
> I_P = (Σ p_1·q_1) / (Σ p_0·q_1) · 100

Vorteil: aktuelles Konsumverhalten. Nachteil:每年 neue Berechnung.

### Fisher-Index
> I_F = √(I_L · I_P)

Ideal-Index, vereint Vorteile."""
        },
    ],

    # ===================== WPR =====================
    "wpr": [
        {
            "id": "wpr_1", "name": "Einführung ins Recht", "icon": "⚖️",
            "filter": ["WPR Foliensatz Kap. 1", "WPR Grundlagen"],
            "explanation": """## Einführung Wirtschaftsprivatrecht

### Rechtsgebiete
**Privatrecht** (Bürger zu Bürger) vs. **Öffentliches Recht** (Staat zu Bürger).

WPR = Privatrecht mit wirtschaftlichem Bezug.

### Wichtigste Gesetze
- **BGB** (Bürgerliches Gesetzbuch)
- **HGB** (Handelsgesetzbuch)
- Spezialgesetze (AGG, AGBG, VerbrG)

### BGB-Aufbau (5 Bücher)
1. **Allgemeiner Teil** (§§ 1–240): Rechtsgeschäftslehre
2. **Schuldrecht** (§§ 241–853): Verträge, Schadensersatz
3. **Sachenrecht** (§§ 854–1296): Eigentum, Besitz
4. **Familienrecht** (§§ 1297–1921)
5. **Erbrecht** (§§ 1922–2385)"""
        },
        {
            "id": "wpr_2", "name": "Natürliche Personen & Rechtsfähigkeit", "icon": "👤",
            "filter": ["WPR Foliensatz Kap. 2", "WPR Foliensatz Kap. 2-7"],
            "explanation": """## Personenrecht

### Natürliche Personen
Menschen. Ab Geburt **rechtsfähig** (§ 1 BGB).

### Rechtsfähigkeit
Fähigkeit, Träger von Rechten und Pflichten zu sein.

### Geschäftsfähigkeit
- **Voll geschäftsfähig** (§ 2): ab 18 Jahren
- **Beschränkt geschäftsfähig** (§§ 106–113): 7–18 Jahre
  - Alltagsgeschäfte (Taschengeldparagraph)
  - Sonst mit Zustimmung der Eltern
- **Geschäftsunfähig**: unter 7 Jahre, psychisch Kranke

### Deliktsfähigkeit
Verantwortlichkeit für unerlaubte Handlungen (§ 823 BGB). Ab 7 bzw. 18 Jahren."""
        },
        {
            "id": "wpr_3", "name": "Rechtsgeschäftslehre", "icon": "📜",
            "filter": ["WPR Foliensatz Kap. 3", "WPR Rechtsgeschaeftslehre", "WPR Willenserkl.", "WPR Vertragsschluss", "WPR Auslegung", "WPR AGB", "WPR Anfechtung", "WPR Stellvertretung", "WPR Formvorschr."],
            "explanation": """## Rechtsgeschäftslehre

### Rechtsgeschäft
Mind. eine Willenserklärung, die auf Rechtsfolge gerichtet ist.

### Willenserklärung
- **Antrag** (Angebot) und **Annahme** → Vertrag (§ 145 BGB)
- Schweigen ist grundsätzlich keine Willenserklärung

### Nichtigkeit
Ein Rechtsgeschäft ist **nichtig**, wenn es nichtigkeitsgründe hat:
- **Geschäftsunfähigkeit** (§ 105)
- **Sittenwidrigkeit** (§ 138)
- **Wucher** (§ 138 II)
- **Formmangel** (z.B. § 311b: Grundstückskauf muss notariell beurkundet werden)
- **Anfängliche Unmöglichkeit** (§ 275)

### Anfechtung (§ 119)
Rückwirkende Vernichtung einer Willenserklärung bei Irrtum:
- Inhaltsirrtum
- Erklärungsirrtum
- Eigenschaftsirrtum
- Täuschung / Drohung (§ 123)

### Lateinische Begriffe
- **caveat emptor** – Käufer, pass auf!
- **dolo agit** – arglistig handeln
- **pacta sunt servanda** – Verträge sind einzuhalten
- **condictio** – Rückforderung"""
        },
        {
            "id": "wpr_4", "name": "Schuldrecht AT", "icon": "💵",
            "filter": ["WPR Foliensatz Kap. 4"],
            "explanation": """## Schuldrecht Allgemeiner Teil

### Schuldverhältnis
Rechtliches Band zwischen Gläubiger und Schuldner mit Leistungspflicht.

### Entstehung
- **Vertrag** (z.B. Kaufvertrag § 433)
- **Gesetzlich** (z.B. § 823: unerlaubte Handlung)
- **Bereicherungsrecht** (§ 812: ungerechtfertigte Bereicherung)

### Vertragsarten
- **Kauf** (§ 433): Pflicht zur Übergabe und Übereignung
- **Dienstvertrag** (§ 611): Dienstleistung
- **Werkvertrag** (§ 631): Erfolgsbezogen
- **Miete** (§ 535)
- **Darlehen** (§ 488)

### Pflichtverletzung
Bei Nichterfüllung:
- **Schadensersatz** (§§ 280 ff.)
- **Rücktritt** (§ 323)
- **Minderung**"""
        },
        {
            "id": "wpr_5", "name": "Verjährung", "icon": "⏰",
            "filter": ["WPR Foliensatz Kap. 5", "WPR Verjaehrung"],
            "explanation": """## Verjährung

### Begriff
Nach Ablauf der Frist kann der Schuldner die Leistung verweigern (§ 214). Die Schuld besteht weiter (naturliche obligation), ist aber nicht einklagbar.

### Regelfrist
**3 Jahre** ab Kenntnis von Anspruch und Schuldner (§ 195).

### Sonstige Fristen
- 10 Jahre (§ 199): ab Entstehung, maximal
- 30 Jahre: dingliche Ansprüche (z.B. Herausgabe einer Sache § 194)
- 30 Jahre: familien- und erbrechtliche Ansprüche

### Hemmung
Verjährung läuft nicht (z.B. Verhandlungen, Insolvenzverfahren).

### Neubeginn (Unterbrechung)
Durch Anerkenntnis, Klageerhebung."""
        },
        {
            "id": "wpr_6", "name": "Handelsrecht", "icon": "🏪",
            "filter": ["WPR Foliensatz Kap. 6"],
            "explanation": """## Handelsrecht

### Kaufmann (§ 1 HGB)
Wer ein Handelsgewerbe betreibt.

### Handelsregister
Öffentliches Register beim Amtsgericht:
- **Abteilung A**: Personengesellschaften (OHG, KG, Einzelkaufleute)
- **Abteilung B**: Kapitalgesellschaften (GmbH, AG)

### Firmenrecht
Firma = Name des Kaufmanns im Rechtsverkehr:
- **Personenfirma**: Name der Gesellschafter
- **Sachfirma**: Gegenstand
- **Phantasiename**: frei erfunden

### Publizität
 negative Publizität: Nicht-Eingetragenes gilt als nicht geschehen (für Dritten).
 positive Publizität: Eingetragenes gilt als bekannt."""
        },
        {
            "id": "wpr_7", "name": "Kaufrecht", "icon": "🛍️",
            "filter": ["WPR Foliensatz Kap. 7"],
            "explanation": """## Kaufvertrag (§ 433 BGB)

### Pflichten
**Verkäufer**: Übergabe und Übereignung der Sache; verschaffung frei von Sach- und Rechtsmängeln.

**Käufer**: Zahlung des Kaufpreises; Abnahme.

### Gewährleistung (Sachmangel § 434)
- Falschlieferung
- Montagemangel
- Aliud-Lieferung (falsche Sache)

### Rechte des Käufers (§ 437)
1. **Nacherfüllung** (Reparatur oder Nachlieferung)
2. **Rücktritt** oder **Minderung**
3. **Schadensersatz**

### Verjährung
- **BGB**: 2 Jahre ab Ablieferung (§ 438)
- **Verbrauchsgüterkauf**: 2 Jahre, zwingend

### Eigentumsvorbehalt
Verkäufer bleibt Eigentümer bis vollständiger Zahlung."""
        },
        {
            "id": "wpr_8", "name": "Sachenrecht", "icon": "🏠",
            "filter": ["WPR Foliensatz Kap. 8", "WPR Sachenrecht"],
            "explanation": """## Sachenrecht

### Besitz vs. Eigentum
- **Besitz** (§ 854): tatsächliche Herrschaft
- **Eigentum** (§ 903): rechtliche Herrschaft

### Übereignung (§ 929)
Eigentumsübertragung:
1. **Einigung** (Verbal)
2. **Übergabe** der Sache
3. Berechtigter Erwerber

### Besitzarten
- **Eigenbesitz**: Eigener Willen
- **Fremdbesitz**: Für andere (z.B. Mieter)
- **Unmittelbarer** / **mittelbarer** Besitz

### Grundbuch
- Bestandsverzeichnis (Parzelle)
- Abteilung I: Eigentümer
- Abteilung II: Lasten (Dienstbarkeiten)
- Abteilung III: Grundschulden, Hypotheken

### Grundbuchprinzipien
- **Eintragungsprinzip**: Wirkung durch Eintragung
- **Publizität**: Vertrauen auf Grundbuch"""
        },
        {
            "id": "wpr_other", "name": "Beweisrecht & Fallbeispiele", "icon": "🔍",
            "filter": ["WPR Foliensatz – Beweis", "WPR Foliensatz – Fallbeispiel", "WPR Foliensatz – Rechtsgrundsätze"],
            "explanation": """## Beweisrecht und Fallbeispiele

### Beweislast
Grundsatz: **Jeder muss die Tatsachen beweisen, die für ihn günstig sind.**

### Beweismaß
Vollbeweis: hoher Grad an Wahrscheinlichkeit.

### Arten
- **Beweis unmittelbar**: Zeuge, Urkunde
- **Beweis mittelbar**: Indizien

Hier findest du praktische Fallbeispiele zur Anwendung der WPR-Konzepte."""
        },
    ],
}

# Schreibe JSON
out_path = os.path.join(BASE, "_data", "topics.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(TOPICS, f, ensure_ascii=False, indent=2)

# Statistik
total_topics = sum(len(v) for v in TOPICS.values())
print(f"✅ {total_topics} Themen in {len(TOPICS)} Fächern")
for bank, topics in TOPICS.items():
    print(f"  {bank}: {len(topics)} Themen")
print(f"\nDatei: {out_path}")
