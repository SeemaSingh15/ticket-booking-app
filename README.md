# 🎟️ Ticket Booking Web Application

This is a simple **Flask-based Ticket Booking Web App** with a clean UI for booking tickets.  
The goal of this project is to demonstrate **Development → Dockerization → CI/CD via Jenkins → Deployment on Kubernetes**.

This project is part of my DevOps assignment and shows the **full software delivery pipeline** in action.

---

## 🚀 Features

- Clean and simple **ticket booking UI** (HTML + CSS)
- Backend built with **Flask (Python)**
- Containerized using **Docker**
- Automated CI/CD using **Jenkins Pipeline**
- Deployment on **Kubernetes**
- All screenshots are inside the `images/` folder

---

## 🛠️ Tech Stack

| Component      | Technology |
|----------------|------------|
| Backend        | Flask (Python) |
| Frontend       | HTML, CSS |
| Container      | Docker |
| CI/CD          | Jenkins |
| Deployment     | Kubernetes |
| Repository     | GitHub |

---

## 📂 Project Structure
```
ticket-booking-app/
│
├── app.py                  # Flask backend
├── templates/              # HTML files
├── static/                 # CSS and assets
├── Dockerfile              # Docker image build file
├── k8s-deployment.yaml     # Kubernetes Deployment
├── k8s-service.yaml        # Kubernetes Service (NodePort)
├── Jenkinsfile             # CI/CD Pipeline
└── images/                 # App & Pipeline screenshots for README
```

---

## ▶️ Run Locally (Without Docker)
```bash
pip install flask
python app.py
```

Open in browser: `http://127.0.0.1:5000`

---

## 🐳 Run with Docker
```bash
docker build -t ticket-app .
docker run -p 5000:5000 ticket-app
```

Open in browser: `http://localhost:5000`

---

## 🔁 CI/CD with Jenkins (Pipeline Stages)

The **Jenkinsfile** performs:
```
1️⃣ Checkout from GitHub  
2️⃣ Build Docker Image  
3️⃣ Push to Docker Hub  
4️⃣ Deploy to Kubernetes
```

**Trigger → Build → Push → Deploy ✅**

---

## ☸️ Deploy on Kubernetes
```bash
kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-service.yaml
kubectl get pods
kubectl get svc
```

Access the app via the **NodePort** service:
```bash
minikube service ticket-app-service
```

Or find the NodePort and access via:
```
http://<NODE_IP>:<NODE_PORT>
```

---

## 🖼️ Screenshots (in `images/` folder)

- `images/homepage.png` – Home UI
- `images/booking.png` – Booking page
- `images/jenkins.png` – Jenkins pipeline output
- `images/docker.png` – Docker image
- `images/k8s.png` – Kubernetes deployment

---

## ✅ Conclusion

This project successfully demonstrates:

✔ Flask Application Development  
✔ Docker Containerization  
✔ CI/CD using Jenkins  
✔ Kubernetes Deployment  

It helped me understand how modern applications are built, automated, shipped, and deployed in real-world DevOps environments.

---

## ✨ Author

**Seema Singh**

---

## 📄 Configuration Files

### **Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "app.py"]
```

---

### **Jenkinsfile**
```groovy
pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'yourdockerhubusername/ticket-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/ticket-booking-app.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                        docker.image("${DOCKER_IMAGE}:latest").push()
                    }
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f k8s-deployment.yaml'
                    sh 'kubectl apply -f k8s-service.yaml'
                    sh 'kubectl rollout status deployment/ticket-app'
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
```

> **Note:** Replace `yourdockerhubusername` and `yourusername` with your actual Docker Hub and GitHub usernames. Add Docker Hub credentials in Jenkins as `docker-hub-credentials`.

---

### **k8s-deployment.yaml**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ticket-app
  labels:
    app: ticket-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ticket-app
  template:
    metadata:
      labels:
        app: ticket-app
    spec:
      containers:
      - name: ticket-app
        image: yourdockerhubusername/ticket-app:latest
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "128Mi"
            cpu: "250m"
          limits:
            memory: "256Mi"
            cpu: "500m"
```

> **Note:** Replace `yourdockerhubusername` with your Docker Hub username.

---

### **k8s-service.yaml**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: ticket-app-service
spec:
  type: NodePort
  selector:
    app: ticket-app
  ports:
    - protocol: TCP
      port: 5000
      targetPort: 5000
      nodePort: 30007
```

> **Note:** The app will be accessible at `http://<NODE_IP>:30007`. You can change the `nodePort` value (range: 30000-32767) if needed.

---

**🚀 Ready to deploy! Copy this entire content and paste it as your README.md file on GitHub.**
