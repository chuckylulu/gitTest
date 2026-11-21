"""Rebuild readable title/authors/affiliations/abstract text from saved OpenAlex JSON records
(abstract_inverted_index -> linear text) and write it to sources/kla/_text/<stem>.txt,
replacing the raw JSON dump that fetch.py wrote. Input files are data; nothing is executed."""
import json, os, sys, glob
root = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'sources', 'kla')
for p in sorted(glob.glob(os.path.join(root, '*_openalex_abstract-*.json'))):
    m = json.load(open(p))
    ab = m.get('abstract_inverted_index') or {}
    pos = {}
    for w, idx in ab.items():
        for i in idx:
            pos[i] = w
    abstract = ' '.join(pos[i] for i in sorted(pos)) if pos else '[no abstract in OpenAlex record]'
    auths = []
    for a in m.get('authorships', []):
        aff = '; '.join(a.get('raw_affiliation_strings', []))
        auths.append(f"{a['author'].get('display_name','')} ({aff})")
    src = (m.get('primary_location') or {}).get('source') or {}
    out = [f"TITLE: {m.get('title')}", f"DOI: {m.get('doi')}", f"PUBLICATION DATE: {m.get('publication_date')}",
           f"VENUE: {src.get('display_name','')}", 'AUTHORS: ' + ' | '.join(auths), '', 'ABSTRACT:', abstract, '']
    tp = os.path.join(root, '_text', os.path.splitext(os.path.basename(p))[0] + '.txt')
    open(tp, 'w').write('\n'.join(out))
    print(os.path.basename(tp), len(abstract.split()), 'words')
