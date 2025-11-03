# 🧠 WorkSyncAI  
**AI-powered productivity and activity tracking platform** designed to help organizations monitor digital behavior, reduce burnout, and enhance efficiency.

---

## 🚀 Overview  
**WorkSyncAI** is a cross-platform productivity analytics system built during a hackathon.  
It combines **FastAPI PC agents**, **Spring AI microservices**, **Elasticsearch vector DB**, and a **React-based chatbot** to deliver intelligent insights from employees’ digital activities — helping teams work smarter and stay balanced.

---

## 🔧 Key Features  
- 🖥️ **Real-time PC agent** – Tracks browser activity (URLs, titles, timestamps), app usage, and system events without browser extensions.  
- ⚙️ **AI-driven insights** – Uses **Spring AI + LLMs** and **Elasticsearch vector search** for semantic understanding of productivity data.  
- 💬 **Interactive chatbot** – Built with **React**, allowing users to query activity insights conversationally.  
- 📊 **Analytics dashboard** – Displays aggregated productivity metrics and burnout indicators.  
- 🧩 **Modular microservices** – Built with **FastAPI** and **Spring Boot** for scalability, separation of concerns, and flexibility.

---

## 🧱 Architecture  

| Component | Technology | Description |
|------------|-------------|--------------|
| PC Agent | FastAPI (Python) | Collects browser and system-level activity data. |
| Backend Services | Spring Boot (Java) | Processes and enriches collected data, exposes REST APIs, integrates with AI modules. |
| Vector Database | Elasticsearch | Stores and queries embeddings for semantic search and analytics. |
| Frontend Chatbot | React | Provides a conversational UI for insights and analytics visualization. |

---

## ⚙️ Installation  

### 1. Clone the repository  
```bash
git clone https://github.com/hrOarr/WorkSyncAI.git
cd WorkSyncAI
2. PC Agent setup
bash
Copy code
cd WorkSyncAI-Agent
pip install -r requirements.txt
python agent.py
3. Backend setup
bash
Copy code
cd WorkSyncAI-Backend
./mvnw clean package
java -jar target/worksyncai-backend.jar
4. Frontend setup
bash
Copy code
cd WorkSyncAI-Frontend
npm install
npm start
```

## 💡 Usage  

- Launch the **PC Agent** on user machines to start collecting activity data.  
- Run the **backend services** for processing and semantic analysis.  
- Use the **React chatbot** to query insights like:  
  - “What apps did I use most today?”  
  - “Show my productivity trend this week.”  
  - “Am I spending too much time switching tasks?”  

## 🔍 Why WorkSyncAI?  
**WorkSyncAI** bridges the gap between **activity tracking** and **intelligent insights**.  
It transforms raw data into actionable productivity analytics while promoting a **privacy-conscious**, **burnout-aware** work environment.  

---

## 🛠️ Future Enhancements  
- OS-level modules for richer system event tracking (Windows/macOS/Linux).  
- Predictive ML models for burnout risk and focus optimization.  
- Privacy-first features: anonymization, opt-out control, and secure data retention.  
- Integration with Slack, Microsoft Teams, or voice assistants.  
- Multi-tenant SaaS deployment with advanced monitoring and scaling.  
