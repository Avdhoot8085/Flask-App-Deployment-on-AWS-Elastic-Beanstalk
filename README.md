# 🚀 Flask App Deployment on AWS Elastic Beanstalk (No CLI)

> **By Avdhoot Lad**  
> Deploy a Flask application to AWS Elastic Beanstalk using the AWS Console — no CLI required.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup & Configuration](#setup--configuration)
- [Deployment Steps](#deployment-steps)
- [How It Works](#how-it-works)
- [Monitoring & Logs](#monitoring--logs)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

This project demonstrates how to deploy a **Flask** web application on **AWS Elastic Beanstalk** entirely through the AWS Management Console — no EB CLI or AWS CLI needed.

The app runs behind **Gunicorn** (a production-grade WSGI server) on an **EC2** instance managed automatically by Elastic Beanstalk.

---

## Architecture

```
User (HTTPS) ──► AWS EC2 ──► Flask + Gunicorn Server
                    ▲
                    │  Managed Automatically
                    │
         ┌──────────────────────┐
         │  AWS Elastic Beanstalk│
         │  ┌────┬──────┬──────┐│
         │  │Auto│Monit-│ Logs ││
         │  │Scal│oring │      ││
         │  └────┴──────┴──────┘│
         └──────────────────────┘
```

| Component | Role |
|---|---|
| **Flask** | Python web framework handling routes and logic |
| **Gunicorn** | Production WSGI server serving the Flask app |
| **AWS EC2** | Virtual server running the app |
| **AWS Elastic Beanstalk** | Manages EC2, auto scaling, monitoring, and logs automatically |

---

## Prerequisites

- An **AWS account** with access to Elastic Beanstalk
- **Python 3.8+** installed locally
- Basic knowledge of Flask

---

## Project Structure

```
my-flask-app/
├── application.py        # Main Flask app (entry point must be named 'application')
├── requirements.txt      # Python dependencies
├── Procfile              # Tells Elastic Beanstalk to use Gunicorn
└── .ebextensions/        # (Optional) EB configuration files
    └── python.config
```

> ⚠️ **Important:** AWS Elastic Beanstalk expects the Flask app object to be named `application` inside `application.py`.

---

## Setup & Configuration

### 1. Flask Application (`application.py`)

```python
from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return '<h1>Hello from AWS Elastic Beanstalk!</h1>'

if __name__ == '__main__':
    application.run(debug=True)
```

### 2. Dependencies (`requirements.txt`)

```
Flask==2.3.3
gunicorn==21.2.0
```

### 3. Procfile

```
web: gunicorn --bind 0.0.0.0:8000 application:application
```

### 4. (Optional) EB Extensions (`.ebextensions/python.config`)

```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: application:application
```

---

## Deployment Steps

### Step 1 — Zip your project

Select all your project files (not the folder itself) and compress them into a `.zip` file.

```
application.py
requirements.txt
Procfile
.ebextensions/   ← include if present
```

### Step 2 — Open AWS Elastic Beanstalk Console

1. Log in to the [AWS Console](https://console.aws.amazon.com)
2. Search for **Elastic Beanstalk** and open it
3. Click **"Create Application"**

### Step 3 — Configure the Application

| Field | Value |
|---|---|
| Application name | `my-flask-app` (or any name) |
| Platform | **Python** |
| Platform branch | Python 3.x on 64-bit Amazon Linux 2 |
| Application code | Upload your `.zip` file |

### Step 4 — Create & Deploy

Click **"Create application"** and wait ~5 minutes. AWS will:

- Provision an EC2 instance
- Install Python and your dependencies
- Start Gunicorn to serve your Flask app
- Set up a health check endpoint

### Step 5 — Access Your App

Once the environment status turns **Green (Healthy)**, click the provided URL:

```
http://my-flask-app.eba-xxxxxxxx.us-east-1.elasticbeanstalk.com
```

---

## How It Works

1. **User** sends an HTTPS request to the app URL
2. **AWS EC2** instance receives the request
3. **Gunicorn** (WSGI server) passes it to your **Flask** application
4. Flask processes the request and returns a response
5. **Elastic Beanstalk** manages the EC2 instance automatically — handling health checks, restarts, scaling, and updates

---

## Monitoring & Logs

AWS Elastic Beanstalk provides built-in tools accessible from the console:

| Feature | Description |
|---|---|
| **Auto Scaling** | Automatically adds/removes EC2 instances based on traffic |
| **Monitoring** | CPU, network, and request metrics with CloudWatch |
| **Logs** | Download or view logs directly from the EB console |

To view logs:
> Elastic Beanstalk Console → Your Environment → **Logs** → Request Logs → Last 100 Lines

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Environment stuck in "Pending" | Check EC2 instance limits in your AWS region |
| 502 Bad Gateway | Verify `Procfile` exists and Gunicorn command is correct |
| App not loading | Ensure Flask app object is named `application` |
| Dependencies missing | Check `requirements.txt` is in the root of your zip |
| Health check failing | Add a `/` route that returns a `200` status |

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

*Crafted with ❤️ by Avdhoot Lad*
# Flask-App-Deployment-on-AWS-Elastic-Beanstalk
