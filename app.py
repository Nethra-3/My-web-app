from flask import Flask, render_template
import platform
import datetime
import psutil

# ✅ 1️⃣ Create the Flask app
app = Flask(__name__)

# ✅ 2️⃣ Define a route
@app.route("/")
def home():
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    server_name = platform.node()
    os_name = f"{platform.system()} {platform.release()}"
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent

    return render_template(
        "index.html",
        uptime=uptime,
        server_name=server_name,
        os_name=os_name,
        cpu_percent=cpu_percent,
        ram_percent=ram_percent,
        disk_percent=disk_percent
    )

# ✅ 3️⃣ Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)