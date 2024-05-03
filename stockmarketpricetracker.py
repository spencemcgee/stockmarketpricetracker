# Main Menu
def mainmenu():
    print("\033c")
    print("\n\n\tWelcome to CCME Manager\n")
    print("\t     1. Database")
    print("\t     2. Calculator")
    print("\t     3. Exit\n\n")
    mainmenusel = int(input("\t\t  "))

    if mainmenusel == 1:
        database()
    if mainmenusel == 2:
        calculator()
    if mainmenusel == 3:
        print("\033c")
        exit()
    elif mainmenusel > 3:
        mainmenu()

def loopback():
    input("\n\n\t Press Enter to continue\n\t\t    ")

def database():
    print("\033c")
    print("\n\n\t    CCME Database\n")
    print("\t 1. View Index")
    print("\t 2. View Deltas")
    print("\t 3. View Share Prices")
    print("\t 4. View Listing Info")
    print("\t 5. Edit Listing Info")
    print("\t 6. Back\n\n")
    dbmenusel = int(input("\t\t  "))

    if dbmenusel == 1:
        viewindex()
    if dbmenusel == 2:
        viewdelta()
    if dbmenusel == 3:
        viewshareprices()
    if dbmenusel == 4:
        viewdatabase()
    if dbmenusel == 5:
        editdatabase()
    if dbmenusel == 6:
        mainmenu()
    elif dbmenusel > 6:
        database()

# Database Pages
def viewdatabase():
    print("\033c")
    print("\n\n\t    View Listing Info\n\n\n")
    listingsel = input("Ticker Symbol: ")
    print("")
    filename = "/content/drive/MyDrive/ccmedatabase/listings/" + listingsel
    try:
        with open(filename, "r") as f:
            lines = [line.rstrip() for line in f]
        for line in lines:
            print(line)
        f.close()
    except:
        print("\n\n\tItem not found in database.\n")
        loopback()
        database()

    print("")
    loopback()
    database()

def editdatabase():
    print("\033c")
    print("\n\n\t    Edit Listing Info\n")
    listingsel = input("Ticker Symbol: ")
    filename = "/content/drive/MyDrive/ccmedatabase/listings/" + listingsel
    ownerinput = input("Owner: ")
    ownerprefix = "Owner: "
    owner = ownerprefix + ownerinput
    balanceinput = input("Balance: ")
    balanceprefix = "Balance: "
    balance = balanceprefix + balanceinput
    splitinput = input("Split: ")
    splitprefix = "Split %: "
    split = splitprefix + splitinput
    totalsharesinput = input("Total # of Shares: ")
    totalsharesprefix = "Total # of Shares: "
    totalshares = totalsharesprefix + totalsharesinput
    ipodateinput = ipodateinput("IPO Date: ")
    ipodateprefix = "IPO Date: "
    ipodate = ipodateprefix + ipodateinput
    lastupdatedinput = input("Last Updated: ")
    lastupdatedprefix = "Last Updated: "
    lastupdated = lastupdatedprefix + lastupdatedinput

    items = [owner, balance, split, totalshares, ipodate, lastupdated]
    with open(filename, "w") as f:
        for item in items:
            f.write(item+"\n")
    f.close()
    print("\n\n\n\t    Database Updated.")
    loopback()
    database()

def viewindex():
    print("\033c")
    print("\n\n\t      Index Prices\n")
    filename = "/content/drive/MyDrive/ccmedatabase/index/"
    with open(filename + "priceSEI", "r") as f:
        pricesei = f.read()
    f.close()
    with open(filename + "priceMIX", "r") as f:
        pricemix = f.read()
    f.close()
    with open(filename + "priceFCX", "r") as f:
        pricefcx = f.read()
    f.close()
    print("\t       SEI: $" + pricesei)
    print("\n\t       MIX: $" + pricemix)
    print("\n\t       FCX: $" + pricefcx)
    loopback()
    database()

def viewdelta():
    print("\033c")
    print("\n\n\t\t Deltas\n")
    filename = "/content/drive/MyDrive/ccmedatabase/delta/"
    with open(filename + "deltaSEI", "r") as f:
        viewdeltasei = f.read()
    f.close()
    with open(filename + "deltaMIX", "r") as f:
        viewdeltamix = f.read()
    f.close()
    with open(filename + "deltaFCX", "r") as f:
        viewdeltafcx = f.read()
    f.close()
    with open(filename + "deltaE", "r") as f:
        viewdeltae = f.read()
    f.close()
    print("Delta SEI: " + viewdeltasei)
    print("\nDelta MIX: " + viewdeltamix)
    print("\nDelta FCX: " + viewdeltafcx)
    print("\nDelta E: " + viewdeltae)
    loopback()
    database()

