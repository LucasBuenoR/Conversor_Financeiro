from flask import Flask, render_template, send_file, url_for

app = Flask(__name__)

@app.route('/')
def download_arquivo():
    caminho_arquivo = '/historico_usuario_1.json'
    json_file = caminho_arquivo
    #zip_file = "caminho_do_seu_arquivo_zip.zip" 
    return render_template('download.html', json_file=json_file) #, zip_file=zip_file)

@app.route('/download/<filename>')
def serve_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)