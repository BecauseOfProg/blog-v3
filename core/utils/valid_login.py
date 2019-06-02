from argon2 import PasswordHasher, exceptions
from pony.orm import db_session
from app.models.user import User
import bcrypt


@db_session
def valid_login(email, password):
    '''Validate user login with the e-mail adress
    and the given password (return True/False)'''
    try:
        p = User.get(email=email)
        # We try to find the user using the given e-mail adress
        if p.password_type == "bcrypt":
            # If the password is encrypted with bcrypt
            return bcrypt.checkpw(bytes(password, "utf-8"),
                                  bytes(p.hashed, "utf-8"))
        elif p.password_type == "argon2":
            # Elif the password is encrypted with Argon2
            ph = PasswordHasher()
            try:
                return ph.verify(p.hashed, password)
            except exceptions.VerifyMismatchError:
                return False
    except:
        # e-mail adress not found in the DB -> wrong login/password
        return False
