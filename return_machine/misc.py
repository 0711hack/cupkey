import datetime
import glob
import hashlib
import os
import random
import subprocess
import sys
import pickle

import pprint

# import qrcode
from cryptography.exceptions import InvalidKey
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.ed25519 import (Ed25519PrivateKey,
                                                               Ed25519PublicKey)
from cryptography.hazmat.primitives.serialization.base import (Encoding,
                                                               NoEncryption,
                                                               PrivateFormat,
                                                               PublicFormat)


class Shop():

    def __init__(self, shop_id, priv_key=None):
        self._shop_id = shop_id
        self._priv_key = priv_key if priv_key else Ed25519PrivateKey.generate()

    @property
    def shop_id(self) -> str:
        return str(self._shop_id)

    @property
    def priv_key(self) -> Ed25519PrivateKey:
        return self._priv_key

    @property
    def pub_key(self) -> Ed25519PublicKey:
        return self._priv_key.public_key()


class Cup():

    def __init__(self, shop_id=None, priv_key=None):
        self._priv_key = priv_key if priv_key else Ed25519PrivateKey.generate()
        self._cup_signature = None

        self._signing_shop = Shop(shop_id)

        cup_id_digest = hashes.Hash(hashes.SHAKE128(16), backend=default_backend())
        cup_id_digest.update(self.pub_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo))
        self._cup_id: bytes = cup_id_digest.finalize()

    @property
    def cup_id(self) -> str:
        """Return the unique, hashed, id of a cup/hash of signature."""
        return self._cup_id.hex()

    @property
    def priv_key(self) -> Ed25519PrivateKey:
        return self._priv_key

    @property
    def pub_key(self) -> Ed25519PublicKey:
        return self._priv_key.public_key()

    @property
    def signature(self, shop=None) -> bytes:
        if shop:
            priv_key = shop.priv_key
        elif self._signing_shop:
            priv_key = self._signing_shop.priv_key
        else:
            raise ValueError

        return priv_key.sign(self.pub_key.public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo))

    @property
    def signature_hash(self) -> bytes:
        signature_hash = hashes.Hash(hashes.SHAKE128(16), backend=default_backend())
        signature_hash.update(self.signature)
        return signature_hash.finalize().hex()

# shop_list = dict()
shop_list = dict(
    starbucks=Shop("starbucks"),
    coffeefellows=Shop("coffeefellows"),
    kaffeehaus=Shop("kaffeehaus"),
)