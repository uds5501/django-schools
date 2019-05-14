Copy Fixture files from google drive into this folder
then run ::

    ./manage.py loaddata schools.json
    ./manage.py loaddata studentstrengths.json

add classes::

	./manage.py shell
	>>> from schools.models import StudentStrength, Course
	>>> courses = []
    >>> for student in StudentStrength.objects.all():
    ...  courses.append(Course(school = student.school, name = "{0}A".format(student.course)))
    >>> Course.objects.bulk_create(courses)

add subjects::

    >>> from quizzes.models import Subject
	>>> for subject in ["Social", "English", "Malayalam"]:
	...  Subject.objects.create(name=subject)

if you want more data, load these::

	./manage.py loaddata basicinfos.json
	./manage.py loaddata staffs.json
	./manage.py loaddata staffstrengths.json
	./manage.py loaddata studentstrengths.json

