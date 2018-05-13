class Blockchain():
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        """"Creates a new block and adds it to the chain."""
        pass

    def new_transaction(self):
        """"Adds a new transaction and to the ledger."""
        pass

    @staticmethod
    def hash_block(block):
        """Hashes a block using SHA256."""
        pass

    @property
    def last_block(self):
        """Returns the last block in the chain."""
        pass
