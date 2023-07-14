from playwright.sync_api import Page, expect


"""
We can get the list of albums from the /albums page
"""
def test_get_albums(page, test_web_address, db_connection): 
    #connecting to a smaller test seed with 2 albums and 2 artists
    db_connection.seed("seeds/test_music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    paragraph_block = page.locator("div")
    expect(paragraph_block).to_have_text([
        'Title: Doolittle\nReleased: 1989',
        'Title: Surfer Rosa\nReleased: 1988'
    ])

'''
We want to get the detail of a single artist (ABBA) when visiting /artists/2
'''
def test_get_ABBA_single_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/2")
    paragraph = page.locator("p")
    expect(paragraph).to_have_text(
        "Artist Name: ABBA Genre: Pop"
    )

'''
We want to see a list of links for all of our artists' pages when visiting /artists
'''
def test_get_artists(page, test_web_address ,db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Artist Name: Pixies")
    paragraph = page.locator("p")
    expect(paragraph).to_have_text(
        "Artist Name: Pixies Genre: Rock"
    )