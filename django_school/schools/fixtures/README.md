Copy Fixture files from google drive into this folder
then run ::

	./manage.py loaddata basicinfos.json
    ./manage.py loaddata schools.json
    ./manage.py loaddata studentstrengths.json

add classes::

	./manage.py shell
	>>> from schools.models import StudentStrength, ClassRoom
	>>> rooms = []
    >>> for student in StudentStrength.objects.all():
    ...  rooms.append(ClassRoom(school = student.school, name = "{0}A".format(student.course)))
    >>> ClassRoom.objects.bulk_create(rooms)

add subjects::

    >>> from quizzes.models import Subject
	>>> for subject in ["Social", "English", "Malayalam"]:
	...  Subject.objects.create(name=subject)

if you want more data, load these::

	./manage.py loaddata staffs.json
	./manage.py loaddata staffstrengths.json
	./manage.py loaddata studentstrengths.json

