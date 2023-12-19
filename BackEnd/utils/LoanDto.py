class LoanDto:
    def __init__(self, id, amount, interestRate, openingDate, closingDate):
        self.id = id
        self.amount = amount
        self.interestRate = interestRate
        self.openingDate = openingDate
        self.closingDate = closingDate

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'interestRate': self.interestRate,
            'openingDate': self.openingDate,
            'closingDate': self.closingDate
        }