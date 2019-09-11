Copy Fixture files from google drive into this folder
then run ::

	./manage.py loaddata basicinfos.json
    ./manage.py loaddata schools.json
    ./manage.py loaddata studentstrengths.json

add classes::

	./manage.py shell
	>>> from schools.models import StudentStrength
    >>> from classroom.models import ClassRoom
	>>> rooms = []
    >>> for student in StudentStrength.objects.all():
    ...  rooms.append(ClassRoom(school = student.school, name = student.course, division='A'))
    >>> ClassRoom.objects.bulk_create(rooms)

school name fix::

    >>> from schools.models import School
    >>> for school in School.objects.all():
    ...  name = school.name.replace('.', ' ')
    ...  school.name = name.replace('  ', ' ')
    ...  school.save()

add subjects::

    >>> from quizzes.models import Subject
	>>> for subject in ["Social", "English", "Malayalam"]:
	...  Subject.objects.create(name=subject)

if you want more data, load these::

	./manage.py loaddata staffs.json
	./manage.py loaddata staffstrengths.json

