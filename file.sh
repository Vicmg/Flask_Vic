cd /mi_env/script/activate

set FLASK_APP=main.py
set FLASK_DEBUG=1
set FLASK_ENV=development

gcloud auth login
gcloud init


flask run
