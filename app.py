from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Narzędzia do automatyzacji budowy oprogramowania!\nVersion: 1.0.0 (test)"

@app.route('/deploy', methods=['POST'])
def deploy():
    if request.method == 'POST':
        # Запустіть ваш deploy.sh скрипт
        subprocess.call(['./deploy.sh'])
        return 'Deployed successfully', 200
    else:
        return 'Method not allowed', 405

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

