from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

class Camera(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cam_number = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'Camera number {self.cam_number} for user {self.user_id}.'

class Rule(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rule = models.CharField(max_length=240)
    camera_id = models.ForeignKey(Camera, on_delete=models.CASCADE)

    def __str__(self):
        return f'Rule: "{self.rule}" for user {self.user_id} on camera {self.camera_id}.'
