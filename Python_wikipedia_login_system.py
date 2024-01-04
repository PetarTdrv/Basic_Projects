import webbrowser

where_are_we_going = input("Enter the paragraph you want to go to(top/\
history/Design/Syntax/Libraries/Development/Implementations) : ").lower()

if where_are_we_going == "top":
    print("Going!")
    url= 'https://en.wikipedia.org/wiki/Python_(programming_language)#'
    webbrowser.open_new_tab(url)
    exit()
elif where_are_we_going == "history":
    print("Going!")
    url= 'https://en.wikipedia.org/wiki/Python_(programming_language)#history'
    webbrowser.open_new_tab(url)
    exit()
elif where_are_we_going == "design":
    print("Going!")
    url= 'https://en.wikipedia.org/wiki/Python_(programming_language)#Design_philosophy_and_features'
    webbrowser.open_new_tab(url)
    exit()
elif where_are_we_going == "syntax":
    print("Going!")
    url= 'https://en.wikipedia.org/wiki/Python_(programming_language)#Syntax_and_semantics'
    webbrowser.open_new_tab(url)
    exit()
elif where_are_we_going == "libraries":
    print("Going!")
    url= 'https://en.wikipedia.org/wiki/Python_(programming_language)#Libraries'
    webbrowser.open_new_tab(url)
    exit()
elif where_are_we_going == "development":
    print("Going!")
    url= 'https://en.wikipedia.org/wiki/Python_(programming_language)#Development_environments'
    webbrowser.open_new_tab(url)
    exit()
elif where_are_we_going == "implementations":
    print("Going!")
    url= 'https://en.wikipedia.org/wiki/Python_(programming_language)#Implementations'
    webbrowser.open_new_tab(url)
    exit()