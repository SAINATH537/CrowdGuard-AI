#  Neural Nexus Dashboard

> AI-Powered Real-Time Surveillance & Security Intelligence Platform

Neural Nexus Dashboard is a production-grade security and surveillance web application that leverages existing CCTV infrastructure, machine learning, and real-time analytics to detect violent activity and manage emergency broadcasts across distributed locations.

The system provides live monitoring, anomaly detection, historical logging, advanced analytics, and secure role-based access control — enabling rapid incident response and operational efficiency.

---

#  Core Features

##  Real-Time Fight Detection
- Processes live CCTV streams using a custom ML model with AttentionLayer
- Real-time classification: Fight vs No Fight
- Low-latency prediction pipeline

##  Live Feed Monitoring
- Multi-camera live feed display
- Overlayed ML predictions
- Authenticated user access only

##  Historical Event Logging
- Stores anomaly events and alarm history
- Timestamped records
- Duration tracking
- Action audit logs

##  Analytics Dashboard
- Built with Chart.js
- Anomaly distribution charts
- Trend analysis over time
- Alarm duration insights

##  Voice Broadcast
- Browser-based microphone recording
- Room-specific audio broadcast
- Admin-only access

##  Text Broadcast
- Real-time text alerts
- Multi-location distribution
- Admin-controlled messaging

##  Role-Based Access Control
- Authenticated user access for feeds
- Admin-only broadcast & data management
- Secure session management

##  Rate Limiting
- API and route rate limiting to prevent abuse
- Configurable request thresholds

##  Modular Architecture
- Organized into Django apps:
  - feed
  - broadcast
  - history
  - analytics
  - authentication
  - ml_model

---

#  Production Setup Guide

## 1️ Clone Repository

```bash
git clone https://github.com/yourusername/neural-nexus-dashboard.git
cd neural-nexus-dashboard
```

## 2️ Create Virtual Environment

### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

## 3️ Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4️ Environment Configuration

Create a `.env` file in the root directory:

```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,localhost,127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/neural_nexus
```

 Never commit `.env` to version control.

## 5️ Database Setup (PostgreSQL Recommended)

Create database:

```bash
createdb neural_nexus
```

Run migrations:

```bash
python manage.py migrate
```

Create admin user:

```bash
python manage.py createsuperuser
```

## 6️ Collect Static Files

```bash
python manage.py collectstatic
```

---

#  Production Deployment

## Recommended Stack
- Gunicorn (WSGI server)
- Nginx (Reverse proxy)
- PostgreSQL (Database)
- Redis (Caching & rate limiting)
- HTTPS via Let's Encrypt

## Install Gunicorn

```bash
pip install gunicorn
```

Run:

```bash
gunicorn neural_nexus.wsgi:application --bind 0.0.0.0:8000
```

## Example Nginx Configuration

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location /static/ {
        alias /path/to/staticfiles/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

#  Machine Learning Model Deployment

Place trained model file in:

```
ml_model/fight_model.h5
```

Ensure:
- TensorFlow version matches training environment
- GPU support configured if required
- Model loads at application startup for reduced latency

---

# 🛠 Management Commands

Seed sample data:

```bash
python manage.py seed_data
```

Clear anomalies:

```bash
python manage.py clear_anomalies
```

---

#  Project Structure

```
neural_nexus/
│
├── manage.py
├── requirements.txt
├── .env
├── neural_nexus/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── feed/
├── broadcast/
├── history/
├── analytics/
├── authentication/
└── ml_model/
```

---

#  Running Tests

```bash
python manage.py test
```

---

#  Security Best Practices

- Set DEBUG=False
- Use strong SECRET_KEY
- Enforce HTTPS
- Configure secure cookies
- Enable CSRF protection
- Use environment variables for secrets
- Enable logging & monitoring
- Keep dependencies updated

---

#  License

MIT License

---

#  Disclaimer

This system is intended for lawful surveillance and security purposes only. Ensure compliance with local data protection and privacy regulations before deployment.
