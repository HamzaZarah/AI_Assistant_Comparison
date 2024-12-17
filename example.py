from flask import Flask, request, redirect, url_for, render_template_string, send_file, abort
import os
import werkzeug.utils
from werkzeug.exceptions import BadRequest
from werkzeug.security import safe_join

app = Flask(_name_)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit file size to 16 MB

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """
    Check if the file has an allowed extension and a secure filename.
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS and \
           werkzeug.utils.secure_filename(filename) == filename

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Ensure a file is provided in the request
        if 'file' not in request.files:
            return "No file part in the request", 400
        file = request.files['file']

        if file and allowed_file(file.filename):
            # Secure the filename
            filename = werkzeug.utils.secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                file.save(file_path)
                return redirect(url_for('upload_file'))
            except Exception as e:
                # Handle unexpected errors
                return f"File upload failed: {e}", 500
        else:
            return "Invalid file type or empty filename", 400

    # List files securely
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        files = [werkzeug.utils.secure_filename(file) for file in files]
    except Exception as e:
        files = []
    return render_template_string('''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <h2>Uploaded Files</h2>
    <ul>
    {% for file in files %}
      <li><a href="{{ url_for('download_file', filename=file) }}">{{ file }}</a></li>
    {% endfor %}
    </ul>
    ''', files=files)

@app.route('/download', methods=['GET'])
def download_file():
    # Get the filename from the query string
    filename = request.args.get('filename')
    if not filename:
        abort(400, description="Filename is required")

    # Ensure the filename is safe
    safe_filename = werkzeug.utils.secure_filename(filename)
    if not safe_filename:
        abort(400, description="Invalid filename")

    # Safely join the path to prevent directory traversal
    file_path = safe_join(app.config['UPLOAD_FOLDER'], safe_filename)
    if not os.path.exists(file_path):
        abort(404, description="File not found")

    try:
        return send_file(file_path, as_attachment=True)
    except Exception as e:
        abort(500, description=f"Failed to download file: {e}")

if _name_ == '_main_':
    # Do not use debug mode in production
    app.run(debug=False)
