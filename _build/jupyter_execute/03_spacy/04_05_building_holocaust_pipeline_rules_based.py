#!/usr/bin/env python
# coding: utf-8

# # <center>Creating Rules-Based Pipeline for Holocaust Documents</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2021</center>

# ## Key Concepts in this Notebook

# 1) How to add pipes to a spaCy model<br>
# 2) How to Consider Rules<br>
# 3) How to Implement those Rules<br>

# ## Introduction

# In this notebook, we will walk through some of the heuristic pipes I developed or am developing for my Holocaust NER spaCy pipeline. The purpose of these heuristic pipes is not to catch all potential entities, but to return with a high degree of confidence only true positives. We accept that the heuristics won't catch everything because the final item in this long pipeline is a machine learning NER model that will generalize, or make predictions, on the unseen data. By structuring many heuristics in the pipeline, we can radically reduce the chances of our ML model making a wrong prediction because the all known true positives will have already been annotated.
# 
# I should also note that the code in my pipes is repetitious by design. As this is a textbook, it would be difficult for the reader to consistently look at the top of the notebook to identify the variable set 20 cells earlier. For this reason, I opt to recreate the variables later in the notebook. While this is bad practice, it allows the reader to understand better what is happening at any given moment in the notebook.

# ## Creating a Blank spaCy Model

# The first thing we need to do is import all of the different components from spaCy and other libraries that we will need. I will explain these as we go forward.

# In[1]:


import spacy
from spacy.util import filter_spans
from spacy.tokens import Span
from spacy.language import Language
import re
import pandas as pd


# We will be using Pandas in this notebook to run data checks in a CSV file originally produced by the <a href="https://holocaustgeographies.org/">Holocaust Geographies Collaborative</a>, headed by Anne Knowles, Tim Cole, Alberto Giordano, Paul Jaskot, and Anika Walke. We will be importing RegEx because a lot of our heuristics will rely on capturing multi-word tokens.
# 
# Now that we have imported everything, let's create a blank English pipeline in spaCy. As we work through this notebook, we will add pipes to it.

# In[2]:


nlp = spacy.load("en_core_web_trf")


# ## Add Pipe for Finding Streets

# In[ ]:


streets_pattern = r"([A-Z][a-z]*(strasse|straße|straat)\b|([A-Z][a-z]* (Street|St|Boulevard|Blvd|Avenue|Ave|Road|Rd|Lane|Ln|Place|Pl)(\.)*))"
@Language.component("find_streets")
def find_streets(doc):
    text = doc.text
    camp_ents = []
    original_ents = list(doc.ents)
    for match in re.finditer(streets_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
            camp_ents.append((span.start, span.end, span.text))
    for ent in camp_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="STREET")
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)
nlp.add_pipe("find_streets", before="ner")


# ## Creating a Pipe for Finding Ships

# The very first pipe I want to create is a pipe that can find ships, specifically transport ships. In order to achieve this objective, this pipe does several things at once. First, it leverages RegEx to find known patterns that are always ships, e.g. multi-word tokens that may or may not begin with "S.S.", "SS", or "The", followed by a list of known ships. I have opted to not use a spaCy EntityRuler here primarily because I want to expand this pipe in the future and it allows me to find matches that are more varied. Were I to implement this in an EntityRuler pipe, I would need to have many patterns sit in its knowledge-base.
# 
# But finding one of these patterns isn't enough. I want to ensure that the thing referenced is in fact a ship. Many of these terms could easily be toponyms, or entities that share the same spelling but mean different things in different contexts, e.g. the Ile de France, could easily be a GPE that refers to the area around Paris. General Hosey could easily be a PERSON. To ensure toponym disambiguation, I set up several contextual clues, e.g. the list of nautical terms. If any of these words appear in area around the hit, then the heuristics assign that token the label of SHIP. If not, it ignores it and allows later pipes or the machine learning model to annotate it.

# In[ ]:


ships_pattern = r"((S.S. |SS |The )*(Lieutenant Colonel James Barker|General Hosey|Pan Crescent|Marilyn Marlene|Winnipeg|Ile de France|Scythia|Aquitania|Empress of Britain|General A. W. Greely|General J. H. McRae|Empress of Scotland|General T. H. Bliss|New Amsterdam|Niagara|Henry Gibbs|Serpa Pinto|Mauretania|Cabo de Hornos|Julius Caesar|Ben Hecht|Sțrumah|Strumah|General Harry Taylor|General W.P. Richardson|Marine Jumper|Simon Bolivar|Pan York|Mauretania|Orduña|Wilhelm Gustloff|Orduna|General W.H. Gordon|Rakuyō Maru|Rakuyo Maru|Mouzinho|Saturnia|St. Louis|Saint Louis|Nyassa|Simon Bolivar|Queen Elizabeth|Exodus 1947|Dunera|Cap Arcona|Ernie Pyle|Hayim Arlozorov|Patria))"
@Language.component("find_ships")
def find_ships(doc):
    text = doc.text
    new_ents = []
    original_ents = list(doc.ents)
    nautical = ["ship", "boat", "sail", "captain", "sea", "harbor", "aboard", "admiral", "liner"]
    for match in re.finditer(ships_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        context = text[start-100:end+100]
        if any(term in context.lower() for term in nautical):
            if span is not None:
                new_ents.append((span.start, span.end, span.text))
            else:
                span = doc.char_span(start, end-1)
                if span is not None:
                    new_ents.append((span.start, span.end-1, span.text))
    for ent in new_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="SHIP")
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)
nlp.add_pipe("find_ships", before="ner")


