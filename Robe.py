import random

# Risposte di conforto
risposte_conforto = [
    "Mi dispiace che tu ti senta così. Sono qui con te.",
    "Capisco, non è facile. Vuoi parlarne?",
    "Grazie per avermelo detto. Non sei solo.",
    "A volte basta essere ascoltati. Io ci sono."
]

# Domande e frasi di compagnia
risposte_compagnia = [
    "Che stai facendo adesso?",
    "Com’è andata la tua giornata?",
    "Ti va di fare due chiacchiere?",
    "Dimmi una cosa a caso 🙂",
    "Se vuoi possiamo parlare di qualunque cosa."
]

# Frasi di presenza
risposte_presenza = [
    "Sono qui, anche se non sai cosa dire.",
    "Possiamo anche stare in silenzio.",
    "Io resto."
]

# Parole chiave
parole_tristi = [
    "triste", "solo", "sola", "male", "piangere", "stanco", "vuoto"
]

parole_compagnia = [
    "compagnia", "parliamo", "noia", "chiacchiere", "annoia"
]


def rispondi(messaggio):
    messaggio = messaggio.lower()

    for parola in parole_tristi:
        if parola in messaggio:
            return random.choice(risposte_conforto)

    for parola in parole_compagnia:
        if parola in messaggio:
            return random.choice(risposte_compagnia)

    # Risposta neutra
    return random.choice(risposte_presenza)


# ---- AVVIO ROBe ----
print("ROBe 🤖")
print("Sono qui per farti compagnia. Scrivi 'esci' per
