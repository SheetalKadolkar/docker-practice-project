# docker-practice-project
# Docker Practice Project

This project demonstrates how to run a **Python web application using Docker and Nginx with Docker Compose**. Nginx acts as a reverse proxy that forwards user requests to the Python application container.

---

## 📁 Project Structure

```
docker-practice-project/
├─ app/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ nginx/
│  └─ nginx.conf
├─ docker-compose.yml
├─ .env
├─ Makefile
└─ README.md
```

### Description of Each File

* **app/app.py** – Main Python application file
* **app/requirements.txt** – List of Python dependencies
* **app/Dockerfile** – Instructions to build the Python application Docker image
* **nginx/nginx.conf** – Nginx configuration file (reverse proxy settings)
* **docker-compose.yml** – Orchestrates all containers (Python + Nginx)
* **.env** – Environment variables
* **Makefile** – Shortcut commands to manage Docker
* **README.md** – Project documentation

---

## ⚙️ Prerequisites

Before running this project, make sure you have the following installed:

* Docker
* Docker Compose

To verify installation:

```
docker --version
docker-compose --version
```

---

## 🚀 How to Run the Project

### Step 1: Navigate to Project Folder

```
cd docker-practice-project
```

### Step 2: Build and Start Containers

For Docker Compose v1:

```
docker-compose up --build
```

For Docker Compose v2:

```
docker compose up --build
```

### Step 3: Access the Application

Open your browser and visit:

```
http://localhost
```

---

## 🛑 Stop the Application

```
docker-compose down
```

---

## 🧾 Using Makefile Commands (Optional)

If you want to use shortcut commands:

```
make up     # Start the project
make down   # Stop the project
```

---

## 🔄 How the Project Works

1. The user sends a request from the browser.
2. The request goes to the **Nginx container**.
3. Nginx forwards the request to the **Python app container**.
4. The Python app processes the request.
5. The response is sent back to the user through Nginx.

---

## 🧑‍💻 Technologies Used

* Python
* Docker
* Docker Compose
* Nginx

---

## ✅ Sample Commands

Build image manually:

```
docker build -t my-python-app ./app
```

List running containers:

```
docker ps
```

View logs:

```
docker-compose logs
```

## 📌 Note

This project is for **learning and practice purposes** to understand Docker, Docker Compose, and Nginx reverse proxy setup with a Python application.
