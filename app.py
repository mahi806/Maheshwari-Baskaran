from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from ocr import im2txt

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      file_type = ((secure_filename(f.filename)).split('.'))[-1]
      file_name = 'tmp.'+file_type
      if 'jpg' == file_type or 'png' == file_type or 'jpeg' == file_type:
          f.save(file_name)
          try:
              text = im2txt(file_name)
          except:
            text = "Unsupported format file"
          return render_template('response.html',text_output=text)
      else:
          text = "Unsupported format file"
          return render_template('response.html',text_output=text)
		
if __name__ == '__main__':
   app.run()
