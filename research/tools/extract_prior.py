#!/usr/bin/env python3
"""Extract readable text from a Google AI Studio chat export (makersuite prompt JSON).

Usage: python3 -I extract_prior.py <input.json> <output_dir>

Writes <output_dir>/<input_stem>.md containing every user prompt and every
non-thought model chunk, in order, headed "## [n] USER" / "## [n] MODEL".
Thought chunks (isThought true) are skipped. Code-execution chunks are kept
as fenced blocks; attachments (driveDocument/driveImage/inlineData/etc.) are
noted as "[attachment: ...]".
"""
import json
import os
import sys

ATTACH_KEYS = ("driveDocument", "driveImage", "driveVideo", "inlineData",
               "inlineImage", "fileData", "youtubeVideo")


def chunk_text(ch):
    if ch.get("text"):
        return ch["text"]
    parts = ch.get("parts") or []
    return "".join(p.get("text", "") for p in parts if not p.get("thought"))


def render_chunk(ch):
    out = []
    for k in ATTACH_KEYS:
        if k in ch:
            v = ch[k]
            desc = v.get("id") or v.get("fileUri") or v.get("mimeType") if isinstance(v, dict) else v
            out.append(f"[attachment: {k} {desc}]")
    txt = chunk_text(ch)
    if txt:
        out.append(txt)
    if "executableCode" in ch:
        ec = ch["executableCode"]
        out.append(f"[executableCode]\n```{ec.get('language', '').lower()}\n{ec.get('code', '')}\n```")
    if "codeExecutionResult" in ch:
        r = ch["codeExecutionResult"]
        out.append(f"[codeExecutionResult: {r.get('outcome', '')}]\n```\n{r.get('output', '')}\n```")
    if "errorMessage" in ch:
        out.append(f"[errorMessage: {ch['errorMessage']}]")
    return "\n\n".join(out)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, outdir = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        d = json.load(f)
    chunks = d.get("chunkedPrompt", {}).get("chunks", [])
    lines = [f"# {os.path.splitext(os.path.basename(src))[0]}",
             f"Source: {src} ({len(chunks)} chunks; thought chunks omitted)", ""]
    n = 0
    for ch in chunks:
        if ch.get("isThought"):
            continue
        body = render_chunk(ch)
        if not body.strip():
            continue
        n += 1
        lines.append(f"## [{n}] {ch.get('role', '?').upper()}")
        lines.append("")
        lines.append(body.rstrip())
        lines.append("")
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, os.path.splitext(os.path.basename(src))[0] + ".md")
    with open(dst, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"wrote {dst}: {n} sections")


if __name__ == "__main__":
    main()
