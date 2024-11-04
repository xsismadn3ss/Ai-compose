import reflex as rx
import dotenv
import os
from web3 import Web3

dotenv.load_dotenv()
w3 = Web3(Web3.HTTPProvider(os.getenv("INFURA_URL")))


class BaseEth(rx.State):
    pk: str = rx.LocalStorage("", name="pk")
    token: str = rx.LocalStorage("", name="token")
    valid_pk: bool = rx.LocalStorage(False, name="pk_valid")
    owner_account: str = os.getenv("OWNER_ACCOUNT")
    input_pk: str = ""

    def test_connection(self, pk):
        try:
            w3.eth.account.from_key(pk)
            return True
        except Exception as e:
            print(e)
            return False

    def connect_wallet(self):
        if self.input_pk != "":
            self.pk = self.input_pk
            is_succes = self.test_connection(self.input_pk)
            if is_succes:
                self.valid_pk = True
                return rx.toast.success(
                    "Cartera conectada con exito", position="top-center"
                )
            else:
                self.valid_pk = False
                return rx.toast.success(
                    "No fue posible conectarse, asegurate de ingresar una clave valida", position="top-center"
                )
            
        self.valid_pk = False
        return rx.toast.error(
            "Asegurate de ingresar una clave privada valida o rellenar todos los campos",
            position="top-center",
        )

    @rx.var
    def wallet_addres(self):
        if self.pk != "":
            try:
                account = w3.eth.account.from_key(self.pk)
                address = account.address
                return address
            except Exception as e:
                self.pk = ""
                self.valid_pk = False
                return None
        else:
            return None

    @rx.var
    def balance(self):
        if (
            self.valid_pk
            and self.wallet_addres is not None
            and self.wallet_addres != ""
        ):
            try:
                to_eth = lambda b: w3.from_wei(b, "ether")
                address = self.wallet_addres
                balance = to_eth(w3.eth.get_balance(address))
                return str(balance)
            except Exception as e:
                print(e)
                self.pk = ""
                return 0.0
        else:
            return 0.0

    @rx.var
    def is_logged_in(self):
        if self.token != "":
            return True
        return False

    @rx.var
    def wallet_connected(self):
        if self.valid_pk:
            return True
        return False

    def disconnect_wallet(self):
        self.valid_pk = False
        self.pk = ""
