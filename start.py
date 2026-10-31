from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
import webbrowser


def main():
    root = Path(__file__).resolve().parent
    handler = partial(SimpleHTTPRequestHandler, directory=str(root))
    server = None
    for port in range(8765, 8776):
        try:
            server = ThreadingHTTPServer(("127.0.0.1", port), handler)
            break
        except OSError:
            continue
    if server is None:
        raise SystemExit("Ports 8765-8775 are unavailable. Close another FMS window and retry.")
    url = f"http://127.0.0.1:{server.server_port}/"
    print(f"FMS: {url}")
    print("Press Ctrl+C to stop.")
    threading.Timer(0.7, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
