from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para descargar tu CV en PDF (cuando lo subas a GitHub)
@app.route('/descargar-cv')
def descargar_cv():
    # Aquí asumimos que subirás tu CV a la carpeta principal con este nombre
    ruta_cv = os.path.join(app.root_path, 'CV_CruzCd_Desarrollador.pdf')
    if os.path.exists(ruta_cv):
        return send_file(ruta_cv, as_attachment=True)
    return "El CV aún no está subido.", 404

if __name__ == '__main__':
    app.run(debug=True)