import pyautogui
from PIL import Image, ImageDraw
# постоянный поск однерок:
# while True:
#     print(pyautogui.locateOnScreen('img\one.png'))
#     print(pyautogui.locateCenterOnScreen('img\one.png'))
# вывод кучи строк с координатами однерок
# for pos in pyautogui.locateAllOnScreen('img\one.png'):
#     print(pos)
def ones():
    listOfOnes = list(pyautogui.locateAllOnScreen('img\one.png'))
    for i in range(len(listOfOnes)):
        # print(i)
        # print(listOfOnes[i][0], listOfOnes[i][1], listOfOnes[i][0]+33, listOfOnes[i][1]+33)
        pyautogui.doubleClick(pyautogui.center(listOfOnes[i]))
        if listOfOnes[i][0] - 60 < 0:
            listOfClosed = list(pyautogui.locateAllOnScreen('img\closed.png', region=(
                1, listOfOnes[i][1] - 60, 140, 140)))
        else:
            listOfClosed = list(pyautogui.locateAllOnScreen('img\closed.png', region=(
                listOfOnes[i][0] - 60, listOfOnes[i][1] - 60, 140, 140)))
        # print(listOfClosed)
        if len(listOfClosed) == 1:
            # print(listOfClosed)
            pyautogui.click(pyautogui.center(listOfClosed[0]), button='right')
            pyautogui.doubleClick(pyautogui.center(listOfOnes[i]))
    secondListOfOnes = list(pyautogui.locateAllOnScreen('img\one.png'))
    for i2 in range(len(secondListOfOnes)):
        if secondListOfOnes[i2][0] - 60 < 0:
            listOfFlag1 = list(pyautogui.locateAllOnScreen('img\\flag.png', region=(
                1, secondListOfOnes[i2][1] - 60, 140, 140)))
        else:
            listOfFlag1 = list(pyautogui.locateAllOnScreen('img\\flag.png', region=(
                secondListOfOnes[i2][0] - 60, secondListOfOnes[i2][1] - 60, 140, 140)))
        if len(listOfFlag1) > 0:
            pyautogui.doubleClick(pyautogui.center(secondListOfOnes[i2]))
    thirdListOfOnes = list(pyautogui.locateAllOnScreen('img\one.png'))
    if len(thirdListOfOnes)>len(secondListOfOnes):
        ones()
    else:
        twos()

def twos():
    listOftwos = list(pyautogui.locateAllOnScreen('img\\two.png'))
    for i in range(len(listOftwos)):
        # print(i)
        # print(listOfOnes[i][0], listOfOnes[i][1], listOfOnes[i][0]+33, listOfOnes[i][1]+33)
        pyautogui.doubleClick(pyautogui.center(listOftwos[i]))
        if listOftwos[i][0] - 60 < 0:
            listOfClosed = list(pyautogui.locateAllOnScreen('img\closed.png', region=(
                1, listOftwos[i][1] - 60, 140, 140)))
            listOfFlag2 = list(pyautogui.locateAllOnScreen('img\\flag.png', region=(
                1, listOftwos[i][1] - 60, 140, 140)))
        else:
            listOfClosed = list(pyautogui.locateAllOnScreen('img\closed.png', region=(
                listOftwos[i][0] - 60, listOftwos[i][1] - 60, 140, 140)))
            listOfFlag2 = list(pyautogui.locateAllOnScreen('img\\flag.png', region=(
                listOftwos[i][0], listOftwos[i][1] - 60, 140, 140)))
        # print(listOfClosed)
        if len(listOfClosed) == 1 and len(listOfFlag2) == 1:
            # print(listOfClosed)
            pyautogui.click(pyautogui.center(listOfClosed[0]), button='right')
            pyautogui.doubleClick(pyautogui.center(listOftwos[i]))
        elif len(listOfFlag2) == 2:
            pyautogui.doubleClick(pyautogui.center(listOftwos[i]))
    secondListOftwos = list(pyautogui.locateAllOnScreen('img\one.png'))
    for i2 in range(len(secondListOftwos)):
        if secondListOftwos[i2][0] - 60 < 0:
            listOfFlag1 = list(pyautogui.locateAllOnScreen('img\\flag.png', region=(
                1, secondListOftwos[i2][1] - 60, 140, 140)))
        else:
            listOfFlag1 = list(pyautogui.locateAllOnScreen('img\\flag.png', region=(
                secondListOftwos[i2][0] - 60, secondListOftwos[i2][1] - 60, 140, 140)))
        if len(listOfFlag1) == 2:
            pyautogui.doubleClick(pyautogui.center(secondListOftwos[i2]))
    thirdListOftwos = list(pyautogui.locateAllOnScreen('img\one.png'))
    if len(thirdListOftwos) > len(secondListOftwos):
        twos()
    else:
        threes()

