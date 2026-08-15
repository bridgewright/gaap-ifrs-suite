# Local Corpus Boundary

This directory intentionally does not contain accounting-standard text.

The retrieval service requires a local corpus built from source documents that the user is legally entitled to access and process. The repository provides provenance registries, ingestion code, schema validation, and synthetic test fixtures; it does not grant rights to download, reproduce, distribute, or commercialize any standard.

Expected local files are excluded by `.gitignore`:

```text
corpus/kifrs.jsonl.zst
corpus/kgaap.jsonl.zst
corpus/cas.jsonl.zst
corpus/vas.jsonl.zst
corpus/vectors/
```

`manifest.json` records the corpus used in the original local evaluation. It is provenance metadata, not bundled content. Before running an ingestion command, review [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) and the terms of the relevant publisher.

When no lawful corpus is present, the service must fail explicitly or use synthetic fixtures in tests. It must not fabricate citations.
