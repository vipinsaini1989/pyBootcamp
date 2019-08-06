movies_text = """
2018 The Equalizer 2 
Robert McCall
 2017 Roman J. Israel, Esq. 
Roman J. Israel, Esq.
 2016 Fences 
Troy Maxson
 2016 The Magnificent Seven 
Chisolm
 2014 The Equalizer 
Robert McCall
 2013 2 Guns 
Bobby
 2012/I Flight 
Whip Whitaker
 2012 Safe House 
Tobin Frost
 2010 Unstoppable 
Frank
 2010 The Book of Eli 
Eli
 2009 The Taking of Pelham 123 
Walter Garber
 2007 The Great Debaters 
Melvin B. Tolson
 2007 American Gangster 
Frank Lucas
 2006 Deja Vu 
Doug Carlin
 2006 Inside Man 
Detective Keith Frazier
 2004 The Manchurian Candidate 
Ben Marco
 2004 Man on Fire 
John W. Creasy
 2003/I Out of Time 
Matt Lee Whitlock
 2002 Antwone Fisher 
Dr. Jerome Davenport
 2002 John Q 
John Quincy Archibald
 2001 Training Day 
Alonzo
 2000 Remember the Titans 
Coach Herman Boone
 1999 The Hurricane 
Rubin Carter
 1999 The Bone Collector 
Lincoln Rhyme
 1998 The Siege 
Anthony Hubbard
 1998 He Got Game 
Jake Shuttlesworth
 1998 Fallen 
John Hobbes
"""


movie_text_splited = movies_text.split("\n")
cleaned_movie_list = []

for movie_line in movie_text_splited:
    if movie_line:
        cleaned_movie_list.append(movie_line.strip())
    else:
        pass

list_len = len(cleaned_movie_list)
movie_db = {}

for i in range(0, list_len, 2):
    year_and_name = cleaned_movie_list[i]
    character_name = cleaned_movie_list[i+1]

    year = year_and_name.split()[0]
    name_dic = year_and_name.split()[1:]
    movie_name = " ".join(name_dic)

    movie_dictionary = {
        "movie": movie_name,
        "character": character_name,
        "year": year
    }

    movie_db[movie_name] = movie_dictionary

print(movie_db)
