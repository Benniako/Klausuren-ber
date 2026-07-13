import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE, "_data", "questions_validated.json")

with open(PATH, "r", encoding="utf-8") as f:
    QS = json.load(f)

# Define extra questions to add
extra_questions = {
    "perso": [
        # perso_02 (need 1)
        {
            "q": "Welcher Begriff beschreibt nach Hofstede das Ausmaß, in dem weniger mächtige Mitglieder von Institutionen und Organisationen erwarten und akzeptieren, dass Macht ungleich verteilt ist?",
            "o": ["Unsicherheitsvermeidung", "Machtdistanz", "Individualismus", "Feminität"],
            "c": 1,
            "s": "Die Machtdistanz beschreibt das Ausmaß der Akzeptanz ungleicher Machtverteilung.",
            "src": "Perso Folie 02 CrossCultural"
        },
        # perso_03 (need 7)
        {
            "q": "Welche der vier Seiten einer Nachricht nach Schulz von Thun offenbart Informationen über die Persönlichkeit, Gefühle und Absichten des Senders?",
            "o": ["Sachinhalt", "Appell", "Beziehung", "Selbstoffenbarung"],
            "c": 3,
            "s": "Die Selbstoffenbarung enthält explizite oder implizite Informationen über den Sender selbst.",
            "src": "Perso Folie 03 Kommunikation"
        },
        {
            "q": "Was versteht man im Sender-Empfänger-Modell unter 'Dekodierung'?",
            "o": ["Das Übersetzen von Gedanken in Signale durch den Sender", "Das Entschlüsseln und Interpretieren der empfangenen Signale durch den Empfänger", "Die physikalische Übertragung der Nachricht über einen Kanal", "Das Ausfiltern von Störgeräuschen"],
            "c": 1,
            "s": "Dekodierung ist der Prozess des Entschlüsselns und Interpretierens der Signale durch den Empfänger.",
            "src": "Perso Folie 03 Kommunikation"
        },
        {
            "q": "Welches Verhalten gehört NICHT zum aktiven Zuhören?",
            "o": ["Paraphrasieren der Aussage des Sprechers", "Verbalisieren emotionaler Untertöne", "Sofortiges Anbieten einer eigenen Lösung oder Ratschläge", "Aufmerksames Schweigen und Nicken"],
            "c": 2,
            "s": "Sofortige Ratschläge oder Bewertungen widersprechen dem Prinzip des aktiven Zuhörens.",
            "src": "Perso Folie 03 Kommunikation"
        },
        {
            "q": "Was ist ein Sachkonflikt im Gegensatz zu einem Beziehungskonflikt?",
            "o": ["Ein Konflikt über persönliche Abneigungen", "Ein Konflikt über sachliche Ziele, Aufgaben oder Methoden", "Ein Konflikt über die Verteilung von Privilegien", "Ein unlösbarer emotionaler Konflikt"],
            "c": 1,
            "s": "Ein Sachkonflikt bezieht sich auf sachliche Differenzen (Inhalte, Ziele, Wege).",
            "src": "Perso Folie 03 Kommunikation"
        },
        {
            "q": "Welcher Aspekt beschreibt die 'Beziehungsseite' einer Nachricht nach dem Vier-Ohren-Modell?",
            "o": ["Wie der Sender den Empfänger sieht und was er von ihm hält", "Welche Fakten und Sachverhalte dargestellt werden", "Was der Empfänger tun, lassen oder denken soll", "Was der Sender von sich preisgibt"],
            "c": 0,
            "s": "Die Beziehungsebene drückt aus, wie der Sender zum Empfänger steht und was er von ihm hält.",
            "src": "Perso Folie 03 Kommunikation"
        },
        {
            "q": "Welche Störung wird als 'semantisches Rauschen' bezeichnet?",
            "o": ["Ein lauter Baustellenlärm während des Gesprächs", "Das Verwenden von Fachbegriffen oder Abkürzungen, die der Empfänger nicht versteht", "Eine schlechte Internetverbindung bei einem Videoanruf", "Ein Vorurteil gegenüber dem Gesprächspartner"],
            "c": 1,
            "s": "Semantisches Rauschen entsteht durch unterschiedliche Bedeutungszuschreibungen (z.B. unverstandene Fachsprache).",
            "src": "Perso Folie 03 Kommunikation"
        },
        {
            "q": "Wie wird das Wiederholen des Gesagten in eigenen Worten beim aktiven Zuhören fachsprachlich genannt?",
            "o": ["Verbalisieren", "Paraphrasieren", "Konditionieren", "Sublimieren"],
            "c": 1,
            "s": "Das Paraphrasieren ist das sachliche Wiederholen des Kerninhalts in eigenen Worten.",
            "src": "Perso Folie 03 Kommunikation"
        },
        # perso_07 (need 5)
        {
            "q": "In welcher Ebene der Maslowschen Bedürfnispyramide ist das Bedürfnis nach Anerkennung, Status und Wertschätzung angesiedelt?",
            "o": ["Physiologische Bedürfnisse", "Sicherheitsbedürfnisse", "Soziale Bedürfnisse", "Wertschätzungsbedürfnisse"],
            "c": 3,
            "s": "Anerkennung und Status gehören zu den Wertschätzungsbedürfnissen (4. Ebene).",
            "src": "Perso Folie 07 Motivation"
        },
        {
            "q": "Nach der VIE-Theorie von Vroom: Was drückt die 'Instrumentalität' aus?",
            "o": ["Die subjektive Erwartung, eine bestimmte Leistung erbringen zu können", "Die Verknüpfung zwischen dem Erreichen eines Zwischenziels und dem Erhalt einer Belohnung", "Der persönliche Wert oder die Attraktivität einer Belohnung", "Die Wahrscheinlichkeit, dass die Anstrengung zur Leistung führt"],
            "c": 1,
            "s": "Instrumentalität beschreibt den perceived link zwischen Handlungsleistung und dem finalen Handlungsergebnis (Belohnung).",
            "src": "Perso Folie 07 Motivation"
        },
        {
            "q": "Welches der folgenden Beispiele stellt nach Herzbergs Zwei-Faktoren-Theorie einen typischen Motivator dar?",
            "o": ["Das Gehalt und freiwillige Sozialleistungen", "Die physischen Arbeitsbedingungen am Arbeitsplatz", "Die Übertragung von Verantwortung und persönliche Entfaltungsmöglichkeiten", "Die Unternehmenspolitik und Richtlinien"],
            "c": 2,
            "s": "Verantwortung und Anerkennung sind Motivatoren (Zufriedenheitsmacher). Gehalt und Bedingungen sind Hygienefaktoren.",
            "src": "Perso Folie 07 Motivation"
        },
        {
            "q": "Welcher Effekt beschreibt die Verdrängung intrinsischer Motivation durch extrinsische Anreize (z.B. Geld)?",
            "o": ["Korrumpierungseffekt (Overjustification Effect)", "Halo-Effekt", "Pygmalion-Effekt", "Sunk-Cost-Effekt"],
            "c": 0,
            "s": "Der Korrumpierungseffekt beschreibt das Phänomen, dass intrinsische Motivation durch äußere Belohnungen sinken kann.",
            "src": "Perso Folie 07 Motivation"
        },
        {
            "q": "Welches Bedürfnis steht an der Spitze der ursprünglichen Maslowschen Bedürfnispyramide?",
            "o": ["Wertschätzungsbedürfnisse", "Soziale Bedürfnisse", "Selbstverwirklichung", "Sicherheitsbedürfnisse"],
            "c": 2,
            "s": "Selbstverwirklichung bildet die oberste (5.) Stufe der Maslow-Pyramide.",
            "src": "Perso Folie 07 Motivation"
        },
        # perso_11 (need 3)
        {
            "q": "Welche Phase gehört nach dem klassischen 3-Phasen-Modell von Kurt Lewin zum Wandlungsprozess?",
            "o": ["Forming, Storming, Performing", "Unfreezing, Changing, Refreezing", "Planung, Steuerung, Kontrolle", "Einführung, Wachstum, Reife"],
            "c": 1,
            "s": "Lewins Modell umfasst die Phasen Unfreezing (Auftauen), Changing (Verändern) und Refreezing (Einfrieren).",
            "src": "Perso Folie 11 Organisationsentwicklung"
        },
        {
            "q": "Was versteht man unter 'Unfreezing' im Change-Management nach Lewin?",
            "o": ["Das dauerhafte Einfrieren neuer Prozesse und Verhaltensweisen", "Die Vorbereitungsphase, um die Notwendigkeit des Wandels aufzuzeigen und Widerstände abzubauen", "Den eigentlichen Veränderungsprozess durch Schulungen", "Die Kündigung unwilliger Mitarbeiter"],
            "c": 1,
            "s": "Unfreezing dient der Mobilisierung und Aufhebung des Gleichgewichts, um Veränderungsbereitschaft zu schaffen.",
            "src": "Perso Folie 11 Organisationsentwicklung"
        },
        {
            "q": "Welche Methode der Organisationsentwicklung setzt stark auf Partizipation der Betroffenen durch Befragung und Feedback?",
            "o": ["Reengineering", "Survey-Feedback-Methode (Aktionsforschung)", "Strikter Top-Down-Wandel", "Machtpromotoren-Konzept"],
            "c": 1,
            "s": "Die Survey-Feedback-Methode basiert auf systematischer Befragung der Mitarbeiter und anschließender gemeinsamer Reflexion.",
            "src": "Perso Folie 11 Organisationsentwicklung"
        }
    ],
    "bwl1": [
        # bwl1_1_2 (need 5)
        {
            "q": "Welcher Bestimmungsfaktor nach Gutenberg kennzeichnet das erwerbswirtschaftliche Prinzip von Betrieben im marktwirtschaftlichen System?",
            "o": ["Das Prinzip des finanziellen Gleichgewichts", "Das Gewinnmaximierungsprinzip", "Das Autonomieprinzip", "Das Prinzip des Gemeineigentums"],
            "c": 1,
            "s": "Das erwerbswirtschaftliche Prinzip beschreibt das Streben nach Gewinnmaximierung.",
            "src": "Folienskript Chwallek Kap. 1.2"
        },
        {
            "q": "Welche Phase folgt im idealtypischen Lebenszyklus eines Unternehmens direkt auf die Gründungsphase?",
            "o": ["Reifephase", "Wachstumsphase", "Sättigungsphase", "Schrumpfungsphase"],
            "c": 1,
            "s": "Auf die Gründung folgt die Wachstumsphase.",
            "src": "Folienskript Chwallek Kap. 1.2"
        },
        {
            "q": "Was unterscheidet Betriebe in einer Zentralverwaltungswirtschaft wesentlich von Betrieben in einer Marktwirtschaft nach Gutenberg?",
            "o": ["Die Pflicht zur Buchführung", "Das Fehlen des Autonomieprinzips und das Planerfüllungsprinzip", "Die ausschließliche Nutzung von Sachgütern", "Das ökonomische Prinzip"],
            "c": 1,
            "s": "In einer Zentralverwaltungswirtschaft gilt das Planerfüllungsprinzip und die Betriebe unterliegen staatlicher Lenkung (keine Autonomie).",
            "src": "Folienskript Chwallek Kap. 1.2"
        },
        {
            "q": "Was ist ein 'Betrieb' im betriebswirtschaftlichen Sinne?",
            "o": ["Jede rechtliche Einheit (juristische Person)", "Eine planvoll organisierte Wirtschaftseinheit zur Bedarfsdeckung", "Ein Gebäude, in dem produziert wird", "Eine reine Verkaufsstelle"],
            "c": 1,
            "s": "Ein Betrieb ist eine planvoll organisierte Wirtschaftseinheit, die Sachgüter und Dienstleistungen zur Bedarfsdeckung herstellt und absetzt.",
            "src": "Folienskript Chwallek Kap. 1.2"
        },
        {
            "q": "Welcher der folgenden Faktoren ist KEIN elementarer Produktionsfaktor nach Gutenberg?",
            "o": ["Objektbezogene Arbeit", "Betriebsmittel", "Werkstoffe", "Geschäftsleitung (dispositiver Faktor)"],
            "c": 3,
            "s": "Die Geschäftsleitung ist der dispositive (leitende) Faktor, kein elementarer Faktor.",
            "src": "Folienskript Chwallek Kap. 1.2"
        },
        # bwl1_2_5 (need 2)
        {
            "q": "Nach welcher Entscheidungsregel unter Unsicherheit wählt ein Entscheider die Alternative mit dem besten Ergebnis im absolut ungünstigsten Fall (pessimistische Sicht)?",
            "o": ["Maximax-Regel", "Maximin-Regel (Wald-Regel)", "Laplace-Regel", "Savage-Niehaus-Regel"],
            "c": 1,
            "s": "Die Maximin-Regel wählt das Parameter-Minimum (Sicherheit vor Risiko).",
            "src": "Folienskript Chwallek Kap. 2.5"
        },
        {
            "q": "Welche Annahme trifft die Laplace-Regel zur Entscheidungsfindung unter Unsicherheit?",
            "o": ["Der Entscheider ist extrem optimistisch.", "Alle Umweltzustände treten mit der gleichen Wahrscheinlichkeit ein.", "Es wird die Alternative mit dem geringsten Bedauern gewählt.", "Nur der schlechteste Umweltzustand wird betrachtet."],
            "c": 1,
            "s": "Die Laplace-Regel unterstellt eine Gleichverteilung aller möglichen Umweltzustände.",
            "src": "Folienskript Chwallek Kap. 2.5"
        },
        # bwl1_other (need 3)
        {
            "q": "Welcher Grundsatz besagt, dass die Erstellung betrieblicher Leistungen wertmäßig über dem Einsatz der Ressourcen liegen soll?",
            "o": ["Das Wertschöpfungsprinzip", "Das Liquiditätsprinzip", "Das Publizitätsprinzip", "Das Haftungsprinzip"],
            "c": 0,
            "s": "Die Wertschöpfung drückt den geschaffenen Mehrwert über die eingesetzten Vorleistungen aus.",
            "src": "Folienskript Chwallek Kap. 2.3"
        },
        {
            "q": "Welche der folgenden Unternehmensziele stehen in einem Zielkonflikt zueinander?",
            "o": ["Gewinnmaximierung und Kostensenkung", "Umsatzsteigerung und Markterschließung", "Steigerung der Dividende und Erhöhung der Mitarbeiterzufriedenheit", "Qualitätsverbesserung und Senkung der Fehlerquote"],
            "c": 2,
            "s": "Höhere Dividende (Eigentümerinteresse) und höhere Gehälter/Zufriedenheit (Mitarbeiterinteresse) stehen oft in einem Zielkonflikt.",
            "src": "Folienskript Chwallek Kap. 2.3"
        },
        {
            "q": "Wenn zwei Unternehmensziele sich gegenseitig unterstützen (z.B. Senkung von Ausschuss und Erhöhung des Gewinns), wie nennt man diese Zielbeziehung?",
            "o": ["Komplementäre Ziele", "Konkurrierende Ziele", "Indifferente Ziele", "Antagonistischer Widerspruch"],
            "c": 0,
            "s": "Komplementäre Ziele unterstützen einander.",
            "src": "Folienskript Chwallek Kap. 2.3"
        }
    ],
    "bwl2": [
        # bwl2_erfolgskonten (need 2)
        {
            "q": "Auf welches übergeordnete Konto wird der Saldo des Gewinn- und Verlustkontos (GuV) am Jahresende abgeschlossen?",
            "o": ["Bankkonto", "Eigenkapitalkonto", "Schlussbilanzkonto (SBK)", "Privatkonto"],
            "c": 1,
            "s": "Der Erfolg (Gewinn oder Verlust) verändert das Eigenkapital des Unternehmens direkt und wird auf das Eigenkapitalkonto abgeschlossen.",
            "src": "Foliensatz BUF Kap. 8-9"
        },
        {
            "q": "Wie werden Aufwendungen auf den Erfolgskonten erfasst?",
            "o": ["Immer im Soll", "Immer im Haben", "Wahlweise im Soll oder Haben", "Nur am Jahresende als Sammelbuchung"],
            "c": 0,
            "s": "Aufwendungen mindern das Eigenkapital und werden daher immer im Soll des jeweiligen Aufwandskontos gebucht.",
            "src": "Foliensatz BUF Kap. 8-9"
        },
        # bwl2_umsatzsteuer (need 2)
        {
            "q": "Welchen Charakter hat die Umsatzsteuer (USt) beim Verkauf von Waren aus Sicht des buchenden Unternehmens?",
            "o": ["Forderung gegenüber dem Finanzamt", "Verbindlichkeit gegenüber dem Finanzamt", "Sofortiger betrieblicher Aufwand", "Ertragserhöhendes Element"],
            "c": 1,
            "s": "Die eingenommene Umsatzsteuer ist eine Verbindlichkeit gegenüber dem Finanzamt und wird auf der Passivseite der Bilanz ausgewiesen.",
            "src": "Foliensatz BUF Kap. 10.2"
        },
        {
            "q": "Wann darf ein Unternehmen die gezahlte Vorsteuer (VSt) geltend machen?",
            "o": ["Nur wenn das Unternehmen keine Gewinne macht", "Beim Einkauf von Waren oder Dienstleistungen von anderen umsatzsteuerpflichtigen Unternehmen", "Nur am Jahresende bei der Steuererklärung", "Beim privaten Einkauf des Inhabers"],
            "c": 1,
            "s": "Unternehmen sind vorsteuerabzugsberechtigt für betriebliche Einkäufe von anderen umsatzsteuerpflichtigen Unternehmen.",
            "src": "Foliensatz BUF Kap. 10.2"
        },
        # bwl2_privat (need 2)
        {
            "q": "Über welches Konto wird das Privatkonto eines Einzelunternehmers am Ende des Geschäftsjahres abgeschlossen?",
            "o": ["Gewinn- und Verlustkonto (GuV)", "Eigenkapitalkonto", "Schlussbilanzkonto (SBK)", "Kasse"],
            "c": 1,
            "s": "Das Privatkonto ist ein Unterkonto des Eigenkapitalkontos und wird direkt über dieses abgeschlossen.",
            "src": "Foliensatz BUF Kap. 12-13"
        },
        {
            "q": "Welche Auswirkung hat eine Privatentnahme des Inhabers auf den Gewinn des Unternehmens?",
            "o": ["Der Gewinn steigt", "Der Gewinn sinkt", "Keine Auswirkung auf den Gewinn, es mindert nur das Eigenkapital", "Der Gewinn verdoppelt sich"],
            "c": 2,
            "s": "Privatentnahmen und -einlagen sind erfolgsneutral. Sie verändern das Eigenkapital, beeinflussen aber nicht die GuV (den Gewinn).",
            "src": "Foliensatz BUF Kap. 12-13"
        },
        # bwl2_absatz (need 5)
        {
            "q": "Wie lautet der Buchungssatz für den Verkauf von fertigen Erzeugnissen auf Ziel?",
            "o": ["Forderungen an Umsatzerlöse und Umsatzsteuer", "Umsatzerlöse an Forderungen und Umsatzsteuer", "Bank an Umsatzerlöse", "Forderungen an Bank und Umsatzsteuer"],
            "c": 0,
            "s": "Verkauf auf Ziel bedeutet eine Forderung entsteht im Soll, Erlöse und USt im Haben.",
            "src": "Foliensatz BUF Kap. 16 "
        },
        {
            "q": "Was versteht man unter einer 'Einzelwertberichtigung' (EWB) auf Forderungen?",
            "o": ["Die pauschale Kürzung aller Forderungen um 5%", "Die Bewertung des konkreten Ausfallrisikos einer einzelnen, bestimmten Forderung", "Das Abschreiben des gesamten Forderungsbestands", "Die Erhöhung von Forderungen wegen Zinsansprüchen"],
            "c": 1,
            "s": "Eine EWB bewertet eine konkrete, zweifelhafte Forderung einzeln nach dem Grad der Wahrscheinlichkeit des Ausfalls.",
            "src": "Foliensatz BUF Kap. 16 "
        },
        {
            "q": "Wie wird eine uneinbringliche Forderung (sicherer Ausfall) gebucht?",
            "o": ["Abschreibung auf Forderungen und Umsatzsteuerkorrektur an Forderungen", "Forderungen an Abschreibungen", "Gewinn an Forderungen", "Privat an Forderungen"],
            "c": 0,
            "s": "Bei Uneinbringlichkeit muss die Forderung komplett abgeschrieben und auch die abgeführte Umsatzsteuer korrigiert werden.",
            "src": "Foliensatz BUF Kap. 16 "
        },
        {
            "q": "Welcher Wertansatz gilt für Forderungen nach dem strengen Niederstwertprinzip am Bilanzstichtag?",
            "o": ["Der Nominalwert (Nennwert) abzüglich erkennbarer Wertminderungen", "Der Anschaffungswert plus Zinsansprüche", "Der geschätzte Marktwert der Forderung", "Ein fiktiver Wert"],
            "c": 0,
            "s": "Forderungen müssen nach dem Niederstwertprinzip am Bilanzstichtag zum Nominalwert abzüglich aller erkennbaren Risiken (Wertberichtigungen) bewertet werden.",
            "src": "Foliensatz BUF Kap. 16 "
        },
        {
            "q": "Was ist der Unterschied zwischen einem Rabatt und einem Skonto im Absatzbereich?",
            "o": ["Skonto wird sofort bei Rechnungsstellung abgezogen, Rabatt bei schneller Zahlung", "Rabatt wird direkt vom Listenpreis abgezogen, Skonto gewährt einen Nachlass bei Zahlung innerhalb einer Frist", "Es gibt keinen Unterschied", "Skonto erhöht den Preis, Rabatt mindert ihn"],
            "c": 1,
            "s": "Rabatt wird bei Kauf direkt abgezogen, Skonto ist eine nachträgliche Preisminderung für schnelle Zahlung.",
            "src": "Foliensatz BUF Kap. 16 "
        }
    ],
    "mawi1": [
        # mawi1_1_2 (need 3)
        {
            "q": "Welche Eigenschaft charakterisiert eine quadratische Funktion der Form f(x) = ax² + bx + c, wenn der Koeffizient a negativ ist?",
            "o": ["Die Parabel ist nach oben geöffnet und besitzt ein Minimum.", "Die Parabel ist nach unten geöffnet und besitzt ein Maximum.", "Die Funktion ist streng monoton steigend.", "Die Funktion hat keine Nullstellen."],
            "c": 1,
            "s": "Bei a < 0 ist die Parabel nach unten geöffnet und hat einen Scheitelpunkt als globales Maximum.",
            "src": "WiMa 1 Kap. 1.2"
        },
        {
            "q": "Wie verhält sich die e-Funktion f(x) = e^x für x gegen minus unendlich?",
            "o": ["Sie geht gegen unendlich.", "Sie nähert sich asymptotisch der 0.", "Sie geht gegen minus unendlich.", "Sie nimmt den Wert 1 an."],
            "c": 1,
            "s": "lim (x->-inf) e^x = 0.",
            "src": "WiMa 1 Kap. 1.2"
        },
        {
            "q": "Welche Funktion ist die Umkehrfunktion der natürlichen Logarithmusfunktion f(x) = ln(x) für x > 0?",
            "o": ["g(x) = x²", "g(x) = e^x", "g(x) = 1/x", "g(x) = 10^x"],
            "c": 1,
            "s": "Die Exponentialfunktion e^x ist die Umkehrfunktion zum natürlichen Logarithmus ln(x).",
            "src": "WiMa 1 Kap. 1.2"
        },
        # mawi1_2 (need 1)
        {
            "q": "Wie lautet die erste Ableitung der Funktion f(x) = 3x^4 - 5x + 2 nach den Ableitungsregeln?",
            "o": ["f'(x) = 12x³ - 5", "f'(x) = 12x^4 - 5", "f'(x) = 3x³ - 5", "f'(x) = 12x³"],
            "c": 0,
            "s": "f'(x) = 3*4*x^(4-1) - 5 = 12x³ - 5.",
            "src": "WiMa 1 Kap. 2"
        }
    ],
    "mawi2": [
        # mawi2_1 (need 4)
        {
            "q": "Welches Skalenniveau besitzt das Merkmal 'Schulnoten (sehr gut bis ungenügend)'?",
            "o": ["Nominalskala", "Ordinalskala", "Intervallskala", "Verhältnisskala"],
            "c": 1,
            "s": "Noten haben eine Rangfolge (besser/schlechter), aber Abstände sind nicht exakt messbar, daher Ordinalskala.",
            "src": "Statistik Kap. 1"
        },
        {
            "q": "Welches Merkmal ist ein Beispiel für eine Nominalskala?",
            "o": ["Körpergröße in cm", "Geburtsort (z.B. Aachen, Köln)", "Zufriedenheit (sehr zufrieden bis unzufrieden)", "Temperatur in Grad Celsius"],
            "c": 1,
            "s": "Nominale Merkmale haben keine natürliche Rangordnung, nur Kategorien zur Unterscheidung.",
            "src": "Statistik Kap. 1"
        },
        {
            "q": "Was unterscheidet eine Verhältnisskala von einer Intervallskala?",
            "o": ["Die Verhältnisskala hat keinen Nullpunkt.", "Die Verhältnisskala besitzt einen natürlichen, absoluten Nullpunkt.", "Auf der Verhältnisskala kann man keine Abstände vergleichen.", "Sie sind identisch."],
            "c": 1,
            "s": "Ein absoluter Nullpunkt existiert nur bei der Verhältnisskala (z.B. Einkommen, Alter), nicht bei der Intervallskala (z.B. Temperatur in °C).",
            "src": "Statistik Kap. 1"
        },
        {
            "q": "Welches Merkmal ist diskret im Gegensatz zu stetig?",
            "o": ["Körpergewicht", "Anzahl der Kinder in einer Familie", "Fahrzeit zur Hochschule", "Benzinverbrauch eines Autos"],
            "c": 1,
            "s": "Diskrete Merkmale nehmen nur abzählbare, isolierte Werte an (z.B. ganze Zahlen).",
            "src": "Statistik Kap. 1"
        }
    ],
    "wpr": [
        # wpr_6 (need 1)
        {
            "q": "Wer ist Kaufmann im Sinne des § 1 HGB?",
            "o": ["Jeder, der Waren einkauft und verkauft", "Wer ein Handelsgewerbe betreibt", "Nur Aktiengesellschaften", "Jeder Freiberufler"],
            "c": 1,
            "s": "Kaufmann ist nach § 1 Abs. 1 HGB, wer ein Handelsgewerbe betreibt.",
            "src": "WPR Handelsrecht"
        },
        # wpr_7 (need 4)
        {
            "q": "Welches Recht steht dem Käufer bei einer mangelhaften Lieferung nach § 437 BGB primär zu?",
            "o": ["Rücktritt vom Vertrag", "Minderung des Kaufpreises", "Nacherfüllung (Beseitigung des Mangels oder Lieferung einer mangelfreien Sache)", "Schadensersatz statt der Leistung"],
            "c": 2,
            "s": "Das Recht auf Nacherfüllung (§ 439 BGB) ist im deutschen Gewährleistungsrecht primär (Vorrang der Nacherfüllung).",
            "src": "WPR Kaufrecht / Verbraucherschutz"
        },
        {
            "q": "Wann geht die Gefahr des zufälligen Untergangs beim Versendungskauf unter Verbrauchern (Verbrauchsgüterkauf, § 474 BGB) auf den Käufer über?",
            "o": ["Bei Übergabe der Ware an den Transporteur", "Erst mit der Übergabe der Ware an den Verbraucher (§ 475 Abs. 2 BGB)", "Mit dem Abschluss des Kaufvertrags", "Wenn die Ware das Lager des Verkäufers verlässt"],
            "c": 1,
            "s": "Beim Verbrauchsgüterkauf geht die Gefahr erst bei Übergabe an den Verbraucher über. § 447 BGB gilt hier im Regelfall nicht.",
            "src": "WPR Kaufrecht / Verbraucherschutz"
        },
        {
            "q": "Wie hoch ist die gesetzliche Verjährungsfrist für Mängelansprüche bei neu hergestellten beweglichen Sachen im Regelfall (§ 438 Abs. 1 Nr. 3 BGB)?",
            "o": ["6 Monate", "1 Jahr", "2 Jahre", "3 Jahre"],
            "c": 2,
            "s": "Die Gewährleistungsfrist beträgt im Regelfall zwei Jahre ab Ablieferung der Sache.",
            "src": "WPR Kaufrecht / Verbraucherschutz"
        },
        {
            "q": "Was ist ein Sachmangel im Sinne des § 434 BGB?",
            "o": ["Wenn die Sache bei Gefahrübergang nicht die vereinbarte Beschaffenheit aufweist", "Wenn ein Dritter Rechte an der Sache geltend machen kann", "Wenn der Preis zu hoch war", "Wenn der Käufer die Sache nicht mehr mag"],
            "c": 0,
            "s": "Ein Sachmangel liegt vor, wenn die Ist-Beschaffenheit bei Gefahrübergang von der vertraglich vereinbarten Soll-Beschaffenheit abweicht.",
            "src": "WPR Kaufrecht / Verbraucherschutz"
        },
        # wpr_other (need 2)
        {
            "q": "Wer trägt im Zivilprozess grundsätzlich die Beweislast für eine anspruchsbegründende Tatsache?",
            "o": ["Der Richter", "Die Partei, die sich auf diese Tatsache beruft, um eine ihr günstige Rechtsfolge abzuleiten", "Stets der Beklagte", "Immer der Kläger"],
            "c": 1,
            "s": "Im Zivilprozess trägt jede Partei die Beweislast für die Voraussetzungen der ihr günstigen Rechtsnorm (Grundsatz).",
            "src": "WPR Foliensatz – Beweis"
        },
        {
            "q": "Welche Ausnahme von den allgemeinen Beweislastregeln gilt beim Verbrauchsgüterkauf innerhalb der ersten Monate (§ 477 BGB)?",
            "o": ["Eine Beweislastumkehr zugunsten des Verbrauchers bezüglich des Vorliegens des Mangels bei Gefahrübergang", "Der Verbraucher muss gar nichts beweisen", "Der Unternehmer entscheidet, wer die Beweislast trägt", "Es gilt keine Ausnahme"],
            "c": 0,
            "s": "Zeigt sich innerhalb der ersten Monate (gesetzlich geregelt) ein Sachmangel, wird vermutet, dass dieser bereits bei Gefahrübergang vorlag (Beweislastumkehr).",
            "src": "WPR Foliensatz – Beweis"
        }
    ]
}

# Append and save questions
for subj, qs in extra_questions.items():
    for q in qs:
        # Standard default keys
        if "type" not in q:
            q["type"] = "mc"
        if "points" not in q:
            q["points"] = 5
        if "difficulty" not in q:
            q["difficulty"] = "mittel"
        QS[subj].append(q)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(QS, f, ensure_ascii=False, indent=2)

print("✅ Extra Fragen erfolgreich hinzugefügt!")
