# 🔗 Hook2Issue: Flask-Based JIRA Automation via GitHub Events

## 📌 Project Overview

This project automates the creation of JIRA tickets based on GitHub issue comments. It uses a lightweight Flask application hosted on an EC2 instance to listen for webhook events and generate JIRA issues dynamically. The goal is to eliminate manual ticket creation and streamline DevOps workflows.

## 🎯 Why I Built This

In real-world engineering teams, QA often reports bugs via GitHub issues, but developers still need to manually create JIRA tickets to track them. This repetitive task slows down sprint velocity and introduces friction between code and task tracking systems. I built this integration to automate that bridge — making ticket creation seamless, conditional, and traceable.

## 🧠 Real-World Use Case

- QA logs a bug in GitHub
- Developer comments `/jira` on the issue
- A JIRA ticket is automatically created with all relevant metadata
- No manual login, no copy-paste, no context switching

This system improves traceability, reduces overhead, and keeps engineering workflows tight and responsive.

## ⚙️ Tech Stack

- **Python 3.12**
- **Flask**
- **GitHub Webhooks**
- **JIRA REST API**
- **AWS EC2 (Ubuntu Server)**
- **requests** (Python HTTP client)


## 📘 User Guide

For a complete step-by-step setup — including EC2 configuration, JIRA API token generation, Flask deployment, and webhook integration — refer to the [User Guide]([url](https://docs.google.com/document/d/1WqYXAU8CLbdxqbh_Gwm6yQwdJUA-Hc4EDcOkYmlqX7A/edit?usp=sharing))
