"""Render the stack block as an aligned monospace table, written into README.md."""
import re, textwrap

ROWS = [
 ("BACKEND",    "Python, FastAPI, Redis, PostgreSQL, Docker, CI/CD, load testing"),
 ("AI SYSTEMS", "LLM agents, multi-agent systems, agentic workflows, MCP servers, voice agents, RAG, retrieval pipelines, model fine-tuning, LLM evaluation"),
 ("ON-DEVICE",  "on-device LLMs, ONNX Runtime, model quantization, PyTorch"),
 ("LANGUAGES",  "Python, C++, TypeScript"),
 ("TOOLING",    "Playwright, Docker Compose, pytest"),
]

LW = max(len(k) for k, _ in ROWS) + 2      # label column
VW = 66                                    # value column

def line(l, m, r):
    return l + "─" * LW + m + "─" * (VW + 2) + r

out = [line("┌", "┬", "┐")]
for i, (label, vals) in enumerate(ROWS):
    wrapped = textwrap.wrap(vals, VW, break_on_hyphens=False, break_long_words=False)
    for j, w in enumerate(wrapped):
        lab = f" {label} " if j == 0 else " " * LW
        out.append(f"│{lab:<{LW}}│ {w:<{VW}} │")
    if i != len(ROWS) - 1:
        out.append(line("├", "┼", "┤"))
out.append(line("└", "┴", "┘"))
table = "```\n" + "\n".join(out) + "\n```"

src = open("README.md").read()
head = src[:src.index("![Stack](assets/hdr-stack.svg)")]
open("README.md", "w").write(head + "![Stack](assets/hdr-stack.svg)\n\n" + table + "\n")
print("\n".join(out))
