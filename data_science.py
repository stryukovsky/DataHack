import os

import django
from django_pandas.io import read_frame
import pandas

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'


def main():
    django.setup()
    from main.models import University
    universities = University.objects.filter(rating_position__lt=99).filter(sum__gt=0)
    data = read_frame(universities)
    print(data.columns)
    data['sum_per_student'] = [university.sum // university.students_count for university in universities]
    q: pandas.DataFrame = data.loc[:, ['abbreviation', 'sum', 'rating_position', 'sum_per_student']]
    print(q.corr())


if __name__ == "__main__":
    main()
