pyinstaller ^
  --onefile ^
  --name LeaseGenerator ^
  --add-data "app.py;." ^
  --collect-metadata streamlit ^
  launcher.py
pause