import reflex as rx
from ..API.api_config import payments
from .base_eth import BaseEth, w3


class EthState(BaseEth):
    formdata:dict = {}


    def buy_tokens(self, form_data:dict):
        if self.valid_pk:
            print(form_data)
            key = self.pk
            address = self.wallet_addres
            amount_to_wei = w3.to_wei(float(form_data['price']), "ether")

            transaction = {
                "nonce": w3.eth.get_transaction_count(address),
                "to": self.owner_account,
                "value": amount_to_wei,
                "gas": 21000,
                "gasPrice": w3.eth.gas_price,
            }

            signed_txn = w3.eth.account.sign_transaction(transaction, key)

            tx_hash = "0x{}".format(
                w3.eth.send_raw_transaction(signed_txn.raw_transaction).hex()
            )

            payment = payments.buytoken(
                token=self.token,
                plan_name=form_data["plan"],
                tx_hash=tx_hash,
            )

            coins = payment["total"]
            print(payment, tx_hash)

            return rx.toast.success(
                "Has comprado: {} Tokens. Hash de la transacción: {}".format(coins, tx_hash),
                position="top-center",
            )

        else:
            return rx.toast.error(
                "Tu cartera de ethereum no esta conectada", position="top-center"
            )

    def paymenet_history(self):
        history = payments.payment_history(token=self.token)

        return history
