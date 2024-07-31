import sqlite3
import yaml
from datetime import datetime, timedelta
from alerts import create_jira_ticket, send_email, send_slack_notification

def execute_sql(sql, params):
    conn = sqlite3.connect('monitoring_system.db')
    c = conn.cursor()
    c.execute(sql, params)
    results = c.fetchall()
    conn.close()
    return results

def main(date=None):
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')

    with open('monitors.yaml', 'r') as file:
        monitors = yaml.safe_load(file)['monitors']

    for monitor in monitors:
        sql = monitor['sql']
        params = {
            'date': date,
            'start_date': (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'),
            'end_date': date
        }
        results = execute_sql(sql, params)
        
        if results:
            if monitor['channel'] == 'JIRA':
                create_jira_ticket(results)
            elif monitor['channel'] == 'email':
                send_email(results)
            elif monitor['channel'] == 'slack':
                send_slack_notification(results)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Run monitoring system.')
    parser.add_argument('--date', type=str, help='The date to run the script for (YYYY-MM-DD).')
    args = parser.parse_args()
    
    main(args.date)
