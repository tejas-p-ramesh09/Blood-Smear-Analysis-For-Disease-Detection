# Blood Smear Analysis for Hematological Disease Detection

## Overview

Blood Smear Analysis for Hematological Disease Detection is an AI-powered healthcare application that automates blood cell detection, counting, disease diagnosis, and report generation from microscopic blood smear images.

The system uses a custom-trained YOLO object detection model to identify Red Blood Cells (RBCs), White Blood Cells (WBCs), and Platelets from blood smear images. Based on detected cell counts, the application predicts potential hematological conditions such as Anemia, Leukopenia, Blood Cancer, or Normal blood profiles and generates a diagnostic report with treatment recommendations.

---

## Features

- Automated RBC detection and counting
- Automated WBC detection and counting
- Automated Platelet detection and counting
- Hematological disease prediction
- Treatment recommendation generation
- PDF report generation
- Interactive desktop GUI using Tkinter
- MySQL-based user authentication system

---

## Technologies Used

### Programming Languages
- Python

### Computer Vision & AI
- YOLO
- Darkflow
- OpenCV

### Machine Learning
- Scikit-Learn
- NumPy
- SciPy
- Pandas

### User Interface
- Tkinter

### Database
- MySQL
- PyMySQL

### Reporting
- FPDF

---

## System Workflow

```text
Blood Smear Image
        ↓
YOLO-Based Cell Detection
        ↓
RBC / WBC / Platelet Counting
        ↓
Cell Count Analysis
        ↓
Disease Prediction
        ↓
Treatment Recommendation
        ↓
PDF Report Generation
---

## Disease Categories

The system can identify the following hematological conditions:

- Anemia
- Leukopenia
- Blood Cancer
- Normal Blood Profile

---

## Project Architecture

```text
Blood Smear Image
        │
        ▼
YOLO Object Detection
        │
        ▼
Cell Counting Module
(RBC, WBC, Platelets)
        │
        ▼
Diagnosis Engine
        │
        ▼
Treatment Recommendation
        │
        ▼
PDF Report Generation
```

---

## Results

- Automated blood cell detection from microscopic blood smear images
- Automated disease diagnosis based on blood cell counts
- PDF-based diagnostic report generation
- Achieved **96.4% platelet detection accuracy**
- Real-time visualization of detected blood cells

---

## Repository Structure

```text
Blood-Smear-Analysis-For-Disease-Detection/
│
├── assets/                 # Screenshots and project images
├── cfg/                    # YOLO configuration files
├── config/                 # Additional configuration files
├── darkflow/               # Darkflow framework
├── data/                   # Training and processing data
├── database/               # Database-related files
├── dataset/                # Blood smear image datasets
├── output/                 # Detection outputs
├── results/                # Generated reports
├── src/                    # Source code
├── weights/                # Model checkpoint files
│
├── labels.txt
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/tejas-p-ramesh09/Blood-Smear-Analysis-For-Disease-Detection.git
cd Blood-Smear-Analysis-For-Disease-Detection
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Build Darkflow Extensions

```bash
python setup.py build_ext --inplace
```

### Configure MySQL Database

```sql
CREATE DATABASE blood;
```

```sql
CREATE TABLE user_information (
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    city VARCHAR(100),
    address VARCHAR(255),
    username VARCHAR(100),
    password VARCHAR(100)
);
```

### Add Model Weights

Place the following trained YOLO checkpoint files inside the `weights/` folder:

```text
tiny-yolo-voc-3c-3750.data-00000-of-00001
tiny-yolo-voc-3c-3750.index
tiny-yolo-voc-3c-3750.meta
checkpoint
```

---

## Running the Application

```bash
PYTHONPATH=. python src/Main.py
```

---

## Sample Output

The application provides:

- Blood cell detection visualization
- RBC count
- WBC count
- Platelet count
- Disease prediction
- Treatment recommendation
- PDF diagnostic report

---

## Screenshots

Add screenshots inside the `assets/` folder:

- Login Page
- Registration Page
- Blood Cell Detection Output
- Disease Prediction Result
- Generated PDF Report

Example:

```markdown
![Detection Output](assets/detection_output.png)
```

---

## Future Improvements

- Web-based application deployment
- Cloud integration
- Advanced disease classification models
- Multi-class hematological disease prediction
- Electronic Health Record (EHR) integration
- Real-time clinical decision support

---

## License

This project is licensed under the MIT License.

---

## Author

### Tejas P. Ramesh

Master of Computer Science  
North Carolina State University

Interests:
- Artificial Intelligence
- Machine Learning
- Computer Vision
- Healthcare Analytics
- Data Science