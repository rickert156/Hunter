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
    ExlameNew, ExlameOld = '!', '%21'
    SharpNew, SharpOld = '#', '%23'
    DollarNew, DollarOld = '$', '%26'
    BrachetOpenNew, BrachetOpenOld = '(', '%28'
    BrachetCloseNew, BrachetCloseOld = ')', '%29'
    StarNew, StarOld = '*', '%2A'
    CommaNew, CommaOld = ',', '%2C'
    SquareBracketOpenNew, SquareBracketOpenOld = '[', '%5B'
    SquareBracketCloseNew, SquareBracketCloseOld = ']', '%5D'
    FuckinENew, FuckinEOld = 'é', '%25C3%25A9'

    if SlashColonOld in link:link = link.replace(SlashColonOld, SlashColonNew)
    if SlashOld in link:link = link.replace(SlashOld, SlashNew)
    if DashOld in link:link = link.replace(DashOld, DashNew)
    if QuestionsOld in link:link = link.replace(QuestionsOld, QuestionsNew)
    if PlusOld in link:link = link.replace(PlusOld, PlusNew)
    if MinusOld in link:link = link.replace(MinusOld, MinusNew)
    if EqualsOld in link:link = link.replace(EqualsOld, EqualsNew)
    if ColonOld in link:link = link.replace(ColonOld, ColonNew)
    if ExlameOld in link:link = link.replace(ExlameOld, ExlameNew)
    if SharpOld in link:link = link.replace(SharpOld, SharpNew)
    if DollarOld in link:link = link.replace(DollarOld, DollarNew)
    if BrachetOpenOld in link:link = link.replace(BrachetOpenOld, BrachetOpenNew)
    if BrachetCloseOld in link:link = link.replace(BrachetCloseOld, BrachetCloseNew)
    if StarOld in link:link = link.replace(StarOld, StarNew)
    if CommaOld in link:link = link.replace(CommaOld, CommaNew)
    if SquareBracketOpenOld in link:link = link.replace(SquareBracketOpenOld, SquareBracketOpenNew)
    if SquareBracketCloseOld in link:link = link.replace(SquareBracketCloseOld, SquareBracketCloseNew)
    if FuckinEOld in link:link = link.replace(FuckinEOld, FuckinENew)

    if ending in link:link = link.split(ending)[0]

    return link

def readSetLinks():
    global RESULT_LINK

    number_link = 0
    for link in RESULT_LINK:
        number_link+=1
        link = processingLink(link)
        print(f'[{number_link}] {link}')
