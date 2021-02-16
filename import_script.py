from adbk.book_app.models import Addressee, Phone, Mail
import csv

with open('99-contacts-addressees.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    objs = []
    for row in reader:
        obj = Addressee()
        obj.name = row[0]
        obj.sex = row[1]
        obj.live = row[2]
        obj.photo = row[3]
        obj.birth = row[4]
        objs.append(obj)
    Addressee.objects.bulk_create(objs)

with open('99-contacts-phones.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    objs = []
    for row in reader:
        obj = Phone()
        obj.user_id = Addressee.objects.get(pk=row[0])
        obj.phone_number = row[1]
        obj.phone_type = row[2]
        objs.append(obj)
    Phone.objects.bulk_create(objs)

with open('99-contacts-mails.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    objs = []
    for row in reader:
        obj = Mail()
        obj.user_id = Addressee.objects.get(pk=row[0])
        obj.mail_address = row[1]
        obj.mail_type = row[2]
        objs.append(obj)
    Mail.objects.bulk_create(objs)

# exec(open('import_script.py').read())
