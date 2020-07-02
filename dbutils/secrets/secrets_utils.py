from typing import List


def get(scope: str, key: str) -> str:
    """
    Gets the string representation of a secret value with scope and key
    """
    print("skip dbutils.secrets.get({},{})".format(scope, key))
    return ''


def getBytes(scope: str, key: str) -> str:
    """
    Gets the bytes representation of a secret value with scope and key
    """
    print("skip dbutils.secrets.get({},{})".format(scope, key))
    return ''


def list(scope: str) -> List[str]:
    """
    Lists secret metadata for secrets within a scope
    """
    rtn: List[str] = []
    print("skip dbutils.secrets.list({})".format(scope))
    return rtn


def listScopes() -> List[str]:
    """
    Lists secret scopes
    """
    rtn: List[str] = []
    print("skip dbutils.secrets.listScopes()")
    return rtn
