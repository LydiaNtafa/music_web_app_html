import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.album import *
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods = ['POST'])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    if 'title' not in request.form:
        return "Need more information !", 400

    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']   
    album = Album(None, title,release_year, artist_id)
    repository.create(album)
    return ""

@app.route('/albums', methods = ['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    list_of_albums = repository.all()
    return render_template('get_albums.html', albums= list_of_albums)

@app.route('/albums/<id>')
def get_one_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = [repository.find(id)]
    return render_template('get_albums.html', albums= album)

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    list_of_artists = repository.all()
    return render_template('get_artists.html',artists= list_of_artists )

@app.route('/artists', methods = ['POST'])
def post_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    repository.create(artist)
    return ""

@app.route('/artists/<id>')
def get_artist_by_id(id):
    connection = get_flask_database_connection(app)
    repo = ArtistRepository(connection)
    artist = repo.find(id)
    return render_template('artist.html', artist_details = artist)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