def viewshareprices():
    print("\033c")
    print("\n\n\t     Share Prices\n")
    filename = "/content/drive/MyDrive/ccmedatabase/listings/shareprice/"
    with open(filename + "DCMCprice", "r") as f:
        DCMCprice = f.read()
        f.close()
    with open(filename + "TKOprice", "r") as f:
        TKOprice = f.read()
        f.close()
    with open(filename + "BJZprice", "r") as f:
        BJZprice = f.read()
        f.close()
    with open(filename + "SPCprice", "r") as f:
        SPCprice = f.read()
        f.close()
    with open(filename + "QTZprice", "r") as f:
        QTZprice = f.read()
        f.close()
    print("\nDCMC: $" + DCMCprice)
    print("\nTKO: $" + TKOprice)
    print("\nBJZ: $" + BJZprice)
    print("\nSPC: $" + SPCprice)
    print("\nQTZ: $" + QTZprice + "\n")
    loopback()
    database()

# Calculator Menu
def calculator():
    print("\033c")
    print("\n\n\t   CCME Calculator\n")
    print("\t  1. Index Price")
    print("\t  2. Delta")
    print("\t  3. Share Price")
    print("\t  4. Sales & Commission")
    print("\t  5. Employee Wages")
    print("\t  6. Back\n\n")
    calcmenusel = int(input("\t\t "))

    if calcmenusel == 1:
        indexcalcmenu()
    if calcmenusel == 2:
        deltacalc()
    if calcmenusel == 3:
        sharecalc()
    if calcmenusel == 4:
        commissioncalc()
    if calcmenusel == 5:
        wagecalc()
    if calcmenusel == 6:
        mainmenu()
    elif calcmenusel > 6:
        calculator()

# Index Calculators (Store results in files)
def indexcalcmenu():
    print("\033c")
    print("\n\n\t Index Calculator\n")
    print("\t    1. SEI")
    print("\t    2. MIX")
    print("\t    3. FCX")
    print("\t    4. Back\n\n")
    indexmenusel = int(input("\t\t  "))

    if indexmenusel == 1:
        seicalc()
    if indexmenusel == 2:
        mixcalc()
    if indexmenusel == 3:
        fcxcalc()
    if indexmenusel == 4:
        calculator()
    elif indexmenusel > 4:
        indexcalcmenu()

def seicalc():
    print("\033c")
    print("\n\n\tSEI Calculator\n")
    cratekeys = input("Price of Crate Keys: $")
    enchantedbooks = input("Price of Enchanted Books: $")
    entropy = input("Price of Entropy: $")
    points = input("Price of Points: $")
    calcseiprice = (cratekeys + enchantedbooks + entropy + points) / 12000
    filename = "/content/drive/MyDrive/ccmedatabase/index/priceSEI"
    with open(filename, "w") as f:
        f.write(str(calcseiprice))
    f.close()
    print("\n\nPrice of SEI: $" + str(calcseiprice))
    print("\n\n\n\t    Database Updated.")
    loopback()
    calculator()

def mixcalc():
    print("\033c")
    print("\n\n\tMIX Calculator\n")
    netherite = input("Price of Netherite: $")
    diamond = input("Price of Diamonds: $")
    gold = input("Price of Gold: $")
    emerald = input("Price of Emeralds: $")
    calcmixprice = (netherite + diamond + gold + emerald) / 300
    filename = "/content/drive/MyDrive/ccmedatabase/index/priceMIX"
    with open(filename, "w") as f:
        f.write(str(calcmixprice))
    f.close()
    print("\n\nPrice of MIX: $" + str(calcmixprice))
    print("\n\n\n\t    Database Updated.")
    loopback()
    calculator()

def fcxcalc():
    print("\033c")
    print("\n\n\tFCX Calculator\n")
    augment = input("Price of Augments: $")
    crab = input("Price of Crab Drops: $")
    fcxentropy = input("Price of Entropy: $")
    calcfcxprice = (augment + crab + fcxentropy) / 3000
    filename = "/content/drive/MyDrive/ccmedatabase/index/priceFCX"
    with open(filename, "w") as f:
        f.write(str(calcfcxprice))
    f.close()
    print("\n\nPrice of FCX: $" + str(calcfcxprice))
    print("\n\n\n\t    Database Updated.")
    loopback()
    calculator()

# Price Change / Price Calculators (Store results in files)
def deltacalc():
    print("\033c")
    print("\n\n\t Delta Calculator\n")
    print("\t   1. Delta SEI")
    print("\t   2. Delta MIX")
    print("\t   3. Delta FCX")
    print("\t   4. Delta E")
    print("\t   5. Back\n\n")
    deltamenusel = int(input("\t\t  "))

    if deltamenusel == 1:
        deltaseicalc()
    if deltamenusel == 2:
        deltamixcalc()
    if deltamenusel == 3:
        deltafcxcalc()
    if deltamenusel == 4:
        deltaecalc()
    if deltamenusel == 5:
        calculator()
    elif deltamenusel > 5:
        deltacalc()

