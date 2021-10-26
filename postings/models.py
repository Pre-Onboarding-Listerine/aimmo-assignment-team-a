from django.db    import models
from django.db.models.deletion import CASCADE

from core.models  import TimeStampModel


class Posting(TimeStampModel):
    title   = models.CharField(max_length = 128)
    author  = models.CharField(max_length = 64)
    content = models.TextField()
    user    = models.ForeignKey('users.User', on_delete = models.CASCADE)

    class Meta:
        db_table = 'postings'