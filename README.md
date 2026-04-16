# Prescription Automation System

A web-based prescription generation system for Bicutan Medical Center. This application allows healthcare providers to quickly create and download professional prescription PDFs.

## Features

- **Patient Information Form**: Capture patient name, address, age, and date
- **Multiple Medications**: Add multiple medications with instructions
- **Professional PDF Output**: Generates prescription PDFs in the standard format
- **Easy to Use**: Simple, intuitive web interface
- **Auto-Download**: Prescriptions automatically download to your computer

## Technology Stack

- **Backend**: Python Flask 2.3.0
- **PDF Generation**: ReportLab 4.0.9
- **Image Processing**: Pillow 10.0.0
- **Frontend**: HTML5, CSS3, JavaScript

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Installation & Setup

### Windows (Batch)
1. Navigate to the project folder
2. Double-click `run.bat`
3. Wait for dependencies to install
4. Open your browser to `http://127.0.0.1:5000`

### Windows (PowerShell)
1. Open PowerShell in the project folder
2. Run: `powershell -ExecutionPolicy Bypass -File run.ps1`
3. Wait for dependencies to install
4. Open your browser to `http://127.0.0.1:5000`

### Mac/Linux
1. Open Terminal in the project folder
2. Run: `chmod +x run.sh && ./run.sh`
3. Wait for dependencies to install
4. Open your browser to `http://127.0.0.1:5000`

## Manual Setup (Advanced)

If you prefer manual setup:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

## Usage

1. **Enter Patient Information**:
   - Patient Name (required)
   - Address
   - Age
   - Date

2. **Add Medications**:
   - Enter each medication with instructions
   - Example: "Amoxicillin 500mg - 3x daily for 7 days"
   - Each medication appears as a bullet point on the prescription
   - Add or remove medication fields as needed

3. **Generate Prescription**:
   - Click "Generate Prescription PDF"
   - The PDF will automatically download to your Downloads folder
   - Filename includes patient name and timestamp

## File Structure

```
PrescriptionAutomationSystem/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── run.bat               # Windows startup script
├── run.ps1               # PowerShell startup script
├── run.sh                # Mac/Linux startup script
├── README.md             # This file
├── templates/
│   └── index.html        # Main form page
└── static/
    └── css/
        └── style.css     # Styling
```

## Configuration

Edit `config.py` to customize:

- **Medical Center Details**: Name, tagline, address
- **PDF Settings**: Page size, margins
- **Font Settings**: Font sizes for different elements
- **Server Settings**: Host, port, debug mode

## Customization

### Change Medical Center Details
Edit `config.py`:
```python
MEDICAL_CENTER_NAME = "Your Center Name"
MEDICAL_CENTER_TAGLINE = "Your Tagline"
MEDICAL_CENTER_ADDRESS = "Your Address"
```

### Modify Prescription Template
Edit `app.py` in the `generate_prescription_pdf()` function to customize:
- Layout and spacing
- Font sizes and styles
- Additional fields (doctor name, license number, etc.)

### Update Styling
Edit `templates/index.html` and `static/css/style.css` to change:
- Colors and gradients
- Form layout
- Button styles
- Responsive behavior

## Troubleshooting

### Issue: "Python is not installed"
- Install Python 3.8+ from https://www.python.org
- Make sure to check "Add Python to PATH" during installation

### Issue: "Port 5000 already in use"
- Change the PORT in `config.py` to an available port (e.g., 5001)
- Or close the application currently using port 5000

### Issue: Dependencies not installing
- Make sure you have internet connection
- Try: `pip install --upgrade pip setuptools`
- Then: `pip install -r requirements.txt`

### Issue: Cannot download PDF
- Check your browser's download settings
- Make sure you have write permissions to your Downloads folder

## License

This application is for Bicutan Medical Center use.

## Support

For issues or feature requests, please contact the development team.
