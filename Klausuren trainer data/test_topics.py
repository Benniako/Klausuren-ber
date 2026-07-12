"""Testet, ob alle Fragen durch genau ein Thema gematcht werden."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE, "_data", "questions_validated.json"), encoding="utf-8") as f:
    QS = json.load(f)
with open(os.path.join(BASE, "_data", "topics.json"), encoding="utf-8") as f:
    TOPICS = json.load(f)

# Bank-Mapping (Part -> Hauptfach-Bank)
PART_TO_BANK = {
    "bwl1": "bwl1", "bwl2": "bwl2",
    "mawi1": "mawi1", "mawi2": "mawi2",
    "vwl": "vwl", "wpr": "wpr", "perso": "perso",
}

total_matched = 0
total_questions = 0
total_orphans = 0
total_overlaps = 0

for subj_key, topics in TOPICS.items():
    # Sammle alle Fragen dieses Fachs (alle Parts)
    all_qs = []
    for topic in topics:
        # topic hat filter-Array, wir suchen passende Bank
        pass

    # Alle Fragen des Fachs sammeln
    subj_qs = []
    for bank in [subj_key]:
        subj_qs.extend([(bank, i, q) for i, q in enumerate(QS[bank])])

    total_questions += len(subj_qs)

    matched_count = 0
    orphans = []
    overlaps = []

    for bank, qi, q in subj_qs:
        matches = []
        for topic in topics:
            for prefix in topic["filter"]:
                if q["src"].startswith(prefix):
                    matches.append(topic["id"])
                    break
        if len(matches) == 0:
            orphans.append(q["src"][:80])
        elif len(matches) > 1:
            overlaps.append((q["src"][:60], matches))
        else:
            matched_count += 1

    total_matched += matched_count
    total_orphans += len(orphans)
    total_overlaps += len(overlaps)

    status = "✅" if not orphans and not overlaps else "❌"
    print(f"{status} {subj_key}: {matched_count}/{len(subj_qs)} matched, {len(orphans)} orphans, {len(overlaps)} overlaps")
    if orphans:
        print(f"   ORPHANS:")
        for o in set(orphans):
            print(f"     - {o}")
    if overlaps:
        print(f"   OVERLAPS:")
        for src, m in overlaps[:5]:
            print(f"     - {src} → {m}")

print(f"\n{'='*50}")
print(f"TOTAL: {total_matched}/{total_questions} matched, {total_orphans} orphans, {total_overlaps} overlaps")
print(f"Verdict: {'✅ ALL OK' if total_orphans == 0 and total_overlaps == 0 else '❌ NEEDS FIX'}")
