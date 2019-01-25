import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Author(User):

    QQ, WeChat, PHONE = ('qq', 'WeChat', 'phone')
    PLATFORM = (
      (QQ, "qq"), (WeChat, "WeChat"), (PHONE, "phone")
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, parent_link=True)
    account_type = models.CharField(verbose_name='登录方式', max_length=16, choices=PLATFORM)
    level = models.CharField(verbose_name='级别', max_length=2, default='0')
    portrait = models.ImageField(upload_to='photos')
    phone = models.CharField(max_length=20, unique=True, verbose_name='手机')
    channel = models.CharField(max_length=225, verbose_name='频道')

    # type = models.CharField(choices=Channel, verbose_name='频道', required=True)
    # tags = models.ManyToManyField(tags, blank=True, verbose_name='标签')

    def __str__(self):
        return self.username


# class Channel(models.Model):
#     Medical, Tourism, Architecture, analysis, Painting, computer, Entertainment, Consumer, Real, Lifestyle, National, = \
#         ('医学', '旅游', '建筑', '数据分析', '绘画', '计算机科学', '娱乐', '消费电子产品', '房地产', '生活方式', '国家政策')
#     GAME, MUSIC, MOVIE, LAW, SCIENCE, DESIGN, BUSINESS, SPORTS, LIFE, ECONOMICS, Dignitary = \
#         ('游戏', '音乐', '电影', '法律', '自然科学', '设计', '商业', '体育', '生活', '经济学', '政要')
#     INTERNET, READING, GOURMET, ANIME, CAR, FINACE, Education, Photography, Professional, Psychology = \
#         ('互联网', '阅读', '美食', '动漫', '汽车', '金融', '教育', '摄影', '职业发展', '心理学')
#     Channel = (
#         (Medical, "医学"), (Tourism, "旅游"), (Architecture, "建筑"), (analysis, "数据分析"), (Painting, "绘画"),
#         (computer, "计算机科学"), (Entertainment, "娱乐"), (Consumer, "消费电子产品"), (Real, "房地产"), (Lifestyle, "生活方式"),
#         (National, "国家政策"), (GAME, "游戏"), (MUSIC, "音乐"), (MOVIE, "电影"), (LAW, "法律"), (SCIENCE, "自然科学"),
#         (DESIGN, "设计"), (BUSINESS, "商业"), (SPORTS, "体育"), (LIFE, "生活"), (ECONOMICS, "经济学"), (Dignitary, "政要"),
#         (INTERNET, "互联网"), (READING, "阅读"), (GOURMET, "美食"), (ANIME, "动漫"), (CAR, "汽车"), (FINACE, "金融"),
#         (Education, "教育"), (Photography, "摄影"), (Professional, "职业发展"), (Psychology, "心理学")
#     )
#
#
# class Attention(models.Model):
#     followig = models.ForeignKey(Author, on_delete=models.CASCADE)
