class Category:
    def __init__(self, ID, username, name, description):
        self.id  = ID
        self.username = username;
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def serialize(self):
            return {
            'id':self.id,
            'username':self.username,
            'name':self.name,
            'description':self.description
    }

    