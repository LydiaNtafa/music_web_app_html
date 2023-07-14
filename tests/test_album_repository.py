from lib.album_repository import AlbumRepository
from lib.album import Album

#testing the all function
def test_all_returns_a_list_of_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    albums = AlbumRepository(db_connection)
    assert albums.all() == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(3,'Waterloo', 1974, 2),
        Album(4,'Super Trouper', 1980, 2),
        Album(5,'Bossanova', 1990, 1),
        Album(6,'Lover', 2019, 3),
        Album(7,'Folklore', 2020, 3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978, 4),
        Album(10,'Here Comes the Sun', 1971, 4),
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973, 2)
    ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = repository.find(3)
    assert album == Album(3,'Waterloo', 1974, 2)


'''
When we call AlbumRepository#create
we get a new Album Object reflecting on the result of the #all
'''

def test_create_new_album_and_get_all(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "Title1", 1999, 1)
    assert repository.create(album) == None
    assert repository.all() == [
        Album(1,'Doolittle', 1989, 1),
        Album(2,'Surfer Rosa', 1988, 1),
        Album(3,'Waterloo', 1974, 2),
        Album(4,'Super Trouper', 1980, 2),
        Album(5,'Bossanova', 1990, 1),
        Album(6,'Lover', 2019, 3),
        Album(7,'Folklore', 2020, 3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978, 4),
        Album(10,'Here Comes the Sun', 1971, 4),
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973, 2),
        Album(13, "Title1", 1999, 1)
    ]
'''
When we call AlbumRepositry#DELETE
it should reflect on the result set of the ALL function
'''
def test_deleting_a_single_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    assert repository.delete(1) == None

    assert repository.all() == [
        Album(2,'Surfer Rosa', 1988, 1),
        Album(3,'Waterloo', 1974, 2),
        Album(4,'Super Trouper', 1980, 2),
        Album(5,'Bossanova', 1990, 1),
        Album(6,'Lover', 2019, 3),
        Album(7,'Folklore', 2020, 3),
        Album(8,'I Put a Spell on You', 1965, 4),
        Album(9,'Baltimore', 1978, 4),
        Album(10,'Here Comes the Sun', 1971, 4),
        Album(11,'Fodder on My Wings', 1982, 4),
        Album(12,'Ring Ring', 1973, 2)
    ]
