# Запуск браузера
import subprocess
import os

fileDir = os.path.dirname('__file__')
subprocess.run(os.path.join(fileDir, "chrome.exe"))
