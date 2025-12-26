import streamlit as st
import datetime

# --- CONFIGURACIÓ DE LA PÀGINA ---
st.set_page_config(
    page_title="Tradició Viva SJ - Generador de Sessions",
    page_icon="🔥",
    layout="wide"
)

# --- BASE DE DADES MESTRA: RELATS SUMATIUS EXTENSOS (25 FITES) ---
# Aquesta estructura conté els textos complets per als fils principals.

discursos_extensos = {
    "🏛️ Història i Evolució Institucional": {
        1521: {
            "titol": "Pamplona: El Trencament Necessari",
            "nivell_1": "La història de l'educació jesuïta comença amb un fracàs militar. La ferida d'Íñigo de Loiola a la batalla de Pamplona no és només un fet mèdic, sinó el col·lapse de l'ideal del 'cavaller cortesà' i l'inici d'una recerca radical de sentit que acabaria transformant la pedagogia occidental.",
            "nivell_2": "Íñigo defensava la fortalesa de Pamplona contra els francesos amb una obstinació suïcida. Una bala de canó li va destrossar la cama i, amb ella, el seu projecte de vida basat en l'honor, l'aparença i l'èxit mundà. Durant la llarga i dolorosa convalescència a Loiola, sense llibres de cavalleries per llegir, es veu obligat a llegir la 'Vita Christi' i la 'Llegenda Àuria'. Allà descobreix que l'heroisme dels sants li provoca una alegria duradora, mentre que les fantasies mundanes el deixen buit. És el descobriment del discerniment.",
            "nivell_3": "Històricament, aquest moment marca el pas de l'Edat Mitjana al Renaixement en la vida d'Ignasi. La pedagogia jesuïta heretarà d'aquest moment una convicció clau: l'error i el fracàs poden ser oportunitats de creixement (Kairós). L'educació no consistirà a crear triomfadors que mai cauen, sinó persones capaces de 'llegir' les seves pròpies ferides i reorientar la seva vida cap a un bé major."
        },
        1522: {
            "titol": "Manresa: El Laboratori de l'Experiència",
            "nivell_1": "Si Pamplona va ser el xoc, Manresa va ser l'escola. Durant 11 mesos, Ignasi viu com un pobre i experimenta en la seva pròpia ànima les llums i les ombres. Aquí neix el llibre dels Exercicis Espirituals, que no és un text per ser llegit, sinó el manual pedagògic per excel·lència de la Companyia.",
            "nivell_2": "A la vora del riu Cardoner, Ignasi té una il·luminació intel·lectual tan forta que diu que 'li semblava ser un altre home i tenir un altre intel·lecte'. Aprèn que Déu no és una idea abstracta, sinó que es comunica directament amb la criatura. A Manresa sistematitza aquest aprenentatge en un mètode: els Exercicis. Entén que per transformar una persona no n'hi ha prou amb discursos; cal fer-la passar per una experiència estructurada que toqui l'afecte i la raó.",
            "nivell_3": "L'aportació fundacional de Manresa a l'educació és la 'cura personalis' i l'adaptació. Ignasi aprèn que Déu el tractava 'com un mestre d'escola tracta un nen', adaptant-se a la seva capacitat. Aquesta pedagogia divina esdevindrà la norma de les escoles jesuïtes: adaptar el mètode al subjecte, respectar els seus ritmes i processos interns, i valorar l'experiència directa per sobre de la teoria memoritzada."
        },
        1534: {
            "titol": "Montmartre: Amics en el Senyor",
            "nivell_1": "A la Universitat de París, Ignasi no està sol. Aplega un grup d'estudiants de diferents nacions (Xavier, Favre, Laínez...) que comparteixen habitació, estudis i ideals. A la cripta de Montmartre fan vots privats, segellant el naixement d'una comunitat d'amics que volen 'ajudar les ànimes'.",
            "nivell_2": "L'ambient universitari de París és decisiu. Allà adopten el 'Modus Parisiensis' (ordre, mètode actiu, discussió) que després portaran als seus col·legis. Però el més important és el vincle humà. No són una organització jeràrquica encara; són 'amics en el Senyor'. Comparteixen la vida i els diners. Aquesta dimensió comunitària és l'origen de la visió jesuïta de l'escola no com una empresa de serveis, sinó com una comunitat educativa.",
            "nivell_3": "Montmartre representa la unió de la 'pietas' (els vots, l'ideal religiós) amb la 'eruditio' (tots eren Mestres en Arts per la Sorbona). Ignasi s'adona que per servir Déu en el món complex del s. XVI, la bona voluntat no és suficient; cal una formació intel·lectual rigorosa. L'excel·lència acadèmica neix aquí com una exigència de la caritat: estimar millor sabent-ne més."
        },
        1540: {
            "titol": "Regimini Militantis: La Missió Universal",
            "nivell_1": "El Papa Pau III aprova oficialment la Companyia de Jesús. Neix una ordre religiosa nova, sense hàbit propi, sense cor (oració cantada en comú) i amb un quart vot d'obediència al Papa per anar a qualsevol lloc del món. Curiosament, l'educació escolar no apareixia com a prioritat.",
            "nivell_2": "La butlla fundacional defineix la missió com la 'defensa i propagació de la fe' mitjançant la predicació, els exercicis i la caritat. Els primers jesuïtes es veien com a 'cavalleria lleugera', mòbils i disponibles per a missions d'urgència. Fundar col·legis estables semblava, d'entrada, una càrrega que els lligaria a un lloc i els impediria aquesta mobilitat apostòlica radical.",
            "nivell_3": "Aquest moment és clau per entendre que l'escola jesuïta és instrumental. No existim 'per fer escoles', sinó que fem escoles perquè vam discernir que són la millor eina per a la missió. Això ens dona una llibertat institucional enorme: si una escola deixa de complir la missió evangelitzadora i social, perd el seu sentit fundacional. L'estructura ha de servir sempre a l'Esperit."
        },
        1548: {
            "titol": "Messina: El Gir Estratègic",
            "nivell_1": "El primer col·legi obert específicament per a laics marca el canvi d'estratègia més gran de la història de la Companyia. Ignasi accepta la petició del Senat de Messina i descobreix que l'escola és una plataforma apostòlica de primer ordre.",
            "nivell_2": "Fins al 1548, els jesuïtes només tenien residències per formar els seus propis estudiants. A Messina, s'obre al públic general. L'èxit és tan gran que Ignasi veu com, a través dels alumnes, transforma les famílies i la ciutat sencera. Envia a Jeroni Nadal a organitzar-ho, i aquest estableix les bases del pla d'estudis. L'educació passa de ser una 'obra de misericòrdia' més, a ser el 'ministeri principal' de l'Ordre.",
            "nivell_3": "Messina suposa una innovació jurídica i teològica. Per mantenir la gratuïtat de l'ensenyament (clau per a la justícia social de l'època), el col·legi havia de tenir rendes pròpies, cosa que aparentment contradeia la pobresa radical de l'ordre. Ignasi ho resol distingint entre el 'cos de la Companyia' (pobre) i els 'col·legis' (institucions amb recursos per al servei). Això demostra un pragmatisme sant: adaptar les estructures per garantir la viabilitat de la missió."
        },
        1551: {
            "titol": "Col·legi Romà: L'Excel·lència Gratuïta",
            "nivell_1": "Ignasi funda a Roma 'l'escola model'. Volia demostrar que es podia oferir la millor educació intel·lectual del moment de manera totalment gratuïta. El Col·legi Romà (avui la Gregoriana) esdevé la mare de totes les universitats jesuïtes.",
            "nivell_2": "Al Col·legi Romà s'hi apleguen els millors professors de tot Europa. S'hi ensenyen llengües clàssiques, teologia, però també matemàtiques i astronomia (Clavius, professor de Galileu, hi treballava). Ignasi posa un rètol a la porta: 'Escola de Gramàtica, Humanitats i Doctrina Cristiana. Gratis'. Volia influir en el centre de la cristiandat per irradiar un model replicable a les perifèries.",
            "nivell_3": "El Col·legi Romà estableix el principi de la 'universalitat'. No és una escola local, és una escola per al món. També consagra la unió entre fe i ciència. Els jesuïtes demostren que ser catòlic no està renyit amb estar a l'avantguarda científica. La pedagogia que s'hi desenvolupa es basa en l'activitat de l'alumne, el teatre, les disputes públiques i una rigorosa progressió acadèmica."
        },
        1556: {
            "titol": "Les Constitucions: El Llegat Legislatiu",
            "nivell_1": "L'any de la mort d'Ignasi es promulguen les Constitucions. La Part IV està dedicada íntegrament a l'educació. Ja no és una improvisació; l'educació queda codificada com a part essencial del carisma jesuïta.",
            "nivell_2": "Ignasi, ja molt malalt, va dictar les normes per assegurar que l'esperit dels inicis no es perdés amb l'expansió. Les Constitucions detallen des del paper del Rector fins als horaris, però sempre deixant una porta oberta: 'segons temps, llocs i persones'. Aquesta flexibilitat constitucional és el que ha permès que els col·legis jesuïtes s'adaptin des del Japó del s. XVI fins al Silicon Valley del s. XXI.",
            "nivell_3": "Un punt clau de la Part IV és la insistència en seleccionar bé els professors i en la seva formació continuada. Ignasi sabia que 'no hi ha mètode millor que un bon mestre'. També s'hi defineix l'objectiu final dels estudis: no l'erudició vanitosa, sinó que els estudiants 'puguin donar fruit en les ànimes i governar la república amb justícia'."
        },
        1599: {
            "titol": "Ratio Studiorum: El Sistema Global",
            "nivell_1": "Sota el generalat de Claudio Acquaviva es publica la versió definitiva de la 'Ratio Studiorum' (Pla d'Estudis). És el document que unifica pedagògicament centenars de col·legis en tots els continents, creant el primer sistema educatiu veritablement global de la història.",
            "nivell_2": "La Ratio no va sortir del no-res. Va ser fruit de dècades d'intercanvi d'esborranys entre col·legis de tot el món (una mena de 'wiki' del segle XVI). Codificava les bones pràctiques: la prelecció, la repetició, la composició, el debat i l'emulació. Garantia que un alumne a Lima, a Goa o a Polònia rebés la mateixa qualitat humana i espiritual.",
            "nivell_3": "Tot i ser un document normatiu, la Ratio institucionalitzava l'humanisme cristià. El seu currículum basat en els clàssics grecollatins buscava l''eloqüència perfecta': la capacitat de pensar amb rigor i comunicar amb bellesa per persuadir cap al bé. Va ser vigent (amb adaptacions) fins ben entrat el segle XX, donant una consistència intel·lectual única a l'Orde."
        },
        1773: {
            "titol": "La Supressió: La Crisi",
            "nivell_1": "El Papa Climent XIV, pressionat per les monarquies absolutistes, suprimeix universalment la Companyia de Jesús. Els jesuïtes són expulsats, empresonats o exiliats. Els seus 845 col·legis són tancats o confiscats. És la mort institucional.",
            "nivell_2": "La Companyia va ser víctima del seu propi èxit i de la seva fidelitat al Papa en un moment de nacionalismes ferotges. Però el fet sorprenent és la supervivència. A la Rússia blanca, la Tsarina Caterina prohibeix llegir el decret de supressió per no perdre els mestres jesuïtes. Allà, un petit grup manté viu el foc sota les cendres durant 40 anys, mentre ex-jesuïtes com Pignatelli mantenen xarxes informals de fidelitat.",
            "nivell_3": "Aquest període ensenya una lliçó vital sobre la resiliència i la identitat. L'educació jesuïta va demostrar que era més que uns edificis; era un esperit. Molts jesuïtes van continuar ensenyant com a sacerdots seculars, mantenint l'estil ignasià sense l'estructura. La Supressió va purificar l'Ordre de qualsevol temptació de poder temporal i la va tornar a la vulnerabilitat dels orígens."
        },
        1814: {
            "titol": "La Restauració: El Renaixement",
            "nivell_1": "El Papa Pius VII restaura la Companyia de Jesús. Els supervivents, ja molt grans, i els nous novicis comencen la tasca titànica de reconstruir la xarxa educativa en un món que ha canviat radicalment després de la Revolució Francesa.",
            "nivell_2": "El món de 1814 ja no és el de 1773. És el món del liberalisme, de la ciència positiva, dels estats-nació. Els jesuïtes tornen amb una certa nostàlgia de l'Antic Règim, cosa que marcarà el segle XIX amb un tarannà conservador i defensiu. Tanmateix, la demanda dels seus col·legis és altíssima. Es reobren escoles i se'n funden de noves, especialment als Estats Units, on l'expansió és explosiva.",
            "nivell_3": "La tensió entre 'restaurar el passat' i 'adaptar-se al present' és constant. Es recupera la Ratio Studiorum, però aviat es veu que cal actualitzar-la per incloure les noves ciències experimentals i les llengües vernacles. És un segle de tensió fecunda que prepararà el terreny per a la gran renovació del segle XX."
        },
        1965: {
            "titol": "CG 31: Renovació Post-Conciliar",
            "nivell_1": "Sota el lideratge del P. Arrupe i l'impuls del Concili Vaticà II, la Congregació General 31 marca l'inici de la modernitat jesuïta. Es revisa tot per tornar a l'esperit original d'Ignasi i abandonar les rigideses acumulades.",
            "nivell_2": "La CG 31 reconeix que el món ha canviat i que l'Església s'ha d'obrir. Es demana una profunda renovació dels mètodes pedagògics i de la vida religiosa. Es deixa enrere l'estructura quasi militar i monàstica per recuperar el discerniment apostòlic. Arrupe impulsa els jesuïtes a afrontar els reptes de l'ateisme, el desenvolupament i la justícia.",
            "nivell_3": "Educativament, la CG 31 és crucial perquè legitima la investigació i l'experimentació. S'anima els col·legis a deixar de ser 'fortaleses de la fe' per esdevenir centres de diàleg amb la cultura contemporània. Es posa l'èmfasi en la formació integral de la persona, més enllà de la mera instrucció acadèmica o catequètica."
        },
        1967: {
            "titol": "Secretariat d'Educació: Creació de l'Estructura",
            "nivell_1": "El P. Arrupe crea a Roma el Secretariat d'Educació de la Companyia. Per primera vegada, hi ha un organisme central encarregat no de 'manar', sinó d'animar, coordinar i donar visió estratègica a la immensa xarxa global.",
            "nivell_2": "Després del Vaticà II, la diversitat era tal que es corria el risc de fragmentació. Cada província feia la seva. El Secretariat neix per facilitar l'intercanvi d'informació i per impulsar reflexions comunes. La seva tasca no és imposar un currículum únic (impossible al s. XX), sinó definir els criteris d'identitat que fan que una escola al Japó i una al Perú siguin ambdues 'jesuïtes'.",
            "nivell_3": "La creació del Secretariat és el reconeixement que l'educació requereix una governança professional i especialitzada. Ja no n'hi ha prou amb la bona voluntat dels superiors religiosos. Comença l'era dels documents corporatius i la construcció conscient d'un 'Cos Universal' d'educadors."
        },
        1973: {
            "titol": "Homes per als altres (València - Arrupe)",
            "nivell_1": "En un discurs als antics alumnes a València, Pedro Arrupe llança la bomba: 'La nostra educació ha fracassat si no formem homes i dones per als altres'. És la crida a vincular la fe amb la justícia social de manera indissoluble.",
            "nivell_2": "El discurs va ser polèmic. Molts antics alumnes, ben situats socialment, es van sentir ofesos. Arrupe els deia que no n'hi havia prou amb anar a missa i ser bons professionals; calia comprometre's amb la transformació de les estructures injustes que generen pobresa. Aquest concepte d' 'homes per als altres' es va convertir en el nou lema identitari de les escoles, reorientant tota la pastoral i l'acció social.",
            "nivell_3": "Teològicament, Arrupe afirma que Déu està en els pobres i que l'amor a Déu és fals si no es tradueix en amor efectiu (polític, econòmic, social) pel proïsme. Això obliga els col·legis a revisar els seus programes: s'introdueixen les experiències de 'pas', els voluntariats i l'anàlisi crítica de la realitat social com a part del currículum."
        },
        1975: {
            "titol": "CG 32: Fe i Justícia",
            "nivell_1": "La Congregació General 32 oficialitza la intuïció d'Arrupe amb el Decret 4: 'La missió de la Companyia de Jesús avui és el servei de la fe, del qual la promoció de la justícia constitueix una exigència absoluta'.",
            "nivell_2": "Ja no és només una opinió del General, és un mandat legislatiu suprem. Això provoca una crisi i una purificació en moltes obres. Algunes escoles tanquen, d'altres es transformen radicalment. S'aposta per l'educació popular (Fe y Alegría agafa fuerza) i es demana a les escoles d'elit que posin els seus recursos al servei del canvi social. El 'màrtir' d'aquesta opció serà Rutilio Grande i, més tard, los màrtirs de la UCA al Salvador.",
            "nivell_3": "La formula 'Fe-Justícia' evita dos extrems: l'espiritualisme desencarnat (resar sense actuar) i l'activisme sociològic (actuar sense arrel transcendent). Per a l'escola, significa que l'excel·lència acadèmica només té sentit si serveix per humanitzar el món. Es comença a parlar de l'alumne com a agent de canvi."
        },
        1980: {
            "titol": "ICAJE: Comissió Internacional",
            "nivell_1": "Es funda la Comissió Internacional per a l'Apostolat de l'Educació Jesuïta (ICAJE). Amb la disminució de jesuïtes, es fa necessari crear un grup mixt (jesuïtes i laics) que reflexioni sobre el futur de la xarxa a nivell mundial.",
            "nivell_2": "L'ICAJE rep un encàrrec vital: posar per escrit l'essència de la pedagogia jesuïta. Fins aleshores, es transmetia per 'osmosi' perquè les escoles estaven plenes de religiosos. Ara que els laics assumeixen la direcció, cal explicitar el carisma. L'ICAJE treballarà durant sis anys consultant a milers d'educadors per redactar les 'Característiques'.",
            "nivell_3": "El naixement de l'ICAJE marca el pas definitiu cap a la col·laboració. Es reconeix que el carisma ignasià no és propietat exclusiva dels jesuïtes, sinó un do per a l'Església que pot ser viscut i liderat per laics. És l'inici de la 'Mesa Apostòlica' compartida i la professionalització de la identitat."
        },
        1986: {
            "titol": "Les Característiques de l'Educació",
            "nivell_1": "Es publica 'Les Característiques de l'Educació de la Companyia de Jesús'. És el primer gran document global des de la Ratio Studiorum de 1599. Defineix 28 trets que fan que una escola sigui jesuïta, més enllà del currículum oficial de cada país.",
            "nivell_2": "El document és una carta de navegació. No diu quins llibres fer servir, sinó quin estil tenir: atenció personal, recerca de l'excel·lència (Magis), visió positiva del món, formació per a l'acció... Serveix perquè les escoles facin autoavaluació. Si una escola compleix les lleis estatals però falla en aquestes característiques, deixa de ser jesuïta.",
            "nivell_3": "Les 'Característiques' posen l'accent en l'atmosfera escolar i en la comunitat educativa. Introdueixen conceptes com 'educació per a la justícia', 'formació d'homes i dones per als altres' i la importància del testimoni adult. És un document fundant per a l'era de la col·laboració laïcal."
        },
        1993: {
            "titol": "Paradigma Pedagògic Ignasià (PPI)",
            "nivell_1": "Les 'Característiques' eren inspiradores, però calia aterrar-les a classe. El 1993 es publica el 'Paradigma Pedagògic Ignasià' (PPI), que estructura l'aprenentatge en 5 passos: Context, Experiència, Reflexió, Acció i Avaluació.",
            "nivell_2": "El PPI no és un invent nou, sinó l'aplicació de l'esquema dels Exercicis Espirituals a l'ensenyament de qualsevol matèria. Supera la classe magistral on l'alumne és passiu. El cicle demana: 1) Saber on és l'alumne (Context), 2) Que l'alumne 'tasti' la realitat (Experiència), 3) Que en capti el significat profund (Reflexió), 4) Que això el mogui a fer alguna cosa bona (Acció), i 5) Que revisi el procés (Avaluació).",
            "nivell_3": "El PPI és una resposta a la fragmentació del saber. En un món d'informació líquida, el PPI ensenya a 'aprendre a aprendre' i a integrar el coneixement amb els valors. La 'Reflexió' ignasiana no és només lògica, és ètica i existencial. El PPI converteix l'aula en un espai de creixement integral, no només d'instrucció."
        },
        1995: {
            "titol": "CG 34: Diàleg i Cultura",
            "nivell_1": "La CG 34 amplia la missió. Ja no és només Fe i Justícia. S'hi afegeix el Diàleg amb la Cultura i el Diàleg Interreligiós. L'escola ha de ser un lloc de frontera on l'Església es troba amb el món modern sense por.",
            "nivell_2": "Es reconeix que vivim en societats pluralistes i secularitzades. L'escola jesuïta no pot ser un gueto catòlic tancat. Ha d'acollir la diversitat i establir ponts. Es promou una cultura de l'acollida on cristians, creients d'altres religions i no creients treballen junts per valors comuns.",
            "nivell_3": "El concepte clau és 'servidors de la missió de Crist'. La CG 34 valida plenament la col·laboració amb els laics, que passen de ser 'col·laboradors dels jesuïtes' a ser 'companys en la missió'. Això empodera els equips directius laics i transforma la governança de les institucions."
        },
        2012: {
            "titol": "Col·loqui Boston: Consciència de Xarxa",
            "nivell_1": "Per primera vegada a la història, 400 líders educatius de tot el món es reuneixen físicament a Boston. Es pren consciència real que som una xarxa global amb un potencial immens si treballem junts.",
            "nivell_2": "Fins al 2012, les xarxes eren regionals. Boston trenca fronteres. El P. General Nicolás llança el repte: 'La globalització de la superficialitat és el nostre enemic. Hem d'educar per a la profunditat i la universalitat'. Es veu que els reptes (ecologia, pobresa) són globals i no es poden resoldre des de l'aïllament local.",
            "nivell_3": "Boston marca l'inici del 'Cicle de Col·loquis Globals' (ICJSE). S'inicia una nova era de projectes compartits, intercanvis d'alumnes i professors, i una consciència d'identitat supranacional. La xarxa deixa de ser un llistat d'adreces per ser un organisme viu."
        },
        2014: {
            "titol": "SIPEI Manresa: Les 4C",
            "nivell_1": "Al lloc fundacional de Manresa, un seminari internacional (SIPEI) defineix el perfil de l'alumne jesuïta del segle XXI amb quatre paraules clau: Conscient, Competent, Compassiu i Compromès.",
            "nivell_2": "Es buscava un llenguatge comú i fàcil de recordar. L'Excel·lència Humana es tradueix en aquestes 4C: Conscient (Amb vida interior i capaç de discernir), Competent (Professionalment preparat), Compassiu (Amb cor sensible al sofriment aliè), Compromès (Disposat a l'acció política i social transformadora).",
            "nivell_3": "Les 4C actualitzen l'ideal humanista de la 'Ratio'. Connecten la tradició espiritual (Conscient) amb l'exigència acadèmica (Competent) i la justícia (Compassiu/Compromès). Esdevenen l'estàndard per avaluar currículums i projectes innovadors: 'Aquest projecte ajuda a fer alumnes més compassius?'."
        },
        2015: {
            "titol": "Educate Magis: La Xarxa Digital",
            "nivell_1": "Es llança 'Educate Magis', una plataforma digital online per connectar tots els educadors jesuïtes del món. La xarxa es fa virtual i quotidiana, permetent compartir recursos i projectes a temps real.",
            "nivell_2": "Davant la impossibilitat de reunir-se físicament sovint, la tecnologia permet trencar l'aïllament. Educate Magis ofereix mapes globals, fòrums i recursos pedagògics. Permet que una classe a Kenya col·labori amb una a Irlanda. És l'encarnació digital de la missió universal.",
            "nivell_3": "Més enllà de l'eina tècnica, Educate Magis simbolitza la democratització de la xarxa. Qualsevol professor, no només els directius, pot connectar amb la comunitat global. Facilita la formació continuada i el sentiment de pertinença a un cos apostòlic que transcendeix les fronteres nacionals."
        },
        2017: {
            "titol": "JESEDU-Rio: Ciutadania Global",
            "nivell_1": "El Congrés Mundial de Rio de Janeiro marca una fita: les escoles jesuïtes es comprometen a educar per a la Ciutadania Global. No formem només ciutadans d'un país, sinó custodis del món.",
            "nivell_2": "A Rio, els delegats signen acords concrets. Es reconeix que els problemes actuals no tenen passaport. L'educació ha de fomentar una consciència planetària, el respecte per la diversitat i la responsabilitat ecològica. Es llança el concepte d''educar com un acte d'esperança'.",
            "nivell_3": "El document de Rio empeny les escoles a sortir de la zona de confort. La Ciutadania Global Ignasiana no és cosmopolitisme de viatges, sinó una mirada solidària que connecta el local amb el global. Exigeix revisar el currículum per incloure els Objectius de Desenvolupament Sostenible (ODS) llegits des de la fe."
        },
        2019: {
            "titol": "PAU i Tradició Viva: El Marc Actual",
            "nivell_1": "Es promulguen les 4 Preferències Apostòliques Universals (PAU) i el document 'Una Tradició Viva'. Aquests textos marquen l'estratègia de la Companyia fins al 2029.",
            "nivell_2": "El P. General Arturo Sosa, després d'un llarg discerniment, fixa les 4 PAU: 1) Mostrar el camí a Déu, 2) Caminar amb els exclosos, 3) Acompanyar els joves, 4) Cuidar la Casa Comuna. El document 'Una Tradició Viva' defineix 10 identificadors globals per a les escoles, assegurant que la innovació (necessària) no ens desviï de la missió.",
            "nivell_3": "Les PAU són un mandat de conversió. No són 'coses a fer', sinó 'maneres de ser'. Posen l'accent en l'espiritualitat com a motor de tot (1a PAU) i en l'ecologia integral (4a PAU) com a nou imperatiu. 'Una Tradició Viva' valida la 'fidelitat creativa': cal canviar molt per continuar sent els mateixos."
        },
        2021: {
            "titol": "JESEDU-Global: Profunditat i Reconciliació",
            "nivell_1": "En plena pandèmia, el col·loqui virtual global posa el focus en 'Construir Ponts'. Davant d'un món polaritzat i ferit, l'escola jesuïta ha de ser un espai de reconciliació i profunditat.",
            "nivell_2": "La pandèmia va mostrar la fragilitat humana i la desigualtat digital. El col·loqui reafirma l'escola com a comunitat de cura. Es crida a educar contra la superficialitat de les 'fake news' i el populisme. La profunditat intel·lectual i espiritual esdevé una urgència democràtica.",
            "nivell_3": "Es treballa el concepte de 'fe que fa justícia i cerca la reconciliació'. La reconciliació té tres dimensions: amb Déu, amb els altres i amb la Creació. L'escola ha de sanar ferides. També es posa en valor el lideratge compartit i el dret universal a una educació de qualitat (advocacy)."
        },
        2024: {
            "titol": "JESEDU-Jogja: Fe i Tecnologia",
            "nivell_1": "El seminari a Yogyakarta (Indonèsia) afronta el diàleg interreligiós i el repte de la tecnologia (IA). Com mantenir l'humanisme i l'espiritualitat en un món dominat per l'algoritme?",
            "nivell_2": "En un context de minoria cristiana (Indonèsia), es valora l'educació com a diàleg de vida. S'aborda l'impacte de la Intel·ligència Artificial: l'educació jesuïta ha de formar persones capaces de guiar la tecnologia amb ètica, no de ser dominades per ella. Es reforça la identitat catòlica no com a imposició, sinó com a oferta de sentit en un món plural.",
            "nivell_3": "Jogja insisteix en la formació interior dels educadors. Davant la pressió tecnològica, l'únic valor afegit del docent és la seva humanitat i la seva capacitat d'acompanyar espiritualment. Es renova el compromís amb una educació que no només instrueix, sinó que ofereix 'saviesa' (sapientia) per viure amb sentit i esperança."
        }
    },
    
    # Placeholder per als altres fils per mantenir l'estructura.
    # En futures versions es poden afegir els textos detallats per a Espiritualitat i Innovació.
    "🔥 Espiritualitat (L'Ànima)": {1522: {"titol": "Manresa", "nivell_1": "Text pendent d'ampliació...", "nivell_2": "...", "nivell_3": "..."}},
    "💡 Innovació (Fidelitat Creativa)": {1548: {"titol": "Messina", "nivell_1": "Text pendent d'ampliació...", "nivell_2": "...", "nivell_3": "..."}}
}

