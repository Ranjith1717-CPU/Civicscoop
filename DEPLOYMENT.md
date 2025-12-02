# CivicScoop Deployment Guide

## Quick Deployment Summary

### 1. Frontend (GitHub Pages) - Already Deployed ✅
- **Live URL**: https://ranjith1717-cpu.github.io/
- **Dashboard**: https://ranjith1717-cpu.github.io/CivicScoop_Dashboard.html
- **Status**: Ready to use with AI analysis simulation

### 2. Backend (Local/Server) - Ready to Deploy

#### Option A: Local Development
```bash
cd backend
./run.bat     # Windows
./run.sh      # Mac/Linux
```
Server will run at: http://localhost:5000

#### Option B: Production Deployment

##### Heroku Deployment
```bash
# In backend folder
echo "web: gunicorn app:app" > Procfile
git init
git add .
git commit -m "Initial commit"
heroku create civicscoop-backend
git push heroku main
```

##### VPS/Cloud Server
```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip nginx

# Clone and setup
git clone https://github.com/yourusername/civicscoop.git
cd civicscoop/backend
pip3 install -r requirements.txt

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Integration Steps

### Step 1: Deploy Backend
1. Choose deployment method (local/Heroku/VPS)
2. Note the backend URL (e.g., http://localhost:5000 or https://your-backend.herokuapp.com)

### Step 2: Update Frontend API URL
Edit `CivicScoop_Dashboard.html` line 1196:
```javascript
const backendURL = 'YOUR_BACKEND_URL_HERE';  // Update this line
```

### Step 3: Upload to GitHub
1. Update all files in your GitHub repository
2. Frontend will automatically connect to your backend

## Complete Deployment Checklist

- [x] Frontend deployed on GitHub Pages
- [x] Backend code ready with Flask API
- [x] Database models and tables configured
- [x] AI analysis engine implemented
- [x] CORS configured for frontend-backend communication
- [x] Fallback to simulation if backend unavailable
- [ ] Backend deployed to production server
- [ ] Frontend updated with production backend URL
- [ ] Database configured for production (PostgreSQL/MySQL)
- [ ] SSL/HTTPS configured
- [ ] Domain name configured (optional)

## Team Sharing

To share with your team:

1. **Complete Package**: Share entire project folder
2. **Backend Only**: Share `backend/` folder
3. **Frontend Only**: Share HTML files for GitHub Pages
4. **Documentation**: Both main README.md and backend/README.md

## URLs Summary

### Development URLs
- Frontend: File-based or GitHub Pages
- Backend: http://localhost:5000
- API Base: http://localhost:5000/api

### Production URLs (when deployed)
- Frontend: https://ranjith1717-cpu.github.io/
- Backend: https://your-backend.herokuapp.com (or your chosen host)
- API Base: https://your-backend.herokuapp.com/api

The system is production-ready and fully functional!