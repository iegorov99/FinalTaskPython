import json
import datetime
import os
import sys

def SaveNotes(notes: list):
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def ReadNotes():
    os.system('CLS')
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

def AddNote():
    os.system('CLS')
    notes = ReadNotes()
    id = len(notes) + 1
    title = input("Input title: ")
    body = input("Input body: ")
    timestemp = str(datetime.datetime.now())

    note = {"id": id, "Title": title, "Body": body, "Timestemp": timestemp}

    notes.append(note)
    SaveNotes(notes)
    input("Note created successfully!")
    PrintNotes()
    try:
        
        num = int(input("Input 1 to continue or any key to return: "))
        if num == 1:
            return AddNote()
    except ValueError:
        return Main()
    

def EditNotes():
    
    notes = ReadNotes()
    if len(notes) == 0:
        input("No notes yet!")
        return
    PrintNotes()

    
    try:
        id = int(input("Input id of note to edit or '-1' to return: "))
    except ValueError:
        input("Incorrect id!")
        return EditNotes
    
    os.system('CLS')
    
    if id == -1:
        return Main()
    
    for note in notes:
        if note["id"] == id:
            title = input("Input new title: ")
            body = input("Input new body: ")
            timestemp = str(datetime.datetime.now())

            note["Title"] = title
            note["Body"] = body
            note["Timestemp"] = timestemp

            SaveNotes(notes)
            input("Note edit successfully!")
            PrintNotes()
            try:
                num = int(input("Input 1 to continue or any key to return: "))
                if num == 1:
                    return EditNotes()
            except ValueError:
                return Main()
    print("Note with this id not found!")
    input("Try again")
    return EditNotes()

def DeleteNote():
    
    notes = ReadNotes()
    if len(notes) == 0:
        input("No notes yet!")
        return
    PrintNotes()

    try:
        id = int(input("Input id of note to delete or '-1' to return: "))
    except ValueError:
        input("Incorrect id!")
        return DeleteNote()
    
    if id == -1:
        return Main()

    for note in notes:
        if note["id"] == id:
            notes.remove(note)

            for note in notes:
                if note["id"] > id:
                    note["id"] = note["id"] - 1

            SaveNotes(notes)
            input("Note remove successfully!")
            PrintNotes()
            try:
                num = int(input("Input 1 to continue or any key to return: "))
                if num == 1:
                    return DeleteNote()
            except ValueError:
                return Main()
            
    print("Note with this id not found!")
    input("Try again")
    return DeleteNote()
        
def PrintNotes():
    os.system('CLS')
    notes = ReadNotes()
    if len(notes) > 0: 
        for note in notes:
            print("id: ", note["id"])
            print("Title: ", note["Title"])
            print("Body: ", note["Body"])
            print("Date:", note["Timestemp"])
            print("--------------------------------")
    else:
        print("No notes yet")
    input()

def Drowing():
    print('1 - Show notes')
    print('2 - Add note')
    print('3 - Edit note')
    print('4 - Remove note')
    print('5 - Exit')

def Choice(user_choice):
    if user_choice == 1:
        PrintNotes()
    elif user_choice == 2:
        AddNote()
    elif user_choice == 3:
        EditNotes()
    elif user_choice == 4:
        DeleteNote()
    elif user_choice == 5:
        print('Program closed!')
        sys.exit()

def Main() :
    while True :
        os.system('CLS')
        Drowing()
        try :
            user_choice = int(input('Input num: '))
        except ValueError :
            print('Incorrect Value!')
            input('Press any key to return')
            return Main()
        Choice(user_choice)


    
