import reflex as rx


class AuthState(rx.State):
    token: str = rx.LocalStorage("")

    def logout(self):
        self.token = ''

    @rx.var
    def is_logged_id(self):
        return self.token != ''