# Let's take a look and load in some data to see how this pipe functions. Remember, our goal is not to capture all ships, just ensure the ones we captured are true positives.

# In[ ]:


# import glob
# hits = []
# files = glob.glob("data/new_ocr/*trs_en.txt")
# all_data = {}
# for file in files[:30]:
#     all_hits = []
#     with open (file, "r", encoding="utf-8") as f:
#         print (file)
#         text = f.read()
#         doc = nlp(text)
#         for ent in doc.ents:
#             if ent.label_ == "SHIP":
#                 print (ent.text, ent.label_)
#                 print (text[ent.start_char-100:ent.end_char+100])
#                 print ()


# Success! File, data/new_ocr\RG-50.030.0006_trs_en.txt, referenced two ships, the Cap Arcona and the St. Louis. Now that we know we can capture ships in this manner, let's try out the same principle on ghettos.

# ## Creating a Pipe for Finding Ghettos

# As of the time of pushing this notebook, August 13, 2021, I have yet to receive a comprehensive dataset of ghettos. In the near future, this pipe will be vastly improved, similar to the concentration camp pipe below. For now, this pipe functions precisely the same way our earlier ship pipe function. Here, we're looking for the use of the word ghetto around one of these known cities that had ghettos. This is absolutely necessary because any of these cities could be a GPE in general. The use of the word ghetto within a small contextual window is a good heuristic for assigning this city the label of GHETTO over GPE.

# In[ ]:


