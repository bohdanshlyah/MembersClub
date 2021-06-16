from datetime import datetime

from django.db import models

import re


class Members(models.Model):
    __name_pattern = r'[^a-zA-Z_. ]'
    __email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    def __init__(self):
        self.list_of_members = []


    def get_list_of_members(self):
        return self.list_of_members

    def add_member(self, name, email):
        name_validation = re.findall(Members.__name_pattern, name)
        email_validation = re.match(Members.__email_pattern, email)
        if len(name_validation) != 0:
            return 'Invalid Name'
        else:
            if email_validation is None:
                return 'Invalid Email'
            else:
                self.list_of_members += {
                    'id': len(self.list_of_members)+1,
                    'name': name,
                    'email': email,
                    'r_date': datetime.now(),
                    }
                return self.list_of_members


