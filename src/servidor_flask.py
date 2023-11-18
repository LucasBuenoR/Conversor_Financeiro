from flask import Flask, render_template, send_file, url_for

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def download_arquivo():
    caminho_arquivo_json = '/historico_usuario_1.json'
    caminho_arquivo_zip = '/historico_usuario_1.zip'
    json_file = caminho_arquivo_json
    zip_file = caminho_arquivo_zip
    return render_template('download.html', json_file=json_file, zip_file=zip_file)


@app.route('/visualizar')
def visualizar_arquivo():
    caminho_arquivo_json = '/my_app/src/historico_usuario_1.json'
    with open(caminho_arquivo_json, 'r') as json_file:
        conteudo_json = json_file.read()
    return render_template('visualizar.html', json_file=caminho_arquivo_json, conteudo_json=conteudo_json)


@app.route('/download-json/<filename>')
def serve_json_file(filename):
    return send_file(filename, as_attachment=True)


@app.route('/download-zip/<filename>')
def serve_zip_file(filename):
    return send_file(filename, as_attachment=True, mimetype='application/zip')


if __name__ == '__main__':
    app.run(debug=True)
