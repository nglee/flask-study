.venv/Scripts/Activate.ps1
$env:FLASK_APP="microblog.py"
flask run --port 5001
$env:FLASK_APP=$null