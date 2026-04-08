import time
import random

def stream_logs():
    logs=[70,60,50,100,55,30,40,80,90,101,66,88,132]
    while true:
        yield random.choice(logs)
        time.sleep(1)

def filter_errors(log_streams):
    for log in log_streams: #
        if 100 < log:
            yield log

def alert(errors_logs):
    from playsound import playsound   # moved outside loop (better)
    for error in errors_logs:
        print("Error detected:", error)
        
        playsound("C:\Users\Guru\Downloads\audiofire Audio 2026-03-24 at 11.52.45 AM.mp3")  # ✅ raw string

logs = stream_logs()
error = filter_errors(logs)
alert(error)
    