ghetto_pattern = r"(Anykščiai|Anyksciai|Arad|Ashmiany|Babruĭsk|Babruisk|Balassagyarmat|Baranavichy|Barysaŭ|Barysau|Będzin|Bedzin|Bełżyce|Belzyce|Berdychiv|Berehove|Berestechko|Berezdiv|Berezhany|Berezne|Bershad'|Biała Podlaska|Biala Podlaska|Birkenau|Biała Rawska|Białystok|Bialystok|Biaroza|Bibrka|Bielsko-Biała|Biržai|Bitola|Blazhiv|Bobowa|Bochnia|Bolekhiv|Borshchuv|Boryslav|Boskovice|Brańsk|Bratslav|Brody|Brzesko|Buczacz|Budapest|Bus'k|Bychawa|Chashniki|Chrzanów|Chrzanow|Ciechanów|Ciechanow|Cieszanów|Cristuru Secuiesc|Czernowitz|Częstochowa|Czortków|Dąbrowa Górnicza|Dąbrowa Tarnowska|Damashėvichy|Daugavpils|Dokshytsy|Dombóvár|Dombrowa|Drohobycz|Drzewica|Dubrovytsia|Dzialoszyce|Dziarechyn|Dziatlava|Glebokie|Gol'shany|Góra Kalwaria|Gorodnaia|Gostynin|Gyöngyös|Hajdúszoboszló|Halushchyntsi|Halych|Hantsavichy|Haradnaia|Hatvan|Hlusk|Hlyniany|Homel'|Horodenka|Horokhiv|Hradzianka|Hrodna|Hvizdets'|Iaktoriv|Izbica Lubelska|Józefów|Kalisz|Kałuszyn|Kam'iane Pole|Kamin'-Kashyrs'kyĭ|Katowice|Kecskemét|Kelme|Kharkiv|Khmel'nyts'ka oblast'|Khmel'nyts'kyĭ|Khust|Kielce|Kisvárda|Kletsk|Kobryn|Kolbuszowa|Kolozsvár|Komarów-Osada|Kopychyntsi|Korets'|Košice|Kőszeg|Kovel'|Kozienice|Kraków|Kraśnik|Kretinga|Krośniewice|Krymne|Kryzhopil'|Kul'chyny|Kunhegyes|Kutno|Kysylyn|Ladyzhyn|Lakhva|Lask|Lęczyca|Lesko|Lida|Liepāja|Lipinki|Lithakia|Litin|Litzmannstadt|Liubavichi|Łomża|Lubaczów|Lubartów|Lublin|Łuck|Lwów|Lyubcha|Mahiliou|Maków Mazowiecki|Marcinkonys|Matejovce nad Hornádom|Mátészalka|Miechów|Międzyrzec Podlaski|Minsk|Mir|Miskolc|Modliborzyce|Mogilev|Monastyrok|Monor|Munkács|Nadvirna|Nagyvárad|Navahrudak|Novomyrhorod|Nowy Sącz|Nyíregyháza|Odessa|Oleyëvo-Korolëvka|Opatów|Opoczno|Opole|Opole Lubelskie|Orla|Orsha|Ostroh|Ostrowiec Świętokrzyski|Otwock|Ozarintsy|Ozorków|Pabianice|Papul|Parichi|Pechera|Pinsk|Piotrków Trybunalski|Płaszów|Płock|Plońsk|Praszka|Prienai|Prużana|Pruzhany|Przemyśl|Pułtusk|Radom|Radomyśl Wielki|Radun'|Rava-Rus'ka|Rawa Mazowiecka|Reghin|Ribnița|Riga|Rohatyn|Romanove Selo|Rozhyshche|Rudky|Rudnik nad Sanem|Rzeszów|Saharna|Šahy|Salgótarján|Sarny|Sátoraljaújhely|Schwientochlowitz|Senkevychivka|Sernyky|Sharhorod|Shchyrets'|Shepetivka|Shpola|Shumilino|Šiauliai|Siedlce|Siedliszcze|Sieradz|Sighetu Marmației|Skalat|Slobodka|Slonim|Slutsk|Smolensk|Sokołów Podlaski|Sokyrnytsia|Solotvyno|Soroca|Sosnowiec|Stalovichy|Stanislav|Stara Mohylʹnytsia|Starachowice|Starokostiantyniv|Stary Sącz|Stepan'|Stoczek Lukowski|Stolbëisy|Stolin|Sucha|Suchowola|Surazh|Švenčionys|Szarvas|Szczebrzeszyn|Szeged|Szolnok|Tarnogród|Tarnów|Telšiai|Terebovlia|Ternopol|Theresienstadt|Thessalonike|Timkovichi|Tlumach|Tolna|Tomaszów Mazowiecki|Torchyn|Trakai|Trebíč|Trnava|Tul'chyn|Tuliszków|Tyvriv|Uzda|Uzhhorod|Vác|Valozhyn|Velizh|Velykyĭ Bereznyĭ|Vilna|Vinnytsia|Vlonia|Volodymyr-Volyns'kyi|Vysokovskiy Rayon|Warka|Warsaw|Wisznice|Wrocław|Žagarė|Zamość|Zarichne|Zboriv|Zduńska Wola|Zhmerinka|Zhytomyr|Žiežmariai|Anyksciai|Arad|Ashmiany|Babruisk|Balassagyarmat|Baranavichy|Barysau|Bedzin|Bełzyce|Berdychiv|Berehove|Berestechko|Berezdiv|Berezhany|Berezne|Bershad'|Biała Podlaska|Biała Rawska|Białystok|Biaroza|Bibrka|Bielsko-Biała|Birzai|Bitola|Blazhiv|Bobowa|Bochnia|Bolekhiv|Borshchuv|Boryslav|Boskovice|Bransk|Bratslav|Brody|Brzesko|Buczacz|Budapest|Bus'k|Bychawa|Chashniki|Chrzanow|Ciechanow|Cieszanow|Cristuru Secuiesc|Czernowitz|Czestochowa|Czortkow|Dabrowa Gornicza|Dabrowa Tarnowska|Damashevichy|Daugavpils|Dokshytsy|Dombovar|Dombrowa|Drohobycz|Drzewica|Dubrovytsia|Dzialoszyce|Dziarechyn|Dziatlava|Glebokie|Gol'shany|Gora Kalwaria|Gorodnaia|Gostynin|Gyongyos|Hajduszoboszlo|Halushchyntsi|Halych|Hantsavichy|Haradnaia|Hatvan|Hlusk|Hlyniany|Homel'|Horodenka|Horokhiv|Hradzianka|Hrodna|Hvizdets'|Iaktoriv|Izbica Lubelska|Jozefow|Kalisz|Kałuszyn|Kam'iane Pole|Kamin'-Kashyrs'kyi|Katowice|Kecskemet|Kelme|Kharkiv|Khmel'nyts'ka oblast'|Khmel'nyts'kyi|Khust|Kielce|Kisvarda|Kletsk|Kobryn|Kolbuszowa|Kolozsvar|Komarow-Osada|Kopychyntsi|Korets'|Kosice|Koszeg|Kovel'|Kozienice|Krakow|Krasnik|Kretinga|Krosniewice|Krymne|Kryzhopil'|Kul'chyny|Kunhegyes|Kutno|Kysylyn|Ladyzhyn|Lakhva|Lask|Leczyca|Lesko|Lida|Liepaja|Lipinki|Lithakia|Litin|Litzmannstadt|Liubavichi|Łomza|Lubaczow|Lubartow|Lublin|Łuck|Lwow|Lyubcha|Mahiliou|Makow Mazowiecki|Marcinkonys|Matejovce nad Hornadom|Mateszalka|Miechow|Miedzyrzec Podlaski|Minsk|Mir|Miskolc|Modliborzyce|Mogilev|Monastyrok|Monor|Munkacs|Nadvirna|Nagyvarad|Navahrudak|Novomyrhorod|Nowy Sacz|Nyiregyhaza|Odessa|Oleyevo-Korolevka|Opatow|Opoczno|Opole|Opole Lubelskie|Orla|Orsha|Ostroh|Ostrowiec Swietokrzyski|Otwock|Ozarintsy|Ozorkow|Pabianice|Papul|Parichi|Pechera|Pinsk|Piotrkow Trybunalski|Płaszow|Płock|Plonsk|Praszka|Prienai|Pruzana|Pruzhany|Przemysl|Pułtusk|Radom|Radomysl Wielki|Radun'|Rava-Rus'ka|Rawa Mazowiecka|Reghin|Ribnita|Riga|Rohatyn|Romanove Selo|Rozhyshche|Rudky|Rudnik nad Sanem|Rzeszow|Saharna|Sahy|Salgotarjan|Sarny|Satoraljaujhely|Senkevychivka|Sernyky|Sharhorod|Shchyrets'|Shepetivka|Shpola|Shumilino|Siauliai|Siedlce|Siedliszcze|Sieradz|Sighetu Marmatiei|Skalat|Slobodka|Slonim|Slutsk|Smolensk|Sokołow Podlaski|Sokyrnytsia|Solotvyno|Soroca|Sosnowiec|Stalovichy|Stanislav|Stara Mohylʹnytsia|Starachowice|Starokostiantyniv|Stary Sacz|Stepan'|Stoczek Lukowski|Stolbeisy|Stolin|Sucha|Suchowola|Surazh|Svencionys|Szarvas|Szczebrzeszyn|Szeged|Szolnok|Tarnogrod|Tarnow|Telsiai|Terebovlia|Ternopol|Theresienstadt|Thessalonike|Timkovichi|Tlumach|Tolna|Tomaszow Mazowiecki|Torchyn|Trakai|Trebic|Trnava|Tul'chyn|Tuliszkow|Tyvriv|Uzda|Uzhhorod|Vac|Valozhyn|Velizh|Velykyi Bereznyi|Vilna|Vinnytsia|Vlonia|Volodymyr-Volyns'kyi|Vysokovskiy Rayon|Warka|Warsaw|Wisznice|Wrocław|Zagare|Zamosc|Zarichne|Zboriv|Zdunska Wola|Zhmerinka|Zhytomyr|Ziezmariai)"
@Language.component("find_ghettos")
def find_ghettos(doc):
    text = doc.text
    ghetto_ents = []
    gpe_ents = []
    original_ents = list(doc.ents)
    for match in re.finditer(ghetto_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        context = text[start-25:end+25]
        if "ghetto" in context.lower():
            if span is not None:
                ghetto_ents.append((span.start, span.end, span.text))
                
        else:
            if span is not None:
                gpe_ents.append((span.start, span.end, span.text))
    for ent in ghetto_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="GHETTO")
        original_ents.append(per_ent)
    for ent in gpe_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="GPE")
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)
nlp.add_pipe("find_ghettos", before="ner")


