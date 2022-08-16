import os

import pyautogui
from datetime import datetime, timedelta
import keyboard
import random
import asyncio


async def boi_smart():  # функция проождения подземелий мулами. Используются основные амулеты,
    # такие как зб, яра, взрыв, приток. По достижению окончания метро выходит
    # из цикла
    timeStartBoi = datetime.now()
    timeFinishBoi = timeStartBoi + timedelta(seconds=150)

    while timeStartBoi < timeFinishBoi:

        playvmmo = pyautogui.locateOnScreen('images/playvmmo.PNG', grayscale=True, region=(0, 0, 600, 1000),
                                            confidence=0.85)
        nazad = pyautogui.locateOnScreen('images/nazad.PNG', grayscale=True, region=(0, 0, 600, 1000),
                                         confidence=0.85)
        proda = pyautogui.locateOnScreen('images/proda.PNG', grayscale=True, region=(0, 0, 600, 1000),
                                         confidence=0.85)
        psevdoVhod = pyautogui.locateOnScreen('images/psevdoVhod.PNG', grayscale=True, region=(0, 0, 600, 1000),
                                              confidence=0.85)
        psevdoVhod2 = pyautogui.locateOnScreen('images/psevdoVhod2.PNG', grayscale=True, region=(0, 0, 600, 1000),
                                               confidence=0.85)

        list_boi = os.listdir('boi')

        for b in list_boi:
            full_boi = "boi/" + b
            button = pyautogui.locateOnScreen(full_boi, grayscale=True, region=(0, 300, 700, 900), confidence=0.9)
            if button:
                pyautogui.click(button)
                await asyncio.sleep(0.1)

        if playvmmo:
            pyautogui.click(nazad)
            await asyncio.sleep(1)

        elif proda or psevdoVhod or psevdoVhod2:  # когда появляется ссылка поделится с друзьями бой заканчивается либо конец квеста
            break
        timeStartBoi: datetime = datetime.now()
        await asyncio.sleep(0.1)


async def boi_smart_2():  # функция проождения подземелий мулами. Используются основные амулеты,
    # такие как зб, яра, взрыв, приток. По достижению окончания метро выходит
    # из цикла
    timeStartBoi2 = datetime.now()
    timeFinishBoi2 = timeStartBoi2 + timedelta(seconds=150)

    while timeStartBoi2 < timeFinishBoi2:

        theEnd = pyautogui.locateOnScreen('images/TheEnd.PNG', grayscale=True, region=(0, 0, 600, 1000),
                                          confidence=0.85)

        list_boi = os.listdir('boi')

        for c in list_boi:
            full_boi = "boi/" + c
            button = pyautogui.locateOnScreen(full_boi, grayscale=True, region=(0, 300, 700, 900), confidence=0.9)
            if button:
                pyautogui.click(button)
                await asyncio.sleep(0.1)

        if theEnd:  # когда появляется ссылка поделится с друзьями бой заканчивается либо конец квеста
            break
        timeStartBoi2: datetime = datetime.now()
        await asyncio.sleep(0.1)

    #  ---------------------------------------------------------------------------------
    #  -----------------БОЙ СМАРТ ДЛЯ ВКЛАДКИ СПРАВА-------------------------------------


