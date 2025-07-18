from tortoise import fields
from tortoise.models import Model

class User(Model):

    id = fields.IntField(pk=True)  # 자동 증가하는 기본 키 (primary key)
    username = fields.CharField(max_length=20, unique=True)
    email = fields.CharField(max_length=100, unique=True, null=False)



    class Meta:
        table = "user"  # DB에 생성될 테이블

    def __str__(self):
        return f"User(username={self.username}, email={self.email})"
