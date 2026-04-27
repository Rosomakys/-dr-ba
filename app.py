# app.py
import streamlit as st
from datetime import datetime
from smeny import kalendar, kontakty

st.title("Údržba - Aktuální směna")

# Zjištění aktuálního času
ted = datetime.now()
dnes_str = ted.strftime("%Y-%m-%d")
hodina = ted.hour

# Logika pro výběr směny
if dnes_str in kalendar:
    if 6 <= hodina < 18:
        aktualni = kalendar[dnes_str]["den"]
        st.info(f"Právě je v práci: **Ranní ({aktualni})**")
    else:
        aktualni = kalendar[dnes_str]["noc"]
        st.warning(f"Právě je v práci: **Noční ({aktualni})**")
    
    # Výpis kontaktů s funkcí volání po kliknutí
    st.write(f"### Kontakty pro směnu {aktualni}")
    for jmeno, cislo in kontakty.get(aktualni, []):
        st.write(f"{jmeno}: [{cislo}](tel:{cislo})")
else:
    st.error("Pro dnešní datum nejsou v kalendáři (smeny.py) uložena žádná data.")

# Zde ponech svůj původní kód pro logování výkonu, pokud ho chceš mít pod tím
# st.divider()
# ... tvůj další kód ...