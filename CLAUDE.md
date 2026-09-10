# GitHub profile README

This repo is `BHUVAN-RJ/BHUVAN-RJ`. Its `README.md` renders on the GitHub profile
page at github.com/BHUVAN-RJ.

## Audience

One reader: a technical recruiter or hiring manager who already has the resume and
is spending 30 seconds verifying the person is real. Optimise for fast scanning,
credibility, and answering screening questions before they get asked. Positioning is
backend and distributed systems.

## Hard rules

- Everything essential stays above the fold. GitHub collapses the profile README
  behind "show more" after roughly 5 to 6 lines.
- No em dashes, no en dashes, no arrows, no lone hyphens as punctuation. Use commas,
  colons, or periods. Date ranges read "Apr to Aug 2025".
- No badge walls, no shields.io grids, no typing-SVG, no profile-trophy, no visitor
  counter, no streak stats, no snake animation.
- No emoji in section headers, one or two in the whole document at most.
- Project descriptions say what the thing does. Tech stack goes in a short
  parenthetical at the end, if at all.
- Nothing invented. Every claim traces to `../context/linkedin.md` or
  `../context/portfolio.md`. If a detail is missing, ask rather than infer.
- Keep the rendered page under about 60 lines.

## Visual theme

The page uses a Matrix film treatment: pure black, `#00ff41` primary green,
`#008f11` for dim and trailing elements.

GitHub strips CSS from READMEs, so only images can carry the theme. Body text,
bullets, and bold runs stay native markdown, which keeps them selectable, ctrl-F
able, and able to reflow on mobile. The themed elements are the banner, the section
headers, and the buttons.

All assets are committed under `assets/` and served from this repo. Nothing is
fetched from a badge CDN or a shared Vercel instance. An earlier version used the
public github-readme-stats instance, which returned 503 and rendered both cards as
broken-image icons on the live profile. That is why self-hosting is not optional
here.

## Assets

| File | What it is |
| --- | --- |
| `assets/banner.gif` | Animated katakana digital rain, 1000x180, 30 frames at 90ms, name burned in |
| `assets/hdr-*.svg` | Section headers drawn as terminal prompts, `> HEADING` plus a cursor block |
| `assets/hdr-stack.svg` | Same, for the STACK block at the bottom |
| `assets/btn-*.svg` | Link buttons, square border with clipped corners and scanlines |

Every glyph in every asset is a real rectangle drawn from a hand-built 5x7 bitmap
font in `tools/pixelfont.py`. GitHub cannot load webfonts inside an SVG served
through its image proxy, so drawing the pixels is what makes the type render at all,
and it is also what gives the genuinely pixelated look.

## Regenerating

```bash
python3 tools/make_buttons.py    # assets/btn-*.svg
python3 tools/make_headers.py    # assets/hdr-*.svg
python3 tools/make_banner.py     # assets/banner.gif, needs Pillow
```

`make_banner.py` needs Pillow, which is not installable into the system Python on
this machine. Use a virtualenv:

```bash
python3 -m venv venv && ./venv/bin/pip install Pillow
./venv/bin/python tools/make_banner.py
```

To resize buttons or headers, change the `PX` pixel scale at the top of the relevant
script and rerun it. Everything else derives from it.

## Checkpoints

| Tag | State |
| --- | --- |
| `flat-buttons` | Plain dark buttons, no theme. Safe fallback if the Matrix look ever needs to go. |
| `matrix` | The current Matrix treatment. |

Roll back with `git reset --hard <tag> && git push --force origin main`.

## Stack block

The bottom of the README carries a two line stack block, backend on one line and AI
systems on the other, separated by `·`. It exists for keyword matching, nothing else,
so it sits below the evidence rather than above it.

Rule for what goes in it: only terms the user would defend in an interview. Every AI
term currently listed traces to shipped work, an MCP server on npm, voice agents, the
multi-agent research, on-device LLM work, fine-tuning, and evals. Two exceptions are
noted under open items.

## Set outside this repo

These cannot be committed and have to be done in the GitHub web UI:

- Pinned repositories, in this order: Project-Hydra,
  Preference-falsification-and-LLM-sycophancy, chrome-extension-testing-mcp,
  AudiTex, Self-Evolving-closed-loop-agent, Physics-Engine. Their descriptions are
  already set via `gh repo edit`.
- Profile sidebar at github.com/settings/profile: photo, bio, location, website,
  and the four social account slots.

Drafted copy for the GitHub bio, the LinkedIn headline, and the LinkedIn About
section lives in `../context/profile-copy.md`. Keep all three consistent with the
README, since a recruiter reads them within a minute of each other.

## Open items

- RAG and retrieval pipelines appear in the stack block on the user's instruction, but
  no public repo backs them. Either build or link evidence, or remove the two terms.
- Kubernetes, Kafka, AWS, GCP, gRPC, Terraform, and Go were deliberately left out,
  pending confirmation that the user has real depth in them.
- AudiTex still needs its homepage field pointed at the Chrome Web Store listing.
- The portfolio "Now" page at bhuvanrj.me is stale, dated March 2026, and describes
  the falsification research as a course project rather than first-author work.
- Commits in this repo carry a Claude co-author trailer, which conflicts with the
  user's standing preference to be sole author. Offered a history rewrite, awaiting a
  decision.
