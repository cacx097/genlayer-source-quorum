# SourceQuorum — GenLayer Intelligent Contract

Repository: https://github.com/cacx097/genlayer-source-quorum

SourceQuorum is a GenLayer-native corroboration oracle for public web evidence. It evaluates one factual claim against two public HTTPS sources and asks validators to classify the evidence as independent support, circular support, conflict, or insufficient evidence.

## Why GenLayer

Counting links is not the same as corroboration. Two articles can repeat the same press release, filing, post, dataset, or report and still look like two independent sources. A conventional smart contract cannot reliably interpret attribution, provenance, contradictions, or semantic support.

SourceQuorum uses GenLayer web access, LLM reasoning, and the Equivalence Principle so validators can reach consensus on the meaning and provenance of public evidence.

## Contract

`contracts/source_quorum.py`

Constructor:

- `claim: str`
- `source_a: str` — required HTTPS URL
- `source_b: str` — required HTTPS URL

Write method:

- `evaluate()` — fetches both sources and stores a validator-backed assessment

View methods:

- `get_claim()`
- `get_sources()`
- `is_evaluated()`
- `get_last_assessment()`

## Closed verdict set

- `INDEPENDENT_SUPPORT`
- `CIRCULAR_SUPPORT`
- `CONFLICT`
- `INSUFFICIENT`

The prompt is intentionally conservative. Different domains or publishers are not treated as proof of independence. If source provenance cannot be established from the supplied evidence, the contract is instructed to return `INSUFFICIENT`.

## Safety

Fetched webpages are explicitly marked as untrusted evidence. Validators are told never to follow instructions, prompts, or commands embedded inside source content.

Both supplied source URLs must use HTTPS.

## Verification

Verified locally on Windows with Python 3.12:

- `genvm-lint check contracts/source_quorum.py` — PASS
- GenLayer contract validation — PASS
- source/structure tests — 7 PASS

Hosted GenLayer Studio end-to-end verification also succeeded.

Deployed contract: `0xbd6E0466a7bF7e58c2384DF0096A24E9b6CEAb8a`

Explorer evidence: https://explorer-studio.genlayer.com/address/0xbd6E0466a7bF7e58c2384DF0096A24E9b6CEAb8a

Runtime flow:

- deployment — accepted
- demo claim — near-surface dry air is about 78% nitrogen and 21% oxygen
- source A — NASA Earth Facts
- source B — Wikipedia, Atmosphere of Earth
- `evaluate()` — transaction accepted
- `get_last_assessment()` — returned a non-empty structured assessment
- returned verdict — `INDEPENDENT_SUPPORT`
- returned claim status — `SUPPORTED`
- response also included non-empty `PROVENANCE` and `EVIDENCE` sections

An earlier runtime attempt using NASA GRC was rejected by that website's server-side blocking of the GenLayer validator web request. The successful deployed instance therefore uses two fetchable public sources.

The `genlayer-test 0.29.2` Direct Mode loader currently hits a Windows temporary-file `WinError 32` before contract execution. Direct Mode tests remain in `tests/test_direct.py` and are skipped only on Windows so they can run on Linux/CI.

## Good uses

- verifying whether multiple reports really corroborate a market or protocol event
- detecting press-release or announcement echo chambers
- comparing governance or incident reports from independent parties
- checking whether multiple campaign/reward sources genuinely establish a claim
- reusable evidence validation inside agents, markets, registries, and dispute workflows

## Scope

This first version deliberately evaluates one claim per deployed contract with two sources. A later Project or Milestone can add source history, additional evidence, weighted source reputation, reusable claim registries, scheduled re-checks, and a frontend.