async def boi_smart_pravo():  # функция проождения подземелий мулами. Используются основные амулеты,
    # такие как зб, яра, взрыв, приток. По достижению окончания метро выходит
    # из цикла
    timeStartBoi = datetime.now()
    timeFinishBoi = timeStartBoi + timedelta(seconds=150)

    while timeStartBoi < timeFinishBoi:

        playvmmo = pyautogui.locateOnScreen('images/playvmmo.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                            confidence=0.85)
        nazad = pyautogui.locateOnScreen('images/nazad.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                         confidence=0.85)
        proda = pyautogui.locateOnScreen('images/proda.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                         confidence=0.85)
        psevdoVhod = pyautogui.locateOnScreen('images/psevdoVhod.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                              confidence=0.85)
        psevdoVhod2 = pyautogui.locateOnScreen('images/psevdoVhod2.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                               confidence=0.85)

        list_boi = os.listdir('boi2')

        for b in list_boi:
            full_boi = "boi2/" + b
            button = pyautogui.locateOnScreen(full_boi, grayscale=True, region=(1150, 300, 1880, 900), confidence=0.9)
            if button:
                pyautogui.sleep(0.1 * random.random())
                pyautogui.click(button)
                await asyncio.sleep(0.1)

        if playvmmo:
            pyautogui.click(nazad)
            await asyncio.sleep(1)

        elif proda or psevdoVhod or psevdoVhod2:  # когда появляется ссылка поделится с друзьями бой заканчивается
            break  # либо конец квеста
        timeStartBoi: datetime = datetime.now()
        await asyncio.sleep(0.1)


async def boi_smart2_pravo():  # функция проождения подземелий мулами. Используются основные амулеты,
    # такие как зб, яра, взрыв, приток. По достижению окончания метро выходит
    # из цикла
    timeStartBoi2 = datetime.now()
    timeFinishBoi2 = timeStartBoi2 + timedelta(seconds=150)

    while timeStartBoi2 < timeFinishBoi2:

        theEnd = pyautogui.locateOnScreen('images/TheEnd.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                          confidence=0.85)

        list_boi = os.listdir('boi2')

        for c in list_boi:
            full_boi = "boi2/" + c
            button = pyautogui.locateOnScreen(full_boi, grayscale=True, region=(1150, 300, 1880, 900), confidence=0.9)
            if button:
                pyautogui.click(button)
                await asyncio.sleep(0.1)

        if theEnd:  # когда появляется ссылка поделится с друзьями бой заканчивается либо конец квеста
            break
        timeStartBoi2: datetime = datetime.now()
        await asyncio.sleep(0.1)

    #  -----------------------------------------------------------------------


def zakritie():
    list_exit = os.listdir('pomeha')
    while True:
        for p in list_exit:
            full_exit = "pomeha/" + p
            button_exit = pyautogui.locateOnScreen(full_exit, grayscale=True, region=(0, 180, 700, 1000),
                                                   confidence=0.85)
            if button_exit:
                pyautogui.click(button_exit)
                pyautogui.sleep(0.8)
                keyboard.send("F5")
                pyautogui.sleep(1.3)
                # keyboard.send("F5")
                # pyautogui.sleep(1.3)
        else:
            break


def zakritie_pravo():
    list_exit = os.listdir('pomeha')
    while True:
        for p in list_exit:
            full_exit = "pomeha/" + p
            button_exit = pyautogui.locateOnScreen(full_exit, grayscale=True, region=(1150, 180, 1880, 1000),
                                                   confidence=0.85)
            if button_exit:
                pyautogui.click(button_exit)
                pyautogui.sleep(0.8)
                keyboard.send("F5")
                pyautogui.sleep(1.3)
        else:
            break

        # --------------------------------------------------------------------------
        # --------------------------------------------------------------------------


def kabina():  # функция выходит в кабинет и делает скрол вниз чтобы открыть всех персонажей
    kabin = pyautogui.locateOnScreen('smena/smena.png', grayscale=True, region=(50, 200, 700, 1000),
                                     confidence=0.85)
    pyautogui.sleep(0.5)
    pyautogui.click(kabin)
    pyautogui.sleep(0.8)
    pyautogui.scroll(-180)
    pyautogui.sleep(0.5)


def kabina_pravo():  # функция выходит в кабинет и делает скрол вниз чтобы открыть всех персонажей
    kabin = pyautogui.locateOnScreen('smena/smena.png', grayscale=True, region=(1150, 200, 1880, 1000),
                                     confidence=0.85)
    pyautogui.sleep(0.5)
    pyautogui.click(kabin)
    pyautogui.sleep(0.8)
    pyautogui.scroll(-180)
    pyautogui.sleep(0.5)
    #  ----------------------------------------------------------------------------------


async def nakril():
    await asyncio.sleep(0.3)
    svetn = pyautogui.locateOnScreen('metro/nakril.png', grayscale=True, region=(50, 50, 700, 1000), confidence=0.85)
    if svetn:
        pyautogui.click(svetn)
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)
        mir = pyautogui.locateOnScreen('metro/mir.PNG', grayscale=True, region=(50, 400, 700, 1000), confidence=0.85)
        if mir:
            pyautogui.click(mir)
            await asyncio.sleep(1)
        podzem = pyautogui.locateOnScreen('metro/podzem.png', grayscale=True, region=(50, 50, 700, 1000),
                                          confidence=0.85)
        if podzem:
            pyautogui.click(podzem)
            await asyncio.sleep(1)
        do30 = pyautogui.locateOnScreen('metro/do30.png', grayscale=True, region=(50, 50, 700, 1000), confidence=0.85)
        if do30:
            pyautogui.click(do30)
        await asyncio.sleep(1)
        svetn = pyautogui.locateOnScreen('metro/nakril.png', grayscale=True, region=(50, 50, 700, 1000),
                                         confidence=0.85)
        if svetn:
            pyautogui.click(svetn)
            await asyncio.sleep(1)
    zakrito = pyautogui.locateOnScreen('metro/zakrito.PNG', grayscale=True, region=(50, 100, 700, 1000),
                                       confidence=0.85)
    if zakrito:
        zakrit = pyautogui.locateOnScreen('metro/exit.PNG', grayscale=True, region=(50, 100, 700, 1000),
                                          confidence=0.85)
        pyautogui.click(zakrit)
        await asyncio.sleep(1)
    else:
        voiti = pyautogui.locateOnScreen('metro/voiti.png', grayscale=True, region=(50, 50, 700, 1000), confidence=0.85)
        if voiti:
            pyautogui.click(voiti)
            await asyncio.sleep(1)
        start = pyautogui.locateOnScreen('metro/start.PNG', grayscale=True, region=(50, 50, 700, 1000), confidence=0.85)
        start2 = pyautogui.locateOnScreen('metro/start2.PNG', grayscale=True, region=(50, 50, 700, 1000),
                                          confidence=0.85)
        if start or start2:
            pyautogui.click(start) or pyautogui.click(start2)
        #  ----------------------------------------


async def nakril_pravo():
    await asyncio.sleep(1)
    svetn = pyautogui.locateOnScreen('metro/nakril.png', grayscale=True, region=(1150, 50, 1880, 1000), confidence=0.85)
    if svetn:
        pyautogui.click(svetn)
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)
        mir = pyautogui.locateOnScreen('metro/mir.PNG', grayscale=True, region=(1150, 50, 1880, 1000), confidence=0.85)
        if mir:
            pyautogui.click(mir)
            await asyncio.sleep(1)
        podzem = pyautogui.locateOnScreen('metro/podzem.png', grayscale=True, region=(1150, 50, 1880, 1000),
                                          confidence=0.85)
        if podzem:
            pyautogui.click(podzem)
            await asyncio.sleep(1)
        do30 = pyautogui.locateOnScreen('metro/do30.png', grayscale=True, region=(1150, 50, 1880, 1000),
                                        confidence=0.85)
        if do30:
            pyautogui.click(do30)
        await asyncio.sleep(1)
        svetn = pyautogui.locateOnScreen('metro/nakril.png', grayscale=True, region=(1150, 50, 1880, 1000),
                                         confidence=0.85)
        if svetn:
            pyautogui.click(svetn)
            await asyncio.sleep(1)
    zakrito = pyautogui.locateOnScreen('metro/zakrito.PNG', grayscale=True, region=(1150, 50, 1880, 1000),
                                       confidence=0.85)
    if zakrito:
        zakrit = pyautogui.locateOnScreen('metro/exit.PNG', grayscale=True, region=(1150, 50, 1880, 1000),
                                          confidence=0.85)
        pyautogui.click(zakrit)
        await asyncio.sleep(1)
    else:
        voiti = pyautogui.locateOnScreen('metro/voiti.png', grayscale=True, region=(1150, 50, 1880, 1000),
                                         confidence=0.85)
        if voiti:
            pyautogui.click(voiti)
            await asyncio.sleep(1)
        start = pyautogui.locateOnScreen('metro/start.PNG', grayscale=True, region=(1150, 50, 1880, 1000),
                                         confidence=0.85)
        start2 = pyautogui.locateOnScreen('metro/start2.PNG', grayscale=True, region=(1150, 50, 1880, 1000),
                                          confidence=0.85)
        if start or start2:
            pyautogui.click(start) or pyautogui.click(start2)
        #  ----------------------------------------


async def razvalina():
    await asyncio.sleep(0.3)
    razwalini = pyautogui.locateOnScreen('metro/adRazwalini.png', grayscale=True, region=(50, 100, 700, 1000),
                                         confidence=0.85)
    if razwalini:
        pyautogui.click(razwalini)
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)
        mir = pyautogui.locateOnScreen('metro/mir.PNG', grayscale=True, region=(50, 100, 700, 1000), confidence=0.85)
        if mir:
            pyautogui.click(mir)
        #  -------------------------------------------
        await asyncio.sleep(1)
        podzem = pyautogui.locateOnScreen('metro/podzem.png', grayscale=True, region=(50, 100, 700, 1000),
                                          confidence=0.85)
        if podzem:
            pyautogui.click(podzem)
            await asyncio.sleep(1)
        do30 = pyautogui.locateOnScreen('metro/do30.png', grayscale=True, region=(50, 100, 700, 1000),
                                        confidence=0.85)
        if do30:
            pyautogui.click(do30)
            await asyncio.sleep(1)
        razwalini = pyautogui.locateOnScreen('metro/adRazwalini.png', grayscale=True, region=(50, 100, 700, 1000),
                                             confidence=0.85)
        if razwalini:
            pyautogui.click(razwalini)
            await asyncio.sleep(1)

    zakrito = pyautogui.locateOnScreen('metro/zakrito.PNG', grayscale=True, region=(50, 100, 700, 1000),
                                       confidence=0.85)
    if zakrito:

        zakrit = pyautogui.locateOnScreen('metro/exit.PNG', grayscale=True, region=(50, 100, 700, 1000),
                                          confidence=0.85)
        pyautogui.click(zakrit)
        await asyncio.sleep(1)
    else:
        brut = pyautogui.locateOnScreen('metro/brut.png', grayscale=True, region=(50, 100, 700, 1000),
                                        confidence=0.85)
        if brut:
            pyautogui.click(brut)
            await asyncio.sleep(1)
        voiti = pyautogui.locateOnScreen('metro/voiti.png', grayscale=True, region=(50, 100, 700, 1000),
                                         confidence=0.85)
        if voiti:
            pyautogui.click(voiti)
            await asyncio.sleep(1)
        start = pyautogui.locateOnScreen('metro/start.PNG', grayscale=True, region=(50, 50, 700, 1000), confidence=0.85)
        start2 = pyautogui.locateOnScreen('metro/start2.PNG', grayscale=True, region=(50, 50, 700, 1000),
                                          confidence=0.85)
        if start or start2:
            pyautogui.click(start) or pyautogui.click(start2)
            pyautogui.sleep(0.2)
        #  ----------------------------------------


async def razvalina_pravo():
    await asyncio.sleep(1)
    razwalini = pyautogui.locateOnScreen('metro/adRazwalini.png', grayscale=True, region=(1150, 100, 1880, 1000),
                                         confidence=0.85)
    if razwalini:
        pyautogui.click(razwalini)
        await asyncio.sleep(1)
    else:
        await asyncio.sleep(1)
        mir = pyautogui.locateOnScreen('metro/mir.PNG', grayscale=True, region=(1150, 100, 1880, 1000), confidence=0.85)
        if mir:
            pyautogui.click(mir)
        #  -------------------------------------------
        await asyncio.sleep(1)
        podzem = pyautogui.locateOnScreen('metro/podzem.png', grayscale=True, region=(1150, 100, 1880, 1000),
                                          confidence=0.85)
        if podzem:
            pyautogui.click(podzem)
            await asyncio.sleep(1)
        do30 = pyautogui.locateOnScreen('metro/do30.png', grayscale=True, region=(1150, 100, 1880, 1000),
                                        confidence=0.85)
        if do30:
            pyautogui.click(do30)
            await asyncio.sleep(1)
        razwalini = pyautogui.locateOnScreen('metro/adRazwalini.png', grayscale=True, region=(1150, 100, 1880, 1000),
                                             confidence=0.85)
        if razwalini:
            pyautogui.click(razwalini)
            await asyncio.sleep(1)

    zakrito = pyautogui.locateOnScreen('metro/zakrito.PNG', grayscale=True, region=(1150, 100, 1880, 1000),
                                       confidence=0.85)
    if zakrito:

        zakrit = pyautogui.locateOnScreen('metro/exit.PNG', grayscale=True, region=(1150, 100, 1880, 1000),
                                          confidence=0.85)
        pyautogui.click(zakrit)
        await asyncio.sleep(1)
    else:
        brut = pyautogui.locateOnScreen('metro/brut.png', grayscale=True, region=(1150, 100, 1880, 1000),
                                        confidence=0.85)
        if brut:
            pyautogui.click(brut)
            pyautogui.sleep(1)
        voiti = pyautogui.locateOnScreen('metro/voiti.png', grayscale=True, region=(1150, 100, 1880, 1000),
                                         confidence=0.85)
        if voiti:
            pyautogui.click(voiti)
            await asyncio.sleep(1)
        start = pyautogui.locateOnScreen('metro/start.PNG', grayscale=True, region=(1150, 100, 1880, 1000),
                                         confidence=0.85)
        start2 = pyautogui.locateOnScreen('metro/start2.PNG', grayscale=True, region=(1150, 100, 1880, 1000),
                                          confidence=0.85)
        if start or start2:
            pyautogui.click(start) or pyautogui.click(start2)
            pyautogui.sleep(0.2)
        #  ----------------------------------------


async def quest_one():
    await asyncio.sleep(0.8)
    person = pyautogui.locateOnScreen('quests/person.PNG', grayscale=True, region=(0, 0, 600, 1000),
                                      confidence=0.85)
    if person:
        pyautogui.click(person)
        await asyncio.sleep(1.2)
    zakritie()
    # ----------------------------------------------------------------
    notes = pyautogui.locateOnScreen('quests/noutes.PNG', grayscale=True, region=(0, 0, 600, 1000),
                                     confidence=0.85)
    if notes:
        pyautogui.click(notes)
        await asyncio.sleep(1.2)
    # ----------------------------------------------------------------
    varvar = pyautogui.locateOnScreen('quests/varvars.PNG', grayscale=True, region=(0, 0, 600, 1000),
                                      confidence=0.85)
    if varvar:
        pyautogui.click(varvar)
        await asyncio.sleep(1.2)

    no_quest = pyautogui.locateOnScreen('quests/no_quest.PNG', grayscale=True, region=(0, 0, 600, 1000),
                                        confidence=0.85)
    if no_quest:
        await asyncio.sleep(0)

    else:
        speed = pyautogui.locateOnScreen('quests/speed.PNG', grayscale=True, region=(0, 0, 600, 1000),
                                         confidence=0.85)
        if speed:
            pyautogui.click(speed)


async def quest_one_pravo():
    await asyncio.sleep(1.2)
    person = pyautogui.locateOnScreen('quests/person.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                      confidence=0.85)
    if person:
        pyautogui.click(person)
        await asyncio.sleep(1.2)
    zakritie_pravo()
    # ----------------------------------------------------------------
    notes = pyautogui.locateOnScreen('quests/noutes.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                     confidence=0.85)
    if notes:
        pyautogui.click(notes)
        await asyncio.sleep(1.2)
    # ----------------------------------------------------------------
    varvar = pyautogui.locateOnScreen('quests/varvars.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                      confidence=0.85)
    if varvar:
        pyautogui.click(varvar)
        await asyncio.sleep(1.2)

    no_quest = pyautogui.locateOnScreen('quests/no_quest.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                        confidence=0.85)
    if no_quest:
        await asyncio.sleep(0)

    else:
        speed = pyautogui.locateOnScreen('quests/speed.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                         confidence=0.85)
        if speed:
            pyautogui.click(speed)


async def ruczak():
    pyautogui.click(650, 650)
    pyautogui.sleep(0.5)
    pyautogui.scroll(-900)
    pyautogui.sleep(0.5)
    ruczak2 = pyautogui.locateOnScreen('metro/ruczak.png', grayscale=True, region=(50, 50, 700, 1000), confidence=0.91)
    pyautogui.click(ruczak2)
    await asyncio.sleep(0.8)
    timeStart = datetime.now()
    timeFinish = timeStart + timedelta(seconds=40)

    while timeStart < timeFinish:
        razbor = pyautogui.locateOnScreen('images/razbor.png', grayscale=True, region=(60, 60, 750, 1000),
                                          confidence=0.84)
        da_razbor = pyautogui.locateOnScreen('images/da_razbor.png', grayscale=True, region=(60, 60, 800, 700),
                                             confidence=0.84)
        throw = pyautogui.locateOnScreen('images/vibros.PNG', grayscale=True, region=(60, 60, 750, 1000),
                                         confidence=0.84)
        pers = pyautogui.locateOnScreen('images/pers.PNG', grayscale=True, region=(60, 60, 750, 1000),
                                        confidence=0.84)
        prodol = pyautogui.locateOnScreen('pomeha/2.PNG', grayscale=True, region=(60, 60, 600, 1000),
                                          confidence=0.84)
        if razbor:
            pyautogui.click(razbor)
            await asyncio.sleep(0.22)
        elif da_razbor:
            pyautogui.click(da_razbor)
            await asyncio.sleep(0.22)
        elif throw:
            pyautogui.click(throw)
            await asyncio.sleep(0.22)
        elif pers:
            pyautogui.click(pers)
            await asyncio.sleep(0.22)
        elif prodol:
            pyautogui.click(prodol)
        else:
            break
        timeStart: datetime = datetime.now()
        await asyncio.sleep(0.42)
    pyautogui.scroll(-1500)
    await asyncio.sleep(0.3)


async def ruczak_pravo():
    pyautogui.click(1850, 650)
    pyautogui.sleep(0.5)
    pyautogui.scroll(-900)
    pyautogui.sleep(0.5)
    ruczak2 = pyautogui.locateOnScreen('metro/ruczak.png', grayscale=True, region=(1150, 50, 1880, 1000),
                                       confidence=0.91)
    pyautogui.click(ruczak2)
    await asyncio.sleep(1.2)
    timeStart = datetime.now()
    timeFinish = timeStart + timedelta(seconds=40)

    while timeStart < timeFinish:
        razbor = pyautogui.locateOnScreen('images/razbor.png', grayscale=True, region=(1150, 60, 1880, 1000),
                                          confidence=0.84)
        da_razbor = pyautogui.locateOnScreen('images/da_razbor.png', grayscale=True, region=(1150, 60, 1880, 10000),
                                             confidence=0.84)
        throw = pyautogui.locateOnScreen('images/vibros.PNG', grayscale=True, region=(1150, 60, 1880, 1000),
                                         confidence=0.84)
        pers = pyautogui.locateOnScreen('images/pers.PNG', grayscale=True, region=(1150, 60, 1880, 1000),
                                        confidence=0.84)
        prodol = pyautogui.locateOnScreen('pomeha/2.PNG', grayscale=True, region=(1150, 60, 1880, 1000),
                                          confidence=0.84)
        if razbor:
            pyautogui.click(razbor)
            await asyncio.sleep(0.22)
        elif da_razbor:
            pyautogui.click(da_razbor)
            await asyncio.sleep(0.22)
        elif throw:
            pyautogui.click(throw)
            await asyncio.sleep(0.22)
        elif pers:
            pyautogui.click(pers)
            await asyncio.sleep(0.22)
        elif prodol:
            pyautogui.click(prodol)
        else:
            break
        timeStart: datetime = datetime.now()
        await asyncio.sleep(0.42)
    pyautogui.scroll(-1500)
    await asyncio.sleep(0.3)


while True:
    # написание цикла для кабины:---------------------------------------------------------------
    obnova = pyautogui.locateOnScreen('images/obnova.PNG', grayscale=True, region=(0, 0, 450, 160), confidence=0.83)
    if obnova:
        keyboard.send("F5")
        pyautogui.sleep(20)
    else:

        # -------------------------------------------------------------
        reboot = pyautogui.locateOnScreen('images/reboot.png', grayscale=True, region=(0, 0, 450, 160), confidence=0.83)
        pyautogui.click(reboot)
        pyautogui.sleep(1)
        zakritie()
        reboot_pravo = pyautogui.locateOnScreen('images/reboot.png', grayscale=True, region=(1150, 0, 1880, 160),
                                                confidence=0.83)
        pyautogui.click(reboot_pravo)
        pyautogui.sleep(1)
        zakritie_pravo()
        listLevo = os.listdir('person')  # обьявляем каталог с никами кабины мага
        listPravo = os.listdir('person2')  # обьявляем каталог с никами кабины монаха
        # ------------------------------------------------------------
        kabina()
        kabina_pravo()
        # -----------------------------------------------------------
        for f, m in zip(listLevo, listPravo):
            fullPutLevo = "person/" + f
            buttonLevo = pyautogui.locateOnScreen(fullPutLevo, grayscale=True, region=(20, 20, 800, 1000),
                                                  confidence=0.84)
            if buttonLevo:
                pyautogui.sleep(0.5)
                pyautogui.click(buttonLevo)
                pyautogui.sleep(0.5)
                zakritie()

            fullPutPravo = "person2/" + m
            buttonPravo = pyautogui.locateOnScreen(fullPutPravo, grayscale=True, region=(1150, 20, 1880, 1000),
                                                   confidence=0.84)
            if buttonPravo:
                pyautogui.sleep(0.5)
                pyautogui.click(buttonPravo)
                pyautogui.sleep(0.8)
                zakritie_pravo()
            #  ------------------------------------------------------
            #  ----- Основной скрипт ----------------
            ioloop = asyncio.get_event_loop()
            tasks_quests = [ioloop.create_task(quest_one()), quest_one_pravo()]
            wait_tasks = asyncio.wait(tasks_quests)
            ioloop.run_until_complete(wait_tasks)

            no_quest = pyautogui.locateOnScreen('quests/no_quest.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                                confidence=0.85)
            no_quest2 = pyautogui.locateOnScreen('quests/no_quest.PNG', grayscale=True, region=(1150, 0, 1880, 1000),
                                                 confidence=0.85)
            if no_quest and no_quest2:
                pyautogui.sleep(0.2)
            else:
                #  ---------------------------------------------------------------
                tasks_boi_quest = [ioloop.create_task(boi_smart()), ioloop.create_task(boi_smart_pravo())]
                wait_tasks_quest = asyncio.wait(tasks_boi_quest)
                ioloop.run_until_complete(wait_tasks_quest)
            #  ----------------------------------------------------------------

            pyautogui.sleep(1)
            pyautogui.click(650, 650)
            pyautogui.scroll(-1000)
            pyautogui.sleep(0.7)
            gorod = pyautogui.locateOnScreen('metro/gorod.png', grayscale=True, region=(0, 0, 600, 1000),
                                             confidence=0.85)
            if gorod:
                pyautogui.click(gorod)
                pyautogui.sleep(0.7)
                zakritie()

            pyautogui.click(1850, 650)
            pyautogui.scroll(-1000)
            pyautogui.sleep(0.7)
            gorod_pravo = pyautogui.locateOnScreen('metro/gorod.png', grayscale=True, region=(1150, 0, 1880, 1000),
                                                   confidence=0.85)
            if gorod_pravo:
                pyautogui.click(gorod_pravo)
                pyautogui.sleep(0.7)
                zakritie_pravo()
            # --------------------------------------------------------------
            tasks = [ioloop.create_task(nakril()), ioloop.create_task(nakril_pravo())]
            wait_tasks_nakril = asyncio.wait(tasks)
            ioloop.run_until_complete(wait_tasks_nakril)
            do30_2 = pyautogui.locateOnScreen('metro/strelka.png', grayscale=True, region=(0, 100, 700, 1000),
                                              confidence=0.85)
            do30 = pyautogui.locateOnScreen('metro/strelka.png', grayscale=True, region=(1150, 100, 1880, 1000),
                                            confidence=0.85)
            if do30 and do30_2:
                pyautogui.sleep(0)
            else:
                tasks_boi = [ioloop.create_task(boi_smart_2()), ioloop.create_task(boi_smart2_pravo())]
                wait_tasks_boi = asyncio.wait(tasks_boi)
                ioloop.run_until_complete(wait_tasks_boi)
            #  -------------------------------------------------------------------

            liv = pyautogui.locateOnScreen('metro/liv.PNG', grayscale=True, region=(50, 50, 700, 1000), confidence=0.85)
            if liv:
                pyautogui.click(liv)
            zakritie()
            pyautogui.sleep(0.4)
            liv_pravo = pyautogui.locateOnScreen('metro/liv.PNG', grayscale=True, region=(1150, 50, 1880, 1000),
                                                 confidence=0.85)
            if liv_pravo:
                pyautogui.click(liv_pravo)
            zakritie_pravo()
            # -----------------Развалины------------------------------------
            tasks2 = [ioloop.create_task(razvalina()), ioloop.create_task(razvalina_pravo())]
            wait_tasks_razvalini = asyncio.wait(tasks2)
            ioloop.run_until_complete(wait_tasks_razvalini)
            do30_2 = pyautogui.locateOnScreen('metro/strelka.png', grayscale=True, region=(0, 100, 700, 1000),
                                              confidence=0.85)
            do30 = pyautogui.locateOnScreen('metro/strelka.png', grayscale=True, region=(1150, 100, 1880, 1000),
                                            confidence=0.85)
            if do30 and do30_2:
                pyautogui.sleep(0)
            else:
                tasks_boi = [ioloop.create_task(boi_smart_2()), ioloop.create_task(boi_smart2_pravo())]
                wait_tasks_boi = asyncio.wait(tasks_boi)
                ioloop.run_until_complete(wait_tasks_boi)
            # --------------------------------------------------------------------
            liv = pyautogui.locateOnScreen('metro/liv.PNG', grayscale=True, region=(50, 50, 700, 1000), confidence=0.85)
            if liv:
                pyautogui.click(liv)
            zakritie()
            pyautogui.sleep(0.4)
            liv_pravo = pyautogui.locateOnScreen('metro/liv.PNG', grayscale=True, region=(1150, 50, 1880, 1000),
                                                 confidence=0.85)
            if liv_pravo:
                pyautogui.click(liv_pravo)
            zakritie_pravo()
            #  -----------------------Разбор лута-------------------------------
            tasks_rukzak = [ioloop.create_task(ruczak()), ioloop.create_task(ruczak_pravo())]
            wait_tasks_rukzak = asyncio.wait(tasks_rukzak)
            ioloop.run_until_complete(wait_tasks_rukzak)

            kabina()
            kabina_pravo()