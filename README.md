# GrowMate — Plant Management Web Application

GrowMate is a simple yet powerful full-stack web app to help users manage their plants — track plant details, care notes, and upload images.  
Built with **FastAPI** backend, **SQLite** database, and a custom **HTML/CSS/JavaScript** frontend.

---

## Features

- Add new plants with name, type, date acquired, notes, and optional image  
- Store plant data persistently in a local SQLite database  
- Fully connected frontend and backend via REST API  
- Responsive, user-friendly interface  
- Image upload and management

---

## Technologies Used

- **Backend:** FastAPI (Python)  
- **Database:** SQLite (local file-based DB)  
- **Frontend:** HTML, CSS, JavaScript  
- **Others:** SQLAlchemy ORM, python-multipart for form handling

---

## Getting Started

### Prerequisites

- Python 3.8+ installed  
- Git (optional, for cloning)  

### Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/GrowMate.git
   cd GrowMate

2. Create and activate a virtual environment

   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate

3. Install dependencies

   ```bash
   pip install -r requirements.txt

4. Run the FastAPI backend server

   ```bash
   uvicorn main:app --reload

---

## How to Use

* Open the frontend in your browser
* Add new plants through the form — fill in details and upload images if available
* Plant details are saved to the SQLite database via the FastAPI backend
* Data persists locally on your machine

---

## Project Structure
GrowMate/
│
├── main.py             # FastAPI backend entry point  
├── database.py         # Database connection and setup  
├── models.py           # SQLAlchemy ORM models  
├── requirements.txt    # Python dependencies  
├── index.html          # Frontend landing page  
├── next.html           # Frontend with Add Plant form  
├── script.js           # Frontend JavaScript logic  
├── uploads/            # Folder to store uploaded images  
└── README.md           # This file

## Future Improvements

* Deploy the app online for live access
* Add user authentication and multi-user support
* Replace SQLite with a cloud database like PostgreSQL
* Improve frontend UI with React or Vue.js
* Add plant care reminders and notifications

## Contact

Created by Siddhi Choudhary
