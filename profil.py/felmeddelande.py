def check_login(email, password):
    # Kolla om e-posten är i giltigt format
    if not validate_email_format(email):
        return "Ogiltig e-postadress"

    # Kolla om e-posten existerar i databasen eller textfilen
    if not email_exists_in_database(email):
        return "E-postadressen existerar inte"

    # Kolla om lösenordet matchar e-postadressen
    if not verify_password(email, password):
        return "Fel lösenord"

    # Inloggningen lyckades
    return "Inloggning lyckades"


def validate_email_format(email):
    # Implementera validering av e-postadressens format här
    # Till exempel: använd en reguljär uttryckning för att kolla om det är ett giltigt e-postformat
    pass


def email_exists_in_database(email):
    # Implementera logik för att kolla om e-postadressen finns i databasen eller textfilen här
    pass


def verify_password(email, password):
    # Implementera logik för att verifiera lösenordet för den angivna e-postadressen här
    pass


# Användning av funktionen
email = input("Ange din e-postadress: ")
password = input("Ange ditt lösenord: ")

result = check_login(email, password)
print(result)

