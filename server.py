import webview
from flask import Flask, render_template, send_from_directory
import markdown
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/md/<filename>')
def serve_md(filename):
    try:
        with open(f'md_files/{filename}', 'r', encoding='utf-8') as file:
            content = file.read()
        return markdown.markdown(content)
    except FileNotFoundError:
        return "File not found.", 404

@app.route('/files/<path:filename>')
def serve_files(filename):
    return send_from_directory('md_files', filename)

def run_flask():
    app.run(port=5000)

if __name__ == '__main__':
    # Запустите Flask в отдельном потоке
    threading.Thread(target=run_flask).start()

    # Откройте WebView
    webview.create_window('Markdown Viewer', 'http://127.0.0.1:5000')
    webview.start()