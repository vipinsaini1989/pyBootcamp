raw_data = """
Video
(HD - Movies)
Alita.Battle.Angel.2019.1080p.WEBRip.x264-MP4
Magnet linkThis torrent has 5 comments.Trusted Uploaded 06-29 08:46, Size 1.96 GiB, ULed by MrStark	7226	853
Video
(HD - Movies)
Hellboy.2019.1080p.WEBRip.x264-MP4
Magnet linkThis torrent has 1 comments.Trusted Uploaded 07-09 19:17, Size 1.95 GiB, ULed by MrStark	6439	996
Video
(HD - Movies)
Long.Shot.2019.720p.WEBRip.x264-MP4
Magnet linkTrusted Uploaded 07-16 17:27, Size 1.03 GiB, ULed by MrStark	3905	1003
Video
(HD - Movies)
Dumbo (2019) [BluRay] [1080p]
Magnet linkThis torrent has 2 comments.VIP Uploaded 06-14 23:19, Size 1.79 GiB, ULed by surferbroadband	4188	509
Video
(HD - Movies)
Alita.Battle.Angel.2019.720p.WEBRip.x264-MP4
Magnet linkThis torrent has 1 comments.Trusted Uploaded 06-29 08:45, Size 1.02 GiB, ULed by MrStark	3712	596
Video
(HD - Movies)
Long.Shot.2019.1080p.WEBRip.x264-MP4
Magnet linkTrusted Uploaded 07-16 17:28, Size 1.99 GiB, ULed by MrStark	2850	1175
"""

raw_data_splited = raw_data.strip().split('\n')

movie_db = []

for i in range(0, len(raw_data_splited), 4):
    movie_name = raw_data_splited[i+2]
    video_type = raw_data_splited[i+1].strip('()')

    long_text = raw_data_splited[i + 3]
    long_text_list = long_text.split(" ")

    size = long_text_list[-5] + " " + long_text_list[-4]
    seed_and_peer_list = long_text_list[-1].split("\t")
    seed = seed_and_peer_list[-2]
    peer = seed_and_peer_list[-1]
    upload_by = seed_and_peer_list[0]

    index_of_uploaded = raw_data_splited[i + 3].find('Uploaded')
    upload_date = long_text[index_of_uploaded:].split()[1]

    movie_list_dict = {
        'video': video_type,
        'movie': movie_name,
        'size': size,
        'seed': seed,
        'peer': peer,
        'upload_by': upload_by,
        'upload_date': upload_date
    }

    movie_db.append(movie_list_dict)

print("-"*110)
print(f"""
    Video           Size      Seed   Peer   Upload By   Uploade Date        Movie name
    """)
print("-"*110)

for movie_info in movie_db:

    print(f"""
    {movie_info["video"]} | {movie_info["size"]} | {movie_info["seed"]} | {movie_info["peer"]} | {movie_info["upload_by"]} | {movie_info["upload_date"]} | {movie_info["movie"]}   
    """)
