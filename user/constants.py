import enum


class CustomEnum(enum.Enum):

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class UserTypes(CustomEnum):
    PATIENT = "PATIENT"
    DOCTOR = "DOCTOR"
    ADMIN = "ADMIN"
    PERSONAL_ASSISTANT = "PERSONAL_ASSISTANT"
    HOSPITAL_STAFF = "HOSPITAL_STAFF"
    SELLER = "SELLER"
    PHARMACY = "PHARMACY"


USER_APP_MAPPING = {
    UserTypes.PATIENT.value: 'patient',
    UserTypes.DOCTOR.value: 'doctor',
    UserTypes.ADMIN.value: 'medbay_admin',
    UserTypes.PERSONAL_ASSISTANT.value: 'personal_assistant',
    UserTypes.HOSPITAL_STAFF.value: 'hospital_staff',
    UserTypes.SELLER.value: 'seller',
    UserTypes.PHARMACY.value: 'pharmacy',
}


class GenderTypes(CustomEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    CANNOT_SPECIFY = "CANNOT_SPECIFY"


class Messages(CustomEnum):
    LOGIN_FAILURE = "Username and Password doesn't match"
