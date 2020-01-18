"""
1.py, by Taufan Prihantoro, 2020-01-18
This program create a JSON output.
"""
# IMPORT JSON
import json

# FUNGSI Biodata
def biodataUser(name, age):
    userName = name
    userAge = age
    
    listJson={
        'Name':userName,
        'Age':userAge,
        'address':'Bandung, Jawa Barat',
        'hobbies':[
            'playing games',
            'designing UI'
        ],
        'is_married': True,
        'list_school':{
            'year_in': 2013,
            'year_out': 2016,
            'major': 'Teknik Jaringan Akses'
        },
        'skills':{
            'Python':'beginner',
            'PHP':'beginner',
            'UI Design': 'advanced',
            'HTML':'expert',
            'CSS':'expert'
        },
        'interest_in_coding': True
    }
    print (json.dumps(listJson))
