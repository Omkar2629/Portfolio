# 🚀 AI-Powered Portfolio & CV Generator

A dynamic full-stack portfolio website built using Django, featuring an AI-powered CV Generator with NLP-based text summarization, multiple templates, and admin-controlled management.

## 📖 About The Project

This project is an advanced personal portfolio that integrates a **CV Generator system** enhanced with **Natural Language Processing (NLP)**.

It allows users to create professional resumes effortlessly by entering their details, automatically summarizing content, selecting from multiple templates, and downloading the final CV as a PDF.

Additionally, the system includes an **admin-only dashboard** for managing and monitoring user interactions.

## ✨ Key Features

### 🧑‍💻 Portfolio Website

* Modern and responsive UI
* Showcases projects, skills, and experience
* Smooth navigation and structured layout


### 📄 CV Generator System

* Dynamic CV generation from user input
* **4 professional CV templates**
* Download CV in PDF format
* Structured and clean resume layouts
  
### 🧠 NLP Text Summarization

* Automatically summarizes user input
* Enhances clarity and professionalism of CV content
* Reduces redundancy in descriptions


### 📬 Email Integration (SMTP)

* Sends emails dynamically using SMTP
* Can be used for contact forms / notifications
* Enables real-time communication

### 🔐 Admin Dashboard

* Secure, restricted access (admin-only)
* Monitor and manage application data
* Control over backend operations

## 🛠️ Tech Stack

### 🔹 Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### 🔹 Backend

* Python
* Django
* Django REST Framework

### 🔹 AI / NLP

* Text Summarization

### 🔹 PDF Generation

* XHTML2PDF

### 🔹 Backend Utilities

* SMTP (Email Services)
* Whitenoise (Static file handling)
* Gunicorn (WSGI server)

---

## ⚙️ How It Works

1. User enters personal and professional details
2. Data is processed via Django backend APIs
3. NLP module summarizes the content
4. User selects a preferred CV template
5. CV is generated and converted into PDF
6. File is available for download
7. Admin can monitor/manage data via dashboard


## 📂 Project Structure

```id="tree01"
Portfolio/
│── portfolio_app/
│── cv_generator/
│── templates/
│── static/
│── media/
│── manage.py
│── requirements.txt
```

## ⚙️ Getting Started

### 1. Clone the repository

```id="clone01"
git clone https://github.com/Omkar2629/Portfolio.git
```

### 2. Navigate to project directory

```id="cd01"
cd Portfolio
```

### 3. Create virtual environment

```id="venv01"
python -m venv venv
```

### 4. Activate environment

```id="venv02"
venv\Scripts\activate   # Windows
source venv/bin/activate   # Mac/Linux
```

### 5. Install dependencies

```id="install01"
pip install -r requirements.txt
```

### 6. Run migrations

```id="mig02"
python manage.py migrate
```

### 7. Start server

```id="run02"
python manage.py runserver
```


## 🚀 Deployment

This project is production-ready and supports deployment using:

* Gunicorn as the application server
* Whitenoise for static file serving
* SMTP configuration for email services

Can be deployed on:

* Render
* Railway
* VPS / Cloud servers


## 📸 Screenshots



## 💡 What I Learned

* Building scalable full-stack applications using Django
* Designing and consuming REST APIs
* Implementing NLP for real-world applications
* Generating PDFs dynamically
* Handling email services using SMTP
* Managing secure admin-level access
* Deploying production-ready applications


## 🔮 Future Improvements

* User authentication system (login/signup)
* Save & edit multiple CV versions
* More advanced NLP models (AI-based suggestions)
* Additional CV templates
* API-based resume import (LinkedIn, etc.)
* Docker-based deployment


## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.


## 📬 Contact

* GitHub: https://github.com/Omkar2629
* Email: omkarsubhankar263@gmail.com
* LinkedIn: www.linkedin.com/in/omkarsubhankar


## ⭐ Show Your Support

If you found this project useful, consider giving it a ⭐ on GitHub!


> Built with 💻 Django, 🤖 AI, and real-world problem solving by Omkar
