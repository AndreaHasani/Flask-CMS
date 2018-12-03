from functools import wraps
from flask import request, current_app
from flask_login import current_user
from SCMS.core.models import Users


def login_required(*role_names):
    """
    Example::
        @route('/escape')
        @login_required('Special', 'Agent')
        def escape_capture():  # User must be 'Special' AND 'Agent'

        @route('/escape')
        @login_required('Special', ('Agent', 'reader')) -> OR case
        def escape_capture():  # User must be 'Special' AND 'Agent'

    | If role_names = None,  this will act as a login_required
    | Checking is lowercase, Reader == reader -> True
    """
    def wrapper(f):

        @wraps(f)
        def decorator(*args, **kwargs):

            if None in role_names:
                return f(*args, **kwargs)

            if not current_user.is_authenticated:
                return current_app.login_manager.unauthorized()
            if not current_user.has_roles(*role_names):
                return current_app.login_manager.unauthorized()

            return f(*args, **kwargs)

        return decorator

    return wrapper
