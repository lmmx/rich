import time
from rich.console import Console
from rich.style import Style
from rich.highlighter import RegexHighlighter


class RequestHighlighter(RegexHighlighter):
    base_style = "req."
    highlights = [
        r"^(?P<protocol>\w+) (?P<method>\w+) (?P<path>\S+) (?P<result>\w+) (?P<stats>\[.+\])$",
        r"\/(?P<filename>\w+\..{3,4})",
    ]


console = Console()
console.push_styles(
    {
        "req.protocol": Style.parse("dim bold green"),
        "req.method": Style.parse("bold cyan"),
        "req.path": Style.parse("magenta"),
        "req.filename": Style.parse("bright_magenta"),
        "req.result": Style.parse("yellow"),
        "req.stats": Style.parse("dim"),
    }
)

console.log("Server starting...")
console.log("Serving on http://127.0.0.1:8000", highlight=None)

time.sleep(1)

console.log(
    "HTTP GET /foo/bar/baz/egg.html 200 [0.57, 127.0.0.1:59076]",
    highlight=RequestHighlighter(),
)

console.log(
    "HTTP GET /foo/bar/baz/background.jpg 200 [0.57, 127.0.0.1:59076]",
    highlight=RequestHighlighter(),
)


time.sleep(1)


def test_locals():
    foo = (1, 2, 3)
    movies = ["Deadpool", "Rise of the Skywalker"]
    console = Console()

    console.log(
        "JSON RPC batch",
        [
            {"jsonrpc": "2.0", "method": "sum", "params": [1, 2, 4], "id": "1"},
            {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
            {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
            {"foo": "boo"},
            {
                "jsonrpc": "2.0",
                "method": "foo.get",
                "params": {"name": "myself", "enable": False, "grommits": None},
                "id": "5",
            },
            {"jsonrpc": "2.0", "method": "get_data", "id": "9"},
        ],
        log_locals=True,
    )


test_locals()