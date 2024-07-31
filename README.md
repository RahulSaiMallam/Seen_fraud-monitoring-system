# Monitoring and Alert System
 
 ## Project Overview
This project implements a monitoring and alert system for fraud detection. The system runs predefined SQL queries on transaction data and generates alerts via JIRA, email, or Slack.

## Features
- **Daily High-Value Transaction Alerts**: Automatically creates JIRA tickets for transactions over $300 from the previous day.
- **Monthly Spending Deviation Alerts**: Sends emails for accounts with significant spending deviations.
- **Monthly High-Spending Account Alerts**: Sends Slack notifications for accounts spending more than $500 in the current month.
- **Configurable Monitors**: Define new monitors easily using a YAML configuration file.
- **Time Travel**: Run the script for any specified date, defaulting to today's date if not provided.
 
 ## Setup 

1. Install dependencies:
   ```bash
   pip install pandas pyyaml



### Summary

This comprehensive solution provides the full logic to build the monitoring and alerting system, including:

- Monitor definitions in a YAML file.
- A main script to execute SQL queries and trigger alerts.
- Stub functions for creating alerts (JIRA tickets, emails, Slack notifications).
- A setup script to initialize the database.
- Unit tests to validate the functionality.
- A README file with setup and usage instructions.

This setup can be extended and refined based on further requirements or feedback.

