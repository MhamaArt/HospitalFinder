import datetime
import uuid

from peewee import BooleanField, IntegerField, UUIDField, prefetch, DoesNotExist, InterfaceError, DatabaseError, DateTimeField
from peewee import TextField, ForeignKeyField, TimestampField

from database.config import DatabaseModel, db


class SymptomLocation(DatabaseModel):

    id = UUIDField(primary_key=True, default=uuid.uuid4)

    name = TextField(null=False)


class Symptom(DatabaseModel):

    id = UUIDField(primary_key=True, default=uuid.uuid4)

    name = TextField(null=False)

    location = ForeignKeyField(SymptomLocation, related_name='symptom_location', on_delete='CASCADE')

    description = TextField()

    gender = BooleanField()


class Decease(DatabaseModel):

    id = UUIDField(primary_key=True, default=uuid.uuid4)

    name = TextField(null=False)

    description = TextField()


class SymptomDecease(DatabaseModel):
    symptom_id = ForeignKeyField(Symptom, related_name='symptom_decease_id', on_delete='CASCADE')

    decease_id = ForeignKeyField(Decease, related_name='decease_symptom_id', on_delete='CASCADE')


class Speciality(DatabaseModel):

    id = UUIDField(primary_key=True, default=uuid.uuid4)

    name = TextField(null=False)

    description = TextField()


class DeceaseSpeciality(DatabaseModel):

    decease_id = ForeignKeyField(Decease, related_name='decease_speciality_id', on_delete='CASCADE')

    speciality_id = ForeignKeyField(Speciality, related_name='speciality_decease_id', on_delete='CASCADE')


class Doctor(DatabaseModel):

    id = UUIDField(primary_key=True, default=uuid.uuid4)

    first_name = TextField(null=False)

    second_name = TextField(null=False)

    third_name = TextField(null=False)

    phone = TextField()

    cabinet = TextField()


class SpecialityDoctor(DatabaseModel):

    speciality_id = ForeignKeyField(Speciality, related_name='speciality_doctor_id', on_delete='CASCADE')

    doctor_id = ForeignKeyField(Doctor, related_name='doctor_speciality_id', on_delete='CASCADE')


class Clinic(DatabaseModel):

    id = UUIDField(primary_key=True, default=uuid.uuid4)

    name = TextField(null=False)

    location = TextField()

    open_time = DateTimeField()

    close_time = DateTimeField()


class DoctorClinic(DatabaseModel):

    doctor_id = ForeignKeyField(Doctor, related_name='doctor_clinic_id', on_delete='CASCADE')

    clinic_id = ForeignKeyField(Clinic, related_name='clinic_doctor_id', on_delete='CASCADE')


