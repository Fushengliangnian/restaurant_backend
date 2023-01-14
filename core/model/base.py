from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, null=False, help_text="创建时间")
    update_time = models.DateTimeField(auto_now=True, null=False, help_text="更新时间")
    delete_time = models.DateTimeField(null=True, help_text="删除时间")

    class Meta:
        abstract = True


class NotNullCharField(models.CharField):
    def __init__(self, *args, max_length=200, db_collation=None, **kwargs):
        kwargs.update(
            max_length=max_length,
            null=False,
            blank=False,
        )

        super(NotNullCharField, self).__init__(*args, db_collation=db_collation, **kwargs)


class NullCharField(models.CharField):
    def __init__(self, *args, max_length=200, db_collation=None, **kwargs):
        kwargs.update(max_length=max_length, null=True, blank=True)
        super(NullCharField, self).__init__(*args, db_collation=db_collation, **kwargs)
