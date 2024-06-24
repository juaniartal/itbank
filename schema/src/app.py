from pkg.html import HtmlProcessor
from pkg.parser import Parser
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        htmlProcessor = HtmlProcessor()

        parser = Parser(target_json_file=sys.argv[1])
        try:
            parser.execute()
        except Exception as error:
            print("Failed to parse JSON")
            raise(error)

        htmlProcessor.crear_html(parser.cliente, parser.transacciones)
    else:
        print("Usage: python.exe app.py [JSON_FILE]")
