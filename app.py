from flask import Flask, request
from dotenv import load_dotenv
from subprocess import check_output
import os



def deploy_shell():
    stdout = check_output(['./deploy.sh']).decode('utf-8')
    return stdout

load_dotenv()

username = os.getenv('USERNAME')

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Narzędzia do automatyzacji budowy oprogramowania!\nVersion: 1.0.3 (post webhook 2)"

@app.route('/deploy', methods=['POST'])
def deploy():

    if request.method == 'POST':
        # subprocess.call([f'/home/{username}/pyrhonanywhere/deploy.sh']) #
        deploy_shell()
        app.logger.error(f'POST success')
        return 'Deployed successfully', 200
    else:
        return 'Method not allowed', 405

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

