# 🛡️ SafeSight - Professional Full-Stack Security Platform

## 📋 Project Overview
SafeSight is an enterprise-grade AI-powered security monitoring system that provides real-time threat detection and response capabilities. This project combines Django backend, TensorFlow ML model, and Next.js frontend into a cohesive, professional web application.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- TensorFlow 2.x
- Virtual Environment

### One-Click Launch (Windows)
```bash
# Run the comprehensive launcher
start_fullstack.bat
```

### Manual Launch
```bash
# 1. Activate Python environment
.\venv\Scripts\activate

# 2. Start Django backend (Terminal 1)
python manage.py runserver 8000

# 3. Start Next.js frontend (Terminal 2)
cd landing-page-for-security
npm run dev
```

## 🌐 Access Points

| Service | URL | Description |
|---------|------|-------------|
| 🏠 **Landing Page** | http://localhost:3000 | Professional marketing site |
| 📊 **Dashboard** | http://127.0.0.1:8000/ | Analytics & overview |
| 📹 **Live Feed** | http://127.0.0.1:8000/feed/ | Real-time monitoring |
| 🔐 **Login** | http://127.0.0.1:8000/auth/login | User authentication |
| ⚙️ **Admin** | http://127.0.0.1:8000/admin/ | Django admin panel |
| 🔮 **API** | http://127.0.0.1:8000/api/predict | ML prediction endpoint |

## 📁 Project Structure

```
CrowdGuard-AI/
├── 🤖 AI Model
│   └── model/fight_detection_model.h5    # TensorFlow model
├── � Django Backend
│   ├── core/                            # Main application
│   │   ├── views.py                    # API endpoints & views
│   │   ├── models.py                   # Database models
│   │   └── urls.py                     # URL routing
│   ├── app/                             # Templates & static
│   │   ├── templates/                  # Modern HTML templates
│   │   │   ├── base_safesight.html  # Professional base template
│   │   │   ├── dashboard.html        # Analytics dashboard
│   │   │   ├── feed_modern.html      # Advanced live feed
│   │   │   ├── login_modern.html      # Modern login page
│   │   │   └── register_modern.html   # Professional registration
│   │   └── static/
│   │       ├── css/safesight.css     # Design system
│   │       └── videos/                # Sample video feeds
│   └── cctvsite/                     # Django configuration
├── 🎨 Next.js Frontend
│   └── landing-page-for-security/      # Professional landing page
│       ├── components/landing/          # React components
│       ├── app/page.tsx               # Main landing page
│       └── styles/globals.css          # Tailwind styling
├── �️ Development Tools
│   ├── start_fullstack.bat             # Windows launcher
│   ├── start_fullstack.py             # Python launcher
│   └── .gitignore                    # Comprehensive ignore file
└── 📚 Documentation
    └── README_FULLSTACK.md            # Complete documentation
```

## 🎨 Design System

### Brand Identity
- **Name**: SafeSight
- **Logo**: 🛡️ Shield emoji
- **Primary Color**: `#0057D9` (Professional Blue)
- **Typography**: System font stack

### UI Components
- **Cards**: Rounded corners, subtle shadows
- **Buttons**: Multiple variants (primary, secondary, destructive)
- **Navigation**: Modern sidebar with icons
- **Forms**: Clean, accessible inputs
- **Status**: Color-coded badges and indicators

### Responsive Design
- **Mobile**: Hamburger menu, stacked layouts
- **Tablet**: Optimized grid systems
- **Desktop**: Full sidebar navigation

## 🤖 AI Model Integration

### Model Specifications
- **Type**: TensorFlow/Keras with Custom Attention Layer
- **Input**: Video frames (299x299 RGB)
- **Output**: Anomaly score (0-1)
- **Performance**: ~0.3s per frame

### API Usage
```python
import requests

# Analyze video frame
with open('frame.jpg', 'rb') as f:
    response = requests.post(
        'http://127.0.0.1:8000/api/predict',
        files={'video_frame': f}
    )
    result = response.json()
    anomaly_score = result['anomaly_score']
```

## � Features

### 🔐 Authentication System
- Modern login/register forms
- Session-based authentication
- Role-based access control
- Secure password handling

