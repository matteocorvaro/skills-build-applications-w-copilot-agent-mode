from django.core.management import execute_from_command_line
import os
import traceback

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
import django

django.setup()

# Updated to use TestModel from octofit_tracker.models
from octofit_tracker.models import TestModel

# Test with a supported query
try:
    # Create a test table and insert a record
    TestModel.objects.create(name="Test Record")
    print("Successfully inserted a record into the test table.")

    # Query the test table
    record = TestModel.objects.first()
    print(f"Queried record: {record.name}")
except Exception as e:
    print(f"Database operation failed: {e}")
    traceback.print_exc()
