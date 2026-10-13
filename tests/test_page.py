"""Check the single page using only the Python standard library."""

from html.parser import HTMLParser
from pathlib import Path
import unittest


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.text = []
        self.declarations = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        if data.strip():
            self.text.append(data.strip())

    def handle_decl(self, decl):
        self.declarations.append(decl.lower())


class PageTests(unittest.TestCase):
    def setUp(self):
        source = Path(__file__).resolve().parents[1] / "index.html"
        self.page = PageParser()
        self.page.feed(source.read_text(encoding="utf-8"))

    def test_exact_greeting_and_no_extra_content(self):
        self.assertEqual(self.page.text, ["Test Garden", "Hello from Test Garden"])
        self.assertEqual(sum(tag == "h1" for tag, _ in self.page.tags), 1)
        self.assertIn(("main", {}), self.page.tags)

    def test_document_metadata(self):
        self.assertEqual(self.page.declarations, ["doctype html"])
        self.assertIn(("html", {"lang": "en"}), self.page.tags)
        self.assertIn(("meta", {"charset": "utf-8"}), self.page.tags)
        self.assertIn(
            ("meta", {"name": "viewport", "content": "width=device-width, initial-scale=1"}),
            self.page.tags,
        )


if __name__ == "__main__":
    unittest.main()
