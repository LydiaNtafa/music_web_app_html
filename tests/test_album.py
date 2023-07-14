from lib.album import Album

#test if the album class constructs the record correctly

def test_album_class():
    album_1 = Album(1, 'Doolittle', 1989, 1)
    assert album_1.id == 1
    assert album_1.title == "Doolittle"
    assert album_1.release_year == 1989
    assert album_1.artist_id ==1