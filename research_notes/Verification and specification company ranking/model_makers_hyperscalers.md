# Model makers and hyperscalers as suppliers of, competitors to, and customers of verification companies

Research date: 12 November 2026 (position as of that date). WORK IN PROGRESS: this file is written progressively; sections below the first are being filled in.

Tag key: [PRIMARY] official document, paper or repository read directly; [INDEPENDENT] confirmed by an outside party; [COMPANY CLAIM] stated by the company and not confirmed by an outside party; [SECONDARY] press or analyst report only; [UNVERIFIED] could not be verified.

## 1. Google DeepMind and Google: AlphaProof Code, its predecessors, and Google's own chip-design verification

### Takeaway
(being drafted)

### Cited Findings

**AlphaProof Code (announced 10 November 2026): the line-count question**

- The technical paper (dated 2026-11-10, 57 pages, authors Swarat Chaudhuri, Andrew Ferraiuolo, Anton Kovsharov, Tej Chajed, Sam Schlesinger, Karn Seth, Jonathan Katz, Charles Sutton, Pushmeet Kohli; Google DeepMind and Google) states in its abstract: "our agents generated about 6.5 million lines of machine-checked Lean proof code, resting on about 26,000 lines of trusted specifications and AArch64 semantics." [PRIMARY] — [AlphaProof Code paper (PDF), 10 Nov 2026](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)
- Breakdown in section 7 of the paper ("Scale"): "The repository contains nearly 7 million lines of Lean, counting comments and blank lines. About 6.5 million of them are proofs: 5.3 million about the binary, which both security proofs share, about 860,000 for the computational proof and about 350,000 for the symbolic proof. Another 140,000 lines prove the reintroduced bugs (§6), and 70,000 verify the allocator. The verified libsignal code is about 560 KB, about 140,000 AArch64 instructions." [PRIMARY] — [AlphaProof Code paper (PDF), 10 Nov 2026](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)
- The DeepMind blog post as read on 12 Nov 2026 says agents "powered by Gemini Carbon did the proofs, generating over six million lines of Lean"; the page shows no update or correction note. [PRIMARY] — [Google DeepMind blog, "Introducing AlphaProof Code: a breakthrough in verifying complex software at depth", 10 Nov 2026](https://deepmind.google/blog/introducing-alphaproof-code/)

(more to follow)

### Inferences
(being drafted)

### Gaps
(being drafted)
