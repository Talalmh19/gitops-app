from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv('APP_VERSION', '1.0')

@app.route('/')
def hello():
    return f'''
    <html>
        <head><title>GitOps Demo</title></head>
        <body style="font-family: Arial; text-align: center; padding: 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
            <h1 style="color: white;">🚀 GitOps Pipeline is WORKING! 🚀</h1>
            <p style="font-size: 24px; color: white;">Version: {VERSION}</p>
            <p style="color: white;">Deployed via GitLab CI → Nexus → ArgoCD</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