def threes():
    print('я в ахуи')


# listOfOnes = list(pyautogui.locateAllOnScreen('img\one.png'))
# scr = pyautogui.screenshot('skrin.png')
# for i in range(len(listOfOnes)):
#     print(listOfOnes[i])

# with Image.open('skrin.png') as im: # закрашивание увиденных однерок, рисование рамки вокруг них, закрашивание закрытых в раамке
#     # print(listOfOnes)
#     # print(len(listOfOnes))
#     draw = ImageDraw.Draw(im)
#     for i in range(len(listOfOnes)):
#         # print(i)
#         # print(listOfOnes[i][0], listOfOnes[i][1], listOfOnes[i][0]+33, listOfOnes[i][1]+33)
#         draw.rectangle((listOfOnes[i][0], listOfOnes[i][1], listOfOnes[i][0]+33, listOfOnes[i][1]+33), fill='blue')
#         draw.rectangle((listOfOnes[i][0]-60,listOfOnes[i][1]-60,listOfOnes[i][0]+100,listOfOnes[i][1]+100), outline='yellow')
#         if listOfOnes[i][0]-60<0:
#             listOfClosed = list(pyautogui.locateAllOnScreen('img\closed.png', region=(
#             1, listOfOnes[i][1] - 60, 140, 140)))
#         else:
#             listOfClosed = list(pyautogui.locateAllOnScreen('img\closed.png', region=(
#                 listOfOnes[i][0]-60,listOfOnes[i][1]-60,140,140)))
#         # print(listOfClosed)
#         if len(listOfClosed) == 1:
#             print(listOfClosed)
#             draw.rectangle((listOfClosed[0][0],listOfClosed[0][1],listOfClosed[0][0]+39,listOfClosed[0][1]+39), fill='yellow')
#     # draw.rectangle((91,471,91+40,471+40), fill='blue')
#     im.show()

# for i in range(len(listOfOnes)):
#     # print(i)
#     # print(listOfOnes[i][0], listOfOnes[i][1], listOfOnes[i][0]+33, listOfOnes[i][1]+33)
#     pyautogui.doubleClick(pyautogui.center(listOfOnes[i]))
#     if listOfOnes[i][0] - 60 < 0:
#         listOfClosed = list(pyautogui.locateAllOnScreen('img\closed.png', region=(
#             1, listOfOnes[i][1] - 60, 140, 140)))
#     else:
#         listOfClosed = list(pyautogui.locateAllOnScreen('img\closed.png', region=(
#             listOfOnes[i][0] - 60, listOfOnes[i][1] - 60, 140, 140)))
#     # print(listOfClosed)
#     if len(listOfClosed) == 1:
#         print(listOfClosed)
#         pyautogui.click(pyautogui.center(listOfClosed[0]), button='right')
#         pyautogui.doubleClick(pyautogui.center(listOfOnes[i]))
# secondListOfOnes = list(pyautogui.locateAllOnScreen('img\one.png'))
# for i2 in range(len(secondListOfOnes)):
#     if listOfOnes[i2][0] - 60 < 0:
#         listOfFlag1 = list(pyautogui.locateAllOnScreen('img\\flag.png', region=(
#             1, listOfOnes[i2][1] - 60, 140, 140)))
#     else:
#         listOfFlag1 = list(pyautogui.locateAllOnScreen('img\\flag.png', region=(
#             listOfOnes[i2][0] - 60, listOfOnes[i2][1] - 60, 140, 140)))
#     if len(listOfFlag1)>0:
#         pyautogui.doubleClick(pyautogui.center(secondListOfOnes[i2]))

if __name__ == "__main__":
    ones()
# print(listOfOnes)
# print(len(listOfOnes))
# print(listOfOnes[0])
# print(listOfOnes[0][0])