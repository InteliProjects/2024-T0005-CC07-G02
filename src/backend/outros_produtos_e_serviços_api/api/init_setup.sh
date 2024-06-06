echo "[`date`]": "Start"
echo "[`date`]": "Creating virtual env"
python -m venv venv/

echo "[`date`]": "Activating virtual env"
# Windows
# venv/Scripts/activate
# Linux
source venv/bin/activate

echo "[`date`]": "Installing requirements"
pip install -r requirements.txt

echo "[`date`]": "Running app"
python app.py
echo "[`date`]": "End"