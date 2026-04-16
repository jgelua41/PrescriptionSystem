# Configuration file for Prescription Automation System
import os

# Medical Center Details
MEDICAL_CENTER_NAME = "Bicutan Medical Center"
MEDICAL_CENTER_TAGLINE = "Your Health, Our Priority"
MEDICAL_CENTER_ADDRESS = "Bicutan Medical Center, M. L. Quezon Avenue, Taguig, Metro Manila, Philippines"

# Application Settings
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
PORT = int(os.environ.get('PORT', 5000))
HOST = os.environ.get('HOST', '0.0.0.0')

# PDF Settings
PAGE_SIZE = (8.5 * 72, 11 * 72)  # Letter size in points (8.5x11 inches)
MARGIN_TOP = 50
MARGIN_LEFT = 50
MARGIN_RIGHT = 50
MARGIN_BOTTOM = 50

# Font Settings
FONT_SIZE_TITLE = 24
FONT_SIZE_SUBTITLE = 11
FONT_SIZE_NORMAL = 10
FONT_SIZE_SMALL = 9