# In[ ]:


second_ghettos_pattern = r"[A-Z]\w+((-| )*[A-Z]\w+)* (g|G)hetto"
@Language.component("find_ghettos2")
def find_ghettos2(doc):
    fps = ["That", "The"]
    text = doc.text
    camp_ents = []
    original_ents = list(doc.ents)
    for match in re.finditer(second_ghettos_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end-7)
        if span is not None and span.text not in fps:
            if "The " in span.text:
                camp_ents.append((span.start+1, span.end, span.text))
            else:
                camp_ents.append((span.start, span.end, span.text))
    for ent in camp_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="GHETTO")
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)
nlp.add_pipe("find_ghettos2", before="ner")


# In[ ]:


# import glob
# hits = []
# files = glob.glob("data/new_ocr/*trs_en.txt")
# all_data = {}
# for file in files[:5]:
#     all_hits = []
#     with open (file, "r", encoding="utf-8") as f:
#         print (file)
#         text = f.read()
#         doc = nlp(text)
#         for ent in doc.ents:
#             if ent.label_ == "GHETTO":
#                 print (ent.text, ent.label_)
#                 print (text[ent.start_char-100:ent.end_char+100])
#                 print ()


# As we can see, the pipe is working. We've grabbed three instances of Warsaw in data/new_ocr\RG-50.030.0001_trs_en.txt.

# ## Create Pipe for Identifying a Person

# For PERSON, we will be leveraging spaCy's small model, but we can add some heuristics that will greatly improve the results. The heuristics here is any known salutation capitalized followed by a series of proper nouns. This RegEx "(?:[A-Z]\w+[ -]?)+)" allows us to grab all continuous capital words and then break when it encounters a non capital letter followed by a space. In English, these will always be PERSON entities.

