from typing import AsyncGenerator
import pathlib

print()
root = pathlib.Path(__file__).parent.resolve()

if __name__ == "__main__":
    readme = root / "README.md"
    
    rewritten = f"""
### Hi there 👋

    嘟咕嘟咕哒哒
    
    """

    readme.open("w",encoding="UTF-8").write(rewritten)
