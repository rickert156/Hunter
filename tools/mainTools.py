from tools.links import RESULT_LINK

def processingLink(link):
    SlashColonNew, SlashColonOld = '://', '%3A%2F%2F'
    SlashNew, SlashOld = '/', '%2F'
    DashNew, DashOld = '-', '%2D'
    ending = '&rut'
    QuestionsNew, QuestionsOld = '?', '%3F'
    PlusNew, PlusOld = '+', '%2B'
    MinusNew, MinusOld = '-', '%2D'
    EqualsNew, EqualsOld = '=', '%3D'
    ColonNew, ColonOld = ':', '%3A'

    if SlashColonOld in link:link = link.replace(SlashColonOld, SlashColonNew)
    if SlashOld in link:link = link.replace(SlashOld, SlashNew)
    if DashOld in link:link = link.replace(DashOld, DashNew)
    if QuestionsOld in link:link = link.replace(QuestionsOld, QuestionsNew)
    if PlusOld in link:link = link.replace(PlusOld, PlusNew)
    if MinusOld in link:link = link.replace(MinusOld, MinusNew)
    if EqualsOld in link:link = link.replace(EqualsOld, EqualsNew)
    if ColonOld in link:link = link.replace(ColonOld, ColonNew)
    if ending in link:link = link.split(ending)[0]

    return link

def readSetLinks():
    global RESULT_LINK

    number_link = 0
    for link in RESULT_LINK:
        number_link+=1
        link = processingLink(link)
        print(f'[{number_link}] {link}')