# In[ ]:


people_pattern = r"((((Mr|Mrs|Miss|Dr|Col|Adm|Lt|Cap|Cpt|Fr|Cl|Cln|Sgt)(\.)*)|(Frau|Herr|President|Rabbi|Queen|Prince|Princess|Pope|Father|Bishop|King|Cardinal|General|Liutenant|Colonel|Lieutenant Colonel|Private|Admiral|Captain|Sergeant|Sergeant First Class|Staff Sergeant|Sergeant Major|Corp Sergeant Major|Field Sergeant|Technical Sergeant|Corporal|Lance Corporal|Ensign|2nd Lieutenant|1st Lieutenant|Major|Hauptmann|Staff Captain|Oberst|Oberstlieutenant|Maj\. Geb\.|Capt\.|Sub Com\.)) (?:[A-Z]\w+[ -]?)+)(the [A-Z]\w*|I\w*|X\w*|v\w*)*"
@Language.component("find_people")
def find_people(doc):
    text = doc.text
    match_ents = []
    original_ents = list(doc.ents)
    for match in re.finditer(people_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
            match_ents.append((span.start, span.end, span.text))
                
        else:
            span = doc.char_span(start, end-1)
            if span is not None:
                match_ents.append((span.start, span.end, span.text))

    for ent in match_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="PERSON")
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)


# In[ ]:


nlp.add_pipe("find_people", before="ner")


# ## Create Pipe for Identifying Spouses

# Often times in historical documents the identity of people are referenced collectively. In some instances, such as those of spouses, this results in the name of the woman being attached to the name of her husband. The purpose of this SPOUSAL entity is to identify such constructs so that users can manipulate the output and reconstruct each individual singularly.

# In[ ]:


spousal_pattern = r"((Mr|Mrs|Miss|Dr)(\.)* and (Mr|Mrs|Miss|Dr)(\.)* (?:[A-Z]\w+[ -]?)+)"
@Language.component("find_spousal")
def find_spousal(doc):
    text = doc.text
    new_ents = []
    original_ents = list(doc.ents)
    for match in re.finditer(spousal_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
            new_ents.append((span.start, span.end, span.text))
        else:
            span = doc.char_span(start, end-1)
            if span is not None:
                new_ents.append((span.start, span.end-1, span.text))
    for ent in new_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="SPOUSAL")
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)


# In[ ]:


nlp.add_pipe("find_spousal", before="ner")


# ## Creating Concentration Camp Pipe

# The correct identification of camp is one of the most important pipes in this pipeline. There are two concentration camp pipes. The first pipe looks at all known camps and subcamps and then looks for surrounding words to identify the context. The second pipe is less strict. It looks for all known main concentration camps without context. The reason for this is because sometimes the subcamps have the same names as frequently cited cities, e.g. Berlin or Neustadt. This is particularly true of the subcamps. The main camps, however, are frequently referenced to the camp itself. Both pipes are activated by default, but a user can deactivate one or other.
# 
# Throughout this pipe, you will see many functions that contain the name "getter". These are custom functions that allow us to add special attributes to our entity spans. If you scroll down to the bottom of this section, you will see that we can use the HGC dataset for conentration camps to retrieve other salient information, such as the subcamp's main camp, its longitude and latitude, opening date, closing date, etc.

# In[ ]:


def subcamp_getter(hit):
    hit = hit.text
    df = pd.read_csv("data/hgc_data.csv")
    subcamps = df.Main.tolist()
    camps = df.SubcampMattingly.tolist()
    i=0
    potential = []
    for c in camps:
        
        try:
            all_c = c.split("^")
            for c in all_c:
                c = c.replace("\(", "(").replace("\)", ")")
#                 if c == "Buna-Monowitz (Auschwitz III)":
#                     print (c)
                if hit.strip() == c.strip():
#                     print (hit, c)
                    if subcamps[i] not in potential:
                        potential.append(subcamps[i])
        except:
            AttributeError
        i=i+1
    return (potential)


# In[ ]:


def date_open_getter(hit):
    hit = hit.text
    df = pd.read_csv("data/hgc_data.csv")
    dates = df.Date_Open.tolist()
    camps = df.SubcampMattingly.tolist()
    i=0
    potential = []
    for c in camps:
        
        try:
            all_c = c.split("^")
            for c in all_c:
                if hit == c:
                    if dates[i] not in potential:
                        potential.append(dates[i])
        except:
            AttributeError
        i=i+1
    return (potential)


# In[ ]:


def date_closed_getter(hit):
    hit = hit.text
    df = pd.read_csv("data/hgc_data.csv")
    dates = df.Date_Close.tolist()
    camps = df.SubcampMattingly.tolist()
    i=0
    potential = []
    for c in camps:
        try:
            all_c = c.split("^")
            for c in all_c:
                if hit == c:
                    if dates[i] not in potential:
                        potential.append(dates[i])
        except:
            AttributeError
        i=i+1
    return (potential)


