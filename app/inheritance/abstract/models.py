"""
1. AbstractBaseClasses
    부모는 테이블이 없고, 자식은 테이블이 있음
2. Multitable inheritance
    부모와 자식 모두 테이블이 있음
3. Proxy model
    부모는 테이블이 있고, 자식은 테이블이 없음
"""

from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    # 상속받은 자식 클래스에서 부모 클래스의 Meta 속성을 가지면서 자신만의 속성을 추가하고 싶다면
    # <부모 클래스>, Meta를 상속받고, 나머지 피룡한 속성들을 정의
    # 아래 경우, 부모로부터 ordering 속성을 상속받음
    class Meta:
        # abstract = True
        # ordering = ['name']
        verbose_name = '학생'
        verbose_name_plural = '학생 목록'
        db_table = 'Abstract_Student_Table'

    def __str__(self):
        return f'{self.name} (학교: {self.school})'


class Student(CommonInfo):
    school = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} (학교: {self.school})'


class Instructor(CommonInfo):
    academy = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} (학원: {self.academy})'


# be careful with related_name and related_query_name
class Base(models.Model):
    m2m = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_set')

    class Meta:
        abstract = True


class ChildA(Base):
    pass


class ChildB(Base):
    pass
