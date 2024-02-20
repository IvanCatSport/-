def logon():
    login = input("Ввидите логин ")
    Possword = int(input("Ввидите пороль "))
    if login == "ivan" and Possword == 3333 :
        print("Привет" ,login )
        print("Вы вошли!")
        import webbrowser
        webbrowser.open("https://Outlook.live.com/")
        
    else :
        print("Неправильный логин или пароль, доступ запрещен!")
        logon()                 
logon()                