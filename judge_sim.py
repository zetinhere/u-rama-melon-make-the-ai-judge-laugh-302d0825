#!/usr/bin/env python3
"""Simulate the published judge brief (pairwise, one order) over the
7 shortlisted jokes, using deepseek-v4.1-flash-free via hms.py.
Proxy signal only — the real judge is z-ai/glm-5.3-flash — but it runs
the exact same brief: truth, surprise, tightness, freshness, in order.
"""
import itertools
import json
import sys

sys.path.insert(0, "/home/hatch/workspace/100milionseek")
import hms

CANDS = {
    "A": "The fire drill is the only meeting everyone attends on time.",
    "B": "Our office thermostat has two settings: arctic and passive-aggressive.",
    "C": "HR's wellness program is a poster of a sunset and a link nobody clicks.",
    "D": "My boss tracks my mouse, so I tied it to the office dog. I'm now employee of the month.",
    "E": "Our manager's favorite phrase is 'quick question' — it's never quick, never a question, and always at 4:55.",
    "F": "I finally understand synergy: it's when five people take credit for the intern's spreadsheet.",
    "H": "The printer only jams when the document matters — it's the most honest performance review in the building.",
}

BRIEF = """You are a comedy club headliner who has heard ten thousand office jokes and only laughs at the ones with a real observation inside.
Each entry is one joke about office life, a single line of under 200 characters, written to be read aloud in one breath. You will be shown two jokes, Entry A and Entry B. Pick the joke that gets the bigger laugh.
Weigh them on these, most important first:
1. The joke is about office life and lands as a joke.
2. The observation is true to the office: meetings, email, bosses, coffee, deadlines, the printer.
3. The turn is surprising: a fresh angle or an unexpected last word rather than a pun or a stock line everyone has heard.
4. It is tight: one line, no wasted setup, every word earning its place, and it reads cleanly aloud.
5. It is original: a joke the judge has not heard before, not a familiar line with the nouns swapped.
A joke that needs explaining has already lost. The laugh is the only measure.
Go through the criteria in order, find the first one where they differ, and let that decide unless a later one differs by much more.
Answer with a short reason (one sentence), then a line 'Verdict: A' or 'Verdict: B', then 'Margin: N' (1 by a hair to 5 overwhelmingly better). No tie allowed."""

wins = {k: 0.0 for k in CANDS}
games = {k: 0 for k in CANDS}
results = []
for (ka, a), (kb, b) in itertools.combinations(CANDS.items(), 2):
    prompt = f"{BRIEF}\n\nEntry A: {a}\nEntry B: {b}"
    try:
        data, _quota = hms.chat(prompt, max_tokens=400)
        out = data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"{ka} vs {kb}: ERROR {e}", flush=True)
        continue
    verdict = None
    margin = 1
    for line in out.splitlines():
        ls = line.strip().lower()
        if ls.startswith("verdict:"):
            verdict = "A" if " a" in ls or ls.endswith("a") else ("B" if " b" in ls or ls.endswith("b") else None)
        if ls.startswith("margin:"):
            try:
                margin = max(1, min(5, int(ls.split(":")[1].strip()[0])))
            except Exception:
                pass
    if verdict is None:
        print(f"{ka} vs {kb}: NO VERDICT :: {out[:200]!r}", flush=True)
        continue
    winner = ka if verdict == "A" else kb
    loser = kb if verdict == "A" else ka
    score = 0.5 + margin / 10.0
    wins[winner] += score
    wins[loser] += 1.0 - score
    games[winner] += 1
    games[loser] += 1
    results.append({"pair": [ka, kb], "winner": winner, "margin": margin})
    print(f"{ka} vs {kb}: {winner} wins, margin {margin} :: {out.strip().splitlines()[0][:120]}", flush=True)

print("\n=== STANDINGS (win share over games played) ===")
for k in sorted(CANDS, key=lambda k: -wins[k] / max(1, games[k])):
    print(f"{k}: {wins[k]:.2f}/{games[k]} = {wins[k]/max(1,games[k]):.3f}  ({CANDS[k]})")
print(json.dumps(results))
