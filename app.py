import streamlit as st
import datetime

# --- CONFIGURACIÓ DE LA PÀGINA ---
st.set_page_config(
    page_title="Tradició Viva SJ",
    page_icon="🔥",
    layout="wide"
)

# --- BASE DE DADES INTERNA (RELATS, TIMELINE I DINÀMIQUES) ---

# 1. DADES DEL TIMELINE
timeline_data = [
    {"any": 1540, "titol": "Fundació de la Companyia", "desc": "Ignasi i els companys funden la Companyia de Jesús a Roma. Missió universal sense geocalització fixa.", "tags": ["Història", "Espiritualitat"], "icon": "🔥"},
    {"any": 1548, "titol": "Col·legi de Messina", "desc": "El primer col·legi per a laics. Neix l'estratègia educativa com a plataforma apostòlica.", "tags": ["Història", "Innovació"], "icon": "🏫"},
    {"any": 1599, "titol": "Ratio Studiorum", "desc": "La sistematització global. Un sol mètode d'estudis per unir tots els col·legis del món.", "tags": ["Història", "Pedagogia"], "icon": "s.📚"},
    {"any": 1773, "titol": "La Supressió", "desc": "El moment de la mort institucional. La Companyia és dissolta pel Papa. Lliçó de resiliència.", "tags": ["Història", "Crisi"], "icon": "🌑"},
    {"any": 1814, "titol": "La Restauració", "desc": "El renaixement. Reconstruir la missió en un món que ha canviat completament.", "tags": ["Història", "Adaptació"], "icon": "🌱"},
    {"any": 1973, "titol": "Homes per als altres (Arrupe)", "desc": "Pedro Arrupe a València. Gir copernicà cap a la justícia i el servei com a fe.", "tags": ["Justícia", "Identitat"], "icon": "❤️"},
    {"any": 1986, "titol": "Característiques Educació SJ", "desc": "Document clau que tradueix l'espiritualitat a l'escola moderna post-Vaticà II.", "tags": ["Pedagogia", "Identitat"], "icon": "📝"},
    {"any": 1993, "titol": "Paradigma Pedagògic (PPI)", "desc": "Es defineix el mètode: Context, Experiència, Reflexió, Acció, Avaluació.", "tags": ["Pedagogia", "Espiritualitat"], "icon": "🔄"},
    {"any": 2019, "titol": "Una Tradició Viva / PAU", "desc": "Les Preferències Apostòliques Universals i la crida a la conversió ecològica i juvenil.", "tags": ["Justícia", "Actualitat"], "icon": "🌍"},
    {"any": 2021, "titol": "Ciutadania Global (Jogja)", "desc": "L'educació com a formació d'agents de reconciliació global.", "tags": ["Justícia", "Innovació"], "icon": "🤝"}
]

# 2. DADES DELS RELATS
relats = {
    "Històric": {
        "titol": "L'Evolució Constant",
        "text": """Des de Messina (1548) fins avui, l'educació jesuïta ha estat una història d'adaptació constant.
        
No va néixer com un pla preconcebut, sinó com una resposta a les necessitats. La *Ratio Studiorum* (1599) ens va donar unitat metodològica durant segles. Però la tradició no és un museu: la Supressió (1773) ens va ensenyar que les estructures poden morir, però l'esperit roman.
        
Després de la Restauració (1814), vam haver de reconstruir-ho tot. Avui, som hereus d'aquesta cadena ininterrompuda que es reinventa a cada segle per respondre als nous reptes."""
    },
    "Espiritualitat": {
        "titol": "L'Ànima de l'Educació",
        "text": """No es pot entendre la pedagogia jesuïta sense Manresa. Tot neix de l'experiència d'Ignasi: aprendre a mirar-se a un mateix i al món.
        
El 'Paradigma Pedagògic Ignasià' (1993) no és més que l'aplicació dels Exercicis Espirituals a l'aula. No ensenyem només continguts, ensenyem a viure un procés:
1. Partir del **Context** real.
2. Viure una **Experiència** sentida.
3. Fer **Reflexió** sobre el viscut.
4. Moure's a l'**Acció**.
5. Fer **Avaluació** per millorar."""
    },
    "Innovació": {
        "titol": "Fidelitat Creativa",
        "text": """La tradició jesuïta no és fer sempre el mateix, sinó buscar sempre el mateix *fi* (ajudar les ànimes) canviant els *mitjans*. Això és la 'Fidelitat Creativa'.
        
Ignasi va trencar motlles adoptant el 'Modus Parisiensis' al segle XVI, que era la innovació del moment. Avui, projectes com l'Horitzó+ o la NEI responen al mateix esperit: adaptar els espais, els horaris i els rols per mantenir viva la missió en un món digital i líquid."""
    },
    "Justícia i Ciutadania": {
        "titol": "Formar per a la Missió",
        "text": """Per a què eduquem? El propòsit ha evolucionat. Vam començar formant bons cristians i ciutadans virtuosos.
        
Però el 1973, el P. Arrupe ens va despertar amb un xoc: 'Formar homes i dones per als altres'. La fe sense justícia no és fe cristiana.
        
Avui (JESEDU-Jogja 2021), això es tradueix en la Ciutadania Global: educar persones que, davant d'un món trencat, no aixequen murs sinó ponts, i esdevenen agents de reconciliació amb Déu, amb els altres i amb la Creació."""
    }
}

