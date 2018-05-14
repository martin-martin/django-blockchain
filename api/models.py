from django.db import models


class Blockchain(models.Model):
    """This class represents the Blockchain model."""

    index = models.IntegerField()
    timestamp = models.DateTimeField()
    proof = models.IntegerField()
    # SHA256 digest will always be 256bit = 64 hex digits
    current_hash = models.CharField(max_length=64, blank=False)
    # maybe unnecessary to store previous_hash, as it'll be there in the
    # block with the previous index anyways, but might be easier like so
    previous_hash = models.CharField(max_length=64, blank=False)


class Transactions(models.Model):
    """represents the Transactions model."""

    # to_field could also point to the current_hash of the block
    # however, since we're not planning to mess with this database
    # and use it as append-only (and only for quick look-up)
    # we're referencing simply the block number.
    block_index = models.ForeignKey('Blockchain', to_field='index')
    # addresses won't be longer than 34 characters.
    # TODO: double-check whether I set this up correctly
    sender = models.CharField(max_length=34)
    recipient = models.CharField(max_length=34)
    # a sensible blockchain would allow storing floats
    # or at least make a BigIntegerField() to allow for satoshi repr.
    amount = models.IntegerField()
