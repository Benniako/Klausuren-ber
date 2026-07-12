"""
Generiert das finale Klausuren-Trainer HTML mit:
- 196 Fragen (25+ pro Fach) mit echten Lösungen
- 'Wichtige Gesetze/Formeln' Tab pro Fach
- Sauberer Code, keine Bugs
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

# Lade Daten (validiert - nur geprüfte Fragen)
with open(os.path.join(BASE, "_data", "questions_validated.json"), "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

with open(os.path.join(BASE, "_data", "summaries.json"), "r", encoding="utf-8") as f:
    SUMMARIES = json.load(f)

with open(os.path.join(BASE, "_data", "topics.json"), "r", encoding="utf-8") as f:
    TOPICS = json.load(f)

def js_string(s):
    """Escaped JS-String"""
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n").replace("`", "\\`")

def gen_questions_js(bank_name, questions):
    lines = []
    for i, q in enumerate(questions):
        q_type = q.get("type", "mc")
        sol = js_string(q["s"])
        src = js_string(q["src"])
        diag = q.get("diagram", "")
        diag_str = f",diagram:'{diag}'" if diag else ""
        
        if q_type == "fitb":
            correct_val = f"'{js_string(str(q['c']))}'"
            acc_list = q.get("acceptable", [])
            acc_js = ", ".join(f"'{js_string(a)}'" for a in acc_list)
            acc_str = f",acceptable:[{acc_js}]" if acc_list else ""
            lines.append(f"{{id:'{bank_name}_{i}',type:'fitb',points:5,question:'{js_string(q['q'])}',options:[],correct:{correct_val},solution:'{sol}',source:'{src}'{diag_str}{acc_str}}}")
        else:
            opts = [js_string(o) for o in q["o"]]
            opts_str = ", ".join(f"'{o}'" for o in opts)
            lines.append(f"{{id:'{bank_name}_{i}',type:'mc',points:{4 if len(opts)>=4 else 3},question:'{js_string(q['q'])}',options:[{opts_str}],correct:{q['c']},solution:'{sol}',source:'{src}'{diag_str}}}")
    return f"var QUESTION_BANK_{bank_name} = [{', '.join(lines)}];"

# Generiere Fragen-JS
all_banks_js = []
for bank, qs in QUESTIONS.items():
    all_banks_js.append(gen_questions_js(bank, qs))
questions_js = "\n".join(all_banks_js)

# Generiere Themen-JS
def gen_topics_js():
    parts = []
    for subj, topics in TOPICS.items():
        topic_lines = []
        for t in topics:
            filters = ",".join(f"'{js_string(f)}'" for f in t["filter"])
            topic_lines.append(
                f"{{id:'{js_string(t['id'])}',name:'{js_string(t['name'])}',icon:'{t['icon']}',"
                f"filter:[{filters}],explanation:'{js_string(t['explanation'])}'}}"
            )
        parts.append(f"  '{subj}':[{','.join(topic_lines)}]")
    return "var TOPICS = {\n" + ",\n".join(parts) + "\n};"

topics_js = gen_topics_js()

# Generiere Zusammenfassungs-JS
summaries_js_parts = []
for bank, summary in SUMMARIES.items():
    summaries_js_parts.append("  '" + bank + "': `" + summary.replace("`", "'") + "`")
summaries_js = "var SUMMARIES = {\n" + ",\n".join(summaries_js_parts) + "\n};"

# Generiere Materialien-JS
def gen_materials_js():
    materials = {
        'bwl': [],
        'mawi': [],
        'vwl': [],
        'wpr': [],
        'perso': []
    }
    mapping = {
        'bwl': 'bwl',
        'mawi': 'mathe und statistik',
        'vwl': 'vwl',
        'wpr': 'wpr',
        'perso': 'Perso'
    }
    workspace_root = os.path.dirname(BASE)
    for key, folder in mapping.items():
        folder_path = os.path.join(workspace_root, folder)
        if os.path.exists(folder_path):
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.startswith('.') or file.startswith('~'):
                        continue
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, workspace_root)
                    
                    # Determine category (Klausur, Zusatzübung, etc.)
                    category = "Allgemein"
                    rel_dir = os.path.relpath(root, folder_path)
                    if rel_dir != ".":
                        category = rel_dir
                    elif "klausur" in file.lower() or "pruefung" in file.lower() or "prüfung" in file.lower() or "probeklausur" in file.lower() or "testklausur" in file.lower():
                        category = "Klausuren & Prüfungen"
                    elif "uebung" in file.lower() or "übung" in file.lower() or "tutorium" in file.lower() or "blatt" in file.lower() or "aufgaben" in file.lower() or "loesungen" in file.lower() or "lösungen" in file.lower():
                        category = "Übungen & Tutorien"
                    elif "folie" in file.lower() or "skript" in file.lower() or "vorl" in file.lower() or "mitschrift" in file.lower():
                        category = "Vorlesungsfolien & Skripte"
                    
                    ext = os.path.splitext(file)[1].lower().replace('.', '')
                    materials[key].append({
                        'name': file,
                        'path': '/' + rel_path.replace('\\', '/'),
                        'category': category,
                        'ext': ext
                    })
            materials[key].sort(key=lambda x: (x['category'], x['name']))
    return "var MATERIALS = " + json.dumps(materials, ensure_ascii=False) + ";"

materials_js = gen_materials_js()

HTML = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>📚 Klausuren-Trainer – FH Aachen</title>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#0a0e1a;--bg2:#111827;--bg3:#1a2332;--bg4:#1e293b;--text:#e2e8f0;--text2:#94a3b8;--text3:#64748b;--accent:#38bdf8;--accent2:#818cf8;--accent3:#34d399;--danger:#ef4444;--warning:#f59e0b;--success:#22c55e;--border:#1e293b;--radius:12px;--radius-sm:8px;--font:'Inter','Segoe UI',system-ui,sans-serif}
html{font-size:15px}
body{font-family:var(--font);background:var(--bg);color:var(--text);min-height:100vh;overflow-x:hidden}
::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:var(--bg2)}::-webkit-scrollbar-thumb{background:var(--bg4);border-radius:3px}
button{cursor:pointer;font-family:inherit;border:none;outline:none;transition:all .2s}
input,select{font-family:inherit}
.app{display:flex;min-height:100vh}
.sidebar{width:240px;background:var(--bg2);border-right:1px solid var(--border);padding:20px 12px;display:flex;flex-direction:column;flex-shrink:0;position:sticky;top:0;height:100vh;overflow-y:auto}
.sidebar-brand{font-size:1.15rem;font-weight:700;padding:0 8px 20px;display:flex;align-items:center;gap:10px;border-bottom:1px solid var(--border);margin-bottom:16px}
.sidebar-brand span{background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.main{flex:1;padding:24px 32px;max-width:1000px;margin:0 auto;width:100%}
.subj-btn{display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:var(--radius-sm);background:transparent;color:var(--text2);font-size:.9rem;font-weight:500;text-align:left;width:100%;margin-bottom:4px;transition:all .2s}
.subj-btn:hover{background:var(--bg3);color:var(--text)}
.subj-btn.active{background:var(--bg4);color:var(--text);box-shadow:inset 3px 0 0 var(--accent)}
.subj-btn .icon{font-size:1.2rem;width:28px;text-align:center}
.subj-btn .badge{font-size:.65rem;padding:2px 7px;border-radius:10px;background:var(--bg4);color:var(--text3);margin-left:auto}
.subj-btn.active .badge{background:var(--accent);color:var(--bg)}
.subj-btn .sub{font-size:.65rem;color:var(--text3);display:block;margin-top:1px}
.tab-btn{padding:10px 16px;border-radius:var(--radius-sm);background:var(--bg3);color:var(--text2);font-size:.85rem;font-weight:600;margin-bottom:8px;width:100%;text-align:left}
.tab-btn:hover{background:var(--bg4)}
.tab-btn.active{background:linear-gradient(135deg,var(--accent),var(--accent2));color:var(--bg)}
.timer-bar{display:flex;align-items:center;gap:16px;padding:16px 20px;background:var(--bg3);border-radius:var(--radius);margin-bottom:24px;border:1px solid var(--border);flex-wrap:wrap}
.timer-display{font-size:2rem;font-weight:700;font-variant-numeric:tabular-nums;letter-spacing:2px;min-width:100px;font-family:'JetBrains Mono',monospace}
.timer-display.warning{color:var(--warning);animation:pulse 1s infinite}
.timer-display.danger{color:var(--danger);animation:pulse .5s infinite}
.timer-controls{display:flex;gap:8px;margin-left:auto}
.timer-btn{padding:8px 16px;border-radius:var(--radius-sm);font-size:.8rem;font-weight:600;background:var(--bg4);color:var(--text2)}
.timer-btn:hover{background:var(--accent);color:var(--bg)}
.timer-btn.success{background:linear-gradient(135deg,var(--success),#059669);color:var(--bg)}
.timer-settings{display:flex;align-items:center;gap:8px;color:var(--text3);font-size:.85rem}
.timer-settings input{width:50px;padding:4px 8px;border-radius:6px;background:var(--bg4);color:var(--text);border:1px solid var(--border);text-align:center}
.timer-settings select{padding:4px 8px;border-radius:6px;background:var(--bg4);color:var(--text);border:1px solid var(--border)}
.progress-bar{width:100%;height:3px;background:var(--bg4);border-radius:2px;margin-top:4px;overflow:hidden}
.progress-fill{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));transition:width 1s linear;border-radius:2px}
.progress-fill.warning{background:linear-gradient(90deg,var(--warning),var(--danger))}
.progress-fill.danger{background:var(--danger);animation:flashBar .5s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}
@keyframes flashBar{0%,100%{opacity:1}50%{opacity:.3}}
.exam-header{margin-bottom:24px}
.exam-title{font-size:1.5rem;font-weight:700;margin-bottom:4px}
.exam-meta{display:flex;gap:16px;flex-wrap:wrap;color:var(--text3);font-size:.85rem;margin-top:6px}
.exam-meta .dot{width:8px;height:8px;border-radius:50%;display:inline-block;background:var(--accent)}
.questions{display:flex;flex-direction:column;gap:20px}
.question-card{background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius);padding:24px;transition:all .2s}
.question-card.correct{border-left:4px solid var(--success)}
.question-card.incorrect{border-left:4px solid var(--danger)}
.q-number{font-size:.75rem;text-transform:uppercase;letter-spacing:1px;color:var(--text3);margin-bottom:4px}
.q-text{font-size:1.05rem;font-weight:500;margin-bottom:16px;line-height:1.6}
.q-source{font-size:.75rem;color:var(--text3);background:var(--bg4);display:inline-block;padding:3px 10px;border-radius:20px;margin-bottom:12px}
.q-source strong{color:var(--accent)}
.options{display:flex;flex-direction:column;gap:8px}
.option{display:flex;align-items:center;gap:12px;padding:12px 16px;background:var(--bg4);border-radius:var(--radius-sm);cursor:pointer;transition:all .15s;border:1px solid transparent}
.option:hover{background:var(--bg3);border-color:var(--text3)}
.option.selected{background:rgba(56,189,248,.1);border-color:var(--accent)}
.option.correct-answer{background:rgba(34,197,94,.12);border-color:var(--success)}
.option.wrong-answer{background:rgba(239,68,68,.12);border-color:var(--danger)}
.option .radio{width:18px;height:18px;border-radius:50%;border:2px solid var(--text3);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.option.selected .radio{border-color:var(--accent);background:var(--accent)}
.option.selected .radio::after{content:'';width:6px;height:6px;border-radius:50%;background:var(--bg)}
.solution{display:none;margin-top:16px;padding:16px;background:rgba(56,189,248,.05);border-radius:var(--radius-sm);border:1px solid rgba(56,189,248,.15)}
.solution.show{display:block;animation:fadeIn .3s}
.solution h4{font-size:.85rem;color:var(--accent);margin-bottom:8px}
.solution p{font-size:.9rem;line-height:1.6;color:var(--text2)}
.solution .ref{font-size:.78rem;color:var(--text3);margin-top:8px;padding-top:8px;border-top:1px solid var(--border)}
@keyframes fadeIn{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:translateY(0)}}
.submit-area{display:flex;gap:12px;margin-top:28px;padding-top:20px;border-top:1px solid var(--border);flex-wrap:wrap}
.btn{padding:12px 28px;border-radius:var(--radius-sm);font-weight:600;font-size:.9rem}
.btn-primary{background:linear-gradient(135deg,var(--accent),var(--accent2));color:var(--bg);box-shadow:0 4px 16px rgba(56,189,248,.25)}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 6px 24px rgba(56,189,248,.35)}
.btn-secondary{background:var(--bg4);color:var(--text2)}
.btn-secondary:hover{background:var(--bg3);color:var(--text)}
.btn-success{background:linear-gradient(135deg,var(--success),#059669);color:var(--bg)}
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);backdrop-filter:blur(8px);z-index:1000;justify-content:center;align-items:center;padding:20px}
.overlay.show{display:flex;animation:fadeIn .3s}
.result-card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);max-width:700px;width:100%;max-height:90vh;overflow-y:auto;padding:40px}
.result-grade{text-align:center;padding:20px 0}
.result-grade .grade{font-size:5rem;font-weight:800;line-height:1}
.result-grade .grade.passed{background:linear-gradient(135deg,var(--success),var(--accent3));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.result-grade .grade.failed{color:var(--danger)}
.result-grade .label{font-size:1.1rem;color:var(--text2);margin-top:8px}
.result-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;margin:24px 0}
.stat-box{text-align:center;padding:16px;background:var(--bg3);border-radius:var(--radius-sm)}
.stat-box .num{font-size:1.8rem;font-weight:700}
.stat-box .desc{font-size:.8rem;color:var(--text3);margin-top:2px}
.summary-box{background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius);padding:32px;line-height:1.7;color:var(--text2);font-size:.9rem;max-width:none}
.summary-box h1,.summary-box h2,.summary-box h3{color:var(--accent);margin:20px 0 10px}
.summary-box h1{font-size:1.5rem}.summary-box h2{font-size:1.2rem}.summary-box h3{font-size:1.05rem}
.summary-box table{border-collapse:collapse;width:100%;margin:12px 0}
.summary-box th,.summary-box td{border:1px solid var(--border);padding:8px;text-align:left}
.summary-box th{background:var(--bg4);color:var(--accent)}
.summary-box code{background:var(--bg4);padding:2px 6px;border-radius:4px;font-family:monospace;color:var(--accent3)}
.summary-box pre{background:var(--bg4);padding:12px;border-radius:var(--radius-sm);overflow-x:auto;margin:12px 0}
.welcome{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:60px 20px;min-height:60vh}
.welcome .icon{font-size:4rem;margin-bottom:16px}
.welcome h1{font-size:2rem;font-weight:700;margin-bottom:8px;background:linear-gradient(135deg,var(--accent),var(--accent2),var(--accent3));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.welcome p{color:var(--text2);max-width:500px;line-height:1.7}
.mobile-header {
  display: none;
}
.sidebar-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(4px);
  z-index: 1999;
}
@media(max-width:768px){
  .app {
    flex-direction: column;
  }
  .mobile-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 16px;
    background: var(--bg2);
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 0;
    z-index: 1000;
    width: 100%;
  }
  .mobile-header .menu-toggle {
    background: var(--bg3);
    border: 1px solid var(--border);
    color: var(--text);
    font-size: 1.4rem;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 42px;
    height: 42px;
    border-radius: var(--radius-sm);
  }
  .mobile-header .brand-title {
    font-size: 1.15rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .sidebar {
    position: fixed;
    left: -280px;
    top: 0;
    width: 260px;
    height: 100vh;
    z-index: 2000;
    transition: left 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 10px 0 30px rgba(0,0,0,0.5);
  }
  .sidebar.open {
    left: 0;
  }
  .sidebar-overlay.active {
    display: block;
  }
  .main {
    padding: 16px;
  }
  .result-card {
    padding: 20px;
  }
}
.diagram-box{background:var(--bg4);border:1px solid var(--border);border-radius:var(--radius-sm);padding:16px;margin:12px 0;display:flex;justify-content:center;overflow:hidden}
.diagram-box svg{max-width:100%;height:auto}
.diagram-box .caption{text-align:center;color:var(--text3);font-size:.8rem;margin-top:8px}
.summary-box h1{color:var(--accent);font-size:1.5rem;margin:24px 0 12px;padding-bottom:8px;border-bottom:2px solid var(--accent)}
.summary-box h2{color:var(--accent2);font-size:1.2rem;margin:20px 0 8px}
.summary-box h3{color:var(--accent3);font-size:1.05rem;margin:16px 0 6px}
.summary-box p{margin:8px 0}
.summary-box strong{color:var(--text);font-weight:600}
.summary-box em{color:var(--text2);font-style:italic}
.summary-box ul{margin:8px 0;padding-left:24px}
.summary-box li{margin:4px 0}
.summary-box table{border-collapse:collapse;width:100%;margin:14px 0;font-size:.82rem;background:var(--bg4)}
.summary-box th,.summary-box td{border:1px solid var(--border);padding:8px 10px;text-align:left;word-break:break-word;max-width:280px;vertical-align:top}
.summary-box th{background:var(--bg2);color:var(--accent);font-weight:600}
.summary-box tr:nth-child(even){background:rgba(56,189,248,.03)}
.summary-box code{background:var(--bg4);padding:2px 6px;border-radius:4px;font-family:monospace;color:var(--accent3)}
.summary-box pre{background:var(--bg4);padding:14px;border-radius:var(--radius-sm);overflow-x:auto;margin:14px 0;border:1px solid var(--border)}
.summary-box pre code{background:none;padding:0;color:var(--accent3)}
.summary-box hr{border:none;border-top:1px solid var(--border);margin:24px 0}
/* Learn Mode */
.learn-controls{padding:12px 0;display:flex;gap:12px;flex-wrap:wrap;margin-bottom:16px}
.learn-controls select{padding:8px 14px;border-radius:var(--radius-sm);background:var(--bg4);color:var(--text);border:1px solid var(--border);font-size:.85rem;cursor:pointer}
.learn-controls select:focus{border-color:var(--accent);outline:none}
.learn-card{background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius);padding:32px;min-height:300px}
/* Themenliste */
.topic-list{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px}
.topic-card{background:var(--bg4);border:1px solid var(--border);border-radius:var(--radius-sm);padding:18px;cursor:pointer;display:flex;align-items:center;gap:14px;transition:all .2s}
.topic-card:hover{border-color:var(--accent);background:var(--bg3);transform:translateY(-2px);box-shadow:0 4px 16px rgba(56,189,248,.15)}
.topic-card .topic-icon{font-size:2rem;width:44px;text-align:center;flex-shrink:0}
.topic-card .topic-info{flex:1;min-width:0}
.topic-card .topic-name{font-weight:600;font-size:.95rem;margin-bottom:2px}
.topic-card .topic-count{font-size:.78rem;color:var(--text3)}
.topic-card .topic-arrow{color:var(--accent);font-size:.8rem;flex-shrink:0}
/* Themendetail */
.topic-detail-header{display:flex;align-items:center;gap:16px;margin-bottom:20px;flex-wrap:wrap}
.topic-back{padding:8px 14px!important;font-size:.85rem!important}
.topic-detail-title{font-size:1.3rem;font-weight:700;color:var(--accent)}
.topic-explanation{background:var(--bg4);border:1px solid var(--border);border-radius:var(--radius-sm);padding:24px;margin-bottom:20px;line-height:1.7;color:var(--text2);font-size:.92rem;max-height:500px;overflow-y:auto}
.topic-explanation h1,.topic-explanation h2,.topic-explanation h3{color:var(--accent);margin:18px 0 8px}
.topic-explanation h1{font-size:1.35rem}.topic-explanation h2{font-size:1.15rem}.topic-explanation h3{font-size:1rem}
.topic-explanation h1:first-child{margin-top:0}
.topic-explanation p{margin:8px 0}
.topic-explanation strong{color:var(--text);font-weight:600}
.topic-explanation em{color:var(--text2);font-style:italic}
.topic-explanation ul{margin:8px 0;padding-left:24px}
.topic-explanation li{margin:4px 0}
.topic-explanation code{background:var(--bg2);padding:2px 6px;border-radius:4px;font-family:monospace;color:var(--accent3)}
.topic-explanation pre{background:var(--bg2);padding:14px;border-radius:var(--radius-sm);overflow-x:auto;margin:14px 0;border:1px solid var(--border)}
.topic-explanation pre code{background:none;padding:0;color:var(--accent3)}
.topic-explanation table{border-collapse:collapse;width:100%;margin:14px 0;font-size:.82rem;background:var(--bg2)}
.topic-explanation th,.topic-explanation td{border:1px solid var(--border);padding:8px 10px;text-align:left;word-break:break-word;vertical-align:top}
.topic-explanation th{background:var(--bg4);color:var(--accent);font-weight:600}
.topic-explanation blockquote{border-left:3px solid var(--accent);padding:6px 14px;margin:10px 0;background:rgba(56,189,248,.05);color:var(--text2);font-style:italic}
.topic-action{text-align:center;padding:20px 0}
.topic-action .btn{padding:14px 32px;font-size:1rem}
.learn-card .q-number{font-size:.75rem;text-transform:uppercase;letter-spacing:1px;color:var(--text3);margin-bottom:4px}
.learn-card .q-source{font-size:.75rem;color:var(--text3);background:var(--bg4);display:inline-block;padding:3px 10px;border-radius:20px;margin-bottom:12px}
.learn-card .q-source strong{color:var(--accent)}
.learn-card .q-text{font-size:1.1rem;font-weight:500;margin-bottom:20px;line-height:1.6}
.learn-nav{display:flex;align-items:center;justify-content:space-between;padding:16px 0;gap:16px;flex-wrap:wrap}
.learn-nav-buttons{display:flex;gap:10px}
.learn-progress-dots{display:flex;gap:6px;flex-wrap:wrap}
.learn-progress-dots .dot{cursor:pointer}
.prog-dot{width:10px;height:10px;border-radius:50%;background:var(--bg4);cursor:pointer;transition:all .2s;border:none;padding:0;flex-shrink:0}
.prog-dot.active{background:var(--accent);box-shadow:0 0 6px var(--accent)}
.prog-dot.answered{background:var(--accent2)}
.prog-dot.correct{background:var(--success)}
.prog-dot.wrong{background:var(--danger)}
.learn-feedback{margin-top:20px;padding:16px 20px;border-radius:var(--radius-sm);display:none}
.learn-feedback.show{display:block;animation:fadeIn .3s}
.learn-feedback.correct{background:rgba(34,197,94,.1);border:1px solid var(--success)}
.learn-feedback.wrong{background:rgba(239,68,68,.1);border:1px solid var(--danger)}
.learn-feedback h4{font-size:.9rem;margin-bottom:6px}
.learn-feedback.correct h4{color:var(--success)}
.learn-feedback.wrong h4{color:var(--danger)}
.learn-feedback p{font-size:.9rem;line-height:1.6;color:var(--text2)}
.learn-feedback .ref{font-size:.78rem;color:var(--text3);margin-top:8px;padding-top:8px;border-top:1px solid var(--border)}
.learn-card .option.correct-answer{background:rgba(34,197,94,.12);border-color:var(--success)}
.learn-card .option.wrong-answer{background:rgba(239,68,68,.12);border-color:var(--danger)}
.learn-card .option.checked-correct{background:rgba(34,197,94,.12);border-color:var(--success)}
.learn-card .option.checked-wrong{background:rgba(239,68,68,.12);border-color:var(--danger)}
.learn-card .option.missed-correct{background:rgba(56,189,248,.08);border-color:var(--accent);border-style:dashed}
.learn-card .ft-input{width:100%;padding:12px 16px;border-radius:var(--radius-sm);background:var(--bg4);color:var(--text);border:2px solid var(--border);font-size:1rem;transition:border-color .2s}
.learn-card .ft-input:focus{border-color:var(--accent);outline:none}
.learn-card .ft-input.correct{border-color:var(--success);background:rgba(34,197,94,.05)}
.learn-card .ft-input.wrong{border-color:var(--danger);background:rgba(239,68,68,.05)}
.learn-card .answer-status{display:inline-flex;align-items:center;gap:6px;padding:6px 14px;border-radius:20px;font-size:.85rem;font-weight:600;margin-bottom:16px}
.learn-card .answer-status.correct{background:rgba(34,197,94,.15);color:var(--success)}
.learn-card .answer-status.wrong{background:rgba(239,68,68,.15);color:var(--danger)}
.learn-card .check-btn{padding:10px 24px;border-radius:var(--radius-sm);font-weight:600;font-size:.9rem;background:linear-gradient(135deg,var(--accent),var(--accent2));color:var(--bg);margin-top:16px}
.learn-card .check-btn:hover{transform:translateY(-1px);box-shadow:0 4px 16px rgba(56,189,248,.3)}
.learn-card .check-btn:disabled{opacity:.5;cursor:default;transform:none;box-shadow:none}
.material-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 12px;
}
.material-item {
  background: var(--bg4);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  padding: 12px 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: all .2s;
  text-decoration: none;
  color: inherit;
}
.material-item:hover {
  border-color: var(--accent);
  background: var(--bg3);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(56,189,248,0.15);
}
.material-icon {
  font-size: 1.5rem;
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  background: var(--bg3);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.material-info {
  flex: 1;
  min-width: 0;
}
.material-name {
  font-size: .85rem;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-bottom: 2px;
  color: var(--text);
}
.material-meta {
  font-size: .7rem;
  color: var(--text3);
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0;
}
.material-badge {
  font-size: .6rem;
  padding: 1px 5px;
  border-radius: 4px;
  font-weight: 700;
  text-transform: uppercase;
  flex-shrink: 0;
}
.material-badge.pdf { background: rgba(239, 68, 68, 0.15); color: #f87171; }
.material-badge.docx, .material-badge.doc { background: rgba(59, 130, 246, 0.15); color: #60a5fa; }
.material-badge.png, .material-badge.jpg, .material-badge.jpeg { background: rgba(16, 185, 129, 0.15); color: #34d399; }

/* Exam parts visual separation cards */
.parts-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}
.part-selector-card {
  background: var(--bg3);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.part-selector-card:hover {
  border-color: var(--text3);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
.part-selector-card.active {
  background: rgba(56, 189, 248, 0.04);
  border-color: var(--accent);
  box-shadow: 0 6px 20px rgba(56, 189, 248, 0.12);
}
.part-selector-card .part-badge {
  font-size: 0.65rem;
  font-weight: 800;
  text-transform: uppercase;
  color: var(--text3);
  letter-spacing: 1px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.part-selector-card.active .part-badge {
  color: var(--accent);
}
.part-selector-card .part-title {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
  line-height: 1.4;
}
.part-selector-card .part-meta {
  font-size: 0.8rem;
  color: var(--text3);
  display: flex;
  align-items: center;
  gap: 6px;
}
.part-selector-card .part-indicator {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: transparent;
  transition: all 0.25s;
}
.part-selector-card.active .part-indicator {
  background: var(--accent);
  box-shadow: 0 0 10px var(--accent);
}
	</style>
</head>
<body>
<div class="mobile-header">
  <button class="menu-toggle" onclick="toggleSidebar()">☰</button>
  <div class="brand-title">📚 Klausuren-Trainer</div>
  <div style="width: 42px;"></div>
</div>
<div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>
<div class="app">
<nav class="sidebar" id="appSidebar">
<div class="sidebar-brand">📚 <span>Klausuren-Trainer</span></div>
<button class="subj-btn" data-subject="bwl" onclick="selectSubject('bwl')"><span class="icon">🏢</span><div>BWL<small class="sub">inkl. Buchführung · 2 Teile</small></div><span class="badge" id="badge-bwl">0</span></button>
<button class="subj-btn" data-subject="mawi" onclick="selectSubject('mawi')"><span class="icon">📐</span><div>Mathe & Statistik<small class="sub">2 Teile · je 45 min</small></div><span class="badge" id="badge-mawi">0</span></button>
<button class="subj-btn" data-subject="vwl" onclick="selectSubject('vwl')"><span class="icon">🌍</span><div>VWL<small class="sub">Volkswirtschaftslehre</small></div><span class="badge" id="badge-vwl">0</span></button>
<button class="subj-btn" data-subject="wpr" onclick="selectSubject('wpr')"><span class="icon">⚖️</span><div>WPR<small class="sub">Wirtschaftsprivatrecht</small></div><span class="badge" id="badge-wpr">0</span></button>
<button class="subj-btn" data-subject="perso" onclick="selectSubject('perso')"><span class="icon">👥</span><div>Perso<small class="sub">Personal & Organisation</small></div><span class="badge" id="badge-perso">0</span></button>
<div style="margin-top:16px;padding-top:16px;border-top:1px solid var(--border)">
<div style="font-size:.7rem;color:var(--text3);padding:0 8px 8px">📚 LERNMATERIALIEN</div>
	<button class="tab-btn active" id="tab-exam" onclick="switchTab('exam')">📝 Klausur-Modus</button>
	<button class="tab-btn" id="tab-learn" onclick="switchTab('learn')">🎯 Lern-Modus</button>
	<button class="tab-btn" id="tab-summary" onclick="switchTab('summary')">📖 Wichtige Gesetze & Formeln</button>
	<button class="tab-btn" id="tab-materials" onclick="switchTab('materials')">📁 Original-Materialien</button>
</div>
<div style="margin-top:auto;padding-top:16px;border-top:1px solid var(--border);font-size:.7rem;color:var(--text3);text-align:center">FH Aachen · SS 2026</div>
</nav>
<main class="main">
	<div class="welcome" id="welcome"><div class="icon">📚</div><h1>Klausuren-Trainer</h1><p>Wähle links ein Fach aus und starte eine <strong>realistische Probeklausur</strong> basierend auf deinen Vorlesungsmaterialien. Mit Timer, Benotung und ausführlichen Lösungen.<br><br>Oder nutze den <strong>"🎯 Lern-Modus"</strong>, um ohne Zeitdruck alle Fragen durchzugehen – mit sofortigem Feedback nach jeder Antwort.<br><br>Wechsle zu <strong>"📖 Wichtige Gesetze & Formeln"</strong>, um die wichtigsten Zusammenfassungen pro Fach zu sehen.</p></div>
<div id="examContent" style="display:none">
<div class="timer-bar"><div class="timer-display" id="timerDisplay">45:00</div><div class="timer-settings"><input type="number" id="timerMinutes" value="45" min="5" max="180" onchange="updateTimerFromInput()"><span>Min</span><select id="timerPartSelect" onchange="onPartSelectChange()" style="display:none"></select></div><div class="timer-controls"><button class="timer-btn success" id="btnStartTimer" onclick="toggleTimer()">▶ Start</button><button class="timer-btn" onclick="resetTimer()">↺</button></div><div class="progress-bar"><div class="progress-fill" id="progressFill" style="width:100%"></div></div></div>
<div class="parts-container" id="partsSelectorContainer" style="display:none"></div>
<div class="exam-header"><div class="exam-title" id="examTitle">Klausur</div><div class="exam-meta"><span id="examPartInfo">📝</span><span>📄 <span id="questionCount">0</span> Fragen</span><span>⭐ <span id="totalPoints">0</span> Punkte</span><span><span class="dot"></span> <span id="difficultyDisplay">Standard</span></span></div></div>
<div class="questions" id="questionsContainer"></div>
<div class="submit-area"><button class="btn btn-primary" id="btnSubmit" onclick="submitExam()">📨 Klausur abgeben & bewerten</button><button class="btn btn-secondary" onclick="generateNewExam()">🔄 Neue Klausur generieren</button></div>
</div>
	<div id="summaryContent" style="display:none">
	<div class="exam-header"><div class="exam-title" id="summaryTitle">📖 Wichtige Gesetze & Formeln</div><div class="exam-meta"><span id="summarySubject">Wähle ein Fach</span></div></div>
	<div class="summary-box" id="summaryBox"><p style="color:var(--text3);text-align:center;padding:40px">Bitte wähle links ein Fach aus.</p></div>
	</div>
	<div id="learnContent" style="display:none">
	<div class="exam-header"><div class="exam-title" id="learnTitle">🎯 Lern-Modus</div><div class="exam-meta"><span id="learnSubject">Wähle ein Fach</span><span>📄 <span id="learnProgress">0 / 0</span></span></div></div>
	<div class="learn-card" id="learnCard">
	<p style="color:var(--text3);text-align:center;padding:60px">Wähle links ein Fach aus, um die Themen zu sehen.<br><br>Im Lern-Modus kannst du <strong>themenspezifisch</strong> lernen: Erst die Theorie lesen, dann die passenden Fragen üben – mit sofortigem Feedback.</p>
	</div>
	<div class="learn-nav" id="learnNav" style="display:none">
	<div class="learn-progress-dots" id="progressDots"></div>
	<div class="learn-nav-buttons">
	<button class="btn btn-secondary" id="btnLearnPrev" onclick="prevLearnCard()">◀ Zurück</button>
	<button class="btn btn-primary" id="btnLearnNext" onclick="nextLearnCard()">Weiter ▶</button>
	</div>
	</div>
	</div>
	<div id="materialsContent" style="display:none">
		<div class="exam-header">
			<div class="exam-title">📁 Original-Materialien & PDFs</div>
			<div class="exam-meta">
				<span>📄 <span id="materialsTotalCount">0</span> Dateien insgesamt</span>
				<span>• Durchsuche deine Original-PDFs, Folien & Übungen</span>
			</div>
		</div>
		<div class="materials-explorer">
			<div class="materials-search-bar" style="margin-bottom: 20px; display: flex; gap: 12px; flex-wrap: wrap;">
				<input type="text" id="materialsSearch" placeholder="🔍 Materialien durchsuchen (z.B. Klausur, Übung, Folie...)" oninput="filterMaterials()" style="flex:1; min-width: 250px; padding: 12px 16px; border-radius: var(--radius-sm); background: var(--bg3); color: var(--text); border: 1px solid var(--border); font-size: .95rem;">
				<select id="materialsSubjectFilter" onchange="filterMaterials()" style="padding: 12px 16px; border-radius: var(--radius-sm); background: var(--bg3); color: var(--text); border: 1px solid var(--border); font-size: .95rem;">
					<option value="all">Alle Fächer</option>
					<option value="bwl">🏢 BWL</option>
					<option value="mawi">📐 Mathe & Statistik</option>
					<option value="vwl">🌍 VWL</option>
					<option value="wpr">⚖️ WPR</option>
					<option value="perso">👥 Perso</option>
				</select>
				<select id="materialsCategoryFilter" onchange="filterMaterials()" style="padding: 12px 16px; border-radius: var(--radius-sm); background: var(--bg3); color: var(--text); border: 1px solid var(--border); font-size: .95rem;">
					<option value="all">Alle Kategorien</option>
					<option value="Vorlesungsfolien & Skripte">Vorlesungsfolien & Skripte</option>
					<option value="Übungen & Tutorien">Übungen & Tutorien</option>
					<option value="Klausuren & Prüfungen">Klausuren & Prüfungen</option>
					<option value="Allgemein">Allgemein & Sonstiges</option>
				</select>
			</div>
			<div id="materialsList" style="display: flex; flex-direction: column; gap: 24px;"></div>
		</div>
	</div>
</main>
</div>
<div class="overlay" id="resultsOverlay"><div class="result-card" id="resultCard"></div></div>
<script>
// === FRAGEN ===
__QUESTIONS_JS__

// === ZUSAMMENFASSUNGEN ===
__SUMMARIES_JS__

// === THEMEN (Lern-Modus) ===
__TOPICS_JS__

// === MATERIALIEN ===
__MATERIALS_JS__

// === SUBJECTS ===
const SUBJECTS = {
  bwl:{name:'BWL',icon:'🏢',parts:2,part1:{key:'bwl1',name:'Grundlagen der BWL',time:45},part2:{key:'bwl2',name:'Buchführung',time:45},strictGrading:true},
  mawi:{name:'Mathe & Statistik',icon:'📐',parts:2,part1:{key:'mawi1',name:'Wirtschaftsmathematik',time:45},part2:{key:'mawi2',name:'Statistik',time:45},strictGrading:false},
  vwl:{name:'VWL',icon:'🌍',parts:1,part1:{key:'vwl',name:'Volkswirtschaftslehre',time:90},strictGrading:false},
  wpr:{name:'WPR',icon:'⚖️',parts:1,part1:{key:'wpr',name:'Wirtschaftsprivatrecht',time:90},strictGrading:false},
  perso:{name:'Perso',icon:'👥',parts:1,part1:{key:'perso',name:'Personal & Organisation',time:90},strictGrading:true}
};

let state={currentSubject:null,currentPart:0,questions:[],selectedAnswers:{},examStarted:false,examSubmitted:false,timer:null,timerRunning:false,timerSeconds:0,timerTotal:0,stats:JSON.parse(localStorage.getItem('klausurenStats')||'{}'),currentTab:'exam',learn:{questions:[],currentIdx:0,answered:{},total:0}};

function toggleSidebar() {
  const sidebar = document.getElementById('appSidebar');
  const overlay = document.getElementById('sidebarOverlay');
  if(sidebar.classList.contains('open')){
    sidebar.classList.remove('open');
    overlay.classList.remove('active');
  }else{
    sidebar.classList.add('open');
    overlay.classList.add('active');
  }
}

function closeSidebarOnMobile() {
  if(window.innerWidth <= 768){
    const sidebar = document.getElementById('appSidebar');
    const overlay = document.getElementById('sidebarOverlay');
    if(sidebar) sidebar.classList.remove('open');
    if(overlay) overlay.classList.remove('active');
  }
}

function switchTab(tab){
  closeSidebarOnMobile();
  state.currentTab=tab;
  document.getElementById('tab-exam').classList.toggle('active',tab==='exam');
  document.getElementById('tab-learn').classList.toggle('active',tab==='learn');
  document.getElementById('tab-summary').classList.toggle('active',tab==='summary');
  document.getElementById('tab-materials').classList.toggle('active',tab==='materials');
  document.getElementById('welcome').style.display='none';
  document.getElementById('examContent').style.display=tab==='exam'?'block':'none';
  document.getElementById('learnContent').style.display=tab==='learn'?'block':'none';
  document.getElementById('summaryContent').style.display=tab==='summary'?'block':'none';
  document.getElementById('materialsContent').style.display=tab==='materials'?'block':'none';
  if(tab==='learn'&&state.currentSubject){enterLearnMode();}
  else if(tab==='summary'){showSummary();}
  else if(tab==='exam'&&state.currentSubject){generateNewExam();}
  else if(tab==='materials'){showMaterials();}
}

// Einfacher Markdown-Parser
function renderMarkdown(md){
  if(!md)return '';
  md=md.replace(/```([^`]*)```/g,(m,c)=>'<pre><code>'+c.replace(/</g,'&lt;')+'</code></pre>');
  md=md.replace(/`([^`]+)`/g,'<code>$1</code>');
  md=md.replace(/^### (.+)$/gm,'<h3>$1</h3>');
  md=md.replace(/^## (.+)$/gm,'<h2>$1</h2>');
  md=md.replace(/^# (.+)$/gm,'<h1>$1</h1>');
  md=md.replace(/\\*\\*([^\\*]+)\\*\\*/g,'<strong>$1</strong>');
  md=md.replace(/\\*([^\\*]+)\\*/g,'<em>$1</em>');
  md=md.replace(/^(\\|.+\\|)\\n(\\|[-| :]+\\|)\\n((?:\\|.+\\|\\n?)*)/gm,(m,header,sep,body)=>{
    const cols=header.split('|').filter(c=>c.trim());
    let t='<table><thead><tr>'+cols.map(c=>'<th>'+c.trim()+'</th>').join('')+'</tr></thead><tbody>';
    body.trim().split('\\n').forEach(row=>{
      const cells=row.split('|').filter(c=>c.trim()||c==='');
      if(cells.length)t+='<tr>'+cells.map(c=>'<td>'+c.trim()+'</td>').join('')+'</tr>';
    });
    return t+'</tbody></table>';
  });
  md=md.replace(/^- (.+)$/gm,'<li>$1</li>');
  md=md.replace(/(<li>[^<]*<\/li>)/g,'<ul>$1</ul>');
  md=md.replace(/<\/ul><ul>/g,'');
  md=md.replace(/  /g,'</p><p>').replace(/(<p>)+/g,'<p>').replace(/(<\/p>)+/g,'</p>');
  md=md.replace(/^(?!<[hupolt])(.+)$/gm,'<p>$1</p>');
  md=md.replace(/<p><p>/g,'<p>').replace(/<\/p><\/p>/g,'</p>');
  return md;
}

function showSummary(){
  const key=state.currentSubject;
  if(!key){document.getElementById('summaryBox').innerHTML='<p style="color:var(--text3);text-align:center;padding:40px">Bitte wähle links ein Fach aus.</p>';return;}
  const cfg=SUBJECTS[key];
  let rawMd='';
  let subtitle='';
  if(cfg.parts>1){
    const p1=cfg.part1.key,p2=cfg.part2.key;
    document.getElementById('summaryTitle').textContent='📖 '+cfg.icon+' '+cfg.name+' – Gesetze & Formeln';
    subtitle=cfg.part1.name+' + '+cfg.part2.name;
    rawMd='# Teil 1: '+cfg.part1.name+'\\n\\n'+(SUMMARIES[p1]||'')+'\\n\\n---\\n\\n# Teil 2: '+cfg.part2.name+'\\n\\n'+(SUMMARIES[p2]||'');
  }else{
    const p=cfg.part1.key;
    document.getElementById('summaryTitle').textContent='📖 '+cfg.icon+' '+cfg.name+' – Wichtige Gesetze & Formeln';
    subtitle=cfg.part1.name;
    rawMd=SUMMARIES[p]||'';
  }
  document.getElementById('summarySubject').textContent=subtitle;
  document.getElementById('summaryBox').innerHTML=renderMarkdown(rawMd);
}

function selectSubject(key){
  closeSidebarOnMobile();
  if(state.timerRunning)toggleTimer();
  if(state.timer)clearInterval(state.timer);
  state.currentSubject=key;
  state.currentPart=0;
  state.examSubmitted=false;
  state.selectedAnswers={};
  state.learn={questions:[],currentIdx:0,answered:{},total:0};
  document.querySelectorAll('.subj-btn').forEach(b=>b.classList.remove('active'));
  document.querySelector('.subj-btn[data-subject="'+key+'"]').classList.add('active');
  document.getElementById('welcome').style.display='none';
  const cfg=SUBJECTS[key];
  if(state.currentTab==='learn'){
    document.getElementById('examContent').style.display='none';
    document.getElementById('summaryContent').style.display='none';
    document.getElementById('learnContent').style.display='block';
    enterLearnMode();
  }else if(state.currentTab==='summary'){
    document.getElementById('examContent').style.display='none';
    document.getElementById('learnContent').style.display='none';
    document.getElementById('summaryContent').style.display='block';
    showSummary();
  }else{
    document.getElementById('summaryContent').style.display='none';
    document.getElementById('learnContent').style.display='none';
    document.getElementById('examContent').style.display='block';
    document.getElementById('timerMinutes').value=cfg.part1.time;
    document.getElementById('timerPartSelect').style.display='none';
    resetTimer();
    generateNewExam();
  }
}

function renderPartsSelector(){
  const key=state.currentSubject;
  const container=document.getElementById('partsSelectorContainer');
  if(!key){container.style.display='none';return;}
  const cfg=SUBJECTS[key];
  if(cfg.parts>1){
    container.style.display='grid';
    const p1Grading=cfg.strictGrading?'Streng':'Standard';
    const p2Grading=cfg.strictGrading?'Streng':'Standard';
    container.innerHTML=''+
      '<div class="part-selector-card'+(state.currentPart===0?' active':'')+'" onclick="selectExamPart(0)">'+
        '<div class="part-badge">Teil 1 <span class="part-indicator"></span></div>'+
        '<div class="part-title">'+cfg.part1.name+'</div>'+
        '<div class="part-meta">⏱️ '+cfg.part1.time+' Min · '+p1Grading+'-Bewertung</div>'+
      '</div>'+
      '<div class="part-selector-card'+(state.currentPart===1?' active':'')+'" onclick="selectExamPart(1)">'+
        '<div class="part-badge">Teil 2 <span class="part-indicator"></span></div>'+
        '<div class="part-title">'+cfg.part2.name+'</div>'+
        '<div class="part-meta">⏱️ '+cfg.part2.time+' Min · '+p2Grading+'-Bewertung</div>'+
      '</div>';
  }else{
    container.style.display='none';
  }
}

function selectExamPart(partIdx){
  if(partIdx===state.currentPart)return;
  const hasAnswers=Object.keys(state.selectedAnswers).length>0;
  if(hasAnswers&&!state.examSubmitted){
    if(!confirm('⚠️ Möchtest du wirklich zum anderen Klausurteil wechseln? Deine bisherigen Antworten gehen dabei verloren.'))return;
  }
  if(state.timerRunning)toggleTimer();
  state.currentPart=partIdx;
  generateNewExam();
}

function generateNewExam(){
  const key=state.currentSubject;
  if(!key)return;
  state.examSubmitted=false;
  state.selectedAnswers={};
  renderPartsSelector();
  const cfg=SUBJECTS[key];
  const partIdx=state.currentPart;
  const partKey=cfg.parts>1?(partIdx===0?cfg.part1.key:cfg.part2.key):cfg.part1.key;
  const bank={bwl1:QUESTION_BANK_bwl1,bwl2:QUESTION_BANK_bwl2,mawi1:QUESTION_BANK_mawi1,mawi2:QUESTION_BANK_mawi2,vwl:QUESTION_BANK_vwl,wpr:QUESTION_BANK_wpr,perso:QUESTION_BANK_perso}[partKey];
  if(!bank||bank.length===0){document.getElementById('questionsContainer').innerHTML='<p style="color:var(--danger)">Keine Fragen gefunden.</p>';return;}
  const numQ=Math.min(25,Math.max(20,bank.length));
  const shuffled=[...bank].sort(()=>Math.random()-0.5);
  state.questions=shuffled.slice(0,numQ);
  renderQuestions();
  const partName=cfg.parts>1?(partIdx===0?cfg.part1.name:cfg.part2.name):cfg.part1.name;
  document.getElementById('examTitle').textContent=cfg.icon+' '+cfg.name;
  document.getElementById('examPartInfo').textContent=cfg.parts>1?'📝 Teil '+(partIdx+1)+' von 2: '+partName:'📝 '+partName;
  document.getElementById('questionCount').textContent=state.questions.length;
  document.getElementById('totalPoints').textContent=state.questions.reduce((s,q)=>s+q.points,0);
  document.getElementById('difficultyDisplay').textContent=cfg.strictGrading?'Streng':'Standard';
  const badge=document.getElementById('badge-'+key);
  const count=(state.stats[key]||{attempts:0}).attempts||0;
  badge.textContent=count;
  const time=cfg.parts>1?(partIdx===0?cfg.part1.time:cfg.part2.time):cfg.part1.time;
  document.getElementById('timerMinutes').value=time;
  resetTimer();
  document.getElementById('btnSubmit').disabled=false;
}

// === Achsen-Bausteine mit Ticks ===
// Alle Diagramme nutzen viewBox 0 0 420 300
// Achsen: X bei y=255, Y bei x=55
// Bereich: x 55-380, y 40-255 (width 325, height 215)

const AX = {
  // SVG-Wrapper Anfang mit allen modernen Gradienten und Filtern im <defs> Block
  svgOpen: '<svg viewBox="0 0 420 300" width="420" height="300" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;border-radius:12px;box-shadow:0 10px 15px -3px rgba(0,0,0,0.3)">'+
    '<defs>'+
      '<linearGradient id="demandGrad" x1="0" y1="0" x2="1" y2="1">'+
        '<stop offset="0%" stop-color="#38bdf8"/>'+
        '<stop offset="100%" stop-color="#0284c7"/>'+
      '</linearGradient>'+
      '<linearGradient id="supplyGrad" x1="0" y1="1" x2="1" y2="0">'+
        '<stop offset="0%" stop-color="#f59e0b"/>'+
        '<stop offset="100%" stop-color="#d97706"/>'+
      '</linearGradient>'+
      '<linearGradient id="socialGrad" x1="0" y1="1" x2="1" y2="0">'+
        '<stop offset="0%" stop-color="#f87171"/>'+
        '<stop offset="100%" stop-color="#ef4444"/>'+
      '</linearGradient>'+
      '<linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1">'+
        '<stop offset="0%" stop-color="#0b1329"/>'+
        '<stop offset="100%" stop-color="#0f172a"/>'+
      '</linearGradient>'+
      '<linearGradient id="areaCS" x1="0" y1="0" x2="0" y2="1">'+
        '<stop offset="0%" stop-color="#38bdf8" stop-opacity="0.3"/>'+
        '<stop offset="100%" stop-color="#38bdf8" stop-opacity="0.02"/>'+
      '</linearGradient>'+
      '<linearGradient id="areaPS" x1="0" y1="0" x2="0" y2="1">'+
        '<stop offset="0%" stop-color="#f59e0b" stop-opacity="0.3"/>'+
        '<stop offset="100%" stop-color="#f59e0b" stop-opacity="0.02"/>'+
      '</linearGradient>'+
      '<linearGradient id="taxGrad" x1="0" y1="0" x2="0" y2="1">'+
        '<stop offset="0%" stop-color="#a855f7" stop-opacity="0.25"/>'+
        '<stop offset="100%" stop-color="#a855f7" stop-opacity="0.05"/>'+
      '</linearGradient>'+
      '<filter id="glow" x="-15%" y="-15%" width="130%" height="130%">'+
        '<feGaussianBlur stdDeviation="2" result="blur"/>'+
        '<feComposite in="SourceGraphic" in2="blur" operator="over"/>'+
      '</filter>'+
      '<style>'+
        '@keyframes flux_flow { to { stroke-dashoffset: -12; } }'+
        '.flow-real { stroke-dasharray: 6, 6; animation: flux_flow 1.2s linear infinite; stroke: #38bdf8; }'+
        '.flow-money { stroke-dasharray: 6, 6; animation: flux_flow 1.2s linear infinite; stroke: #10b981; animation-direction: reverse; }'+
        '.label-pill { font-family: system-ui, -apple-system, sans-serif; font-size: 8px; font-weight: 600; fill: #0f172a; }'+
      '</style>'+
    '</defs>',
  svgClose:'</svg>',
  // Basis-Rechteck (Hintergrund) + Gitternetz
  bg:'<rect width="420" height="300" fill="url(#bgGrad)" rx="12"/>'+
    // Gitternetzlinien (horizontal)
    '<line x1="55" y1="211" x2="390" y2="211" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="2,2" opacity="0.6"/>'+
    '<line x1="55" y1="167" x2="390" y2="167" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="2,2" opacity="0.6"/>'+
    '<line x1="55" y1="123" x2="390" y2="123" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="2,2" opacity="0.6"/>'+
    '<line x1="55" y1="79" x2="390" y2="79" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="2,2" opacity="0.6"/>'+
    // Gitternetzlinien (vertikal)
    '<line x1="122" y1="35" x2="122" y2="255" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="2,2" opacity="0.6"/>'+
    '<line x1="189" y1="35" x2="189" y2="255" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="2,2" opacity="0.6"/>'+
    '<line x1="256" y1="35" x2="256" y2="255" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="2,2" opacity="0.6"/>'+
    '<line x1="323" y1="35" x2="323" y2="255" stroke="#1e293b" stroke-width="0.75" stroke-dasharray="2,2" opacity="0.6"/>',
  // X-Achse: Menge 0-50, Ticks alle 10
  xAxis:'<line x1="55" y1="255" x2="390" y2="255" stroke="#475569" stroke-width="2"/>'+
    '<polygon points="390,255 378,250 378,260" fill="#475569"/>'+
    '<line x1="55" y1="255" x2="55" y2="261" stroke="#475569" stroke-width="1"/><text x="55" y="272" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="system-ui">0</text>'+
    '<line x1="122" y1="255" x2="122" y2="261" stroke="#475569" stroke-width="1"/><text x="122" y="272" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="system-ui">10</text>'+
    '<line x1="189" y1="255" x2="189" y2="261" stroke="#475569" stroke-width="1"/><text x="189" y="272" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="system-ui">20</text>'+
    '<line x1="256" y1="255" x2="256" y2="261" stroke="#475569" stroke-width="1"/><text x="256" y="272" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="system-ui">30</text>'+
    '<line x1="323" y1="255" x2="323" y2="261" stroke="#475569" stroke-width="1"/><text x="323" y="272" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="system-ui">40</text>'+
    '<line x1="390" y1="255" x2="390" y2="261" stroke="#475569" stroke-width="1"/><text x="390" y="272" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="system-ui">50</text>',
  // Y-Achse: Preis 0-10, Ticks alle 2
  yAxis:'<line x1="55" y1="255" x2="55" y2="35" stroke="#475569" stroke-width="2"/>'+
    '<polygon points="55,35 50,47 60,47" fill="#475569"/>'+
    '<line x1="49" y1="255" x2="55" y2="255" stroke="#475569" stroke-width="1"/><text x="44" y="258" fill="#94a3b8" font-size="9" text-anchor="end" font-family="system-ui">0</text>'+
    '<line x1="49" y1="211" x2="55" y2="211" stroke="#475569" stroke-width="1"/><text x="44" y="214" fill="#94a3b8" font-size="9" text-anchor="end" font-family="system-ui">2</text>'+
    '<line x1="49" y1="167" x2="55" y2="167" stroke="#475569" stroke-width="1"/><text x="44" y="170" fill="#94a3b8" font-size="9" text-anchor="end" font-family="system-ui">4</text>'+
    '<line x1="49" y1="123" x2="55" y2="123" stroke="#475569" stroke-width="1"/><text x="44" y="126" fill="#94a3b8" font-size="9" text-anchor="end" font-family="system-ui">6</text>'+
    '<line x1="49" y1="79" x2="55" y2="79" stroke="#475569" stroke-width="1"/><text x="44" y="82" fill="#94a3b8" font-size="9" text-anchor="end" font-family="system-ui">8</text>'+
    '<line x1="49" y1="35" x2="55" y2="35" stroke="#475569" stroke-width="1"/><text x="44" y="38" fill="#94a3b8" font-size="9" text-anchor="end" font-family="system-ui">10</text>',
  // Achsenbeschriftungen
  xLabel:'<text x="220" y="291" fill="#cbd5e1" font-size="11" text-anchor="middle" font-weight="600" font-family="system-ui">Menge (Q)</text>',
  yLabel:'<text x="16" y="145" fill="#cbd5e1" font-size="11" text-anchor="middle" font-weight="600" transform="rotate(-90,16,145)" font-family="system-ui">Preis (P)</text>',
  // Title
  title: function(t){
    return '<rect x="110" y="8" width="200" height="20" rx="4" fill="#1e293b" opacity="0.6"/>'+
      '<text x="210" y="22" fill="#f8fafc" font-size="11" text-anchor="middle" font-weight="bold" font-family="system-ui" letter-spacing="0.5">'+t.toUpperCase()+'</text>';
  }
};

// Koordinaten-Transformation: Datenwert -> SVG-Pixel
function px(x){return Math.round(55 + x*6.7);}
function py(p){return Math.round(255 - p*22);}

function getDiagram(type){
  const d={
    'supply-demand': AX.bg+AX.xAxis+AX.yAxis+AX.xLabel+AX.yLabel+AX.title('Marktgleichgewicht')+
      // Nachfrage D: von (Q=0,P=10) bis (Q=50,P=0)
      '<line x1="'+px(0)+'" y1="'+py(10)+'" x2="'+px(50)+'" y2="'+py(0)+'" stroke="url(#demandGrad)" stroke-width="3" filter="url(#glow)"/>'+
      '<text x="325" y="45" fill="#38bdf8" font-size="10" font-weight="bold" font-family="system-ui">D (Nachfrage)</text>'+
      // Angebot S: von (Q=0,P=0) bis (Q=50,P=5)
      '<line x1="'+px(0)+'" y1="'+py(0)+'" x2="'+px(50)+'" y2="'+py(5)+'" stroke="url(#supplyGrad)" stroke-width="3" filter="url(#glow)"/>'+
      '<text x="325" y="150" fill="#f59e0b" font-size="10" font-weight="bold" font-family="system-ui">S (Angebot)</text>'+
      // Gleichgewicht: Q*≈33, P*≈3.3
      '<line x1="'+px(33)+'" y1="255" x2="'+px(33)+'" y2="'+py(3.3)+'" stroke="#ef4444" stroke-width="1.25" stroke-dasharray="4,4"/>'+
      '<line x1="55" y1="'+py(3.3)+'" x2="'+px(33)+'" y2="'+py(3.3)+'" stroke="#ef4444" stroke-width="1.25" stroke-dasharray="4,4"/>'+
      '<circle cx="'+px(33)+'" cy="'+py(3.3)+'" r="7" fill="#ef4444" opacity="0.3"/>'+
      '<circle cx="'+px(33)+'" cy="'+py(3.3)+'" r="4.5" fill="#ef4444"/>'+
      '<text x="'+px(33)+'" y="243" fill="#f87171" font-size="9" font-weight="bold" text-anchor="middle" font-family="system-ui">GG-Punkt (E)</text>'+
      '<text x="'+px(33)+'" y="272" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle" font-family="system-ui">Q* = 33</text>'+
      '<text x="42" y="'+(py(3.3)+4)+'" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="end" font-family="system-ui">P* = 3.3</text>',

    'externality': AX.bg+AX.xAxis+AX.yAxis+AX.xLabel+AX.yLabel+AX.title('Negative Externalität & Wohlfahrtsverlust')+
      // Nachfrage D: P = 8 - 0.15Q
      '<line x1="'+px(0)+'" y1="'+py(8)+'" x2="'+px(50)+'" y2="'+py(0.5)+'" stroke="url(#demandGrad)" stroke-width="2.5"/>'+
      '<text x="330" y="65" fill="#38bdf8" font-size="9" font-weight="bold" font-family="system-ui">Nachfrage D (PrivatNutzen)</text>'+
      // Private Kosten PK: P = 0.1Q
      '<line x1="'+px(0)+'" y1="'+py(0)+'" x2="'+px(50)+'" y2="'+py(5)+'" stroke="url(#supplyGrad)" stroke-width="2.5"/>'+
      '<text x="340" y="165" fill="#f59e0b" font-size="9" font-weight="bold" font-family="system-ui">S = Private Kosten (PK)</text>'+
      // Soziale Kosten SK: P = 0.1Q + 2 (externer Schaden = 2)
      '<line x1="'+px(0)+'" y1="'+py(2)+'" x2="'+px(50)+'" y2="'+py(7)+'" stroke="url(#socialGrad)" stroke-width="2.5" stroke-dasharray="5,3"/>'+
      '<text x="310" y="105" fill="#f87171" font-size="9" font-weight="bold" font-family="system-ui">Soziale Kosten (SK)</text>'+
      // Wohlfahrtsverlust-Dreieck schattieren: zwischen Q=24 und Q=32, oberhalb Nachfrage und unterhalb Soziale Kosten
      '<path d="M'+px(24)+','+py(4.4)+' L'+px(32)+','+py(5.2)+' L'+px(32)+','+py(3.2)+' Z" fill="url(#socialGrad)" fill-opacity="0.3" stroke="#f87171" stroke-width="1.25"/>'+
      '<text x="'+px(29.5)+'" y="'+py(4.25)+'" fill="#f8fafc" font-size="8" font-weight="bold" font-family="system-ui" text-anchor="middle">DWL</text>'+
      // Marktgleichgewicht (PK ∩ D): Q≈32, P≈3.2
      '<circle cx="'+px(32)+'" cy="'+py(3.2)+'" r="4" fill="#f59e0b"/>'+
      '<line x1="'+px(32)+'" y1="255" x2="'+px(32)+'" y2="'+py(3.2)+'" stroke="#f59e0b" stroke-width="1" stroke-dasharray="3,3"/>'+
      '<text x="'+px(32)+'" y="272" fill="#f59e0b" font-size="9" font-weight="bold" text-anchor="middle" font-family="system-ui">Q_Markt=32</text>'+
      // Optimales Gleichgewicht (SK ∩ D): Q≈24, P≈4.4
      '<circle cx="'+px(24)+'" cy="'+py(4.4)+'" r="4" fill="#ef4444"/>'+
      '<line x1="'+px(24)+'" y1="255" x2="'+px(24)+'" y2="'+py(4.4)+'" stroke="#ef4444" stroke-width="1" stroke-dasharray="3,3"/>'+
      '<text x="'+px(24)+'" y="272" fill="#ef4444" font-size="9" font-weight="bold" text-anchor="middle" font-family="system-ui">Q_Opt=24</text>'+
      // Externer Schaden Kennzeichnung
      '<line x1="'+px(15)+'" y1="'+py(1.5)+'" x2="'+px(15)+'" y2="'+py(3.5)+'" stroke="#ef4444" stroke-width="1.5"/>'+
      '<polygon points="15,143 12,148 18,148" fill="#ef4444" transform="rotate(0,15,143)"/>'+
      '<polygon points="15,199 12,194 18,194" fill="#ef4444" transform="rotate(0,15,199)"/>'+
      '<text x="'+px(17)+'" y="'+py(2.5)+'" fill="#f87171" font-size="8" font-weight="bold" font-family="system-ui">Schaden (d)</text>',

    'angebot-nachfrage-diagramm': AX.bg+AX.xAxis+AX.yAxis+AX.xLabel+AX.yLabel+AX.title('Angebot &amp; Nachfrage')+
      '<line x1="'+px(0)+'" y1="'+py(10)+'" x2="'+px(50)+'" y2="'+py(0)+'" stroke="url(#demandGrad)" stroke-width="3"/>'+
      '<text x="330" y="45" fill="#38bdf8" font-size="10" font-weight="bold" font-family="system-ui">D (Nachfrage)</text>'+
      '<line x1="'+px(0)+'" y1="'+py(0)+'" x2="'+px(50)+'" y2="'+py(5)+'" stroke="url(#supplyGrad)" stroke-width="3"/>'+
      '<text x="330" y="150" fill="#f59e0b" font-size="10" font-weight="bold" font-family="system-ui">S (Angebot)</text>',

    'konsumenten-produzenten-rente': AX.bg+AX.xAxis+AX.yAxis+AX.xLabel+AX.yLabel+AX.title('Konsumenten- &amp; Produzentenrente')+
      // Konsumentenrente-Fläche: Dreieck über P=3.3, unter D-Linie (0,10)->(33,3.3)->(0,3.3)
      '<path d="M'+px(0)+','+py(10)+' L'+px(33)+','+py(3.3)+' L'+px(0)+','+py(3.3)+' Z" fill="url(#areaCS)"/>'+
      // Produzentenrente-Fläche: Dreieck unter P=3.3, über S-Linie (0,0)->(33,3.3)->(0,3.3)
      '<path d="M'+px(0)+','+py(0)+' L'+px(33)+','+py(3.3)+' L'+px(0)+','+py(3.3)+' Z" fill="url(#areaPS)"/>'+
      // Kurven
      '<line x1="'+px(0)+'" y1="'+py(10)+'" x2="'+px(50)+'" y2="'+py(0)+'" stroke="url(#demandGrad)" stroke-width="2.5"/>'+
      '<line x1="'+px(0)+'" y1="'+py(0)+'" x2="'+px(50)+'" y2="'+py(5)+'" stroke="url(#supplyGrad)" stroke-width="2.5"/>'+
      // Gleichgewichtslinien
      '<line x1="'+px(33)+'" y1="255" x2="'+px(33)+'" y2="'+py(3.3)+'" stroke="#64748b" stroke-dasharray="3,3" stroke-width="1.25"/>'+
      '<line x1="55" y1="'+py(3.3)+'" x2="'+px(33)+'" y2="'+py(3.3)+'" stroke="#64748b" stroke-dasharray="3,3" stroke-width="1.25"/>'+
      '<circle cx="'+px(33)+'" cy="'+py(3.3)+'" r="4" fill="#f8fafc"/>'+
      // Beschriftungen KR und PR
      '<rect x="80" y="90" width="105" height="20" rx="4" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1" opacity="0.9"/>'+
      '<text x="132" y="103" fill="#f0f9ff" font-size="8" font-weight="bold" font-family="system-ui" text-anchor="middle">Konsumentenrente (KR)</text>'+
      '<rect x="80" y="195" width="105" height="20" rx="4" fill="#78350f" stroke="#f59e0b" stroke-width="1" opacity="0.9"/>'+
      '<text x="132" y="208" fill="#fef3c7" font-size="8" font-weight="bold" font-family="system-ui" text-anchor="middle">Produzentenrente (PR)</text>'+
      '<text x="'+px(33)+'" y="272" fill="#94a3b8" font-size="9" text-anchor="middle" font-family="system-ui">Q* = 33</text>'+
      '<text x="42" y="'+(py(3.3)+4)+'" fill="#94a3b8" font-size="9" text-anchor="end" font-family="system-ui">P* = 3.3</text>',

    'steuerlast': AX.bg+AX.xAxis+AX.yAxis+AX.xLabel+AX.yLabel+AX.title('Steuerlast &amp; Wohlfahrtsverlust')+
      // S+Steuer: P = 0.1Q + 2 (Steuer = 2)
      '<line x1="'+px(0)+'" y1="'+py(2)+'" x2="'+px(50)+'" y2="'+py(7)+'" stroke="url(#supplyGrad)" stroke-width="2.5" stroke-dasharray="4,2" opacity="0.8"/>'+
      '<text x="310" y="80" fill="#f59e0b" font-size="9" font-family="system-ui">S + Steuer</text>'+
      // S original
      '<line x1="'+px(0)+'" y1="'+py(0)+'" x2="'+px(50)+'" y2="'+py(5)+'" stroke="url(#supplyGrad)" stroke-width="2.5"/>'+
      '<text x="345" y="165" fill="#f59e0b" font-size="9" font-family="system-ui">S (Angebot)</text>'+
      // Nachfrage D
      '<line x1="'+px(0)+'" y1="'+py(10)+'" x2="'+px(50)+'" y2="'+py(0)+'" stroke="url(#demandGrad)" stroke-width="2.5"/>'+
      '<text x="345" y="45" fill="#38bdf8" font-size="9" font-family="system-ui">D (Nachfrage)</text>'+
      // Steuereinnahmen (Rechteck von 0 bis Q=27, zwischen P_S=2.7 und P_C=4.7)
      '<path d="M'+px(0)+','+py(4.7)+' L'+px(27)+','+py(4.7)+' L'+px(27)+','+py(2.7)+' L'+px(0)+','+py(2.7)+' Z" fill="url(#taxGrad)"/>'+
      '<rect x="65" y="145" width="100" height="18" rx="3" fill="#3b0764" stroke="#a855f7" stroke-width="0.75" opacity="0.9"/>'+
      '<text x="115" y="157" fill="#f3e8ff" font-size="8" font-weight="bold" font-family="system-ui" text-anchor="middle">Steuereinnahmen</text>'+
      // DWL-Dreieck: zwischen Q=27 und Q=33, begrenzt durch S, D, und Steuerkeil
      '<path d="M'+px(27)+','+py(4.7)+' L'+px(33)+','+py(3.3)+' L'+px(27)+','+py(2.7)+' Z" fill="url(#socialGrad)" fill-opacity="0.3" stroke="#ef4444" stroke-width="1.25"/>'+
      '<text x="'+px(30)+'" y="'+py(3.5)+'" fill="#f87171" font-size="8" font-weight="bold" font-family="system-ui" text-anchor="middle">DWL</text>'+
      // Kennzeichnung Verbraucherpreis P_C=4.7 und Erzeugerpreis P_S=2.7
      '<circle cx="'+px(27)+'" cy="'+py(4.7)+'" r="4" fill="#ef4444"/>'+
      '<circle cx="'+px(27)+'" cy="'+py(2.7)+'" r="4" fill="#a855f7"/>'+
      '<line x1="55" y1="'+py(4.7)+'" x2="'+px(27)+'" y2="'+py(4.7)+'" stroke="#ef4444" stroke-width="1" stroke-dasharray="2,2"/>'+
      '<line x1="55" y1="'+py(2.7)+'" x2="'+px(27)+'" y2="'+py(2.7)+'" stroke="#a855f7" stroke-width="1" stroke-dasharray="2,2"/>'+
      '<text x="42" y="'+(py(4.7)+4)+'" fill="#f87171" font-size="9" font-weight="bold" text-anchor="end" font-family="system-ui">P_K = 4.7</text>'+
      '<text x="42" y="'+(py(2.7)+4)+'" fill="#c084fc" font-size="9" font-weight="bold" text-anchor="end" font-family="system-ui">P_P = 2.7</text>'+
      '<line x1="'+px(27)+'" y1="255" x2="'+px(27)+'" y2="'+py(4.7)+'" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3,3"/>'+
      '<text x="'+px(27)+'" y="272" fill="#94a3b8" font-size="9" font-weight="bold" text-anchor="middle" font-family="system-ui">Q_Steuer = 27</text>',

    'elastizitaet': AX.bg+AX.xAxis+AX.yAxis+AX.xLabel+AX.yLabel+AX.title('Preiselastizität der Nachfrage')+
      // D elastisch (flach)
      '<line x1="'+px(5)+'" y1="'+py(7.5)+'" x2="'+px(45)+'" y2="'+py(2.5)+'" stroke="url(#demandGrad)" stroke-width="3" filter="url(#glow)"/>'+
      '<text x="300" y="85" fill="#38bdf8" font-size="9" font-weight="bold" font-family="system-ui">D1 (elastisch)</text>'+
      // D unelastisch (steil)
      '<line x1="'+px(15)+'" y1="'+py(9)+'" x2="'+px(25)+'" y2="'+py(1)+'" stroke="#818cf8" stroke-width="3" filter="url(#glow)"/>'+
      '<text x="'+px(15)+'" y="'+py(9.5)+'" fill="#818cf8" font-size="9" font-weight="bold" font-family="system-ui">D2 (unelastisch)</text>'+
      // Angebot
      '<line x1="'+px(0)+'" y1="'+py(0)+'" x2="'+px(50)+'" y2="'+py(5)+'" stroke="url(#supplyGrad)" stroke-width="2"/>'+
      '<text x="350" y="160" fill="#f59e0b" font-size="9" font-weight="bold" font-family="system-ui">S (Angebot)</text>'+
      // Schnittpunkt
      '<circle cx="'+px(20)+'" cy="'+py(5)+'" r="4.5" fill="#f8fafc"/>',

    'angebot-nachfrage-verschiebung': AX.bg+AX.xAxis+AX.yAxis+AX.xLabel+AX.yLabel+AX.title('Rechtsverschiebung der Nachfrage')+
      // Angebot S
      '<line x1="'+px(0)+'" y1="'+py(0)+'" x2="'+px(50)+'" y2="'+py(5)+'" stroke="url(#supplyGrad)" stroke-width="2.5"/>'+
      // D1
      '<line x1="'+px(0)+'" y1="'+py(7.5)+'" x2="'+px(42)+'" y2="'+py(0.5)+'" stroke="url(#demandGrad)" stroke-width="2.5" opacity="0.5"/>'+
      '<text x="260" y="70" fill="#38bdf8" fill-opacity="0.6" font-size="9" font-weight="bold" font-family="system-ui">Nachfrage D1</text>'+
      // D2 (nach rechts verschoben)
      '<line x1="'+px(8)+'" y1="'+py(10)+'" x2="'+px(50)+'" y2="'+py(3)+'" stroke="url(#demandGrad)" stroke-width="3" filter="url(#glow)"/>'+
      '<text x="310" y="50" fill="#38bdf8" font-size="9" font-weight="bold" font-family="system-ui">Nachfrage D2</text>'+
      // Verschiebungs-Pfeil
      '<path d="M '+px(20)+' '+py(4.25)+' L '+px(28)+' '+py(5.5)+'" stroke="#ef4444" stroke-width="2.5" marker-end="url(#arrow)" fill="none"/>'+
      '<line x1="'+px(20)+'" y1="'+py(4.25)+'" x2="'+px(28)+'" y2="'+py(5.5)+'" stroke="#ef4444" stroke-width="2"/>'+
      '<polygon points="'+px(28)+','+py(5.5)+' '+(px(28)-6)+','+(py(5.5)-2)+' '+(px(28)-4)+','+(py(5.5)+4)+'" fill="#ef4444"/>'+
      // Gleichgewichte
      '<circle cx="'+px(25)+'" cy="'+py(2.5)+'" r="3.5" fill="#38bdf8" opacity="0.6"/>'+
      '<circle cx="'+px(34)+'" cy="'+py(3.4)+'" r="4.5" fill="#ef4444"/>'+
      '<text x="350" y="180" fill="#f59e0b" font-size="9" font-weight="bold" font-family="system-ui">S</text>',

    'preiskontrolle': AX.bg+AX.xAxis+AX.yAxis+AX.xLabel+AX.yLabel+AX.title('Preisobergrenze &amp; Marktknappheit')+
      '<line x1="'+px(0)+'" y1="'+py(10)+'" x2="'+px(50)+'" y2="'+py(0)+'" stroke="url(#demandGrad)" stroke-width="2.5"/>'+
      '<text x="340" y="45" fill="#38bdf8" font-size="9" font-weight="bold" font-family="system-ui">D</text>'+
      '<line x1="'+px(0)+'" y1="'+py(0)+'" x2="'+px(50)+'" y2="'+py(5)+'" stroke="url(#supplyGrad)" stroke-width="2.5"/>'+
      '<text x="340" y="165" fill="#f59e0b" font-size="9" font-weight="bold" font-family="system-ui">S</text>'+
      // Marktgleichgewicht
      '<circle cx="'+px(33)+'" cy="'+py(3.3)+'" r="3.5" fill="#94a3b8" opacity="0.6"/>'+
      // Höchstpreis-Schranke bei P=2 (bindend)
      '<line x1="55" y1="'+py(2)+'" x2="390" y2="'+py(2)+'" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="6,4"/>'+
      '<rect x="65" y="185" width="130" height="18" rx="3" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>'+
      '<text x="130" y="197" fill="#fca5a5" font-size="8" font-weight="bold" font-family="system-ui" text-anchor="middle">HÖCHSTPREIS P_Max = 2</text>'+
      // Schnittpunkte bei P=2
      // Angebot bei Q_S = 20, Nachfrage bei Q_D = 40
      '<circle cx="'+px(20)+'" cy="'+py(2)+'" r="4.5" fill="#f59e0b"/>'+
      '<circle cx="'+px(40)+'" cy="'+py(2)+'" r="4.5" fill="#38bdf8"/>'+
      '<line x1="'+px(20)+'" y1="255" x2="'+px(20)+'" y2="'+py(2)+'" stroke="#f59e0b" stroke-width="1" stroke-dasharray="2,2"/>'+
      '<line x1="'+px(40)+'" y1="255" x2="'+px(40)+'" y2="'+py(2)+'" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2,2"/>'+
      '<text x="'+px(20)+'" y="272" fill="#f59e0b" font-size="9" font-weight="bold" text-anchor="middle" font-family="system-ui">Q_S = 20</text>'+
      '<text x="'+px(40)+'" y="272" fill="#38bdf8" font-size="9" font-weight="bold" text-anchor="middle" font-family="system-ui">Q_D = 40</text>'+
      // Knappheits-Klammer/Pfeil
      '<line x1="'+px(20.5)+'" y1="'+py(1.3)+'" x2="'+px(39.5)+'" y2="'+py(1.3)+'" stroke="#ef4444" stroke-width="2"/>'+
      '<polygon points="'+px(20.5)+','+py(1.3)+' '+(px(20.5)+5)+','+(py(1.3)-3)+' '+(px(20.5)+5)+','+(py(1.3)+3)+'" fill="#ef4444"/>'+
      '<polygon points="'+px(39.5)+','+py(1.3)+' '+(px(39.5)-5)+','+(py(1.3)-3)+' '+(px(39.5)-5)+','+(py(1.3)+3)+'" fill="#ef4444"/>'+
      '<text x="'+px(30)+'" y="'+py(0.7)+'" fill="#fca5a5" font-size="9" font-weight="bold" font-family="system-ui" text-anchor="middle">KNAPPHEIT / NACHFRAGEÜBERSCHUSS</text>',

    'wirtschaftskreislauf': AX.bg+AX.title('Der Wirtschaftskreislauf (Interaktiv)')+
      // Haushalte Card
      '<rect x="35" y="55" width="120" height="40" rx="8" fill="#1e1b4b" stroke="#38bdf8" stroke-width="1.5" filter="url(#glow)"/>'+
      '<text x="95" y="80" fill="#f0f9ff" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Haushalte (HH)</text>'+
      // Unternehmen Card
      '<rect x="265" y="55" width="120" height="40" rx="8" fill="#311005" stroke="#f59e0b" stroke-width="1.5" filter="url(#glow)"/>'+
      '<text x="325" y="80" fill="#fffbeb" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Unternehmen (UN)</text>'+
      // Staat Card
      '<rect x="150" y="160" width="120" height="40" rx="8" fill="#022c22" stroke="#10b981" stroke-width="1.5" filter="url(#glow)"/>'+
      '<text x="210" y="185" fill="#ecfdf5" font-size="11" font-weight="bold" font-family="system-ui" text-anchor="middle">Staat</text>'+
      // Banken/Finanzsektor Card
      '<rect x="150" y="240" width="120" height="35" rx="8" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>'+
      '<text x="210" y="262" fill="#cbd5e1" font-size="10" font-weight="bold" font-family="system-ui" text-anchor="middle">Finanzsektor</text>'+
      // Flows Haushalte <-> Unternehmen
      // 1. Gütermärkte (Oben): HH kaufen Konsumgüter, UN liefern Konsumgüter
      '<path d="M 155 60 C 210 35, 210 35, 265 60" fill="none" class="flow-real" stroke-width="2"/>'+
      '<text x="210" y="42" fill="#38bdf8" font-size="8" font-weight="bold" font-family="system-ui" text-anchor="middle">Konsumgüter</text>'+
      // 2. Geldstrom Konsumausgaben (darunter): HH zahlen, UN nehmen ein
      '<path d="M 265 72 C 210 50, 210 50, 155 72" fill="none" class="flow-money" stroke-width="2"/>'+
      '<text x="210" y="68" fill="#10b981" font-size="8" font-weight="bold" font-family="system-ui" text-anchor="middle">Konsumausgaben (€)</text>'+
      // 3. Faktormärkte (Unten): HH bieten Arbeit/Kapital, UN zahlen Einkommen
      '<path d="M 265 90 C 210 115, 210 115, 155 90" fill="none" class="flow-real" stroke-width="2"/>'+
      '<text x="210" y="112" fill="#38bdf8" font-size="8" font-weight="bold" font-family="system-ui" text-anchor="middle">Produktionsfaktoren</text>'+
      '<path d="M 155 95 C 210 125, 210 125, 265 95" fill="none" class="flow-money" stroke-width="2"/>'+
      '<text x="210" y="132" fill="#10b981" font-size="8" font-weight="bold" font-family="system-ui" text-anchor="middle">Faktoreinkommen (€)</text>'+
      // Staatliche Ströme (Dünnere statische Pfeile)
      '<line x1="95" y1="95" x2="160" y2="160" stroke="#10b981" stroke-width="1" stroke-dasharray="3,3"/>'+
      '<text x="110" y="135" fill="#10b981" font-size="7" font-weight="bold" font-family="system-ui">Steuern</text>'+
      '<line x1="180" y1="160" x2="115" y2="95" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,3"/>'+
      '<text x="150" y="135" fill="#38bdf8" font-size="7" font-weight="bold" font-family="system-ui">Transfers</text>'+
      '<line x1="325" y1="95" x2="260" y2="160" stroke="#10b981" stroke-width="1" stroke-dasharray="3,3"/>'+
      '<text x="310" y="135" fill="#10b981" font-size="7" font-weight="bold" font-family="system-ui">Steuern</text>'+
      '<line x1="240" y1="160" x2="305" y2="95" stroke="#38bdf8" stroke-width="1" stroke-dasharray="3,3"/>'+
      '<text x="250" y="135" fill="#38bdf8" font-size="7" font-weight="bold" font-family="system-ui">Subventionen</text>'+
      // Key Legend
      '<rect x="35" y="245" width="100" height="30" rx="4" fill="#0f172a" opacity="0.8" stroke="#1e293b"/>'+
      '<line x1="45" y1="253" x2="65" y2="253" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3"/>'+
      '<text x="70" y="256" fill="#94a3b8" font-size="7" font-weight="bold" font-family="system-ui">Realstrom</text>'+
      '<line x1="45" y1="267" x2="65" y2="267" stroke="#10b981" stroke-width="2" stroke-dasharray="3,3"/>'+
      '<text x="70" y="270" fill="#94a3b8" font-size="7" font-weight="bold" font-family="system-ui">Geldstrom (€)</text>',

    'bip-entwicklung': AX.bg+AX.xAxis+AX.yAxis+
      '<text x="220" y="291" fill="#cbd5e1" font-size="11" text-anchor="middle" font-weight="600" font-family="system-ui">Zeit (Jahre)</text>'+
      '<text x="16" y="145" fill="#cbd5e1" font-size="11" text-anchor="middle" font-weight="600" transform="rotate(-90,16,145)" font-family="system-ui">Reales BIP</text>'+
      AX.title('Konjunkturverlauf &amp; Wachstum')+
      // Langfristiger Trend (Wachstums-Gerade)
      '<line x1="'+px(5)+'" y1="'+py(2)+'" x2="'+px(45)+'" y2="'+py(8)+'" stroke="#64748b" stroke-width="2" stroke-dasharray="6,4"/>'+
      '<text x="290" y="90" fill="#94a3b8" font-size="8" font-weight="bold" font-family="system-ui">Langfristiger Trend</text>'+
      // Konjunkturzyklus (Sinus-Welle)
      // Wir berechnen Punkte auf einer Welle
      '<path d="M '+px(5)+' '+py(1.5)+
        ' Q '+px(15)+' '+py(6.5)+', '+px(25)+' '+py(5)+
        ' T '+px(45)+' '+py(8.5)+'" fill="none" stroke="url(#demandGrad)" stroke-width="3.5" filter="url(#glow)"/>'+
      '<text x="325" y="140" fill="#38bdf8" font-size="9" font-weight="bold" font-family="system-ui">Konjunkturzyklus</text>'+
      // Punkte markieren: Boom & Rezession
      '<circle cx="'+px(15)+'" cy="'+py(4.9)+'" r="4" fill="#ef4444"/>'+
      '<text x="'+px(15)+'" y="'+(py(4.9)-8)+'" fill="#f87171" font-size="8" font-weight="bold" text-anchor="middle" font-family="system-ui">Boom</text>'+
      '<circle cx="'+px(32)+'" cy="'+py(4.6)+'" r="4" fill="#38bdf8"/>'+
      '<text x="'+px(32)+'" y="'+(py(4.6)+14)+'" fill="#38bdf8" font-size="8" font-weight="bold" text-anchor="middle" font-family="system-ui">Rezession</text>',

    'koordinatensystem': AX.bg+AX.xAxis+AX.yAxis+AX.xLabel+AX.yLabel+AX.title('Koordinatensystem')
  };
  const content=d[type]||'';
  if(!content)return '';
  return AX.svgOpen+content+AX.svgClose;
}

// ===================== LERN-MODUS (Themenbasiert) =====================

// Hilfsfunktion: Holt alle Themen eines Fachs (auch über Parts hinweg)
function getTopicsForSubject(subjKey){
  const cfg=SUBJECTS[subjKey];
  let topics=[];
  if(cfg.parts>1){
    topics=topics.concat(TOPICS[cfg.part1.key]||[]);
    topics=topics.concat(TOPICS[cfg.part2.key]||[]);
  }else{
    topics=TOPICS[cfg.part1.key]||[];
  }
  return topics;
}

function enterLearnMode(){
  const key=state.currentSubject;
  if(!key){
    document.getElementById('learnCard').innerHTML='<p style="color:var(--text3);text-align:center;padding:60px">Wähle links ein Fach aus, um die Themen zu sehen.<br><br>Im Lern-Modus kannst du <strong>themenspezifisch</strong> lernen: Erst die Theorie lesen, dann die passenden Fragen üben – mit sofortigem Feedback.</p>';
    document.getElementById('learnNav').style.display='none';
    return;
  }
  const cfg=SUBJECTS[key];
  const topics=getTopicsForSubject(key);
  
  document.getElementById('learnTitle').textContent='🎯 '+cfg.icon+' '+cfg.name+' – Lern-Modus';
  document.getElementById('learnSubject').textContent=topics.length+' Themen';
  document.getElementById('learnNav').style.display='none';
  
  if(topics.length===0){
    document.getElementById('learnCard').innerHTML='<p style="color:var(--text3);text-align:center;padding:40px">Keine Themen verfügbar.</p>';
    return;
  }
  
  // Lern-Fortschritt laden
  const progress=JSON.parse(localStorage.getItem('learnProgress')||'{}');
  const subjProgress=progress[key]||{};
  
  // Themenliste rendern
  let html='<div class="topic-list">';
  topics.forEach((t,idx)=>{
    const qCount=countQuestionsForTopic(key,t.filter);
    const answered=countAnsweredInTopic(key,t.filter);
    const topicProg=subjProgress[t.id]||{correct:0,total:0};
    let statusClass='';
    if(answered>0&&topicProg.correct===answered)statusClass=' topic-done';
    else if(answered>0)statusClass=' topic-partial';
    html+='<div class="topic-card'+statusClass+'" onclick="selectTopicByIdx('+idx+')">';
    html+='<div class="topic-icon">'+t.icon+'</div>';
    html+='<div class="topic-info">';
    html+='<div class="topic-name">'+t.name+'</div>';
    html+='<div class="topic-count">'+qCount+' Frage(n)';
    if(answered>0)html+=' · '+topicProg.correct+'/'+answered+' richtig';
    html+='</div></div>';
    if(answered>0){
      const pct=Math.round((topicProg.correct/answered)*100);
      html+='<div class="topic-badge" style="color:'+(pct>=70?'var(--success)':pct>=40?'var(--warning)':'var(--danger)')+'">'+pct+'%</div>';
    }else{
      html+='<div class="topic-arrow">▶</div>';
    }
    html+='</div>';
  });
  html+='</div>';
  document.getElementById('learnCard').innerHTML=html;
}

function selectTopicByIdx(idx){
  const key=state.currentSubject;
  const topics=getTopicsForSubject(key);
  if(idx>=0&&idx<topics.length)selectTopic(topics[idx].id);
}

function countAnsweredInTopic(subjKey,filters){
  const qs=getQuestionsForTopic(subjKey,filters);
  const key=subjKey;
  const progress=JSON.parse(localStorage.getItem('learnProgress')||'{}');
  const subjProgress=progress[key]||{};
  let answered=0;
  qs.forEach(q=>{
    if(subjProgress[q.id])answered++;
  });
  return answered;
}

function countQuestionsForTopic(subjKey,filters){
  const cfg=SUBJECTS[subjKey];
  const BANK_MAP={bwl1:QUESTION_BANK_bwl1,bwl2:QUESTION_BANK_bwl2,mawi1:QUESTION_BANK_mawi1,mawi2:QUESTION_BANK_mawi2,vwl:QUESTION_BANK_vwl,wpr:QUESTION_BANK_wpr,perso:QUESTION_BANK_perso};
  let allQ=[];
  if(cfg.parts>1){
    allQ=(BANK_MAP[cfg.part1.key]||[]).concat(BANK_MAP[cfg.part2.key]||[]);
  }else{
    allQ=BANK_MAP[cfg.part1.key]||[];
  }
  return allQ.filter(q=>filters.some(f=>q.source.startsWith(f))).length;
}

function getQuestionsForTopic(subjKey,filters){
  const cfg=SUBJECTS[subjKey];
  const BANK_MAP={bwl1:QUESTION_BANK_bwl1,bwl2:QUESTION_BANK_bwl2,mawi1:QUESTION_BANK_mawi1,mawi2:QUESTION_BANK_mawi2,vwl:QUESTION_BANK_vwl,wpr:QUESTION_BANK_wpr,perso:QUESTION_BANK_perso};
  let allQ=[];
  if(cfg.parts>1){
    allQ=(BANK_MAP[cfg.part1.key]||[]).concat(BANK_MAP[cfg.part2.key]||[]);
  }else{
    allQ=BANK_MAP[cfg.part1.key]||[];
  }
  return allQ.filter(q=>filters.some(f=>q.source.startsWith(f)));
}

function selectTopic(topicId){
  const key=state.currentSubject;
  if(!key)return;
  const topics=getTopicsForSubject(key);
  const topic=topics.find(t=>t.id===topicId);
  if(!topic)return;
  const qCount=countQuestionsForTopic(key,topic.filter);
  
  document.getElementById('learnSubject').textContent=topic.icon+' '+topic.name;
  document.getElementById('learnNav').style.display='none';
  
  let html='<div class="topic-detail-header">';
  html+='<button class="btn btn-secondary topic-back" onclick="enterLearnMode()">◀ Zurück zur Themenliste</button>';
  html+='<h2 class="topic-detail-title">'+topic.icon+' '+topic.name+'</h2>';
  html+='</div>';
  
  html+='<div class="topic-explanation">'+renderMarkdown(topic.explanation)+'</div>';
  
  if(qCount>0){
    html+='<div class="topic-action">';
    html+='<button class="btn btn-primary" onclick="startTopicQuiz(currentTopicId)">✍️ '+qCount+' Frage(n) zu diesem Thema üben</button>';
    html+='</div>';
  }else{
    html+='<p style="color:var(--text3);text-align:center;padding:20px">Keine Fragen zu diesem Thema.</p>';
  }
  window.currentTopicId=topicId;
  
  document.getElementById('learnCard').innerHTML=html;
}

function startTopicQuiz(topicId){
  const key=state.currentSubject;
  if(!key)return;
  const topics=getTopicsForSubject(key);
  const topic=topics.find(t=>t.id===topicId);
  if(!topic)return;
  
  const qs=getQuestionsForTopic(key,topic.filter);
  if(qs.length===0){
    enterLearnMode();
    return;
  }
  
  state.learn.questions=qs;
  state.learn.currentIdx=0;
  state.learn.answered={};
  state.learn.total=qs.length;
  state.learn.currentTopicId=topicId;
  
  document.getElementById('learnNav').style.display='flex';
  renderLearnCard();
}

function renderLearnCard(){
  const qs=state.learn.questions;
  const idx=state.learn.currentIdx;
  if(!qs||qs.length===0){
    document.getElementById('learnCard').innerHTML='<p style="color:var(--text3);text-align:center;padding:40px">Keine Fragen verfügbar.</p>';
    document.getElementById('learnProgress').textContent='0 / 0';
    document.getElementById('progressDots').innerHTML='';
    return;
  }
  
  const q=qs[idx];
  const answered=state.learn.answered[idx]||{};
  const isAns=answered.selected!==undefined;
  
  document.getElementById('learnProgress').textContent=(idx+1)+' / '+qs.length;
  document.getElementById('btnLearnPrev').disabled=idx===0;
  document.getElementById('btnLearnNext').textContent=idx<qs.length-1?'Weiter ▶':'🎉 Fertig!';
  
  // Progress-Dots
  const dots=document.getElementById('progressDots');
  dots.innerHTML='';
  for(let i=0;i<qs.length;i++){
    const d=document.createElement('button');
    d.className='prog-dot';
    if(i===idx)d.classList.add('active');
    const a=state.learn.answered[i];
    if(a&&a.correct!==undefined)d.classList.add(a.correct?'correct':'wrong');
    else if(a)d.classList.add('answered');
    d.onclick=()=>{state.learn.currentIdx=i;renderLearnCard();};
    d.title='Frage '+(i+1);
    dots.appendChild(d);
  }
  
  // Card bauen
  let html='';
  html+='<div class="q-number">Frage '+(idx+1)+' · '+q.points+' Punkte';
  if(q.type==='ma')html+=' · <span style="color:var(--warning)">Mehrfachauswahl</span>';
  if(q.type==='fitb')html+=' · <span style="color:var(--accent3)">Lückentext</span>';
  html+='</div>';
  html+='<div class="q-source">📖 '+q.source+'</div>';
  
  // Status-Badge
  if(isAns){
    const cls=answered.correct?'correct':'wrong';
    const txt=answered.correct?'✅ Richtig!':'❌ Falsch';
    html+='<div class="answer-status '+cls+'">'+txt+' ('+answered.points+'/'+q.points+' Pkt)</div>';
  }
  
  if(q.diagram){html+='<div class="diagram-box">'+getDiagram(q.diagram)+'</div>';}
  html+='<div class="q-text">'+q.question+'</div>';
  
  if(q.type==='mc'||q.type==='ma'){
    html+='<div class="options">';
    const isMA=q.type==='ma';
    const selArr=isAns?(Array.isArray(answered.selected)?answered.selected:[answered.selected]):[];
    q.options.forEach((opt,oi)=>{
      const selected=isAns&&selArr.includes(oi);
      let extra='';
      if(isAns){
        if(isMA&&Array.isArray(q.correct)){
          // MA: markiere richtig gewählte, falsch gewählte, verpasste
          if(selected&&q.correct.includes(oi))extra=' checked-correct';
          else if(selected&&!q.correct.includes(oi))extra=' checked-wrong';
          else if(!selected&&q.correct.includes(oi))extra=' missed-correct';
        }else{
          if(oi===q.correct)extra=' correct-answer';
          if(selected&&oi===q.correct)extra=' checked-correct';
          else if(selected&&oi!==q.correct)extra=' checked-wrong';
        }
      }
      html+='<div class="option'+extra+'" onclick="learnSelectOption('+idx+','+oi+')">';
      if(isMA){
        html+='<div class="radio" style="border-radius:4px">'+(selected?'✓':'')+'</div>';
      }else{
        html+='<div class="radio">'+(selected?'<div style="width:6px;height:6px;border-radius:50%;background:'+(isAns?(answered.correct?'var(--success)':'var(--danger)'):'var(--bg)')+'"></div>':'')+'</div>';
      }
      html+='<span>'+opt+'</span></div>';
    });
    html+='</div>';
    if(!isAns&&isMA)html+='<div style="font-size:.78rem;color:var(--text3);margin-top:6px">💡 Mehrere Antworten möglich</div>';
  }else if(q.type==='fitb'){
    const val=isAns?answered.text:'';
    const cls=isAns?(answered.correct?'correct':'wrong'):'';
    html+='<input type="text" class="ft-input '+cls+'" id="learnFtInput" value="'+val+'" placeholder="Antwort eingeben..." '+(isAns?'disabled':'')+' onkeydown="if(event.key===\\'Enter\\')learnCheckFill()">';
  }
  
  // Check-Button
  if(!isAns){
    if(q.type==='fitb'){
      html+='<div><button class="check-btn" id="btnCheckFill" onclick="learnCheckFill()">✅ Antwort prüfen</button></div>';
    }else{
      html+='<div><button class="check-btn" id="btnCheckMC" onclick="learnCheckMC('+idx+')">✅ Antwort prüfen</button></div>';
    }
  }
  
  // Feedback (Lösung)
  if(isAns){
    html+='<div class="learn-feedback show '+(answered.correct?'correct':'wrong')+'">';
    html+='<h4>💡 Musterlösung</h4>';
    html+='<p>'+(q.solution||'Siehe Vorlesungsmaterial')+'</p>';
    if(q.type==='mc'||q.type==='ma'){
      if(Array.isArray(q.correct)){
        const richtige=q.correct.map(i=>'<strong>'+(q.options[i]||'')+'</strong>');
        html+='<p style="margin-top:8px">✔️ Richtig: '+richtige.join(', ')+'</p>';
      }else{
        html+='<p style="margin-top:8px">✔️ Richtige Antwort: <strong>'+(q.options[q.correct]||'')+'</strong></p>';
      }
    }else if(q.type==='fitb'){
      html+='<p style="margin-top:8px">✔️ Richtige Antwort: <strong>'+(q.correct||'')+'</strong></p>';
    }
    html+='<div class="ref">📖 Quelle: '+q.source+'</div>';
    html+='</div>';
  }
  
  document.getElementById('learnCard').innerHTML=html;
}

function learnSelectOption(qIdx,oi){
  const answered=state.learn.answered[qIdx];
  if(answered&&answered.selected!==undefined)return; // bereits beantwortet
  const q=state.learn.questions[qIdx];
  if(!q)return;
  
  if(q.type==='ma'){
    // MA: toggle
    if(!state.learn.answered[qIdx])state.learn.answered[qIdx]={selected:[]};
    const arr=state.learn.answered[qIdx].selected;
    const pos=arr.indexOf(oi);
    if(pos>=0)arr.splice(pos,1);
    else arr.push(oi);
    renderLearnCard();
  }else{
    // MC: select single
    state.learn.answered[qIdx]={selected:oi};
    renderLearnCard();
  }
}

function learnCheckMC(qIdx){
  const answered=state.learn.answered[qIdx];
  if(!answered||answered.selected===undefined)return;
  const q=state.learn.questions[qIdx];
  if(!q)return;
  
  if(q.type==='ma'){
    // MA-Bewertung
    const userSel=Array.isArray(answered.selected)?answered.selected:[answered.selected];
    const correct=q.correct||[];
    let richtigCount=0;
    const totalCorrect=correct.length;
    userSel.forEach(idx=>{if(correct.includes(idx))richtigCount++;});
    // Punkte = anteilig: jede richtig/nicht-richtig gewählte
    const allOptions=q.options.length;
    let gewonnene=0;
    for(let i=0;i<allOptions;i++){
      const isUser=userSel.includes(i);
      const isCor=correct.includes(i);
      if(isUser&&isCor)gewonnene++;
      else if(!isUser&&!isCor)gewonnene++;
    }
    const pct=gewonnene/allOptions;
    const points=Math.round(pct*q.points*10)/10;
    answered.points=points;
    answered.correct=pct>=0.5;
    answered.pct=pct;
  }else{
    // MC
    answered.correct=answered.selected===q.correct;
    answered.points=answered.correct?q.points:0;
  }
  renderLearnCard();
}

function learnCheckFill(){
  const input=document.getElementById('learnFtInput');
  if(!input)return;
  const qIdx=state.learn.currentIdx;
  const q=state.learn.questions[qIdx];
  if(!q)return;
  const val=input.value.trim();
  if(!val)return;
  
  state.learn.answered[qIdx]={selected:val,text:val};
  const correct=String(q.correct).trim().toLowerCase();
  const answer=val.toLowerCase();
  // Prüfe gegen acceptable-Liste
  let matched=false;
  if(q.acceptable&&Array.isArray(q.acceptable)){
    for(let a of q.acceptable){
      if(answer===String(a).trim().toLowerCase()){matched=true;break;}
    }
  }
  matched=matched||answer===correct;
  state.learn.answered[qIdx].correct=matched;
  state.learn.answered[qIdx].points=matched?q.points:0;
  renderLearnCard();
}

function prevLearnCard(){
  if(state.learn.currentIdx>0){
    state.learn.currentIdx--;
    renderLearnCard();
  }
}

function nextLearnCard(){
  if(state.learn.currentIdx<state.learn.questions.length-1){
    state.learn.currentIdx++;
    renderLearnCard();
  }else{
    // Fertig – Ergebnisse zeigen
    showLearnResults();
  }
}

function goExamMode(){switchTab('exam');}

function showLearnResults(){
  const qs=state.learn.questions;
  let correct=0,totalP=0,earnedP=0,answeredCount=0;
  qs.forEach((q,i)=>{
    const a=state.learn.answered[i];
    totalP+=q.points;
    if(a&&a.selected!==undefined){
      answeredCount++;
      if(a.correct)correct++;
      earnedP+=a.points||0;
    }
  });
  const pct=totalP>0?(earnedP/totalP)*100:0;
  const card=document.getElementById('learnCard');
  card.innerHTML='<div style="text-align:center;padding:30px">'+
    '<div style="font-size:3rem;margin-bottom:12px">🎉</div>'+
    '<h2 style="margin-bottom:8px">Lern-Modus abgeschlossen!</h2>'+
    '<p style="color:var(--text2);margin-bottom:20px">Du hast '+answeredCount+' von '+qs.length+' Fragen beantwortet.</p>'+
    '<div class="result-stats" style="grid-template-columns:repeat(auto-fit,minmax(100px,1fr));max-width:500px;margin:0 auto 24px">'+
    '<div class="stat-box"><div class="num" style="color:var(--success)">'+correct+'/'+answeredCount+'</div><div class="desc">Richtig</div></div>'+
    '<div class="stat-box"><div class="num" style="color:var(--accent)">'+earnedP+'/'+totalP+'</div><div class="desc">Punkte</div></div>'+
    '<div class="stat-box"><div class="num" style="color:'+(pct>=48?'var(--success)':'var(--danger)')+'">'+pct.toFixed(1)+'%</div><div class="desc">Quote</div></div>'+
    '</div>'+
    '<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">'+
    '<button class="btn btn-primary" onclick="state.learn.currentIdx=0;state.learn.answered={};renderLearnCard()">🔄 Wiederholen</button>'+
    '<button class="btn btn-secondary" onclick="goExamMode()">📝 Klausur versuchen</button>'+
    '</div></div>';
  document.getElementById('learnNav').style.display='none';
}

function renderQuestions(){
  const container=document.getElementById('questionsContainer');
  container.innerHTML='';
  state.questions.forEach((q,idx)=>{
    const card=document.createElement('div');
    card.className='question-card';
    card.id='qcard-'+idx;
    let html='<div class="q-number">Frage '+(idx+1)+' · '+q.points+' Punkte</div>';
    html+='<div class="q-source">📖 '+q.source+'</div>';
    if(q.diagram){html+='<div class="diagram-box">'+getDiagram(q.diagram)+'</div>';}
    html+='<div class="q-text">'+q.question+'</div>';
    html+='<div class="options" id="opts-'+idx+'">';
    q.options.forEach((opt,oi)=>{
      html+='<div class="option" id="opt-'+idx+'-'+oi+'" onclick="selectOption('+idx+','+oi+')"><div class="radio"></div><span>'+opt+'</span></div>';
    });
    html+='</div>';
    html+='<div class="solution" id="sol-'+idx+'"><h4>💡 Musterlösung</h4><p>'+(q.solution||'Siehe Vorlesungsmaterial')+'</p><div class="ref">📖 Quelle: '+q.source+'</div></div>';
    card.innerHTML=html;
    container.appendChild(card);
  });
}

function selectOption(qIdx,optIdx){
  if(state.examSubmitted)return;
  state.selectedAnswers[qIdx]=optIdx;
  const opts=document.getElementById('opts-'+qIdx);
  if(opts){opts.querySelectorAll('.option').forEach((el,i)=>el.classList.toggle('selected',i===optIdx));}
}

function submitExam(auto){
  if(state.examSubmitted)return;
  const unanswered=[];
  state.questions.forEach((q,idx)=>{if(state.selectedAnswers[idx]===undefined)unanswered.push(idx+1);});
  if(!auto&&unanswered.length>0){if(!confirm('⚠️ '+unanswered.length+' Frage(n) nicht beantwortet (Nr. '+unanswered.join(', ')+'). Trotzdem abgeben?'))return;}
  if(state.timerRunning)toggleTimer();
  state.examSubmitted=true;
  document.getElementById('btnSubmit').disabled=true;
  let correct=0,totalPoints=0,earnedPoints=0;
  state.questions.forEach((q,idx)=>{
    const sel=state.selectedAnswers[idx];
    const isCorrect=sel===q.correct;
    if(isCorrect){correct++;earnedPoints+=q.points;}
    totalPoints+=q.points;
    const card=document.getElementById('qcard-'+idx);
    if(card){card.classList.add(isCorrect?'correct':'incorrect');}
    const opts=document.getElementById('opts-'+idx);
    if(opts){opts.querySelectorAll('.option').forEach((el,i)=>{
      if(i===q.correct)el.classList.add('correct-answer');
      if(i===sel&&sel!==q.correct)el.classList.add('wrong-answer');
    });}
    const sol=document.getElementById('sol-'+idx);
    if(sol)sol.classList.add('show');
  });
  const pct=totalPoints>0?(earnedPoints/totalPoints)*100:0;
  const grade=calcGrade(pct,state.currentSubject);
  updateStats(state.currentSubject,pct>=passThreshold(state.currentSubject));
  showResults(correct,state.questions.length,earnedPoints,totalPoints,pct,grade);
}

function calcGrade(pct,subj){
  const strict=SUBJECTS[subj]&&SUBJECTS[subj].strictGrading;
  const th=strict?[93,82,65,48,32,0]:[85,70,55,40,25,0];
  if(pct>=th[0])return 1;
  if(pct>=th[1])return 2;
  if(pct>=th[2])return 3;
  if(pct>=th[3])return 4;
  if(pct>=th[4])return 5;
  return 6;
}

function passThreshold(subj){return SUBJECTS[subj]&&SUBJECTS[subj].strictGrading?48:40;}

function showResults(correct,total,earned,possible,pct,grade){
  const passed=pct>=passThreshold(state.currentSubject);
  const card=document.getElementById('resultCard');
  const emoji=passed?(grade<=2?'🎉':'✅'):'😞';
  card.innerHTML='<div class="result-grade"><div class="grade '+(passed?'passed':'failed')+'">'+emoji+' '+grade+',0</div><div class="label">'+(passed?'🎊 Bestanden!':'📖 Nicht bestanden')+'</div></div><div class="result-stats"><div class="stat-box"><div class="num" style="color:var(--success)">'+correct+'/'+total+'</div><div class="desc">Richtig</div></div><div class="stat-box"><div class="num" style="color:var(--accent)">'+earned+'/'+possible+'</div><div class="desc">Punkte</div></div><div class="stat-box"><div class="num" style="color:'+(passed?'var(--success)':'var(--danger)')+'">'+pct.toFixed(1)+'%</div><div class="desc">Quote</div></div><div class="stat-box"><div class="num" style="color:var(--accent2)">'+grade+',0</div><div class="desc">Note</div></div></div><div style="text-align:center;margin-bottom:16px;font-size:.85rem;color:var(--text3);padding:12px;background:var(--bg3);border-radius:var(--radius-sm)">'+(SUBJECTS[state.currentSubject].strictGrading?'⚠️ Strenger Bewertungsmaßstab':'📊 Normaler Bewertungsmaßstab')+'</div><div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:20px"><button class="btn btn-primary" onclick="closeResults()">📚 Weiter üben</button><button class="btn btn-success" onclick="closeResults();generateNewExam()">🔄 Neue Klausur</button></div>';
  document.getElementById('resultsOverlay').classList.add('show');
}

function closeResults(){document.getElementById('resultsOverlay').classList.remove('show');}

function resetTimer(){
  if(state.timer)clearInterval(state.timer);
  state.timerRunning=false;
  const mins=parseInt(document.getElementById('timerMinutes').value)||45;
  state.timerSeconds=mins*60;
  state.timerTotal=mins*60;
  updateTimerDisplay();
  document.getElementById('btnStartTimer').textContent='▶ Start';
}

function toggleTimer(){
  if(state.timerRunning){clearInterval(state.timer);state.timerRunning=false;document.getElementById('btnStartTimer').textContent='▶ Weiter';}
  else{state.timerRunning=true;state.timer=setInterval(timerTick,1000);document.getElementById('btnStartTimer').textContent='⏸ Pause';}
}

function timerTick(){
  if(state.timerSeconds<=0){
    clearInterval(state.timer);state.timerRunning=false;
    document.getElementById('btnStartTimer').textContent='▶ Start';
    submitExam(true);return;
  }
  state.timerSeconds--;
  updateTimerDisplay();
}

function updateTimerDisplay(){
  const m=Math.floor(state.timerSeconds/60),s=state.timerSeconds%60;
  const d=document.getElementById('timerDisplay');
  d.textContent=m.toString().padStart(2,'0')+':'+s.toString().padStart(2,'0');
  const pct=state.timerTotal>0?(state.timerSeconds/state.timerTotal)*100:0;
  d.className='timer-display';
  if(pct<10)d.classList.add('danger');else if(pct<25)d.classList.add('warning');
  const bar=document.getElementById('progressFill');
  bar.style.width=pct+'%';bar.className='progress-fill';
  if(pct<10)bar.classList.add('danger');else if(pct<25)bar.classList.add('warning');
}

function updateTimerFromInput(){if(state.timerRunning)toggleTimer();resetTimer();}

function onPartSelectChange(){
  if(state.timerRunning)toggleTimer();
  state.currentPart=parseInt(document.getElementById('timerPartSelect').value);
  generateNewExam();
}

function updateStats(subj,passed){
  if(!state.stats[subj])state.stats[subj]={attempts:0,passed:0};
  state.stats[subj].attempts++;
  if(passed)state.stats[subj].passed++;
  localStorage.setItem('klausurenStats',JSON.stringify(state.stats));
  document.getElementById('badge-'+subj).textContent=state.stats[subj].attempts;
}

function showMaterials(){
  let totalFiles = 0;
  for(let key in MATERIALS){
    totalFiles += MATERIALS[key].length;
  }
  document.getElementById('materialsTotalCount').textContent = totalFiles;
  
  document.getElementById('materialsSearch').value = '';
  document.getElementById('materialsSubjectFilter').value = state.currentSubject || 'all';
  document.getElementById('materialsCategoryFilter').value = 'all';
  
  filterMaterials();
}

function filterMaterials(){
  const search = document.getElementById('materialsSearch').value.toLowerCase().trim();
  const subjectFilter = document.getElementById('materialsSubjectFilter').value;
  const categoryFilter = document.getElementById('materialsCategoryFilter').value;
  
  const container = document.getElementById('materialsList');
  container.innerHTML = '';
  
  const subjectsToRender = subjectFilter === 'all' ? Object.keys(MATERIALS) : [subjectFilter];
  let matchCount = 0;
  
  subjectsToRender.forEach(subj => {
    const files = MATERIALS[subj] || [];
    const filteredFiles = files.filter(f => {
      const nameMatch = f.name.toLowerCase().includes(search) || f.path.toLowerCase().includes(search);
      const catMatch = categoryFilter === 'all' || f.category === categoryFilter;
      return nameMatch && catMatch;
    });
    
    if (filteredFiles.length === 0) return;
    
    matchCount += filteredFiles.length;
    
    const groups = {};
    filteredFiles.forEach(f => {
      if(!groups[f.category]) groups[f.category] = [];
      groups[f.category].push(f);
    });
    
    const subjMeta = SUBJECTS[subj] || { name: subj.toUpperCase(), icon: '📁' };
    
    const subjDiv = document.createElement('div');
    subjDiv.className = 'material-subject-section';
    subjDiv.style.marginBottom = '24px';
    
    let html = `<h2 style="font-size: 1.25rem; font-weight: 700; color: var(--accent); margin-bottom: 16px; display: flex; align-items: center; gap: 8px; border-bottom: 2px solid var(--border); padding-bottom: 8px;">
      <span>${subjMeta.icon}</span> ${subjMeta.name}
    </h2>`;
    
    for(let cat in groups){
      html += `<div style="margin-bottom: 16px;">
        <h3 style="font-size: .95rem; font-weight: 600; color: var(--text2); margin-bottom: 10px; display: flex; align-items: center; gap: 6px;">
          📁 ${cat} <span style="font-size: .75rem; color: var(--text3); font-weight: normal;">(${groups[cat].length} Dateien)</span>
        </h3>
        <div class="material-grid">`;
      
      groups[cat].forEach(f => {
        let fileIcon = '📄';
        if (f.ext === 'pdf') fileIcon = '🔴';
        else if (f.ext === 'docx' || f.ext === 'doc') fileIcon = '🔵';
        else if (['png', 'jpg', 'jpeg'].includes(f.ext)) fileIcon = '🖼️';
        
        html += `<a href="${f.path}" target="_blank" class="material-item">
          <div class="material-icon">${fileIcon}</div>
          <div class="material-info">
            <div class="material-name" title="${f.name}">${f.name}</div>
            <div class="material-meta">
              <span class="material-badge ${f.ext}">${f.ext}</span>
              <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${f.path}</span>
            </div>
          </div>
        </a>`;
      });
      
      html += `</div></div>`;
    }
    
    subjDiv.innerHTML = html;
    container.appendChild(subjDiv);
  });
  
  if (matchCount === 0) {
    container.innerHTML = `<div style="text-align: center; padding: 60px 20px; color: var(--text3);">
      <div style="font-size: 3rem; margin-bottom: 12px;">🔍</div>
      <p>Keine Materialien gefunden, die deinen Filtern entsprechen.</p>
    </div>`;
  }
}

console.log('✅ Klausuren-Trainer geladen');
console.log('Fragen: BWL1='+QUESTION_BANK_bwl1.length+', BWL2='+QUESTION_BANK_bwl2.length+', MAWI1='+QUESTION_BANK_mawi1.length+', MAWI2='+QUESTION_BANK_mawi2.length+', VWL='+QUESTION_BANK_vwl.length+', WPR='+QUESTION_BANK_wpr.length+', PERSO='+QUESTION_BANK_perso.length);
</script>
</body>
</html>"""

# Insert questions and summaries
html_final = HTML.replace("__QUESTIONS_JS__", questions_js)
html_final = html_final.replace("__SUMMARIES_JS__", summaries_js)
html_final = html_final.replace("__TOPICS_JS__", topics_js)
html_final = html_final.replace("__MATERIALS_JS__", materials_js)

# Fix the typo "Frague" -> "Frage"
html_final = html_final.replace("Frague", "Frage")

# Write
with open(os.path.join(BASE, "klausuren-trainer.html"), "w", encoding="utf-8") as f:
    f.write(html_final)

# Count
import re
total = 0
for bank in ['bwl1','bwl2','mawi1','mawi2','vwl','wpr','perso']:
    cnt = len(re.findall(rf'QUESTION_BANK_{bank} = \[', html_final))
    print(f"{bank}: ~{len(QUESTIONS[bank])} Fragen")
    total += len(QUESTIONS[bank])
print(f"\nTOTAL: {total} Fragen")
print(f"Dateigröße: {len(html_final):,} Bytes")
print(f"\n✅ HTML geschrieben: klausuren-trainer.html")
