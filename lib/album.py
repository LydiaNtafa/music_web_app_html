class Album:
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
    
    def is_valid(self):
        list_of_properties = [self.title, self.release_year, self.artist_id]
        if None not in list_of_properties and "" not in list_of_properties:
            return True
        else: 
            return False
        
    def error_messages(self):
        errors = []
        if self.title == None or self.title == "":
            errors.append("Title can't be blank")
        if self.release_year == None or self.release_year == "":
            errors.append("Release year can't be blank")
        if self.artist_id == None or self.artist_id == "":
            errors.append("Artist id can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)