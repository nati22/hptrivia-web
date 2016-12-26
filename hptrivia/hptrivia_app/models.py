from __future__ import unicode_literals

from django.db import models

from django.utils import timezone


class BaseModel(models.Model):

    class Meta:
        abstract = True

    created_datetime = models.DateTimeField('date created', null=False)
    modified_datetime = models.DateTimeField('date modified', null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_datetime = timezone.now()
        self.modified_datetime = timezone.now()


class Question(BaseModel):
    HARRY_POTTER_BOOKS = (
        (1, 'Harry Potter and the Philosopher\'s Stone'),
        (2, 'Harry Potter and the Chamber of Secrets'),
        (3, 'Harry Potter and the Prisoner of Azkaban'),
        (4, 'Harry Potter and the Goblet of Fire'),
        (5, 'Harry Potter and the Order of the Phoenix'),
        (6, 'Harry Potter and the Half-Blood Prince'),
        (7, 'Harry Potter and the Deathly Hallows')
    )

    question_text = models.CharField(max_length=500, null=False, blank=False)
    correct_answer_text = models.CharField(max_length=500, null=False, blank=False)
    wrong_answer1_text = models.CharField(max_length=500, null=False, blank=False)
    wrong_answer2_text = models.CharField(max_length=500, null=False, blank=False)
    wrong_answer3_text = models.CharField(max_length=500, null=False, blank=False)

    book_number = models.IntegerField(choices=HARRY_POTTER_BOOKS, null=True, blank=False)

    def save(self, *args, **kwargs):
        super(Question, self).save(*args, **kwargs)
