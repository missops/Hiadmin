from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class DailyReport(models.Model):
    CAT_CHOICE = (
        ('0', '工作日报'),
        ('1', '项目报告'),
        ('2', '投产报告'),
        ('3', '其他任务')
    )
    category = models.CharField("分类", max_length=20, choices=CAT_CHOICE, default='0')
    content = models.TextField("内容")
    user = models.ForeignKey(User, related_name='report_user', on_delete=models.DO_NOTHING, default='')
    start_time = models.DateTimeField(default='', verbose_name='开始时间')
    end_time = models.DateTimeField(default='', verbose_name='结束时间')
    add_time = models.DateField(auto_now_add=True, verbose_name="添加时间")

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = '工作日报'
        verbose_name_plural = verbose_name