# 3. DADES DE LES DINÀMIQUES
dinamiques = {
    "Petit": {
        "nom": "Conversa Espiritual",
        "desc": "Ideal per a grups de menys de 15 persones.",
        "passos": [
            "Lectura personal del relat en silenci (5 min).",
            "1a Ronda: 'Què em ressona?' (Sense debat, només escolta).",
            "2a Ronda: 'Què m'ha tocat del que heu dit?'.",
            "3a Ronda: Conclusions o crida al grup."
        ]
    },
    "Gran": {
        "nom": "El Mur del Temps",
        "desc": "Ideal per a grups grans (més de 15 persones).",
        "passos": [
            "Projecteu o imprimiu les fitxes del Timeline seleccionades i pengeu-les a la paret.",
            "Doneu gomets vermells i verds als participants.",
            "Els participants s'aixequen i enganxen el gomet Verd on veuen una fortalesa avui, i el Vermell on veuen un repte pendent.",
            "Debat obert sobre on s'acumulen els colors."
        ]
    },
    "Rapid": {
        "nom": "La Imatge Clau (Visual Thinking)",
        "desc": "Per a sessions curtes (menys de 45 min).",
        "passos": [
            "Projecteu només dues imatges del Timeline: la més antiga (1548) i la més nova (2021).",
            "Pregunta llançada: 'Què hem de mantenir del 1548 per arribar vius al 2021?'",
            "Pluja de idees ràpida (Brainstorming) en pissarra."
        ]
    }
}

# --- INTERFÍCIE (SIDEBAR) ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Ihs-logo.svg/1200px-Ihs-logo.svg.png", width=100)
st.sidebar.header("⚙️ Configura la Sessió")

tema = st.sidebar.selectbox("Fil Conductor", list(relats.keys()))
temps = st.sidebar.select_slider("Durada disponible", options=["30 min", "1 hora", "2 hores", "Matí sencer"])
participants = st.sidebar.number_input("Nombre de participants", min_value=1, value=20)
idioma = st.sidebar.selectbox("Idioma de sortida", ["Català", "Castellano", "English"]) # (Només visual per ara)

# Lògica de selecció automàtica
tipus_dinamica = "Gran"
if temps == "30 min":
    tipus_dinamica = "Rapid"
elif participants < 15:
    tipus_dinamica = "Petit"
else:
    tipus_dinamica = "Gran"

dinamica_triada = dinamiques[tipus_dinamica]

# --- PÀGINA PRINCIPAL ---
st.title("Generador de Sessions: Tradició Viva SJ")
st.markdown(f"**Proposta personalitzada per a:** {participants} participants | {temps} | Enfocament: {tema}")
st.markdown("---")

# PESTANYES
tab1, tab2, tab3 = st.tabs(["📖 El Relat", "⏳ Timeline Visual", "🤝 La Dinàmica"])

with tab1:
    st.subheader(relats[tema]["titol"])
    st.write(relats[tema]["text"])
    st.info("💡 **Consell pel formador:** Llegeix aquest text a poc a poc o fes que un participant el llegeixi en veu alta.")

with tab2:
    st.subheader("Fitxes Clau per a aquest tema")
    st.write("Selecció automàtica dels moments històrics més rellevants per al fil conductor triat:")
    
    # Filtratge simple (per ara mostrem tots, o podríem filtrar per tags)
    col1, col2 = st.columns(2)
    for i, event in enumerate(timeline_data):
        # Filtre bàsic: Si el tema coincideix amb algun tag de l'event, o mostrem els generals
        if tema in event["tags"] or "Història" in event["tags"]:
            with (col1 if i % 2 == 0 else col2):
                st.markdown(f"### {event['icon']} {event['any']}")
                st.markdown(f"**{event['titol']}**")
                st.caption(event['desc'])
                st.markdown("---")

with tab3:
    st.subheader(f"Activitat Proposada: {dinamica_triada['nom']}")
    st.warning(f"🎯 {dinamica_triada['desc']}")
    
    st.markdown("#### Passos a seguir:")
    for pas in dinamica_triada["passos"]:
        st.markdown(f"- {pas}")

# --- PEU DE PÀGINA ---
st.markdown("---")
st.caption("Generat amb IA (Lògica de Gemini) | Basat en els documents 'Una Tradició Viva'.")
