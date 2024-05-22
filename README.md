# Zakat And Donation Platform
---
This project aims to develop a database system for collecting and distributing Zakat and donation.


## Table of Contents
- [Project Overview](#project-overview)
- [Database Implementation](#database-implementation)
	- [ER diagram](#er-diagram)
	- [Relationships](#relationships)
	- [Relational Mapping](#relational-mapping)
	- [Normalization](#normalization)
- [GUI Implementation](#gui-implementation)
- [Technology](#technnology)
- [Project Structure](#project-structure)
- [Installation and Usage](#installation-and-usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
Zakat and donation platform is mainly focused on database design and implementation. It also involves the design and implementation of a database schema using SQLite3 and a GUI using PyQt.

The system consists of three user roles: 
- Donor, 
- Representative, 
- Admin. 

Each user must log in with a unique username. Donors can update their information, make zakat or charity contributions, and view their donation history. Representatives can view the total amount received, and Admins can manage the overall budget and transactions.


## Database Implementation
The Database is designed using conventional methods. The ER diagram shows the general relations and entities then the normalization form is obtained using systematic approach.
### ER Diagram

The basic schema includes six strong entities:
- **Donor**
- **Donation**
- **Representative**
- **Received_amount**
- **Admin**
- **Login**

### Relationships

- **Pays**: Donor pays charity or zakat to Donation
- **Receives**: Representative receives amount in Received_amount
- **Register**: Donor, Admin, Representative's login data with Login table
- **Transaction**: Ternary relationship between Admin, Donation, and Received_amount with amount as a relationship attribute

### Relational Mapping

Entities and relationships are converted into tables:
- **DONOR** (NID, first_name, last_name, address, phone, email, religion, net_amount, user_name)
- **ADMIN** (admin_id, name, email, user_name)
- **REPRESENTATIVE** (company_id, name, address, email, city, user_name)
- **LOGIN** (user_name, password)
- **DONATION** (TnxID, given_zakat, given_charity, don_id)
- **RECEIVED_AMOUNT** (TnxID, zakat_received, charity_received, rep_id)
- **TRANSACTION** (adm_id, rep_tid, don_tid, zakat, charity)

### Normalization

All basic relations are in at least 3NF form. Redundant data storage is minimized, ensuring efficient data management and retrieval.


## GUI Implementation

The GUI is created using PyQt, with the database managed by Python’s integrated SQLite3. The interfaces include:
- **Login Page**
- **Donor Page**
- **Representative Page**
- **Admin Page**

## Technology
- Python
- SQLite
- PyQt
## Project Structure
```
.
├── Design
│   ├── 0NF ERD
│   │   ├── First_dbms_er_diagram.jpeg
│   │   └── First_dbms_er_diagram.png
│   └── 3NF+
│       ├── 3NF_form_database_project_mapping.jpeg
│       └── 3NF_form_database_project_mapping.png
├── Final
│   ├── zakat&donation_Final_presentation.pptx
│   └── ZnDFinalReportCSE-252.pdf
├── Implementation
│   ├── db.py
│   ├── main.py
│   ├── requirements.txt
│   ├── zakat_donation_db.db
│   └── zakat_donation_platform.ui
├── LICENSE
└── README.md
```
## Installation and Usage
### Prerequisites
- Python(v3.x or later)
- SQlite3
- PyQt(v5 or later)

### Clone the repository
```bash
git clone https://github.com/akib35/Zakat-and-Donation-Platform.git
cd Zakat-and-Donation-Platform/
```

### Install dependencies
```bash
cd Implementation
pip install -r requirements.txt
```
### Run 
```bash
python -m main
```
## Contributing 
This platform is developed as study or academic purpose. The aim of the course was mainly focused on the procedure of development of a database and contribution to this project is limited.

## License
This project is licensed under the MIT License. See the [LICENSE](/LICENSE) file for more details.

--- 

Thank you being interested in our project! If you have any questions, please feel free to contact us.

**Note**: This project is part of an academic endeavor and may require further enhancements for deployment in a real-world scenario. 