# 3. DADES DE LES DINÀMIQUES (Mantenim les existents)
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

# Selector de Tema (Per defecte Història que és el complet)
tema = st.sidebar.selectbox("Fil Conductor", list(discursos_extensos.keys()))

temps = st.sidebar.select_slider("Durada disponible", options=["30 min", "1 hora", "2 hores", "Matí sencer"])
participants = st.sidebar.number_input("Nombre de participants", min_value=1, value=20)
idioma = st.sidebar.selectbox("Idioma de sortida", ["Català", "Castellano", "English"])

# Lògica de selecció automàtica de dinàmica
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
tab1, tab2, tab3 = st.tabs(["📖 El Relat Modular", "⏳ Timeline Visual", "🤝 La Dinàmica"])

with tab1:
    st.subheader(f"Narrativa: {tema}")
    st.info("Selecciona el nivell de profunditat desitjat per a la lectura o exposició:")
    
    # Selector de Nivell Sumatiu
    nivell_user = st.radio("Profunditat del contingut:", 
             ["1. L'Essència (Titulars)", "2. El Relat (Narrativa)", "3. El Magis (Aprofundiment Teològic)"],
             index=1, horizontal=True)

    st.markdown("---")
    
    # Bucle per mostrar els milestones
    dades_fil = discursos_extensos.get(tema, {})
    
    if not dades_fil or len(dades_fil) < 5:
        st.warning("Aquest fil encara està en construcció. Si us plau, selecciona 'Història i Evolució' per veure el contingut complet.")
    else:
        for any_fita, info in dades_fil.items():
            # Creem un expander per a cada fita per mantenir l'ordre visual
            with st.expander(f"{any_fita} - {info['titol']}", expanded=False):
                
                # SEMPRE mostrem el Nivell 1 com a introducció
                st.markdown(f"### 📌 {info['nivell_1']}")
                
                # Si l'usuari vol Nivell 2 o 3, afegim el text narratiu
                if "2" in nivell_user or "3" in nivell_user:
                    st.markdown(f"{info['nivell_2']}")
                    
                # Si l'usuari vol Nivell 3, afegim el Magis
                if "3" in nivell_user:
                    st.info(f"**🔍 Aprofundiment:** {info['nivell_3']}")

with tab2:
    st.subheader("Línia de Temps")
    st.write("Visualització ràpida de les fites clau.")
    col1, col2 = st.columns(2)
    
    # Mostrem les fites de manera simple
    for i, (any_fita, info) in enumerate(dades_fil.items()):
        with (col1 if i % 2 == 0 else col2):
            st.metric(label=str(any_fita), value=info['titol'])

with tab3:
    st.subheader(f"Activitat Proposada: {dinamica_triada['nom']}")
    st.warning(f"🎯 {dinamica_triada['desc']}")
    
    st.markdown("#### Passos a seguir:")
    for pas in dinamica_triada["passos"]:
        st.markdown(f"- {pas}")

# --- PEU DE PÀGINA ---
st.markdown("---")
st.caption("Generat amb IA (Lògica de Gemini) | Basat en els documents 'Una Tradició Viva'.")
