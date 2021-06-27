def PrintingCosts(Line):
    tonner = 0
    for x in Line:
        if x == ' ':
            tonner += 0
        elif x in ["'", "`"]:
            tonner += 3
        elif x == ".":
            tonner += 4
        elif x == '"':
            tonner += 6
        elif x in ',-^':
            tonner += 7
        elif x in ':_':
            tonner += 8
        elif x in '!~':
            tonner += 9
        elif x in '>\/<':
            tonner += 10
        elif x == ';':
            tonner += 11
        elif x in '(|)':
            tonner += 12
        elif x in 'vrx+':
            tonner += 13
        elif x in 'Y=':
            tonner += 14
        elif x in '?i':
            tonner += 15
        elif x in 'LTl7':
            tonner += 16
        elif x in 'tcu*':
            tonner += 17
        elif x in 'Jn]{X}fI[':
            tonner += 18
        elif x in 'Vzw1':
            tonner += 19
        elif x in 'oFjC':
            tonner += 20
        elif x in 'hKk4s':
            tonner += 21
        elif x in '20Zm%':
            tonner += 22
        elif x in '8P3eaU':
            tonner += 23
        elif x in '&#Ay':
            tonner += 24
        elif x in 'bdpqGSHN':
            tonner += 25
        elif x in '96DEWO':
            tonner += 26
        elif x == '5':
            tonner += 27
        elif x in 'MR':
            tonner += 28
        elif x in '$B':
            tonner += 29
        elif x == 'g':
            tonner += 30
        elif x == 'Q':
            tonner += 31
        elif x == '@':
            tonner += 32
        else:
            tonner += 23
    return tonner
