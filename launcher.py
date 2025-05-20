# launcher.py
import os
import sys
from streamlit.web import cli as stcli

if __name__ == "__main__":
    # when PyInstaller onefile, everything is unpacked to _MEIPASS
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.abspath(os.path.dirname(__file__))

    app_py = os.path.join(base, "app.py")

    sys.argv = [
        "streamlit", "run", app_py,
        "--server.headless", "true",
    ]
    sys.exit(stcli.main())
