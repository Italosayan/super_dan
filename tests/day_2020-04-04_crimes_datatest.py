"""
A basic generated Great Expectations tap that validates a single batch of data.

Data that is validated is controlled by BatchKwargs, which can be adjusted in
this script.

Data are validated by use of the `ActionListValidationOperator` which is
configured by default. The default configuration of this Validation Operator
saves validation results to your results store and then updates Data Docs.

This makes viewing validation results easy for you and your team.

Usage:
- Run this file: `python day_2020-04-04_crimes_test.py`.
- This can be run manually or via a scheduler such as cron.
- If your pipeline runner supports python snippets you can paste this into your
pipeline.
"""
import sys
from great_expectations import DataContext

# tap configuration
context = DataContext("./great_expectations")
suite = context.get_expectation_suite("day_2020-04-04_crimes")
# You can modify your BatchKwargs to select different data
batch_kwargs = {
    "path": "./super_dan_app/dataset/queried_data/day_2020-04-04|00:26:03_crimes.csv",
    "datasource": "files_datasource",
    "reader_method": "read_csv",
}

# tap validation process
batch = context.get_batch(batch_kwargs, suite)
results = context.run_validation_operator("action_list_operator", [batch])

if not results["success"]:
    print("Validation Failed!")
    sys.exit(1)

print("Validation Succeeded!")
sys.exit(0)
