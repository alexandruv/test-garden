# Test Garden

## Scope

A single page that says Hello from Test Garden

Created from the phone via Paseo intake. Previews: https://preview-main.test-garden.pages.dev

## Usage

Open `index.html` in a browser, or serve the repository locally:

```sh
python3 -m http.server 8000
```

Visit http://localhost:8000. The page needs no dependencies or build step.
Static hosting can serve `index.html` directly.

## Tests

Run the dependency-free tests with Python 3:

```sh
python3 -m unittest discover -s tests -v
```
