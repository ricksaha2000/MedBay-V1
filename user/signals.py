from .constants import UserTypes


def pre_save_user_model(instance, sender, *args, **kwargs):
    instance.is_active = True
