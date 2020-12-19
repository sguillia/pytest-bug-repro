# Pytest

Run the following

```bash
pytest a/test/main.py
pytest 0/test/main.py
```

The first command fails, the second succeeds. Why?

`a` and `0` have exactly the same layout and contents.  
`0` was created with `cp -R a 0`

I would expect the second line not to work.

## Traces

`a`

```
=========================================== test session starts ============================================
platform linux -- Python 3.7.9, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /path/to/repro
plugins: mock-3.4.0
collected 0 items / 1 error                                                                                

================================================== ERRORS ==================================================
_____________________________________ ERROR collecting a/test/main.py ______________________________________
ImportError while importing test module '/path/to/repro/a/test/main.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/usr/lib/python3.7/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
a/test/main.py:1: in <module>
    import src
E   ModuleNotFoundError: No module named 'src'
========================================= short test summary info ==========================================
ERROR a/test/main.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
============================================= 1 error in 0.05s =============================================
```

`0`

```
=========================================== test session starts ============================================
platform linux -- Python 3.7.9, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /path/to/repro
plugins: mock-3.4.0
collected 1 item                                                                                           

0/test/main.py .                                                                                     [100%]

============================================ 1 passed in 0.01s =============================================
```
