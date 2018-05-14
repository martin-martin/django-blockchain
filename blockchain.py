import hashlib
import json
from time import time
from uuid import uuid4


class Blockchain():
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # create the genesis block with default seed values
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """"Creates a new block and adds it to the chain.

        Args:
            proof (<int>): proof provided by Proof-Of-Work algorithm
            previous_hash (<str>, optional): hash of previous block

        Returns:
            <dict>: a new block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash_block(self.chain[-1])
        }
        # reset list of current transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """"Creates a new transaction and adds it to next mined block.

        Args:
            sender (<str>): address of the sender
            recipient (<str>): address of the recipient
            amount (<int>): Description

        Returns:
            <int>: index of the block that will contain the transaction
        """
        self.current_transactions.append({
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            })
        return self.last_block['index'] + 1

    @staticmethod
    def hash_block(block):
        """Hashes a block using SHA-256.

        Args:
            block (<dict>): block information

        Returns:
            <str>: the SHA-256 hash of the block
        """
        # to assure consistent hashes, we need to sort the dictionary
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Returns the last block in the chain.

        Returns:
            <dict>: last block in the blockchain
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """Simple Proof-Of-Work Algorithm:
        Find a number p' such that hash(pp') contains 4 leading zeroes,
        where p is the previous p'

        Args:
            last_proof (<int>): p

        Returns:
            <int>: p'
        """
        proof = 0
        while self.validate_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def validate_proof(last_proof, proof):
        """Validates the proof by checking whether hash(last_proof, proof)
        contains 4 leading zeroes.

        Args:
            last_proof (<int>): previous proof
            proof (<int>): current proof

        Returns:
            <bool>: True if correct, False if not
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'
