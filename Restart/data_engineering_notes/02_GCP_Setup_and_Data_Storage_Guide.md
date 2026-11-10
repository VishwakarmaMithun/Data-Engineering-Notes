# Author: Mithun Vishwakarma
# Date: 2026-11-10
# Version: 2.0

# Google Cloud Platform (GCP) Setup Guide

This guide provides a practical setup flow for creating a GCP project, enabling billing, setting alerts, and choosing the right cloud storage/data services for your workload.

---

## 1. Create a GCP Project, Enable Billing, and Set Alerts

### Step 1: Create a GCP Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click the project selector in the top navigation bar.
3. Select **NEW PROJECT**.
4. Enter a unique project name, such as `my-production-project`.
5. Choose your organization or folder if applicable.
6. Click **CREATE**.
7. After creation, switch to the new project from the project selector.

---

### Step 2: Enable Billing

Most GCP services require a valid billing account.

1. Open the navigation menu in the top-left corner.
2. Click **Billing**.
3. If no billing account exists, choose **Set up billing** or **Create account**.
4. Add a valid payment method when prompted.
5. If a billing account already exists, go to **Account management**.
6. Select your project and choose **Change billing**.
7. Pick the correct billing account and click **Set account**.

---

### Step 3: Set Up Budget Alerts

Budget alerts help you stay informed before spending exceeds your limit.

1. Open **Billing**.
2. Select **Budgets & alerts**.
3. Click **+ CREATE BUDGET**.
4. Enter a budget name such as `Monthly-Project-Budget`.
5. Choose the scope:
   - Billing account or specific project
   - Services: leave as **All services** unless you want to limit the scope
6. Set the monthly budget amount, for example `$100` or `$500`.
7. Add threshold rules:
   - 50%
   - 80%
   - 100%
8. Enable notifications for billing admins and users.
9. Click **SAVE**.

---

## 2. Choosing the Right Data Store

Choosing the correct GCP data service depends on the workload type: object storage, warehouse analytics, transactional databases, or document storage.

| Service | Best For | Avoid For |
| --- | --- | --- |
| Cloud Storage | Files, backups, raw data lakes, media | SQL queries and transactional row updates |
| BigQuery | Analytical queries, dashboards, reporting | OLTP apps with low-latency writes |
| Cloud SQL | Relational app data, transactions, CRUD apps | Massive analytical workloads |
| Firestore | JSON-like application data, mobile/web apps | Heavy relational analytics |

---

### 2.1 Cloud Storage (GCS)

**What it is:**
Object storage for unstructured or semi-structured data.

**Best used for:**
- storing files and media
- raw data lakes and backups
- logs and archival data
- static website assets

**Avoid when:**
- you need relational queries
- you want row-level transactional updates
- you need low-latency random access by key for application logic

---

### 2.2 BigQuery

**What it is:**
A fully managed serverless data warehouse for analytical workloads.

**Best used for:**
- data analytics at scale
- business intelligence dashboards
- SQL-based reporting and trend analysis
- ELT / lakehouse patterns

**Avoid when:**
- building transactional systems requiring strict row-level updates
- low-latency operational queries

**Example use cases:**
- monthly revenue analysis
- product trend dashboards
- ad-hoc SQL exploration over large datasets

---

### 2.3 Cloud SQL

**What it is:**
A managed relational database service supporting PostgreSQL, MySQL, and SQL Server.

**Best used for:**
- traditional application databases
- CMS and ERP systems
- structured business data with joins and constraints
- transactional workloads

**Avoid when:**
- you need very large-scale analytical SQL over petabyte-scale datasets

**Typical workloads:**
- user accounts
- orders
- inventory records
- relational application data

---

### 2.4 Firestore

**What it is:**
A NoSQL document database designed for app development.

**Best used for:**
- mobile and web app data
- document-based data models
- real-time sync and flexible schemas

**Avoid when:**
- heavy analytical queries
- advanced relational modeling
- large-scale reporting workloads

---

## 3. Quick Decision Guide

### Use Cloud Storage when:
- you are storing raw files, logs, or backups
- you need cheap, durable object storage

### Use BigQuery when:
- you need SQL queries across massive datasets
- your focus is analytics and reporting

### Use Cloud SQL when:
- your application needs relational data and transactions

### Use Firestore when:
- you are building modern app backends with flexible document data

---

## 4. Suggested Architecture Pattern

A common production setup is:

```text
Application / Web App
        ↓
Cloud SQL / Firestore
        ↓
Cloud Storage
        ↓
BigQuery
        ↓
Dashboards / BI / ML
```

This pattern keeps transactional systems separate from analytics systems and makes it easier to scale each layer independently.

---

## 5. Summary

Google Cloud gives you a flexible ecosystem for modern data engineering and application development. The key is to match each service to the right workload:

- use Cloud Storage for raw and large file data
- use BigQuery for analytics and reporting
- use Cloud SQL for relational transactions
- use Firestore for flexible app data

This clear separation improves scalability, maintainability, and cost control.