def deltaseicalc():
    print("\033c")
    seiold = float(input("Old Price: $"))
    seinew = float(input("New Price: $"))
    deltasei = float(seinew / seiold)
    filename = "/content/drive/MyDrive/ccmedatabase/delta/deltaSEI"
    with open(filename, "w") as f:
        f.write(str(deltasei))
    f.close()
    print("\n\nDelta SEI: " + str(deltasei))
    print("\n% Change: " + str(float(100 * (deltasei - 1))) + " %")
    print("\n\n\n\t    Database Updated.")
    loopback()
    calculator()

def deltamixcalc():
    print("\033c")
    mixold = float(input("Old Price: $"))
    mixnew = float(input("New Price: $"))
    deltamix = float(mixnew / mixold)
    filename = "/content/drive/MyDrive/ccmedatabase/delta/deltaMIX"
    with open(filename, "w") as f:
        f.write(str(deltamix))
    f.close()
    print("\n\nDelta MIX: " + str(deltamix))
    print("\n% Change: " + str(float(100 * (deltamix - 1))) + " %")
    print("\n\n\n\t    Database Updated.")
    loopback()
    calculator()

def deltafcxcalc():
    print("\033c")
    fcxold = float(input("Old Price: $"))
    fcxnew = float(input("New Price: $"))
    deltafcx = float(fcxnew / fcxold)
    filename = "/content/drive/MyDrive/ccmedatabase/delta/deltaFCX"
    with open(filename, "w") as f:
        f.write(str(deltafcx))
    f.close()
    print("\n\nDelta FCX: " + str(deltafcx))
    print("\n% Change: " + str(float(100 * (deltafcx - 1))) + " %")
    print("\n\n\n\t    Database Updated.")
    loopback()
    calculator()

def deltaecalc():
    print("\033c")
    filename = "/content/drive/MyDrive/ccmedatabase/delta/deltaSEI"
    with open(filename, "r") as f:
        rdeltasei = float(f.read())
    f.close()
    filename = "/content/drive/MyDrive/ccmedatabase/delta/deltaMIX"
    with open(filename, "r") as f:
        rdeltamix = float(f.read())
    f.close()
    filename = "/content/drive/MyDrive/ccmedatabase/delta/deltaFCX"
    with open(filename, "r") as f:
        rdeltafcx = float(f.read())
    f.close()
    deltaE = float((rdeltasei + rdeltamix + rdeltafcx) / 3)
    deltaE = str(deltaE)
    filename = "/content/drive/MyDrive/ccmedatabase/delta/deltaE"
    with open(filename, "w") as f:
        f.write(deltaE)
    f.close()
    print("\nDelta E: " + str(deltaE))
    print("\n\n\n\t    Database Updated.")
    loopback()
    calculator()

def sharecalc():
    print("\033c")
    print("\n\n\t    Share Price Calculator\n\n")
    calcticker = input("Ticker Symbol: ")
    calcbal = float(input("Owner Balance: "))
    calcsplit = float(input("Owner Split %: ")) * .01
    calctotalshares = float(input("Total # of Shares: "))
    filename = "/content/drive/MyDrive/ccmedatabase/delta/deltaE"
    with open(filename, "r") as f:
        calcdeltae = float(f.read())
        f.close()
        calcshareprice = float((calcbal * calcsplit * calcdeltae) / calctotalshares)
        filename = "/content/drive/MyDrive/ccmedatabase/listings/shareprice/" + calcticker + "price"
        try:
            with open(filename, "w") as f:
                f.write(str(calcshareprice))
                f.close()
                print("\n\nShare Price: " + str(calcshareprice))
                print("\n\n\n\t    Database Updated.")
        except:
            sharecalc()
    loopback()
    calculator()

# Income Calculators
def commissioncalc():
    print("\033c")
    print("\n\n\t    Sales & Commission Calculator\n\n")
    calcsharesbefore = float(input("# of Shares Before: "))
    calcsharesafter = float(input("# of Shares After: "))
    calcsharepricecommiss = float(input("Share Price: "))
    calcsharessold = calcsharesbefore - calcsharesafter
    calccommissiontotal = float(calcsharepricecommiss * calcsharessold)
    calccommission = float(.03 * calccommissiontotal)
    calcownerrevenue = float(calccommissiontotal - calccommission)
    print("\n\n# of Shares Sold: " + str(calcsharessold))
    print("\nTotal Revenue: " + str(calccommissiontotal))
    print("\nOwner Revenue: " + str(calcownerrevenue))
    print("\nCCME Commission: " + str(calccommission))
    loopback()
    calculator()

def wagecalc():
    print("\033c")
    print("\n\n\t    Wage Calculator\n")
    calctotalincome = float(input("Total Income: "))
    calcccmewage = .85 * calctotalincome
    calcsecwage = .15 * calctotalincome
    calcpresidentwage = .70 * calcccmewage
    calcvpwage = .30 * calcccmewage
    nagents = 1
    calcsecagentwage = calcsecwage / nagents
    print("\nPresident: " + str(calcpresidentwage))
    print("\nVice President: " + str(calcvpwage))
    print("\nSEC Agent: " + str(calcsecagentwage))
    loopback()
    calculator()


# Call Main Function
mainmenu()

