# Kütüphaneler

from flask import Flask, render_template

# App oluşturma

app = Flask(__name__)

# Sunucu ayarları

host = "0.0.0.0"  # Herhangi bir IPden gelen isteklerini kabul etmemizi sağlar.
port = 5000


@app.route("/")  # http://ip:port/
def main():  # Ana sayfa fonksiyonunu oluşturur.
    return render_template(
        "index.html"
    )  # templates klasöründeki index.html'i başlatır.


if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)  # Web Server'i başlatır.
