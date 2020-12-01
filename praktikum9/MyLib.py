import Globals


def CheckOnOff():
    return Globals.g_onoff


def TurnOnOff():
    if CheckOnOff():
        Globals.g_onoff = False
        print("Ac Berhasil Mati")
    else:
        Globals.g_onoff = True
        print("Ac Berhasil Hidup")


def TempUp():
    if CheckOnOff():
        if Globals.g_temp < 28 and Globals.g_temp > 18:
            Globals.g_temp += 1


def TempDown():
    if CheckOnOff():
        if Globals.g_temp < 28 and Globals.g_temp > 18:
            Globals.g_temp -= 1


def FanSpeed():
    if CheckOnOff():
        if (Globals.g_fanlevel < 4):
            Globals.g_fanlevel += 1
        else:
            Globals.g_fanlevel = 1


def PowerChill():
    if CheckOnOff():
        Globals.g_fanlevel = 4
        Globals.g_temp = 18


def Display():
    print("Temperatur Suhu : ", Globals.g_temp)
    print("Level Kipas : ", Globals.g_fanlevel)
