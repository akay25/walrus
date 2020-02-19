import os


def env(keyname):
    val = os.getenv(keyname)

    if val == None:
        return val

    if val == "True":
        val = True
    elif val == "False":
        val = False
    elif val.find(".") != -1:
        try:
            val = float(val)
        except:
            pass
    else:
        try:
            val = int(val)
        except:
            pass

    return val
