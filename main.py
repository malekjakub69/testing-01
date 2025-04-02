# Globální seznam úkolů
ukoly = []

def hlavni_menu():
    """
    Hlavní menu programu:
      1. Přidání úkolu
      2. Zobrazení úkolů
      3. Odstranění úkolu
      4. Konec programu
      
    Při zadání neplatné volby uživatele je ošetřena chyba a nabídnuta možnost zadat volbu znovu.
    """
    while True:
        print("\n===== Hlavní menu =====")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Zadejte volbu (1-4): ").strip()
        
        if volba == '1':
            pridat_ukol()
        elif volba == '2':
            zobrazit_ukoly()
        elif volba == '3':
            odstranit_ukol()
        elif volba == '4':
            print("Ukončuji program. Nashledanou!")
            break
        else:
            print("Neplatná volba. Zkuste to prosím znovu.")

def pridat_ukol():
    """
    Umožňuje přidání nového úkolu.
    Uživatel musí zadat nenulový název a popis.
    V případě prázdného vstupu je uživatel vyzván k opětovnému zadání.
    """
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print("Název úkolu nesmí být prázdný. Zkuste to prosím znovu.")
            continue
        
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Popis úkolu nesmí být prázdný. Zkuste to prosím znovu.")
            continue
        
        # Pokud jsou oba vstupy platné, úkol uložíme jako slovník
        ukoly.append({"nazev": nazev, "popis": popis})
        print(f"Úkol '{nazev}' byl úspěšně přidán.")
        break  # úspěšné zadání, ukončíme cyklus

def zobrazit_ukoly():
    """
    Zobrazuje všechny aktuálně uložené úkoly.
    Pokud je seznam prázdný, informuje uživatele.
    """
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("\n===== Seznam úkolů =====")
        for index, ukol in enumerate(ukoly, start=1):
            print(f"{index}. Název: {ukol['nazev']} | Popis: {ukol['popis']}")
    # Po zobrazení se program vrátí do hlavního menu

def odstranit_ukol():
    """
    Umožňuje odstranění úkolu.
    Nejprve se zobrazí seznam všech úkolů, poté se uživatele vyzve k zadání čísla úkolu.
    Program ošetřuje situace:
      - Seznam úkolů je prázdný.
      - Zadání nečíselného vstupu.
      - Zadání čísla, které neodpovídá žádnému úkolu.
      - Možnost zrušení operace.
    """
    if not ukoly:
        print("Seznam úkolů je prázdný. Není co odstranit.")
        return

    while True:
        print("\n===== Odstranit úkol =====")
        zobrazit_ukoly()  # zobrazíme aktuální seznam úkolů
        
        vstup = input("Zadejte číslo úkolu k odstranění (nebo 'z' pro zrušení): ").strip()
        
        # Možnost zrušení operace
        if vstup.lower() == 'z':
            print("Odstranění úkolu zrušeno.")
            break
        
        try:
            index = int(vstup)
            if index < 1 or index > len(ukoly):
                print("Neplatné číslo úkolu. Zkuste to prosím znovu.")
                continue
            # Odebrání vybraného úkolu (index je upraven o -1, protože seznam začíná na 0)
            odstraneny = ukoly.pop(index - 1)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
            break
        except ValueError:
            print("Prosím zadejte platné číslo.")
            continue

if __name__ == "__main__":
    hlavni_menu()