"""Small regression tests for information-preserving and fail-closed behavior."""

import unittest

from build_catalog import attach_links, bibtex, latex, split_cells


class ConversionTests(unittest.TestCase):
    def test_annotations_and_evidence_direction_survive(self):
        source = r"\TableSixFit{BGE\textsuperscript{t}\allowbreak{}(E\textsuperscript{T}\ensuremath{\rightarrow}[E\textsuperscript{T}, P\textsuperscript{V}])}"
        self.assertEqual(latex(source), "BGE^(t)(E^(T)→[E^(T), P^(V)])")
        self.assertEqual(latex(r"\MethodYes{}(18.9\%) / \MethodNo{} / --"), "✓(18.9%) / ✗ / --")

    def test_unknown_markup_fails_instead_of_losing_content(self):
        with self.assertRaises(ValueError):
            latex(r"Page \newannotation{uncertain}")

    def test_bibtex_nested_braces_accents_and_current_year(self):
        entry = bibtex(r"""@article{x,
          title={A {VQA} study}, author={Tito, Rub{\`e}n}, year={2023},
          journal={A \& B}, note={release {2022}}
        }""")["x"]
        self.assertEqual(entry["fields"], {"title": "A VQA study", "author": "Tito, Rubèn", "year": "2023", "journal": "A & B", "note": "release 2022"})

    def test_duplicate_bibliography_keys_are_rejected(self):
        entry = "@article{x,title={A},author={B},year={2024}}"
        with self.assertRaises(ValueError):
            bibtex(entry + entry)

    def test_literal_and_nested_ampersands_do_not_split_cells(self):
        self.assertEqual(split_cells(r"A \& B & \mbox{C & D} & E"), [r"A \& B", r"\mbox{C & D}", "E"])

    def test_provenance_cannot_override_bibliography_or_turn_search_into_paper(self):
        entries = bibtex("@article{x,title={Current title},author={Current author},year={2026}}")
        attach_links(entries, {"x": {"title": "Stale title", "year": "2025", "authorSourceUrl": "https://scholar.google.com/scholar?q=Stale"}})
        self.assertIsNone(entries["x"]["paper_url"])
        self.assertEqual(entries["x"]["fields"]["year"], "2026")
        self.assertIn("Current%20title", entries["x"]["scholar_search_url"])
        self.assertEqual(entries["x"]["link_provenance"]["kind"], "scholar_search")

    def test_explicit_arxiv_identifier_provides_a_paper_destination(self):
        entries = bibtex("@article{x,title={A},author={B},year={2024},journal={arXiv preprint arXiv:2411.01106}}")
        attach_links(entries, {})
        self.assertEqual(entries["x"]["paper_url"], "https://arxiv.org/abs/2411.01106")
        self.assertEqual(entries["x"]["link_provenance"]["source"], "references.bib:journal")


if __name__ == "__main__":
    unittest.main()
