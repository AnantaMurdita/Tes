import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins,secs)
        print("sabar 1 menit doang")
        time.sleep(1)
        time_sec -= 1

# Contoh pemanggilan fungsi countdown
countdown(60) 
# Menghitung mundur selama 60 detik
