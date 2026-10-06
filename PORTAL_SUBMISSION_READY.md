# GenLayer Portal Submission — Draft

## Contribution type
Intelligent Contracts

## Title
SourceQuorum — Independent Source Corroboration Oracle

## Short description
A GenLayer Intelligent Contract that uses validator consensus to distinguish genuine independent corroboration from circular sourcing, conflicting reports, or insufficient evidence.

## Detailed description
SourceQuorum evaluates one factual claim against two public HTTPS sources. Validators fetch and interpret the source content, then return a closed verdict: INDEPENDENT_SUPPORT, CIRCULAR_SUPPORT, CONFLICT, or INSUFFICIENT.

The contract does not treat different domains as proof of independence. It looks for provenance, attribution, syndication, shared upstream evidence, material contradictions, and direct support for the claim. If independence cannot be established from the supplied evidence, it resolves conservatively to INSUFFICIENT.

This is GenLayer-native because it requires nondeterministic web access, semantic reasoning, and validator consensus through the Equivalence Principle. Fetched source text is explicitly treated as untrusted evidence so embedded instructions are not followed.

## Repository
https://github.com/cacx097/genlayer-source-quorum

## Contract address
0xbd6E0466a7bF7e58c2384DF0096A24E9b6CEAb8a

## Explorer evidence
https://explorer-studio.genlayer.com/address/0xbd6E0466a7bF7e58c2384DF0096A24E9b6CEAb8a

## Runtime verification
- Hosted Studio deployment: Accepted
- evaluate(): Transaction Accepted
- get_last_assessment(): non-empty structured assessment returned
- VERDICT: INDEPENDENT_SUPPORT
- CLAIM_STATUS: SUPPORTED

## Verified demo
Claim: Near Earth's surface, dry air is about 78% nitrogen and 21% oxygen.

Source A: https://science.nasa.gov/earth/facts/

Source B: https://en.wikipedia.org/wiki/Atmosphere_of_Earth
