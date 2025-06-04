from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', title="Beranda", message="Halo Selamat Datang Di flask! MUHAMAD IKBAR TIKANTO 1152800011", deskripsi="ini adalah tugas flask saya")
if __name__ == '__main__':
    app.run(debug=True)