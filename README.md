# System Monitor web application
A simple Python Flask web application that displays **real-time server status** including OS details, CPU usage, memory usage, and disk usage.  
It is deployed in a **production-ready environment** using **Gunicorn** as a WSGI server and **Nginx** as a reverse proxy.

#Tech Stack
- **Python 3**
- **Flask** — Web framework
- **psutil** — For fetching system details
- **Gunicorn** — WSGI HTTP server for running Flask in production
- **Nginx** — Reverse proxy to handle HTTP requests and serve the app
- **Ubuntu Server** (AWS EC2)

- ## ⚙️ Features

✅ Shows:
- Operating System information (system, node name, release, version, machine, processor)
- CPU usage percentage
- RAM usage percentage
- Disk usage percentage

✅ Runs locally with Flask or in production with Gunicorn & Nginx  
✅ Lightweight & easy to deploy on any Linux server

## 📂 Project Structure

server_info_app/
│
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
├── .gitignore
└── README.md

1. Clone the repository : git clone (URL)
2. Create the virtual environment - python3 -m venv venv , source /venv/bin/activate
3. Install dependencies - pip install -r requirements.txt
4. Run with flask - python3 app.py

Run in production:
1. Start Gunicorn: gunicorn --bind 127.0.0.1:5000 app:app
2. Configure Nginx: Point nginx to proxy requests to Gunicorn
3. Reload nginx: sudo nginx -t , sudo systemctl restart nginx
4. Visit your server IP in browser and you would see the output/results of your web server status
