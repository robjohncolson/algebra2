# Continuation Prompt — Algebra 2 Unit 4 Lesson 1

## What to do NOW

Unit 4 Lesson 1 (Inverse Variation & Reciprocal Function) is **feature-complete**. All deliverables are built, deployed, and linked. The next session should either:

1. **Start Unit 4 Lesson 2** — Drop the next set of Savvas source files into this repo and repeat the workflow:
   - Topic 4 Assessment (already in repo as `aga_24_a2_na_04_ttb.docx`) → filter L2 items
   - New L2 source files (lp, lps, lq, ml, rbu) → extract, verify, build deliverables
   - The TTB assessment mapping for non-L1 items is already done in `unit4_lesson1_verified.json` → use it as a starting point

2. **Polish existing L1 deliverables** — potential improvements:
   - Google Form images: currently manual attach. Could extend `create_quiz.gs` to pull from Drive URLs
   - Blooket: user uploads images manually after CSV import
   - Cartridge: test on live Vercel deployment, verify all 6 levels work end-to-end

3. **Build the cartridge into lrsl-driller properly** — the cartridge is registered but the app.html dropdown has some hardcoded entries that are stale (only 12 options listed vs 20 in registry). The dynamic `populateCartridgeList()` at line 3638 handles it, but worth verifying.

## Session Commits (2026-03-18)

```
1fb44bd Use plain vocab terms as Blooket answers, fix Q1 table clipping
ff37483 Add graphics for Blooket + Google Form, shorten Blooket questions
59cf630 Rewrite Blooket CSV to match official import template format
31cdcf5 Rewrite Blooket CSV with scenario-only clues, no raw definitions
47d444d Add heuristic-resistant Blooket CSV and Google Forms auto-create script
af398d6 Add Lesson 1 deliverables: Blooket, Google Form quiz, lrsl-driller cartridge
349151a Add Codex-verified JSON data and update spec with recovered formulas
ac898e6 Add Unit 4 Lesson 1 source materials and content mapping spec
```

## Live Deliverable Links

- **Google Form**: https://docs.google.com/forms/d/e/1FAIpQLSdUtowoMwcb18djM5GM_kuiNhLSg-_GW5GihfLe9OUBf_aDUw/viewform?usp=header
- **Blooket**: https://dashboard.blooket.com/set/69baeaabd7770a6b4579a5ea
- **Driller**: https://lrsl-driller.vercel.app/platform/app.html?cartridge=a2t4l1-inverse-variation&mode=1

## Key Files

| File | Purpose |
|------|---------|
| `unit4_lesson1_verified.json` | Authoritative structured data — all formulas, mappings, strands |
| `unit4_lesson1_raw_extracts.json` | Raw text from all 6 source files |
| `spec_0401.md` | Human-readable spec (verified, matches JSON) |
| `deliverables/unit4_lesson1/blooket/unit4_lesson1_blooket_import.csv` | Blooket-compliant CSV (12 questions) |
| `deliverables/unit4_lesson1/blooket/images/` | 12 matplotlib PNGs for Blooket cards |
| `deliverables/unit4_lesson1/google-form/create_quiz.gs` | Apps Script auto-creates 5-question quiz |
| `deliverables/unit4_lesson1/google-form/images/` | 5 matplotlib PNGs for quiz questions |
| `generate_graphics.py` | Python script that generates all 17 images |

## Cartridge in lrsl-driller

| File | Purpose |
|------|---------|
| `cartridges/a2t4l1-inverse-variation/manifest.json` | 6 levels, progression tiers, hints |
| `cartridges/a2t4l1-inverse-variation/generator.js` | Shuffle-bag problem banks |
| `cartridges/a2t4l1-inverse-variation/grading-rules.js` | Numeric tolerance + partial credit |
| `cartridges/a2t4l1-inverse-variation/ai-grader-prompt.txt` | Wired in manifest (aiPromptFile) |
| `cartridges/registry.json` | Entry added (id: a2t4l1-inverse-variation, shortCode: IVAR) |

## Assessment Mapping Summary

**Core L1 anchors on Topic 4 Assessment**: TTB1, TTB5, TTB14
**Extension**: TTB16
**Not L1**: TTB2-4, TTB6-13, TTB15, TTB17-19 (available for L2-L5 mapping)

## Environment

- Platform: Windows 11, Git Bash
- Python: 3.12 (matplotlib 3.9.2, numpy 1.26.4, Pillow 10.4.0)
- Node: v22.19.0
- Repos: `C:\Users\ColsonR\algebra2` (GitHub: robjohncolson/algebra2), `C:\Users\ColsonR\lrsl-driller` (GitHub: robjohncolson/lrsl-driller)
- lrsl-driller frontend: Vercel (`lrsl-driller.vercel.app`)
- lrsl-driller API: Railway (`lrsl-driller-production.up.railway.app`)
