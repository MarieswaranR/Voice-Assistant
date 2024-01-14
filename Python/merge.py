# main.py
import subprocess

proc1 = subprocess.Popen(['python', 'voice.py'])
proc2 = subprocess.Popen(['python', 'mongodb.py'])
proc3 = subprocess.Popen(['python', 'app.py'])

# Wait for the processes to finish
proc1.wait()
proc2.wait()
proc3.wait()
