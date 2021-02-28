import csv
import os

import django
from django.db import IntegrityError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'paper_search.settings')
django.setup()
from paper.models import PaperLength


def read_paper_length(filename):
    with open(filename, 'r')as opener:
        number = 0
        reader = csv.reader(opener)
        for r in reader:
            paper_id, paper_length = r
            try:
                paper_len = PaperLength.objects.create(paper_id=paper_id, length=paper_length)
            except IntegrityError:
                continue
            number += 1
            # print('created', number, paper_id)


import os

files = os.listdir('.')

for file in files:
    if file.startswith('doc_length'):
        print('write file', file)
        read_paper_length(file)
