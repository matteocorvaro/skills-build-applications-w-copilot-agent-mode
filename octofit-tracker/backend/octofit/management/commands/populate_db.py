from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Use pymongo for database operations
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many([
            {"email": "thundergod@mhigh.edu", "name": "Thor"},
            {"email": "metalgeek@mhigh.edu", "name": "Tony Stark"},
            {"email": "zerocool@mhigh.edu", "name": "Steve Rogers"},
            {"email": "crashoverride@mhigh.edu", "name": "Natasha Romanoff"},
            {"email": "sleeptoken@mhigh.edu", "name": "Bruce Banner"},
        ])

        teams = [
            {"name": "Blue Team", "members": ["thundergod@mhigh.edu", "metalgeek@mhigh.edu"]},
            {"name": "Gold Team", "members": ["zerocool@mhigh.edu", "crashoverride@mhigh.edu", "sleeptoken@mhigh.edu"]},
        ]
        db.teams.insert_many(teams)

        activities = [
            {"user": "thundergod@mhigh.edu", "activity_type": "Cycling", "duration": 60},
            {"user": "metalgeek@mhigh.edu", "activity_type": "Crossfit", "duration": 120},
            {"user": "zerocool@mhigh.edu", "activity_type": "Running", "duration": 90},
            {"user": "crashoverride@mhigh.edu", "activity_type": "Strength", "duration": 30},
            {"user": "sleeptoken@mhigh.edu", "activity_type": "Swimming", "duration": 75},
        ]
        db.activity.insert_many(activities)

        leaderboard = [
            {"team": "Blue Team", "score": 100},
            {"team": "Gold Team", "score": 90},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {"name": "Cycling Training", "description": "Training for a road cycling event"},
            {"name": "Crossfit", "description": "Training for a crossfit competition"},
            {"name": "Running Training", "description": "Training for a marathon"},
            {"name": "Strength Training", "description": "Training for strength"},
            {"name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
