
yes_no = ["Jah", "Ei"]
directions = ["vasak", "parem", "otse", "tagasi"]
 
name = input("Mis su nimi on, seikleja?\n")
print("Tere, " + name + ". Hakkame kohe pihta!")
print("Sa seisad tiheda metsa serval")
print("Kas sa suudad leida tee läbi metsa?\n")
 
response = ""
while response not in yes_no:
    response = input("Kas sa sooviksid alustada?\nJah/Ei\n")
    if response == "Jah":
        print("Sa astusid metsa sisse. Sa kuuled vareseid kraaksumas\n")
    elif response == "Ei":
        print("Sa ei ole veel selleks piisavalt julge. Nägemist, " + name + ".")
        quit()
    else: 
        print("Vasta ainult Jah või Ei\n")
 
response = ""
while response not in directions:
    print("Mine vasakule kus on karu")
    print("Mine paremale, veel sügavamale metsa")
    print("Otse ees on suur kivimüür")
    print("Seljataga on metsaserv kus sa alustasid\n")
    response = input("Mis suunas sa liigud?\nvasakule/paremale/otse/tagasi\n")
    if response == "vasakule":
        print("Karu sööb su ära. Puhka rahus, " + name + ".")
        quit()
    elif response == "paremale":
        print("Sa läksid sügavamale metsa\n")
    elif response == "otse":
        print("Sa ei saa seinast üle.\n")
        response = "" 
    elif response == "tagasi":
        print("Sa lahkusid metsast. Nägemist, " + name + ".")
        quit()
    else:
        print("Kirjuta suund kuhu poole liigud\n")
