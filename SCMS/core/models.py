from SCMS import db, login_manager
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    active = db.Column(db.Boolean())

    # Relationships
    roles = db.relationship('Role', secondary='user_roles')
    posts = db.relationship('Posts', backref='author', lazy=True)

    def get_roles(self):
        return [item.name.lower() for item in self.roles]

    def add_role(self, role):
        self.roles.append(Role(name=role))
        db.session.commit()

    def remove_role(self, role):
        # Checking if role exist, needs improvements

        roles = [r.name for r in self.roles]
        try:
            self.roles.pop(roles.index(role))
        except ValueError:
            raise ValueError('Role not found on user: %s' % self.username)
        except Exception as e:
            raise

    def has_roles(self, *requirements):
        """ Return True if the user has all of the specified roles. Return False otherwise.
            has_roles() accepts a list of requirements:
                has_role(requirement1, requirement2, requirement3).
            Each requirement is either a role_name, or a tuple_of_role_names.
                role_name example:   'manager'
                tuple_of_role_names: ('funny', 'witty', 'hilarious')
            A role_name-requirement is accepted when the user has this role.
            A tuple_of_role_names-requirement is accepted when the user has ONE of these roles.
            has_roles() returns true if ALL of the requirements have been accepted.
            For example:
                has_roles('a', ('b', 'c'), d)
            Translates to:
                User has role 'a' AND (role 'b' OR role 'c') AND role 'd'

                |Added: Lowercase checking
                """

        # Translates a list of role objects to a list of role_names
        role_names = [item.name.lower() for item in self.roles]

        for requirement in requirements:
            if isinstance(requirement, (list, tuple)):
                tuple_of_role_names = requirement
                authorized = False
                for role_name in tuple_of_role_names:
                    if role_name.lower() not in role_names:
                        authorized = True
                        break
                if not authorized:
                    return False
            else:
                role_name = requirement
                if role_name.lower() not in role_names:
                    return False

        # All requirements have been met: return True
        return True

    def __repr(self):
        return f"User('{self.username}'), '{self.email}')"

    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email
        self.active = 1


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)

# Define the Role data-model


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(db.Model):
    """User roles, normal roles are
    :reader
    :admin
    :contributor
    :author
    """
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey(
        'roles.id', ondelete='CASCADE'))

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
