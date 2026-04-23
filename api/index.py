import os
import sys

# Add the parent directory to the path so we can import modules if needed
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from streamlit.web.cli import main

if __name__ == "__main__":
    # Point Streamlit to the actual app.py in the root
    sys.argv = [
        "streamlit",
        "run",
        os.path.join(os.path.dirname(__file__), "..", "app.py"),
        "--server.port=8501",
        "--server.address=0.0.0.0",
    ]
    sys.exit(main())
