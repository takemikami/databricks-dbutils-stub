import sys


def exit(value: str) -> None:
    """
    This method lets you exit a notebook with a value
    """
    sys.exit(value)


def run(path: str, timeoutSeconds: int, arguments: dict) -> str:
    """
    This method runs a notebook and returns its exit value
    """
    print("skip dbutils.notebook.run({},{},{})".format(path, timeoutSeconds, arguments))
    return ''
