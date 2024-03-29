
// Validera e-post vid inlogg
function validateLogin(email, password) {
    // Kolla om e-posten är i ogiltigt format
    if (!isEmailValid(email)) {
      return "Ogiltig e-postadress";
    }
  
    // Kolla om e-posten existerar i databasen/textfilen
    if (!isEmailExists(email)) {
      return "E-posten existerar inte i databasen";
    }
  
    // Kolla om lösenordet matchar angiven e-post
    if (!isPasswordCorrect(email, password)) {
      return "Fel lösenord för angiven e-postadress";
    }
  
    // Inloggning lyckades, ingen felmeddelande behövs
    return "";
  }
  
  // Funktion för att kolla om e-post är i godkänt format
  function isEmailValid(email) {
    // Implementera valideringslogik här (t.ex. med hjälp av reguljära uttryck)
    return true; // Returnera true om e-posten är i korrekt format, annars false
  }
  
  // Funktion för att kolla om e-posten existerar i databasen/textfilen
  function isEmailExists(email) {
    // Implementera söklogik här för att kolla om e-posten finns i databasen/textfilen
    return true; // Returnera true om e-posten existerar, annars false
  }
  
  // Funktion för att kolla om lösenordet tillhör angiven e-post
  function isPasswordCorrect(email, password) {
    // Implementera logik för att kolla om lösenordet matchar angiven e-post
    return true; // Returnera true om lösenordet är korrekt, annars false
  }
  
  // Använda funktionen vid inlogg
  let errorMessage = validateLogin("example@example.com", "password123");
  if (errorMessage) {
    // Visar felmeddelandet om det finns ett fel
    console.log(errorMessage);
  } else {
    // Ingen felmeddelande visas vid lyckad inloggning
    console.log("Inloggning lyckades");
  }
  
  
  