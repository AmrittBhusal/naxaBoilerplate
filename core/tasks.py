from celery import  shared_task
from core.models import Summary
from core.views import SummarySerializer
from django.core.management import call_command

# from django.core.management.base import BaseCommand
# from faker import Faker
# from django .utils import timezone
# import random
# from core.models import Deparment,project
# # from django.contrib.auth.models import User
# from user.models import UserProfile
# from datetime import timedelta

@shared_task
def add(x,y):
    return x+y


# @shared_task
def update_summary_everynight():

    summaries= Summary.objects.all()
    for summary in summaries:
        print("--------------------", summary)
        return summary


# @shared_task
# class Command(BaseCommand):

#     def handle(self, *args, **kwargs):
#         fake= Faker()

#         faker=fake.seed_instance(timezone.now().timestamp())
#         user_id= random.randint(1,10)
#         department_id = random.randint(1, 10)
#         department_instance, created = Deparment.objects.get_or_create(id=department_id)
#         status= random.choice(['True','False'])
#         userprofile_instance= UserProfile.objects.get(id=user_id)

#         created_at=timezone.now() - timedelta(days=random.randint(0,365))
#         end_at=created_at + timedelta(days=random.randint(0,30))

#         # print("======================================================")
#         # print(end_at)
#         # print(userprofile_instance)
#         # project_bulk=[]
#         for _ in range(1):
#             data={
#                 'project_name':fake.word(),
#                 'department_field':department_instance,
#                 'start_date':created_at,
#                 'end_date':end_at,
#                 'is_active':status
#             }
#             project.objects.create(**data)
#             # projects=project(**data)
#             # project_bulk.append(projects)
@shared_task
def calling_fake_project_data():
    call_command('fake_project_data')

