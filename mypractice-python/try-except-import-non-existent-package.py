# 22.12 Trying to import a nonexistent package
try:
    import wrong_package
except ImportError as e:
    print("Oops! Module Not Found.")
    print(format(e))