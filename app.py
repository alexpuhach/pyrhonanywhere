from flask import Flask, request
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('USERNAME')

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Narzędzia do automatyzacji budowy oprogramowania!\nVersion: 1.0.1 (post webhook)"

@app.route('/deploy', methods=['POST'])
def deploy():
    if request.method == 'POST':
        subprocess.call([f'/home/{username}/pyrhonanywhere/deploy.sh'])
        return 'Deployed successfully', 200
    else:
        return 'Method not allowed', 405

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

