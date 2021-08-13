from django.db import models
import datetime
from django.utils.timezone import now

# Create your models here.

"""

List - eg. IMG TODO LIST, cad TODO list
Item - what task it is.

"""
# database model structure


# table
class TodoList(models.Model):
 
    list_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.list_name}"

# table
class TodoItem(models.Model):

    # table_attributes -->columns
    title = models.CharField(max_length=100)
    checked = models.BooleanField(default=False)
    due_date= models.DateTimeField(default=datetime.datetime.now())

    # foreignkey 
    todo_list = models.ForeignKey(to=TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.todo_list.list_name}: {self.title}"