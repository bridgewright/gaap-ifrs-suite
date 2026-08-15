from pathlib import Path


def test_public_repository_excludes_source_text_corpora():
    corpus_dir = Path("corpus")
    assert not list(corpus_dir.glob("*.jsonl.zst"))
    notice = (corpus_dir / "README.md").read_text(encoding="utf-8")
    assert "does not contain accounting-standard text" in notice
