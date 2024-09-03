import json
import random
from channels_redis.core import RedisChannelLayer as _RedisChannelLayer


class RedisChannelLayer(_RedisChannelLayer):


    ### Serialization ###

    def serialize(self, message):
        """
        Serializes message to a byte string.
        """
        message = json.dumps(message).encode('utf-8')
        if self.crypter:
            message = self.crypter.encrypt(message)

        # As we use an sorted set to expire messages we need to guarantee uniqueness, with 12 bytes.
        random_prefix = random.getrandbits(8 * 12).to_bytes(12, "big")
        return random_prefix + message

    def deserialize(self, message):
        """
        Deserializes from a byte string.
        """
        # Removes the random prefix
        message = message[12:]

        if self.crypter:
            message = self.crypter.decrypt(message, self.expiry + 10)
        return json.loads(message.decode('utf-8'))
