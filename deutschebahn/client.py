import requests


class AuthError(Exception):
    def __init__(self, message):
        """
            :arg message: Message to print out in case this error is raised
        """
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


def Auth(access_token: str) -> bool:
    """
    Stores the access token for use in the API. Must be called before
    using any function!

    **Make sure that you are subscribed to the relevant modules!**

    :arg access_token: The token provided to you by the DB API.

    """
    global __TOKEN__

    if type(access_token) != str:
        raise ValueError("Token must be a string")

    if __TOKEN__ is None:
        __TOKEN__ = access_token
    elif requests.get('https://api.deutschebahn.com/fasta/v1/stations/1',
                          headers={"Authorization": f"Bearer {__TOKEN__}"}).status_code == 401:
        raise AuthError("Invalid Credentials.")
    else:
        raise RuntimeError("Already authenticated")
    return True


# Check global variables not null
def authenticated(f):
    """
    decorator that runs the function only if __TOKEN__ exists and if token is valid

    :arg f: function given below the decorator
    :return: f(*args, **kwargs**)
    """

    def wrapper(*args, **kwargs):

        if __TOKEN__ is None:
            raise AuthError("Not authenticated")
        elif requests.get('https://api.deutschebahn.com/fasta/v1/stations/1',
                          headers={"Authorization": f"Bearer {__TOKEN__}"}).status_code == 401:
            raise AuthError("Invalid Credentials.")
        else:
            return f(*args, **kwargs)

    return wrapper


__TOKEN__ = None
