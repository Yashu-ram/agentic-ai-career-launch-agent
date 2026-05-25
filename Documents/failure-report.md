Failure 1 — Invalid JSON Arrays

Problem:

model returned string instead of list

Fix:

output normalization
Failure 2 — Markdown Wrapped JSON

Problem:

```json

breaking parser

Fix:

markdown cleaning
Failure 3 — Schema Mismatch

Problem:

missing answer field

Fix:

synchronized prompt + schema