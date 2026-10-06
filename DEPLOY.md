# Fast Hosted Studio Verification

## Contract file
C:\AI-Workspace\genlayer-source-quorum\contracts\source_quorum.py

## Demo constructor

claim:
Near Earth's surface, dry air is about 78% nitrogen and 21% oxygen.

source_a:
https://science.nasa.gov/earth/facts/

source_b:
https://www.noaa.gov/jetstream/atmosphere

source_c:
Leave empty.

## Why this demo
Both public pages directly state the atmospheric composition. NASA says Earth's near-surface atmosphere is 78% nitrogen and 21% oxygen. NOAA lists dry-atmosphere nitrogen at 78.084% and oxygen at 20.946%.

The contract is allowed to return any verdict in its closed set. Runtime verification succeeds if the transaction is accepted and get_last_assessment() returns a non-empty structured assessment; do not force a preferred verdict.

## Minimal verification path
1. Upload/import source_quorum.py into Hosted GenLayer Studio.
2. Deploy with the constructor values above.
3. Record the deployed contract address.
4. Call evaluate() using Send Transaction.
5. Confirm the transaction is accepted.
6. Call get_last_assessment() using Call Contract.
7. Confirm a non-empty response with VERDICT, CLAIM_STATUS, PROVENANCE, and EVIDENCE.
8. Save the GenLayer Explorer contract URL for Portal evidence.

## Pass condition
- deployment accepted
- evaluate() transaction accepted
- get_last_assessment() returns non-empty structured text
