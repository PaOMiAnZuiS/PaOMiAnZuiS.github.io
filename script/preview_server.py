#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse
import html
import mimetypes
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
CSS_FALLBACK = ROOT / "_site" / "assets" / "css" / "style.css"


def strip_front_matter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].lstrip("\n")
    return text


def inline_markdown(text):
    links = []

    def store_link(match):
        token = f"@@PMGG_LINK_{len(links)}@@"
        label = match.group(1)
        href = html.escape(match.group(2), quote=True)
        links.append((token, f'<a href="{href}">{label}</a>'))
        return token

    text = re.sub(r"\[([^\]]+)\]\(([^\)]+)\)", store_link, text)
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    for token, value in links:
        text = text.replace(token, value)
    return text


def render_markdown(text):
    text = strip_front_matter(text)
    out = []
    paragraph = []
    list_mode = None

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            out.append("<p>" + inline_markdown(" ".join(paragraph).strip()) + "</p>")
            paragraph = []

    def close_list():
        nonlocal list_mode
        if list_mode:
            out.append(f"</{list_mode}>")
            list_mode = None

    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            close_list()
            continue

        if stripped.startswith("<") and stripped.endswith(">"):
            flush_paragraph()
            close_list()
            out.append(stripped)
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline_markdown(heading.group(2))}</h{level}>")
            continue

        unordered = re.match(r"^[-*]\s+(.*)$", stripped)
        ordered = re.match(r"^\d+\.\s+(.*)$", stripped)
        if unordered or ordered:
            flush_paragraph()
            tag = "ul" if unordered else "ol"
            item = unordered.group(1) if unordered else ordered.group(1)
            if list_mode != tag:
                close_list()
                out.append(f"<{tag}>")
                list_mode = tag
            out.append(f"<li>{inline_markdown(item)}</li>")
            continue

        paragraph.append(stripped)

    flush_paragraph()
    close_list()
    return "\n".join(out)


def page_template(body, title="PMGG's Blog"):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)}</title>
    <link rel="stylesheet" href="/assets/css/style.css">
    <link rel="stylesheet" href="/assets/css/pmgg.css">
  </head>
  <body>
    <div class="site-backdrop" aria-hidden="true"></div>
    <header class="site-header">
      <div class="container">
        <div class="header-inner">
          <a id="a-title" class="brand-link" href="/">
            <h1>PMGG's Blog</h1>
          </a>
          <nav class="top-nav" aria-label="主要导航">
            <a href="/#ai-notes">AI札记</a>
            <a href="/#knowledge-map">知识地图</a>
            <a href="/welcome-page.html">关于</a>
          </nav>
        </div>
        <h2>Build, test, think, and learn with AI.</h2>
      </div>
    </header>
    <main class="container site-main">
      <section id="main_content">
{body}
      </section>
    </main>
  </body>
</html>"""


def markdown_path_for(request_path):
    path = unquote(urlparse(request_path).path)
    if path in ("", "/"):
        return ROOT / "index.md"
    rel = path.lstrip("/")
    if rel.endswith(".html"):
        rel = rel[:-5] + ".md"
    return (ROOT / rel).resolve()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        request_path = unquote(urlparse(self.path).path)

        if request_path == "/assets/css/style.css" and CSS_FALLBACK.exists():
            self.send_file(CSS_FALLBACK, "text/css; charset=utf-8")
            return

        static = (ROOT / request_path.lstrip("/")).resolve()
        if str(static).startswith(str(ROOT)) and static.is_file() and static.suffix != ".md":
            content_type = mimetypes.guess_type(str(static))[0] or "application/octet-stream"
            self.send_file(static, content_type)
            return

        markdown_path = markdown_path_for(request_path)
        if (
            str(markdown_path).startswith(str(ROOT))
            and markdown_path.exists()
            and markdown_path.suffix == ".md"
        ):
            text = markdown_path.read_text(encoding="utf-8")
            body = render_markdown(text)
            clean_text = strip_front_matter(text)
            title_match = re.search(r"^#\s+(.+)$", clean_text, re.M)
            title = re.sub(r"<[^>]*>", "", title_match.group(1)) if title_match else "PMGG's Blog"
            data = page_template(body, title).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Not found")

    def send_file(self, path, content_type):
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        print(f"{self.address_string()} - {fmt % args}", flush=True)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Serving preview at http://127.0.0.1:{PORT}", flush=True)
    server.serve_forever()
