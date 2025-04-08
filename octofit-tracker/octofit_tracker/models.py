# Added TestModel to the models.py file
class TestModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'octofit'