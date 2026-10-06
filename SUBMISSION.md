# GenLayer Builder submission draft

## Category
Intelligent Contracts

## Title
SourceQuorum — Independent Source Corroboration Oracle

## One-line description
A GenLayer Intelligent Contract that decides whether multiple public web sources independently corroborate a factual claim, repeat the same upstream source, conflict, or remain insufficient.

## Problem
Multiple URLs can create a false appearance of corroboration when articles merely repeat the same announcement, filing, dataset, post, or report. Link count alone cannot establish independent evidence, and a conventional smart contract cannot interpret semantic attribution or contradictions.

## Solution
SourceQuorum accepts one factual claim plus two public HTTPS sources. GenLayer validators fetch the sources and classify the evidence using a closed verdict set:

- INDEPENDENT_SUPPORT
- CIRCULAR_SUPPORT
- CONFLICT
- INSUFFICIENT

The contract is deliberately conservative: different domains are not enough to prove independence, and unclear provenance resolves to INSUFFICIENT.

## Why GenLayer
The contract depends on GenLayer-native capabilities:

- nondeterministic public web access
- LLM semantic reasoning over source content and provenance
- comparative validation through the Equivalence Principle
- validator consensus instead of a centralized evidence oracle

## Safety and robustness
Fetched webpages are treated as untrusted evidence. The prompt explicitly rejects instructions embedded in source content. Both required sources must use HTTPS.

## Verification
Completed:

- genvm-lint: PASS
- GenLayer contract validation: PASS
- source/structure tests: 7 PASS
- Hosted GenLayer Studio deployment: accepted
- evaluate(): transaction accepted
- get_last_assessment(): returned a non-empty structured assessment
- verdict: INDEPENDENT_SUPPORT
- claim status: SUPPORTED

## Public repository
https://github.com/cacx097/genlayer-source-quorum

## Deployment evidence
0xbd6E0466a7bF7e58c2384DF0096A24E9b6CEAb8a

Explorer: https://explorer-studio.genlayer.com/address/0xbd6E0466a7bF7e58c2384DF0096A24E9b6CEAb8a
