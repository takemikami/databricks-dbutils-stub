# databricks-dbutils-stub

Test-stub for databricks utilities 'dbutils'.

see. https://docs.databricks.com/dev-tools/databricks-utils.html

## Install

Run following command.

```
pip install git+https://github.com/takemikami/databricks-dbutils-stub@master
```

If you like install from ``test-requirements.txt``,  
make ``test-requirements.txt`` includes following.  
and run ``pip install -r test-requirements.txt``.

```
-e git+https://github.com/takemikami/databricks-dbutils-stub@master#egg=databricks-dbutils-stub
```

## Example

This test stub support to write unit tests for your function that use dbutils,  
like following sample code.

```python
import dbutils

def print_file_list(path):
    files = dbutils.fs.ls(path)
    print(files)

print_file_list('file:///tmp')  # for unit test at local machine
print_file_list('dbfs:///tmp')  # for production at databricks
```
