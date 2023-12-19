class UserDto:
    def __init__(self, id, userName, email, role):
        self.id = id
        self.userName = userName
        self.email = email
        self.role = role

    def to_dict(self):
        return {
            'id': self.id,
            'userName': self.userName,
            'email': self.email,
            'role': self.role
        }