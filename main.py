try:
    import ctypes
    myappid = 'kerbalapp.cardmatching.github.one'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except Exception:
    pass

if __name__ == "__main__":
    import sys
    from package import app
    sys.exit(app.run())