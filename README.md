# 🎓 Academic Mentorship Workflow using LangGraph

A sophisticated AI-powered academic guidance system that uses sequential agent collaboration to provide comprehensive research planning, analysis, and resource mapping for academic projects.

## 🌟 Features

### **Four-Agent Sequential Workflow:**
1. **🎯 Scoping Agent** - Refines topics into focused research questions
2. **📊 Analyst Agent** - Provides methodology and risk assessment  
3. **📚 Resource Mapper** - Creates learning plans with skills and resources
4. **🗓️ Planner Agent** - Develops structured timelines and success criteria

### **Dual AI Model Support:**
- **OpenAI** - GPT-4o-mini and GPT-4 models
- **Google Gemini** - Gemini 2.0 Flash model

### **Professional Web Interface:**
- **Dark Mode Theme** - Modern, sophisticated UI
- **Responsive Design** - Works on desktop and mobile
- **Interactive Cards** - Collapsible sections with animations
- **Professional Tables** - Clean HTML formatting for resources
- **Real-time Processing** - Live agent collaboration

## 🚀 Quick Start

### Option 1: Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/Em-Deesha/Academic-Mentorship-workflow-using-Langraph.git
cd Academic-Mentorship-workflow-using-Langraph

# Set up your API keys in .env file
echo "OPENAI_API_KEY=your_openai_key_here" > .env
echo "GEMINI_API_KEY=your_gemini_key_here" >> .env

# Run with Docker
./run-docker.sh
```

### Option 2: Local Python
```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENAI_API_KEY=your_key_here
export GEMINI_API_KEY=your_key_here

# Run application
python3 app.py
```

## 🌐 Access Application
- **URL**: http://localhost:8080
- **Features**: Both OpenAI and Gemini workflows
- **UI**: Professional dark mode with responsive design

## 📋 What You Get

### **Enhanced Agent Outputs:**

#### **Agent 1 - Research Scope:**
- Clear research question
- 3-4 specific objectives
- Scope and limitations
- Expected results
- Why it's important

#### **Agent 2 - Analyst Report:**
- Research methodology
- Key metrics with targets
- Baseline vs stretch goals
- Risk assessment and solutions

#### **Agent 3 - Resource Map:**
- **Professional HTML table** with skills and resources
- 6-8 essential skills
- Specific courses/books for each skill
- Skill levels (Beginner/Intermediate/Advanced)
- Why each skill matters

#### **Agent 4 - Final Report:**
- Success criteria
- 30-day goals
- 60-day goals
- 90-day goals

## 🎯 Sample Questions to Try

- "I want to research machine learning in healthcare"
- "How can I study voice model integration in AI agents?"
- "I'm interested in blockchain technology for supply chains"
- "I want to explore quantum computing applications"
- "I want to research renewable energy technologies"

## 🛠️ Technical Stack

### **Backend:**
- **LangGraph** - Agent orchestration framework
- **LangChain** - LLM integration and tools
- **Flask** - Web framework
- **Python 3.11+** - Core language

### **Frontend:**
- **HTML5/CSS3** - Modern web standards
- **JavaScript** - Interactive functionality
- **Responsive Design** - Mobile-first approach
- **Dark Mode** - Professional UI theme

### **AI Models:**
- **OpenAI** - GPT-4o-mini, GPT-4
- **Google Gemini** - Gemini 2.0 Flash

### **Deployment:**
- **Docker** - Containerized deployment
- **Docker Compose** - Easy orchestration
- **Gunicorn** - Production WSGI server

## 📁 Project Structure

```
Academic-Mentorship-workflow-using-Langraph/
├── app.py                          # Flask web application
├── mentorship_workflow.py          # OpenAI workflow
├── gemini_mentorship_workflow.py  # Gemini workflow
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker configuration
├── docker-compose.yml            # Docker orchestration
├── run-docker.sh                 # Automated setup script
├── templates/
│   └── index.html                # Main web interface
├── static/
│   ├── style.css                 # Dark mode styling
│   └── script.js                 # Interactive functionality
├── logs/                         # Application logs
├── .env                          # API keys (create this)
├── .gitignore                    # Git ignore rules
├── README.md                     # This file
├── README-Docker.md              # Docker documentation
└── quick-start.md                # Quick start guide
```

## 🔧 Configuration

### **Environment Variables:**
```bash
# Required API Keys
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here

# Optional Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
```

### **API Key Setup:**
1. **OpenAI**: Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. **Gemini**: Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

## 🐳 Docker Deployment

### **Automated Setup:**
```bash
# One-command setup
./run-docker.sh
```

### **Manual Docker Commands:**
```bash
# Build and start
docker-compose up --build

# Run in background
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop application
docker-compose down
```

## 🔍 Troubleshooting

### **Common Issues:**

1. **API Key Problems:**
   ```bash
   # Check if keys are set
   cat .env
   
   # Test API keys
   python3 -c "import os; print('OpenAI:', bool(os.getenv('OPENAI_API_KEY')))"
   ```

2. **Docker Issues:**
   ```bash
   # Check Docker status
   docker --version
   docker-compose --version
   
   # Fix permissions (Linux)
   sudo usermod -aG docker $USER
   ```

3. **Port Conflicts:**
   ```bash
   # Check if port 8080 is free
   netstat -tulpn | grep 8080
   
   # Use different port in docker-compose.yml
   ports: - "8081:8080"
   ```

## 📊 Performance

### **Response Times:**
- **OpenAI GPT-4o-mini**: ~10-15 seconds
- **Google Gemini 2.0 Flash**: ~8-12 seconds
- **Total Workflow**: ~30-60 seconds

### **Resource Usage:**
- **Memory**: ~200-400MB
- **CPU**: Low usage during processing
- **Storage**: ~100MB for application

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangGraph** - For the powerful agent orchestration framework
- **LangChain** - For seamless LLM integration
- **OpenAI** - For providing advanced language models
- **Google** - For the Gemini AI model
- **Flask** - For the lightweight web framework

## 📞 Support

If you encounter any issues:

1. Check the [troubleshooting section](#troubleshooting)
2. View application logs: `docker-compose logs -f`
3. Verify your API keys are correct
4. Ensure Docker is running properly

## 🎉 Features Showcase

### **Professional UI:**
- ✅ **Dark Mode Theme** - Modern, sophisticated design
- ✅ **Responsive Layout** - Works on all devices
- ✅ **Interactive Cards** - Collapsible sections
- ✅ **Smooth Animations** - Fade-in and slide-up effects

### **Enhanced Agent Outputs:**
- ✅ **Concise Content** - Clear, actionable information
- ✅ **Professional Tables** - HTML formatting for resources
- ✅ **Structured Data** - Organized, easy-to-read format
- ✅ **Mobile-Friendly** - Horizontal scroll for tables

### **Production Ready:**
- ✅ **Docker Support** - Cross-platform compatibility
- ✅ **Security Best Practices** - Non-root user execution
- ✅ **Health Checks** - Automatic monitoring
- ✅ **Logging** - Persistent log files

---

**Built with ❤️ using LangGraph, LangChain, and modern web technologies**

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/Em-Deesha/Academic-Mentorship-workflow-using-Langraph)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge&logo=python)](https://python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-red?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)