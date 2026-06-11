![Pipeline](https://cdn.jsdelivr.net/gh/zzxhotmail-beep/azure_project@main/logo.png)
# 🎵 Spotify End-to-End Azure Data Engineering Project

## 🚀 Overview

This project demonstrates a production-style **end-to-end Azure Data Engineering solution** built using the **Medallion Architecture (Bronze → Silver → Gold)**.

The pipeline ingests Spotify streaming data from **Azure SQL Database**, performs incremental ingestion and transformations, and delivers analytics-ready datasets using **Azure Databricks**, **Delta Lake**, and **Delta Live Tables (DLT)**.

The project focuses on modern data engineering best practices, including:

✅ Incremental Data Loading

✅ Historical Backfilling

✅ Auto Loader Incremental Processing

✅ Schema Evolution Handling

✅ Metadata-Driven Pipelines

✅ Data Quality Validation

✅ Slowly Changing Dimensions (SCD Type 2)

✅ Infrastructure as Code with Databricks Asset Bundles

# 🏗️ Solution Architecture

```text
Azure SQL Database
        │
        ▼
Azure Data Factory
(Incremental Load + Backfill)
        │
        ▼
Azure Data Lake Storage Gen2
      Bronze Layer
        │
        ▼
Databricks Auto Loader
      Silver Layer
        │
        ▼
Delta Live Tables (DLT)
       Gold Layer
        │
        ▼
Analytics & Reporting
```

📌 Add your architecture diagram here:

```text
architecture/architecture.png
```

# 📂 Source Data

The project processes five Spotify datasets:

| Table      | Description              |
| ---------- | ------------------------ |
| DimUser    | User information         |
| DimArtist  | Artist information       |
| DimTrack   | Track information        |
| DimDate    | Calendar dimension       |
| FactStream | Streaming activity facts |

# 🛠️ Technology Stack

## ☁️ Azure Services

* Azure Data Factory (ADF)
* Azure SQL Database
* Azure Data Lake Storage Gen2 (ADLS Gen2)
* Azure Logic Apps
* Azure Databricks

## ⚡ Data Processing

* PySpark
* Auto Loader
* Delta Lake
* Delta Live Tables (DLT)

## 🔐 Governance

* Unity Catalog
* Metastore

## 🚀 DevOps & Deployment

* Databricks Asset Bundles (DAB)
* YAML Configuration

## 🧩 Automation

* Jinja Templating

# 🥉 Bronze Layer – Incremental Data Ingestion

The Bronze layer was built using **Azure Data Factory**.

## ✨ Features

### 🔄 Incremental Data Loading

Implemented an ADF pipeline that continuously loads only new or modified records from Azure SQL Database into ADLS Gen2.

### ⏪ Historical Backfilling

Implemented a backfill mechanism that allows users to reload historical data by specifying a custom date range.

### 📧 Automated Failure Notifications

Integrated **Azure Logic Apps** with ADF Web Activities.

Whenever a pipeline fails:

* Failure notifications are automatically generated
* Alert emails are sent to stakeholders

### 💾 Raw Data Storage

Raw source data is stored in the **Bronze container** of Azure Data Lake Storage Gen2.

## 📷 Pipeline Preview

![Pipeline](https://cdn.jsdelivr.net/gh/zzxhotmail-beep/azure_project@main/Pipeline_pic.png)

# 🥈 Silver Layer – Data Transformation & Standardization

The Silver layer was implemented using **Azure Databricks**.

## 🔐 Unity Catalog & Governance

Configured Unity Catalog and Metastore to:

* Centrally govern data assets
* Securely manage access permissions
* Enable secure access to ADLS Gen2

## 📦 Databricks Asset Bundles (DAB)

Used Databricks Asset Bundles to package and manage:

* Notebooks
* Jobs
* DLT Pipelines
* Catalog Objects

Benefits:

✅ Infrastructure as Code

✅ Version Control

✅ Reproducible Deployments

## ⚡ Auto Loader

Implemented Databricks Auto Loader to:

* Continuously detect new files
* Process only incremental data
* Handle schema evolution automatically
* Reduce operational overhead

Key capabilities:

```python
cloudFiles
schemaEvolutionMode = "addNewColumns"
```

File:
```text
Databricks Code/silver_Dimensions.ipynb
```

## 🧰 Reusable Utility Framework

Created reusable PySpark utility functions inside:

```text
Databricks Code/transformations.py
```

Example use cases:

* Column removal
* Shared transformations
* Reusable ETL logic

This minimizes code duplication and improves maintainability.

## ⚙️ Metadata-Driven Pipeline

Implemented a metadata-driven framework where processing behavior is controlled through configuration rather than hardcoded logic.

Benefits include:

* One codebase for multiple tables
* Reduced maintenance effort
* Faster onboarding of new datasets
* Standardized processing patterns

## 📝 Dynamic SQL with Jinja

Implemented Jinja templating to dynamically generate transformation logic.

Notebook:

```text
Databricks Code/Jinja_Notebook.ipynb
```

Benefits:

* Dynamic SQL generation
* Reduced repetitive coding
* Improved scalability

# 🥇 Gold Layer – Business-Ready Data Products

The Gold layer was built using **Delta Live Tables (DLT)**.

## 🔄 Slowly Changing Dimension (SCD Type 2)

Implemented SCD Type 2 using Delta Live Tables AUTO CDC capabilities.

Benefits:

* Preserves historical changes
* Supports auditability
* Enables historical analytics

Code:

```text
gold_pipeline/DimDate.py
gold_pipeline/DimTrack.py
gold_pipeline/DimUser.py
gold_pipeline/FactStream.py
```

## ✅ Data Quality Enforcement

Implemented DLT Expectations to enforce data quality rules.

Example:

* Records containing NULL values in critical fields are automatically dropped.

```python
@dlt.expect_or_drop(...)
```

Benefits:

* Improved data reliability
* Reduced downstream issues
* Automated quality monitoring

# 📊 Key Engineering Highlights

✅ End-to-End Azure Data Engineering Pipeline

✅ Medallion Architecture (Bronze → Silver → Gold)

✅ Incremental Data Loading

✅ Historical Backfilling

✅ Azure Logic Apps Alerting

✅ Auto Loader Incremental Processing

✅ Schema Evolution Handling

✅ Metadata-Driven Design

✅ Reusable PySpark Utilities

✅ Dynamic SQL with Jinja

✅ Delta Lake Architecture

✅ Delta Live Tables (DLT)

✅ Slowly Changing Dimension (SCD Type 2)

✅ DLT Expectations

✅ Unity Catalog Governance

✅ Databricks Asset Bundles (DAB)

# 📈 Business Value

This project demonstrates how modern cloud-native technologies can be combined to build scalable, maintainable, and production-ready data pipelines.

The solution incorporates enterprise-grade capabilities such as:

* Incremental processing
* Historical backfilling
* Data governance
* Data quality monitoring
* Change data tracking
* Automated alerting

These are common requirements in real-world data engineering environments.

## 👤 Author - Zixuan Zhang

This project demonstrates my ability to build a production-style Azure Data Engineering platform from data ingestion to business-ready data products.

Key areas covered include Azure Data Factory, ADLS Gen2, Databricks, Auto Loader, Delta Lake, Delta Live Tables (DLT), Metadata-Driven Pipelines, Data Quality Validation, and SCD Type 2 implementation.

The architecture follows enterprise data engineering best practices and reflects the technologies and patterns commonly used in modern cloud data platforms.
- **LinkedIn**: [My Professional Profile](https://www.linkedin.com/in/zixuan-zhang-78ba38274)
