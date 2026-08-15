def test_skill_md_has_contract():
    t = open("skills/gaap-standards-qa/SKILL.md", encoding="utf-8").read()
    assert t.startswith("---") and "name: gaap-standards-qa" in t
    for kw in ["search_standards", "no relevant paragraph was found", "unofficial", "provenance"]:
        assert kw in t
