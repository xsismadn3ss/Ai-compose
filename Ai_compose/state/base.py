import reflex as rx

class State(rx.State):

    authenticated: bool = False

    def logout(self):
        self.reset()
        return rx.redirect('/')
    
    def check_login(self):
        if not self.authenticated:
            rx.redirect('/')

    @rx.var
    def logged_in(self):
        if self.authenticated:
            return True

        return False