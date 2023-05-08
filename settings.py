"""Simple Blog Settings"""

import os
from dotenv import load_dotenv

### DotENV #################################################################
load_dotenv()

# Application title name
APP_TITLE = os.getenv("APP_TITLE")

# Color Palette: #2C3333 #395B64 #A5C9CA #E7F6F2
# Color Hunt https://colorhunt.co/palette/2c3333395b64a5c9cae7f6f2

# Primary accent color for interactive elements.
# using by Streamlit Dashboard for Indico Software
PRIMARY_COLOR = os.getenv("PRIMARY_COLOR")

# Background color for the main content area.
BACKGROUND_COLOR = os.getenv("BACKGROUND_COLOR")

# Background color used for the sidebar and most interactive widgets.
# using by Blog Header Main Title Color
SECONDARY_BACKGROUND_COLOR = os.getenv("SECONDARY_BACKGROUND_COLOR")

# Color used for almost all text.
# using by Blog Header Main Title Background Color
TEXT_COLOR = os.getenv("TEXT_COLOR")
