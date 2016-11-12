import os
from flask import Flask, make_response, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png','jpg','jpeg'])
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/uploadForm")
def form():
	return """
		<html>
			<body>
				<h1>Upload Images</h1>
				<form action="uploads" method="post" enctype="multipart/form-data">
					<input type="file" name="user_image" />
					<input type="submit" value="Upload" />
				</form>
			</body>
		</html>
	"""

@app.route("/uploads", methods=["POST"])
def upload_file():
	file = request.files['user_image']
	if not file: return "No file"
	if file.filename == '': return "No selected file"
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		return redirect(url_for('upload_file', filename=filename))
	
# @app.route("/uploads/<filename>")
# def uploaded_file(filename):
# 	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
