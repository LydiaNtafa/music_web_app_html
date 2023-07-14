from lib.album import Album

class AlbumRepository:
    def __init__(self,connections):
        self.connections = connections

    def all(self):
        albums = []
        rows = self.connections.execute("SELECT * FROM albums")
        for row in rows:
            album = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return albums
    
    def find(self, id):
        rows = self.connections.execute("SELECT * FROM albums WHERE id=%s", [id])
        album = Album(rows[0]["id"], rows[0]["title"], rows[0]["release_year"], rows[0]["artist_id"])
        return album
    
    def create(self, album):
        rows = self.connections.execute(
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s,%s) RETURNING id",[
                album.title, album.release_year, album.artist_id]
        )
        return rows[0]["id"]

    def delete(self, id):
        self.connections.execute(
            "DELETE FROM albums WHERE id = %s", [id]
        )