# In[ ]:


def latlong_getter(hit):
    hit = hit.text
    df = pd.read_csv("data/hgc_data.csv")
    lats = df.LAT.tolist()
    longs = df.LONG.tolist()
    camps = df.SubcampMattingly.tolist()
    i=0
    potential = []
    for c in camps:
        
        try:
            all_c = c.split("^")
            for c in all_c:
                if hit == c:
                    if lats[i] not in potential:
                        potential.append((lats[i], longs[i]))
        except:
            AttributeError
        i=i+1
    return (potential)


# In[ ]:





# In[ ]:


def hgc_id_getter(hit):
    hit = hit.text
    df = pd.read_csv("data/hgc_data.csv")
    ids = df.HGC_ID.tolist()
    camps = df.SubcampMattingly.tolist()
    i=0
    potential = []
    for c in camps:
        
        try:
            all_c = c.split("^")
            for c in all_c:
                if hit == c:
                    if ids[i] not in potential:
                        potential.append(ids[i])
        except:
            AttributeError
        i=i+1
    return (potential)


# In[ ]:


def camp_type_getter(hit):
    hit = hit.text


# In[ ]:


df = pd.read_csv("data/hgc_data.csv")
camps = df.SubcampMattingly.tolist()
subcamps = df.Main.tolist()
i=0
final_camps = []
for c in camps:
    if c != "nan" and c != "FALSE":
        if subcamps[i] != "nan" and subcamps[i] != "FALSE":
            try:
                if c.split()[0] != "":
                    c=c.replace("*", "")
                    for item in c.split("^"):
                        final_camps.append(item.replace("(", "\(").replace(")", "\)").strip())
            except:
                AttributeError
    i=i+1
    
final_camps.sort(key=len, reverse=True)
final_list = "|".join(final_camps)
strict_camps_pattern = r"("+final_list+")"
# print (strict_camps_pattern)
@Language.component("find_camps_strict")
def find_camps_strict(doc):
    text = doc.text
    camp_ents = []
    original_ents = list(doc.ents)
    context_terms = ["camp", "concentration", "labor", "forced", "gas", "chamber"]
    for match in re.finditer(strict_camps_pattern, doc.text):
#         print (match)
        start, end = match.span()
        span = doc.char_span(start, end)
        context = text[start-100:end+100]
        if any(term in context.lower() for term in context_terms):
            if span is not None:
#                 print (span)
                camp_ents.append((span.start, span.end, span.text))
    for ent in camp_ents:
#         print (ent)
        start, end, name = ent
#         per_ent = Span(doc, start, end, label="CAMP")
#         per_ent.set_extension("subcamp", getter=subcamp_getter, force=True)
#         per_ent.set_extension("date_open", getter=date_open_getter, force=True)
#         per_ent.set_extension("date_closed", getter=date_closed_getter, force=True)
#         per_ent.set_extension("latlong", getter=latlong_getter, force=True)
#         per_ent.set_extension("hgc_id", getter=hgc_id_getter, force=True)
        
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)


# In[ ]:


camps_pattern = r"(Alderney|Amersfoort|Auschwitz|Banjica|Belzec|Bergen-Belsen|Bernburg|Bogdanovka|Bolzano|Bor|Breendonk|Breitenau|Buchenwald|Chelmno|Dachau|Drancy|Falstad|Flossenburg|Fort VII|Fossoli|Grini|Gross-Rosen|Herzogenbusch|Hinzert|Janowska|Jasenovac|Kaiserwald|Kaunas|Kemna|Klooga|Le Vernet|Majdanek|Malchow|Maly Trostenets|Mechelen|Mittelbau-Dora|Natzweiler-Struthof|Neuengamme|Niederhagen|Oberer Kuhberg|Oranienburg|Osthofen|Plaszow|Ravensbruck|Risiera di San Sabba|Sachsenhausen|Sajmište|Salaspils|Sobibor|Soldau|Stutthof|Theresienstadt|Trawniki|Treblinka|Vaivara)(-[A-Z]\S+)*"
@Language.component("find_camps")
def find_camps(doc):
    text = doc.text
    camp_ents = []
    original_ents = list(doc.ents)
    for match in re.finditer(camps_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
            camp_ents.append((span.start, span.end, span.text))
    for ent in camp_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="CAMP")
        per_ent.set_extension("subcamp", getter=subcamp_getter, force=True)
        per_ent.set_extension("date_open", getter=date_open_getter, force=True)
        per_ent.set_extension("date_closed", getter=date_closed_getter, force=True)
        per_ent.set_extension("latlong", getter=latlong_getter, force=True)
        per_ent.set_extension("hgc_id", getter=hgc_id_getter, force=True)
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)


# In[ ]:


