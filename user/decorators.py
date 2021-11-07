from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from .constants import UserTypes


def patient_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):

    custom_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type == UserTypes.PATIENT.value,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return custom_decorator(function)
    return custom_decorator


def doctor_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):

    custom_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type == UserTypes.DOCTOR.value,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return custom_decorator(function)
    return custom_decorator


def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):

    custom_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type == UserTypes.ADMIN.value,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return custom_decorator(function)
    return custom_decorator


def pa_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):

    custom_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type == UserTypes.PERSONAL_ASSISTANT.value,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return custom_decorator(function)
    return custom_decorator


def staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):

    custom_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type == UserTypes.HOSPITAL_STAFF.value,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return custom_decorator(function)
    return custom_decorator


def seller_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):

    custom_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type == UserTypes.SELLER.value,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return custom_decorator(function)
    return custom_decorator


def pharmacy_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):

    custom_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type == UserTypes.PHARMACY.value,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return custom_decorator(function)
    return custom_decorator


def custom_role_required(roles, function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None):
    custom_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.user_type in roles,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return custom_decorator(function)
    return custom_decorator
