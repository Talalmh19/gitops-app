from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv('APP_VERSION', '1.0')

@app.route('/')
def hello():
    return f'''
    <html>
        <head><title>GitOps Demo</title></head>
	<body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1 style="color: #2196F3;">Hello from GitOps Pipeline!</h1>
            <p style="font-size: 20px;">Version: {VERSION}</p>
            <p>This app was deployed automatically via ArgoCD</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

