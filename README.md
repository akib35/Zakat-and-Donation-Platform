# Zakat and Charity Management System

## Introduction

The purpose of this application is to centrally collect and distribute zakat and charity. It maintains proper collection and donation in a systematic way, aiding Muslims in fulfilling their annual zakat obligations. The application helps users calculate the minimum amount they need to donate to fulfill the conditions of paying zakat and keeps track of their donations in a transparent manner. Additionally, it supports general charity contributions for emergency situations, ensuring timely and effective distribution of aid.

## Objective

The primary objective of this project is to improve the practice of zakat collection and distribution in our nation. By centralizing the process, we aim to ensure that zakat reaches those who qualify in a timely manner, especially during natural disasters. This project also aims to create a platform for efficient charity fund management, ensuring that aid reaches the genuine deprived individuals.

## Motivation

- To enhance the practice of zakat collection and distribution according to Shariah.
- To provide timely assistance to victims of natural disasters and ensure aid reaches the true needy in rural areas.
- To create an efficient platform for anyone to contribute to charity and participate in welfare activities.

## Project Description

The project involves the design and implementation of a database schema using SQLite3 and a GUI using PyQt. The system consists of three user roles: Donor, Representative, and Admin. Each user must log in with a unique username. Donors can update their information, make zakat or charity contributions, and view their donation history. Representatives can view the total amount received, and Admins can manage the overall budget and transactions.

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

### Sample Tables and SQL Commands

Sample tables and SQL commands are used to manage and query data effectively. Commands include inserting donation data, updating personal data, showing debatable zakat and charity, and creating transactions.

## GUI Implementation

The GUI is created using PyQt, with the database managed by Python’s integrated SQLite3. The interfaces include:
- **Login Page**
- **Donor Page**
- **Representative Page**
- **Admin Page**

## Conclusion

This project aims to address the gaps in zakat collection and distribution in our nation. By centralizing the process and creating an efficient platform for charity contributions, we can ensure timely aid to disaster victims and proper distribution of zakat according to Shariah, ultimately assisting the underprivileged in improving their economic situation.

---

**Note**: This project is part of an academic endeavor and may require further enhancements for deployment in a real-world scenario.
