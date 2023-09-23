import os
from flask import Flask, redirect, render_template, request, send_file
app = Flask(__name__)

@app.route("/")
def index():

    index_html = render_template('home.html')

    for file in list_files():
        index_html += "<a href=\"/files/" + file + "\"><button>" + file + "</button></a><br/>"

    return index_html

@app.route('/upload', methods = ['POST'])
def upload():

    file = request.files['form_file']  # item name must match name in HTML form
    file.save(os.path.join("./files", file.filename))

    return redirect("/") 

@app.route('/files/<filename>' )
def get_file(filename):

    return send_file('./files/'+filename)

def list_files():

    files = os.listdir("./files")
    jpegs = []

    for file in files:
        print("FIle: " + file )

        if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".JPEG"):
            jpegs.append(file)

    return jpegs

if __name__ == '__main__':
    app.run('0.0.0.0', port=8081)