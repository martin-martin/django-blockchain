from django.test import TestCase
from .models import Blockchain


class ModelTestCase():
    """Defines the test suite for the Blockchain model."""

    def set_up(self):
        """Defines the test client and other test variables."""

        # TODO: change below to accept a new block input to database
        self.blockchain_block = None  # change this
        self.blockchain = Blockchain()  # add the required args

    def test_model_can_create_a_block(self):
        """Test if the model can create a block."""

        old_count = Blockchain.objects.count()
        self.blockchain.save()
        new_count = Blockchain.objects.count()
        self.assertNotEqual(old_count, new_count)
