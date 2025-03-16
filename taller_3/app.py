from flask import Flask, request, render_template
from googletrans import Translator

# Inicializar la aplicación Flask
app = Flask(__name__)

# Crear un objeto Translator
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    # Obtener el texto del formulario
    text = request.form['text']
    target_language = request.form.get('language', 'en')  # Idioma objetivo por defecto: inglés (en)

    if not text:
        return render_template('index.html', error="No se proporcionó texto")

    # Traducir el texto
    translated = translator.translate(text, dest=target_language)
    translated_text = translated.text

    # Pasar los resultados a la plantilla
    return render_template('index.html', text=text, translated_text=translated_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
