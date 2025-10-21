from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data (dependents first)
        for obj in Leaderboard.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Activity.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.pk:
                obj.delete()
        for obj in User.objects.all():
            if obj.pk:
                obj.delete()
        for obj in Team.objects.all():
            if obj.pk:
                obj.delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Users
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Activities
        Activity.objects.create(user=spiderman, type='Running', duration=30, date='2025-10-21')
        Activity.objects.create(user=ironman, type='Cycling', duration=45, date='2025-10-20')
        Activity.objects.create(user=batman, type='Swimming', duration=60, date='2025-10-19')
        Activity.objects.create(user=superman, type='Yoga', duration=20, date='2025-10-18')

        # Workouts
        cardio = Workout.objects.create(name='Cardio', description='Cardio session')
        strength = Workout.objects.create(name='Strength', description='Strength training')
        cardio.suggested_for.add(marvel, dc)
        strength.suggested_for.add(marvel)

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
