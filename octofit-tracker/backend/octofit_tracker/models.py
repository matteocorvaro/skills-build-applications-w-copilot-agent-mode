from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        app_label = 'octofit_tracker'

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.email} - {self.activity_type}"

    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.score}"

    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'octofit_tracker'

class TestModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'octofit_tracker'
