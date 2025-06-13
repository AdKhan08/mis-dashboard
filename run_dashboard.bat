@echo off
set PYTHON_PATH=C:\Users\Asus\AppData\Local\Programs\Python\Python312
set PATH=%PYTHON_PATH%;%PYTHON_PATH%\Scripts;%PATH%
"%PYTHON_PATH%\python.exe" -m streamlit run app.py
pause 