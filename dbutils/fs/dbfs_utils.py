import os
import glob
import shutil
from typing import List


def is_local(path: str) -> bool:
    return path.startswith("file:")


def local_path(full_path: str) -> str:
    return full_path[7:]


def cp(path_from: str, path_to: str, recurse: bool = False) -> bool:
    """
    Copies a file or directory, possibly across FileSystems
    """
    if is_local(path_from) and is_local(path_to):
        if os.path.exists(local_path(path_to)):
            shutil.rmtree(local_path(path_to), ignore_errors=True)
        if recurse:
            shutil.copytree(local_path(path_from), local_path(path_to))
        else:
            shutil.copy(local_path(path_from), local_path(path_to))
        return True
    print("skip: dbutils.fs.mv({},{})".format(path_from, path_to))
    return False


def head(file: str, maxBytes: int = 65536) -> str:
    """
    Returns up to the first 'maxBytes' bytes of the given file as a String encoded in UTF-8
    """
    rtn = ''
    if is_local(file):
        with open(local_path(file), 'r', encoding='UTF-8') as f:
            rtn = f.read(maxBytes)
    else:
        print("skip: dbutils.fs.head({},{})".format(file, maxBytes))
    return rtn


def ls(dir: str) -> List:
    """
    Lists the contents of a directory
    """
    rtn = list()
    if is_local(dir):
        if not os.path.exists(local_path(dir)):
            raise FileNotFoundError
        for f in glob.glob(dir[7:] + "/*"):
            ff = f.replace('//', '/')
            rtn.append(FileInfo("file://{}".format(ff)))
    else:
        print("skip: dbutils.fs.ls({})".format(dir))
    return rtn


def mkdirs(dir: str) -> bool:
    """
    Creates the given directory if it does not exist, also creating any necessary parent directories
    """
    if is_local(dir):
        os.makedirs(local_path(dir), exist_ok=True)
        return True
    print("skip: dbutils.fs.mkdirs({})".format(dir))
    return False


def mv(path_from: str, path_to: str) -> bool:
    """
    Moves a file or directory, possibly across FileSystems
    """
    if is_local(path_from) and is_local(path_to):
        if os.path.exists(local_path(path_to)):
            shutil.rmtree(local_path(path_to), ignore_errors=True)
        shutil.move(local_path(path_from), local_path(path_to))
        return True
    print("skip: dbutils.fs.mv({},{})".format(path_from, path_to))
    return False


def put(file: str, contents: str, overwrite: bool = False) -> bool:
    """
    Writes the given String out to a file, encoded in UTF-8
    """
    if is_local(file):
        if not overwrite and os.path.exists(local_path(file)):
            raise Exception('already exist: {}'.format(file))
        with open(local_path(file), 'w', encoding='UTF-8') as f:
            f.write(contents)
        return True
    print("skip: dbutils.fs.put({},{},{})".format(file, contents, overwrite))
    return False


def rm(dir: str, recurse: bool = False) -> bool:
    """
    Removes a file or directory
    """
    if dir.startswith("file:"):
        shutil.rmtree(dir[7:], recurse)
        return True
    print("skip: dbutils.fs.rm({},{})".format(dir, recurse))
    return False


class FileInfo:
    def __init__(self, path: str):
        self.path = path
        self.name = path.split('/')[-1]
        self.isFile = os.path.isfile(local_path(path))
        self.size = 0
        if not os.path.isdir(path[7:]):
            self.size = os.path.getsize(local_path(path))

    def __str__(self) -> str:
        return "FileInfo(path='{}', name='{}', size={})".format(self.path, self.name, self.size)

    def __repr__(self) -> str:
        return self.__str__()

    def isDir(self) -> bool:
        return os.path.isdir(self.path[7:])


def mount(source: str, mountPoint: str, encryptionType: str = "", owner: str = None, extraConfigs: dict = None) -> bool:
    print("skip: dbutils.fs.mount({},{},{},{},{})".format(source, mountPoint, encryptionType, owner, extraConfigs))
    return False


def mounts() -> List[str]:
    print("skip: dbutils.fs.mounts()")
    return list()


def refreshMounts() -> bool:
    print("skip: dbutils.fs.refreshMounts()")
    return False


def unmount(mountPoint: str) -> bool:
    print("skip: dbutils.fs.unmount({})".format(mountPoint))
    return False
