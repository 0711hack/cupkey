from cryptography.hazmat.primitives.asymmetric.ed25519 import (Ed25519PrivateKey,
                                                               Ed25519PublicKey)
from cryptography.hazmat.primitives.serialization.base import (Encoding,
                                                               NoEncryption,
                                                               PrivateFormat,
                                                               PublicFormat)
from flask import Flask

from flask_restful import Api, Resource
from misc import Cup, Shop, shop_list

app = Flask(__name__)
api = Api(app)


class CupSignature(Resource):
    def post(self):
        """Generate a cup-key and sign it (basically the id of a cup)."""
        shop = None
        cup = None

        if "shop_id" in event and isinstance(event["shop_id"], str):
            shop: Shop = Shop(event["shop_id"])
            cup: Cup = Cup(shop_id=shop.shop_id)
            return dict(cup_id=cup.cup_id, cup_sighash=cup.signature_hash, shop_id=shop.shop_id)


class ShopKeys(Resource):

    def post(self):
        """Generate a keypair for cup-selling shops like starbucks."""
        if "shop_id" in event and event["shop_id"] in shop_list:
            shop = shop_list[event["shop_id"]]
        else:
            shop = Shop(event["shop_id"])
            shop_list[event["shop_id"]] = shop

        return dict(
            shop_id=str(shop.shop_id),
            priv_key=str(
                shop.priv_key.private_bytes(
                    Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()
                ).decode()
            ),
            pub_key=str(
                shop.pub_key.public_bytes(
                    Encoding.PEM, PublicFormat.SubjectPublicKeyInfo
                ).decode()
            ),
        )


class VerifyCupSignature(Resource):
    def post(self):
        shop_pub_key.verify(cup_signature, cup_id)
        return True

api.add_resource(CupSignature, '/cup/sign')
api.add_resource(VerifyCupSignature, '/cup/verify')
api.add_resource(ShopKeys, '/keys/shop')

if __name__ == '__main__':
    app.run(debug=True)
