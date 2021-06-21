from datetime import datetime
from django.core.exceptions import ValidationError

import re

list_of_members = [
                {
                    'id': 1,
                    'name': 'First Member',
                    'email': 'firstmember@gmail.com',
                    'r_date': datetime.now().strftime("%d.%m.%Y"),
                }
            ]

def get_list_of_members(member={}):
    if member != {}:
        list_of_members.append(member)
    return list_of_members

def add_member(name, email):
        __name_pattern = r'[^a-zA-Z_. ]'
        __email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        name_validation = re.findall(__name_pattern, name)
        email_validation = re.match(__email_pattern, email)

        if len(name_validation) != 0:
            raise ValidationError('Invalid Name!')
        else:
            if email_validation is None:
                raise ValidationError('Invalid Email!')
            else:
                list_of_members = get_list_of_members()
                for i in list_of_members:
                    if i['email'] == email:
                        raise ValidationError('Email already exist!')
                member = {
                    'id': len(list_of_members)+1,
                    'name': name,
                    'email': email,
                    'r_date': datetime.now().strftime("%d.%m.%Y"),
                    }
                list_of_members = get_list_of_members(member)


