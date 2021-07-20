list_redo = []
list_undo = []
text = ''
flag1 = False

def BastShoe(command):
    global text
    global flag1

    if not command:
        return text

    if command[0] == '1' and command[1] == ' ':
        text += command[2:]
        if flag1:
            list_undo.clear()
            list_redo.clear()
            flag1 = False
        list_undo.append(f'2 {len(command[2:])}')
    elif command[0] == '2' and command[1] == ' ':
        num = int(command[2:])
        if num > len(text):
            num = len(text)
        if flag1:
            list_undo.clear()
            list_redo.clear()
            flag1 = False
        list_undo.append(f'1 {text[len(text) - num:]}')
        text = text[:len(text) - num]
    elif command[0] == '3' and command[1] == ' ':
        if int(command[2:]) >= len(text) or int(command[2:]) < -len(text):
            return ''
        else:
            return text[int(command[2:])]
    elif command[0] == '4' and len(command) == 1:
        if not list_undo:
            return text
        undo = list_undo.pop(-1)
        if undo[0] == '1':
            list_redo.append(f'2 {len(undo[2:])}')
            text += undo[2:]
        elif undo[0] == '2':
            list_redo.append(f'1 {text[len(text) - int(undo[2:]):]}')
            text = text[:len(text) - int(undo[2:])]
        flag1 = True
    elif command[0] == '5' and len(command) == 1:
        if not list_redo:
            return text
        redo = list_redo.pop(-1)
        if redo[0] == '1':
            list_undo.append(f'2 {len(redo[2:])}')
            text += redo[2:]
        elif redo[0] == '2':
            list_redo.append(f'1 {text[len(text) - int(redo[2:]):]}')
            text = text[:len(text) - int(redo[2:])]
    return text