ukoly = []

def hlavni_menu():
    print("\n----- Hlavní menu -----")
    print("1. Přidat úkol")
    print("2. Zobrazit úkoly")
    print("3. Odstranit úkol")
    print("4. Konec")
        
    volba = input("Vyberte možnost 1-4: ")
        
    if volba == '1':
        pridat_ukol()
    elif volba == '2':
        zobrazit_ukoly()
    elif volba == '3':
        odstranit_ukol()
    elif volba == '4':
        print("\nKončíme.")
    else:
        print("\nNeplatná volba, vyberte možnost 1-4.")
        hlavni_menu()

def pridat_ukol():
    while True:
        nazev_ukolu = input("\nZadejte název úkolu: ")
        if nazev_ukolu == "":  
            print("\nNázev úkolu nesmí být prázdný, zadejte název úkolu.")
        else:
            break

    while True:
        popis_ukolu = input("\nZadejte popis úkolu: ")
        if popis_ukolu == "": 
            print("\nPopis úkolu nesmí být prázdný, zadejte popis úkolu.")
        else:
            break 
        
    ukoly.append({"nazev_ukolu": nazev_ukolu, "popis_ukolu": popis_ukolu})
    print(f"\nÚkol '{nazev_ukolu} - {popis_ukolu}' byl přidán.")

    hlavni_menu()

def zobrazit_ukoly():
    if not ukoly:
        print("\nŽádné úkoly k zobrazení.")
    else:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol['nazev_ukolu']} - {ukol['popis_ukolu']}")

    hlavni_menu()

def odstranit_ukol():
    if not ukoly:
        print("\nŽádné úkoly k odstranění.")
        hlavni_menu()
    
    else:
        while True:
            index = input("\nZadejte číslo úkolu, který chcete odstranit: ") # input pro zadání čísla úkolu
            try:
                index = int(index) - 1 # převod čísla úkolu na index od 0 
                if 0 <= index < len(ukoly): # index musí být větší nebo roven 0 a menší než počet prvků v seznamu   
                    odstraneny_ukol = ukoly.pop(index)
                    print(f"\nÚkol '{odstraneny_ukol['nazev_ukolu']}' byl odstraněn.")
                    hlavni_menu()  
                    break
                else:
                    print("\nNeplatné číslo úkolu.")
            except ValueError:
                print("\nZadejte platné číslo.")

hlavni_menu()
