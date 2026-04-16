from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime
import config
import os

app = Flask(__name__)
app.config['DEBUG'] = config.DEBUG

def generate_prescription_png(patient_name, address, age, date, medications, signature_line):
    """Generate a prescription PNG image"""
    
    # Create image (8.5x11 inches at 300 DPI)
    width = int(8.5 * 300)
    height = int(11 * 300)
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Set up margins and positions
    margin_top = int(0.35 * 300)  # 0.35 inches
    margin_left = int(0.35 * 300)
    margin_right = int(0.35 * 300)
    y = margin_top
    
    try:
        # Try to use a better font, fall back to default if not available
        # Use DejaVuSans which is available on Linux servers
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(40 * 300 / 72))
        subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", int(18 * 300 / 72))
        normal_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", int(16 * 300 / 72))
    except:
        # Fallback - try Windows fonts
        try:
            title_font = ImageFont.truetype("arial.ttf", int(40 * 300 / 72))
            subtitle_font = ImageFont.truetype("arial.ttf", int(18 * 300 / 72))
            normal_font = ImageFont.truetype("arial.ttf", int(16 * 300 / 72))
        except:
            # Last resort - use default font
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
            normal_font = ImageFont.load_default()
    
    # Add logo if it exists
    logo_path = os.path.join(os.path.dirname(__file__), 'static', 'css', 'logocircle.png')
    if os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path)
            logo.thumbnail((int(1.5 * 300), int(1.5 * 300)))  # 1.5 inch logo
            logo_x = width - margin_right - logo.width
            img.paste(logo, (logo_x, margin_top), logo if logo.mode == 'RGBA' else None)
        except Exception as e:
            print(f"Warning: Could not load logo: {e}")
    
    y += int(1.2 * 300)  # Add space after logo
    
    # Medical Center Name
    title_text = config.MEDICAL_CENTER_NAME
    bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = bbox[2] - bbox[0]
    draw.text(((width - title_width) // 2, y), title_text, fill='black', font=title_font)
    y += int(0.6 * 300)
    
    # Tagline
    tagline_text = config.MEDICAL_CENTER_TAGLINE
    bbox = draw.textbbox((0, 0), tagline_text, font=subtitle_font)
    tagline_width = bbox[2] - bbox[0]
    draw.text(((width - tagline_width) // 2, y), tagline_text, fill='black', font=subtitle_font)
    y += int(0.4 * 300)
    
    # Address
    address_text = config.MEDICAL_CENTER_ADDRESS
    bbox = draw.textbbox((0, 0), address_text, font=normal_font)
    address_width = bbox[2] - bbox[0]
    draw.text(((width - address_width) // 2, y), address_text, fill='black', font=normal_font)
    y += int(0.6 * 300)
    
    # Horizontal line
    line_y = y
    draw.line([(margin_left, line_y), (width - margin_right, line_y)], fill='black', width=2)
    y += int(0.3 * 300)
    
    # Patient Information
    y += int(0.2 * 300)
    
    # Patient Name - label and data with underline
    draw.text((margin_left, y), "Patient Name:", fill='black', font=normal_font)
    draw.text((margin_left + int(1.9 * 300), y), patient_name, fill='black', font=normal_font)
    y += int(0.4 * 300)
    # Underline for Patient Name
    draw.line([(margin_left + int(1.3 * 300), y), (width - margin_right - int(3.2 * 300), y)], fill='black', width=2)
    
    # Date - label and data with underline
    y -= int(0.4 * 300)
    draw.text((width - margin_right - int(2.2 * 300), y), "Date:", fill='black', font=normal_font)
    draw.text((width - margin_right - int(1.5 * 300), y), date, fill='black', font=normal_font)
    y += int(0.4 * 300)
    # Underline for Date
    draw.line([(width - margin_right - int(1.7 * 300), y), (width - margin_right, y)], fill='black', width=2)
    
    y += int(0.5 * 300)
    
    # Address - label and data with underline
    draw.text((margin_left, y), "Address:", fill='black', font=normal_font)
    draw.text((margin_left + int(1 * 300), y), address, fill='black', font=normal_font)
    y += int(0.4 * 300)
    # Underline for Address
    draw.line([(margin_left + int(1 * 300), y), (width - margin_right - int(3.2 * 300), y)], fill='black', width=2)
    
    # Age - label and data with underline
    y -= int(0.4 * 300)
    draw.text((width - margin_right - int(2.2 * 300), y), "Age:", fill='black', font=normal_font)
    draw.text((width - margin_right - int(1.5 * 300), y), age, fill='black', font=normal_font)
    y += int(0.4 * 300)
    # Underline for Age
    draw.line([(width - margin_right - int(1.8 * 300), y), (width - margin_right, y)], fill='black', width=2)
    
    y += int(0.7 * 300)
    
    # Rx Symbol (large)
    try:
        rx_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", int(72 * 300 / 72))
    except:
        try:
            rx_font = ImageFont.truetype("arial.ttf", int(72 * 300 / 72))
        except:
            rx_font = normal_font
    draw.text((margin_left, y), "Rx", fill='black', font=rx_font)
    y += int(1.3 * 300)
    
    # Medications Section
    if medications:
        for med in medications:
            if med.strip():
                # Bullet point
                draw.text((margin_left + int(0.25 * 300), y), "• " + med, fill='black', font=normal_font)
                y += int(0.35 * 300)
    
    y += int(0.5 * 300)
    
    # Signature line (centered on line)
    sig_y = height - int(1.5 * 300)
    sig_line_start = width - margin_right - int(3 * 300)
    sig_line_end = width - margin_right
    draw.line([(sig_line_start, sig_y), (sig_line_end, sig_y)], fill='black', width=2)
    
    # Center "Signature:" on the line
    sig_text = "Signature:"
    bbox = draw.textbbox((0, 0), sig_text, font=normal_font)
    sig_text_width = bbox[2] - bbox[0]
    sig_line_mid = (sig_line_start + sig_line_end) // 2
    sig_text_x = sig_line_mid - sig_text_width // 2
    draw.text((sig_text_x, sig_y + int(0.2 * 300)), sig_text, fill='black', font=normal_font)
    
    # Convert image to PNG
    png_buffer = BytesIO()
    img.save(png_buffer, format='PNG')
    png_buffer.seek(0)
    return png_buffer

@app.route('/')
def index():
    """Home page with prescription form"""
    return render_template('index.html')

@app.route('/preview', methods=['POST'])
def preview():
    """Preview prescription PNG"""
    try:
        # Get form data
        patient_name = request.form.get('patient_name', '')
        address = request.form.get('address', '')
        age = request.form.get('age', '')
        date = request.form.get('date', datetime.now().strftime('%m/%d/%Y'))
        
        # Get medications (from multiple fields)
        medications = []
        for key in request.form:
            if key.startswith('medication_'):
                med = request.form.get(key, '').strip()
                if med:
                    medications.append(med)
        
        # Generate PNG
        png = generate_prescription_png(patient_name, address, age, date, medications, "")
        
        return send_file(
            png,
            mimetype='image/png'
        )
    
    except Exception as e:
        return f"Error generating prescription: {str(e)}", 500

@app.route('/download', methods=['POST'])
def download():
    """Download prescription PNG"""
    try:
        # Get form data
        patient_name = request.form.get('patient_name', '')
        address = request.form.get('address', '')
        age = request.form.get('age', '')
        date = request.form.get('date', datetime.now().strftime('%m/%d/%Y'))
        
        # Get medications (from multiple fields)
        medications = []
        for key in request.form:
            if key.startswith('medication_'):
                med = request.form.get(key, '').strip()
                if med:
                    medications.append(med)
        
        # Generate PNG
        png = generate_prescription_png(patient_name, address, age, date, medications, "")
        
        # Create filename
        filename = f"Prescription_{patient_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        
        return send_file(
            png,
            mimetype='image/png',
            as_attachment=True,
            download_name=filename
        )
    
    except Exception as e:
        return f"Error generating prescription: {str(e)}", 500

@app.route('/generate', methods=['POST'])
def generate():
    """Generate prescription PNG"""
    try:
        # Get form data
        patient_name = request.form.get('patient_name', '')
        address = request.form.get('address', '')
        age = request.form.get('age', '')
        date = request.form.get('date', datetime.now().strftime('%m/%d/%Y'))
        
        # Get medications (from multiple fields)
        medications = []
        for key in request.form:
            if key.startswith('medication_'):
                med = request.form.get(key, '').strip()
                if med:
                    medications.append(med)
        
        # Generate PNG
        png = generate_prescription_png(patient_name, address, age, date, medications, "")
        
        # Create filename
        filename = f"Prescription_{patient_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        
        return send_file(
            png,
            mimetype='image/png',
            as_attachment=True,
            download_name=filename
        )
    
    except Exception as e:
        return f"Error generating prescription: {str(e)}", 500

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
