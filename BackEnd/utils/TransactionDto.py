class TransactionDto:
    def __init__(self, id, data, amount, description, user_id_sender, user_id_reciver):
        self.id = id
        self.data = data
        self.amount = amount
        self.description = description
        self.user_id_sender = user_id_sender
        self.user_id_reciver = user_id_reciver