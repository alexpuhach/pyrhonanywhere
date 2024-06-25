# deploy.sh
cd /home/alexalexl/pyrhonanywhere
source myvenv/bin/activate
git pull origin main
pip install -r requirements.txt
python deploy.py

