class TransactionDto:
    def __init__(self, id, data, amount, description, user_id_sender, user_id_receiver):
        self.id = id
        self.data = data
        self.amount = amount
        self.description = description
        self.user_id_sender = user_id_sender
        self.user_id_receiver = user_id_receiver

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.data,
            'amount': self.amount,
            'sender': self.user_id_sender,
            'receiver': self.user_id_receiver,
            'description': self.description
        }