### 📹 Live Monitoring
- Real-time video feed display
- AI-powered threat detection
- Interactive controls (record, alarm, snapshot)
- Prediction score overlays

### 📈 Analytics Dashboard
- System statistics
- Active camera monitoring
- Incident tracking
- Performance metrics

### 🚨 Alert System
- Real-time alarm triggering
- Audio alert integration
- Visual notification system
- Guard acknowledgment

### 📱 Responsive Design
- Mobile-first approach
- Touch-friendly interfaces
- Adaptive layouts
- Progressive enhancement

## 🔧 Development

### Environment Setup
```bash
# Python virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Node.js dependencies
cd landing-page-for-security
npm install --legacy-peer-deps
```

### Database Management
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### Static Files
```bash
# Collect static files
python manage.py collectstatic
```

## � Security Features

### Application Security
- ✅ CSRF protection
- ✅ Session security
- ✅ Input validation
- ✅ SQL injection prevention
- ✅ XSS protection

### Model Security
- ✅ Custom model loading
- ✅ Input sanitization
- ✅ Error handling
- ✅ Resource cleanup

### Data Protection
- ✅ Encrypted sessions
- ✅ Secure headers
- ✅ Environment variables
- ✅ Access controls

## 📦 Dependencies

### Python (requirements.txt)
```
Django>=4.2
django-cors-headers>=4.0
Jinja2>=3.1
MarkupSafe>=2.1
tensorflow>=2.0.0
opencv-python>=4.0.0
numpy>=1.18.0
```

### Node.js (package.json)
```json
{
  "name": "safesight-landing",
  "version": "1.0.0",
  "dependencies": {
    "next": "16.1.6",
    "react": "19.2.3",
    "@radix-ui/*": "latest",
    "lucide-react": "^0.544.0",
    "tailwindcss": "^3.4.17"
  }
}
```

## � Deployment

### Production Setup
1. **Environment Variables**
   ```bash
   export DJANGO_SECRET_KEY='your-secret-key'
   export DEBUG=False
   export ALLOWED_HOSTS='yourdomain.com'
   ```

2. **Database Configuration**
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'safesight',
           'USER': 'user',
           'PASSWORD': 'password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. **Static File Serving**
   ```nginx
   location /static/ {
       alias /path/to/staticfiles/;
       expires 1y;
       add_header Cache-Control "public, immutable";
   }
   ```

4. **Process Management**
   ```bash
   # Gunicorn for Django
   gunicorn cctvsite.wsgi:application

   # PM2 for Next.js
   pm2 start npm --name "landing" -- start
   ```

## 🐛 Troubleshooting

### Common Issues

**Model Loading Error**
```bash
# Check model file exists
ls -la model/fight_detection_model.h5

# Verify TensorFlow installation
python -c "import tensorflow; print(tensorflow.__version__)"
```

**Port Conflicts**
```bash
# Find processes on ports 8000 and 3000
netstat -ano | findstr :8000
netstat -ano | findstr :3000

# Kill processes
taskkill /PID <PID> /F
```

**Dependency Issues**
```bash
# Reinstall Python dependencies
pip install -r requirements.txt --force-reinstall

# Clear Node.js cache
npm cache clean --force
npm install
```

### Debug Mode
```bash
# Django with verbose output
python manage.py runserver --verbosity=2

# Next.js with debug
NODE_ENV=development npm run dev
```

## 📞 Support

### Documentation
- 📖 **Full Documentation**: `README_FULLSTACK.md`
- 🔧 **API Reference**: Check `/api/` endpoints
- 🎨 **UI Guidelines**: Review `safesight.css`

### Getting Help
1. Check troubleshooting section
2. Review debug logs
3. Verify environment setup
4. Test individual components

---

## 🎯 Business Value

SafeSight provides enterprise-grade security monitoring with:
- **🤖 AI-Powered Detection**: Advanced threat recognition
- **📱 Modern Interface**: Professional user experience
- **📊 Business Intelligence**: Comprehensive analytics
- **🔒 Enterprise Security**: Robust protection measures
- **🚀 Scalable Architecture**: Production-ready deployment

**🛡️ SafeSight** - Making communities safer with AI-powered security!
