Client
#############################################

def Auth
===============================================
``def Auth(access_token: str) -> bool``

Stores the token for usage. **Must be called
before using any functions or classes in the
package**

Checks if authentication is successful by calling
https://api.deutschebahn.com/fasta/v1/stations/1
and waiting for non-401 response.

Returns:
    * True if authenticated

Raises:
    * AuthError if not authenticated


@authenticated
==============================================

Decorator to check if authentication is
successful and token is valid.

class AuthError
==============================================

``class AuthError(Exception)``

Exception raised when there's an error in the
authentication process. Specific information
is given when the error is called.