second_camps_pattern = r"[A-Z]\w+((-| )*[A-Z]\w+)* (c|C)oncentration (c|C)amp"
@Language.component("find_camps2")
def find_camps2(doc):
    text = doc.text
    camp_ents = []
    original_ents = list(doc.ents)
    for match in re.finditer(second_camps_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end-19)
        if span is not None:
            camp_ents.append((span.start, span.end, span.text))
    for ent in camp_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="CAMP")
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)


# In[ ]:


nlp.add_pipe("find_camps_strict", before="ner")
nlp.add_pipe("find_camps", before="ner")
nlp.add_pipe("find_camps2", before="ner")


# In[ ]:


# import glob
# hits = []
# files = glob.glob("data/new_ocr/*trs_en.txt")
# all_data = {}
# for file in files[1:2]:
#     all_hits = []
#     with open (file, "r", encoding="utf-8") as f:
#         print (file)
#         text = f.read()
#         doc = nlp(text)
#         for ent in doc.ents:
#             if ent.label_ == "CAMP":
#                 print ((ent.text, ent.label_, ent._.subcamp, ent._.date_open, ent._.date_closed, ent._.latlong, ent._.hgc_id))
#                 print (text[ent.start_char-100:ent.end_char+100])
#                 print ()


# ## Creating Revolutionary Groups Pipe

# The purpose of this pipe is to find known Revolutionary Groups. Again, this pipe is not an EntityRuler because I intend to do a few extra things with it in the future beyond the limitations of the EntityRuler.

# In[ ]:


groups_pattern = r"(Ethnikon Apeleutherotikon Metopon|Weisse Rose|Rote Kapelle|Affiche rouge|Edelweisspiraten|White Rose|Bielski|Nekamah|Voroshilov|OEuvre de secours aux enfants|Union des juifs pour la résistance et l'entraide|Zorin Unit|Komsomolski|Fareynikte|Korzh|Zhukov|Budenny|Parkhomenko|Sixième)((-)*[A-Z]\S+)*( (Brigade|brothers|group))*"
@Language.component("find_groups")
def find_groups(doc):
    text = doc.text
    camp_ents = []
    original_ents = list(doc.ents)
    for match in re.finditer(groups_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
            camp_ents.append((span.start, span.end, span.text))
    for ent in camp_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="GROUP")
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)


# In[ ]:


nlp.add_pipe("find_groups", before="ner")


# ## Creating a Places Pipe

# The ML model will capture place fairly well. Nevertheless, if you can write a simple rule, write a simple rule.

# In[ ]:


city_pattern = r"(?:[A-Z]\w+[ -]?)+, (Germany|Poland|England|Russia|Italy|USA|U.S.A.|United States|United States of America|America|United Kingdom|France|Spain|Ukraine|Romania|Netherlands|Belgium|Greece|Portugal|Sweden|Hungary|Austria|Belarus|Serbia|Switzerland|Bulgaria|Denmark|Finland|Slovakia|Norway|Ireland|Croatia|Moldova|Bosnia|Albania|Estonia|Malta|Iceland|Andorra|Luxembourg|Montenegro|Macedonia|San Marino|Lichtenstein|Monaco)"
country_pattern = r"(Germany|Poland|England|Russia|Italy|USA|U.S.A.|United States|United States of America|America|United Kingdom|France|Spain|Ukraine|Romania|Netherlands|Belgium|Greece|Portugal|Sweden|Hungary|Austria|Belarus|Serbia|Switzerland|Bulgaria|Denmark|Finland|Slovakia|Norway|Ireland|Croatia|Moldova|Bosnia|Albania|Estonia|Malta|Iceland|Andorra|Luxembourg|Montenegro|Macedonia|San Marino|Lichtenstein|Monaco)"
@Language.component("find_places")
def find_places(doc):
    text = doc.text
    new_ents = []
    original_ents = list(doc.ents)
    for match in re.finditer(city_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
            new_ents.append((span.start, span.end, span.text))
        else:
            span = doc.char_span(start, end-1)
            if span is not None:
                new_ents.append((span.start, span.end-1, span.text))
    for ent in new_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="GPE")
        if per_ent.text.split(",")[0] not in city_pattern:
            original_ents.append(per_ent)
            
    for match in re.finditer(country_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
            new_ents.append((span.start, span.end, span.text))
        else:
            span = doc.char_span(start, end-1)
            if span is not None:
                new_ents.append((span.start, span.end-1, span.text))
    for ent in new_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="GPE")
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)


# In[ ]:


nlp.add_pipe("find_places", before="ner")


# ## Creating a Geography Pipe

# In[ ]:


