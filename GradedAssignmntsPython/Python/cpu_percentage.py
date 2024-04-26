from flask import Flask, render_template
import psutil
import threading
import time  # Import the time module

app = Flask(__name__)

def monitor_cpu(threshold):
    try:
        while True:
            cpu_percentage = psutil.cpu_percent(interval=1)
            if cpu_percentage > threshold:
                print("Alert: CPU usage exceeds threshold!")
            else:
                print(f"Current CPU usage: {cpu_percentage}%")
            app.config['cpu_percentage'] = cpu_percentage
            time.sleep(1)  # Add a sleep to avoid excessive CPU usage
    except KeyboardInterrupt:
        print("Monitoring stopped.")

@app.route('/')
def index():
    cpu_percentage = app.config.get('cpu_percentage', 0)
    return render_template('passwordstrength.html', message='', cpu_percentage=cpu_percentage)

if __name__ == '__main__':
    threshold = 80  # Set the CPU usage threshold (e.g., 80%)
    t = threading.Thread(target=monitor_cpu, args=(threshold,))
    t.start()
    app.run(debug=True)
