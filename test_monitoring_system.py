import unittest
from main_script import execute_sql

class TestMonitoringSystem(unittest.TestCase):

    def test_high_value_transactions(self):
        results = execute_sql("SELECT * FROM transactions WHERE transaction_amount > 300 AND DATE(transaction_date) = DATE('2024-01-03')", {})
        self.assertEqual(len(results), 0)  # Based on provided sample data

    def test_monthly_spending_deviation(self):
        results = execute_sql("SELECT account_id, SUM(transaction_amount) as total FROM transactions GROUP BY account_id HAVING total > (SELECT AVG(transaction_amount) * 1.5 FROM transactions)", {})
        self.assertEqual(len(results), 0)  # Based on provided sample data

    def test_monthly_high_spending_accounts(self):
        results = execute_sql("SELECT account_id, SUM(transaction_amount) as total FROM transactions WHERE DATE(transaction_date) BETWEEN DATE('2024-01-01') AND DATE('2024-01-31') GROUP BY account_id HAVING total > 500", {})
        self.assertEqual(len(results), 0)  # Based on provided sample data

if __name__ == '__main__':
    unittest.main()
