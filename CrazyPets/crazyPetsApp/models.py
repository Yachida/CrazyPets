from django.db import models


class Pet(models.Model):
    # CreatePets
    # 'mouse_x', 'mouse_y', 'eye_right_x', 'eye_right_y', 'eye_left_x', 'eye_left_y', 'nose_right_x', 'nose_right_y'
    mouth_x = models.FloatField()
    mouth_y = models.FloatField()
    eye_right_x = models.FloatField()
    eye_right_y = models.FloatField()
    eye_left_x = models.FloatField()
    eye_left_y = models.FloatField()
    nose_x = models.FloatField()
    nose_y = models.FloatField()

class Pets(models.Model):
    mouth_x = models.FloatField()
    mouth_y = models.FloatField()
    eye_right_x = models.FloatField()
    eye_right_y = models.FloatField()
    eye_left_x = models.FloatField()
    eye_left_y = models.FloatField()
    nose_x = models.FloatField()
    nose_y = models.FloatField()
    # STATUS_DRAFT = "draft"
    # STATUS_PUBLIC = "public"
    # STATUS_SET = (
    #         (STATUS_DRAFT, "下書き"),
    #         (STATUS_PUBLIC, "公開中"),
    # )
    # title = models.CharField(max_length=128)
    # body = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    # author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
