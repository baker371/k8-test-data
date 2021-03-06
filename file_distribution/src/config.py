import os


def get_envar(k, required=True):
    val = os.environ.get(k, None)
    if not val and required:
        exit(f"{k} not supplied")
    return val


class Config(object):
    DEBUG = True
    auth_token = get_envar("auth_token", False)
    download_path = "/usr/src/app"
