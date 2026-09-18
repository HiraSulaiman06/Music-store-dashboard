# 🎵 Music Store Sales & Analytics Dashboard

## 📌 Project Overview

This project analyzes **music store sales data** to uncover insights into revenue, customers, music genres, tracks, and sales trends.

The project combines **PostgreSQL, SQL, Power BI, Python, and Streamlit** to build an interactive analytics solution.

The main dashboard was developed in **Power BI using DirectQuery with PostgreSQL**, allowing the dashboard to connect directly to the database.

---

## 🎯 Project Objectives

* Analyze overall music store revenue and sales performance
* Identify top-performing countries and cities
* Analyze revenue by music genre
* Identify popular tracks and customers
* Monitor monthly revenue trends
* Create interactive dashboards for business insights
* Practice SQL, Power BI, Python, and data visualization skills

---

## 🛠️ Tools & Technologies

* **Power BI** – Interactive dashboard and visualization
* **PostgreSQL** – Database management
* **SQL** – Data querying and analysis
* **Python** – Data analysis and preprocessing
* **Pandas** – Data manipulation
* **Jupyter Notebook** – Exploratory Data Analysis (EDA)
* **Streamlit** – Interactive web dashboard
* **GitHub** – Project version control and portfolio

---

## 📊 Dataset

The project uses music store data containing information about:

* Invoices
* Invoice items
* Customers
* Tracks
* Genres
* Countries
* Cities
* Sales quantities
* Unit prices
* Revenue

The data was combined to create an analytical dataset containing **4,757 records and 13 columns**.

---

## 📈 Key Dashboard Insights

Some of the key findings include:

### 💰 Revenue by Country

| Country |  Revenue |
| ------- | -------: |
| USA     | 1,040.49 |
| Canada  |   535.59 |
| Brazil  |   427.68 |
| France  |   389.07 |
| Germany |   334.62 |

### 🎸 Revenue by Genre

* **Rock:** 2,608.65
* **Metal:** 612.81

### 🌎 Top Cities by Revenue

* Prague – 273.24
* Mountain View – 169.29
* London – 166.32
* Berlin – 158.40
* Paris – 151.47

### 🧾 Average Invoice Value

**7.67**

---

## 🔄 Power BI DirectQuery

Power BI is connected to **PostgreSQL using DirectQuery**.

This approach allows the dashboard to query the PostgreSQL database directly rather than importing the complete dataset into Power BI.

### Data Flow

```text
CSV Files
    ↓
Python / Data Cleaning
    ↓
PostgreSQL Database
    ↓
SQL Queries / Views
    ↓
Power BI DirectQuery
    ↓
Interactive Dashboard
```

---

## 🐍 Python EDA

Exploratory Data Analysis was performed using **Python and Jupyter Notebook**.

The analysis included:

* Data cleaning
* Data type conversion
* Missing-value checking
* Revenue analysis
* Country analysis
* City analysis
* Genre analysis
* Monthly sales trends
* Data visualization

---

## 🌐 Streamlit Dashboard

A Streamlit dashboard was also developed to provide an interactive web-based view of the music store data.

The application allows users to explore sales information through filters and visualizations.

**Streamlit App:**
*https://hira-music-store.streamlit.app/*

---

## 📂 Project Structure

Music-Store-Dashboard/
│
├── data/
│   └── music_store_invoice.csv
│
├── notebooks/
│   └── music_store_eda.ipynb
│
├── app.py
├── requirements.txt
└── README.md

---

## 🚀 Skills Demonstrated

This project demonstrates practical experience with:

* Data Cleaning & Transformation
* Exploratory Data Analysis
* Data Visualization
* Dashboard Development
* Python & Pandas
* Streamlit
* Business Data Analysis

---

## 📌 Conclusion

This project demonstrates an end-to-end **data analytics workflow**, starting from raw data and moving through data cleaning, SQL analysis, PostgreSQL database development, Power BI DirectQuery, Python EDA, and Streamlit dashboard development.

It was created as a practical portfolio project to strengthen my skills in **Data Analytics, SQL, Power BI, Python, and Dashboard Development**.

---

## 👩‍💻 Author

**Hira Sulaiman**

**Junior Data Analyst | Power BI Developer**

🔗 GitHub: https://github.com/HiraSulaiman06/
🔗 LinkedIn: https://www.linkedin.com/in/hira-sulaiman-21181b29/