general_pattern = r"([A-Z]\w+) (River|Mountain|Mountains|Forest|Forests|Sea|Ocean)*"
river_pattern = "(the|The) (Rhone|Volga|Danube|Ural|Dnieper|Don|Pechora|Kama|Oka|Belaya|Dniester|Rhine|Desna|Elbe|Donets|Vistula|Tagus|Daugava|Loire|Tisza|Ebro|Prut|Neman|Sava|Meuse|Kuban River|Douro|Mezen|Oder|Guadiana|Rhône|Kuma|Warta|Seine|Mureș|Northern Dvina|Vychegda|Drava|Po|Guadalquivir|Bolshoy Uzen|Siret|Maly Uzen|Terek|Olt|Vashka|Glomma|Garonne|Usa|Kemijoki|Great Morava|Moselle|Main 525|Torne|Dalälven|Inn|Maritsa|Marne|Neris|Júcar|Dordogne|Saône|Ume|Mur|Ångerman|Klarälven|Lule|Gauja|Weser|Kalix|Vindel River|Ljusnan|Indalsälven|Vltava|Ponoy|Ialomița|Onega|Somes|Struma|Adige|Skellefte|Tiber|Vah|Pite|Faxälven|Vardar|Shannon|Charente|Iskar|Tundzha|Ems|Tana|Scheldt|Timiș|Genil|Severn|Morava|Luga|Argeș|Ljungan|Minho|Venta|Thames|Drina|Jiu|Drin|Segura|Torne|Osam|Arda|Yantra|Kamchiya|Mesta)"
@Language.component("find_geography")
def find_geography(doc):
    text = doc.text
    river_ents = []
    general_ents = []
    original_ents = list(doc.ents)
    for match in re.finditer(river_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
            river_ents.append((span.start, span.end, span.text))
    for match in re.finditer(general_pattern, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end)
        if span is not None:
            general_ents.append((span.start, span.end, span.text))       
            
#     all_ents = river_ents+general_ents       
    for ent in river_ents:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="RIVER")
        original_ents.append(per_ent)
        
    for ent in general_ents:
        start, end, name = ent
        if "River" in name:
            per_ent = Span(doc, start, end, label="RIVER")
        elif "Mountain" in name:
            per_ent = Span(doc, start, end, label="MOUNTAIN")
        elif "Sea" in name:
            per_ent = Span(doc, start, end, label="SEA-OCEAN")
        elif "Forest" in name:
            per_ent = Span(doc, start, end, label="FOREST")
        original_ents.append(per_ent)
    filtered = filter_spans(original_ents)
    doc.ents = filtered
    return (doc)
nlp.add_pipe("find_geography", before="ner")


# ## Adding Streets

# In[ ]:





# ## Seeing the Pipes at Work

# Now that we have assembled all these pipes into a pipeline, let's see how they perform on a real testimony.

# In[ ]:


# import glob
# from spacy import displacy
# hits = []
# files = glob.glob("data/new_ocr/*trs_en.txt")
# all_data = {}
# for file in files[5:6]:
#     all_hits = []
#     with open (file, "r", encoding="utf-8") as f:
#         print (file)
#         text = f.read().replace("(ph)", "")
#         while "  " in text:
#             text =  text.replace("  ", " ")
#         doc = nlp(text)
#         colors = {"CAMP": "#FF5733", "GHETTO": "#1F9D12", "SHIP": "#557DB4", "SPOUSAL": "#55B489", "GPE":"#17B4C2", "RIVER": "#9017C2", "MOUNTAIN": "#878787", "SEA-OCEAN": "#0A6DF5", "FOREST": "#1F541D"}
#         options = {"ents": ["CAMP", "GHETTO", "SHIP", "SPOUSAL", "GPE", "RIVER", "MOUNTAIN", "SEA-OCEAN", "FOREST"], "colors":colors}
#         displacy.render(doc, style="ent", jupyter=True)
doc = nlp("This is Berlinstrasse, which is also known as Berlin Street or Berlin St. That Ghetto and The Ghetto. The Warsaw Ghetto")
from spacy import displacy
displacy.render(doc, style="ent")


# This result is not perfect, but again, that's not the point here. Here we are less interested in catching all entities as much as not catching any false positives. At a quick glance, we have achieved that. Now that were are tentatively happy, wan save our pipeline to disk, but first, let's add some metadata.

# ## Saving a spaCy Model

# In[ ]:


nlp.meta["name"] = "ushmm"
nlp.meta["version"] = '0.1.2'
nlp.meta["author"] = "W.J.B. Mattingly"
nlp.meta["author_email"] = "wjbmattingly@gmail.com"
nlp.meta["description"] = "This is a pipeline of heuristics to help identify essential entities for research into the Holocaust."
nlp.meta['url'] = "www.wjbmattingly.com"
nlp.to_disk("models/rules_pipeline")


# If we are particularly happy with our results, we can even save the file to disk. It is important to note that we need to copy and paste all of our code into a python script that we can inject into the model. I'll cover this in greater detail in the next notebook as we start working on an ML model.

# In[ ]:


get_ipython().system('python -m spacy package models/rules_pipeline models --code data/components.py --force')


# In[ ]:





# In[ ]:




