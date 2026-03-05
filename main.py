from dataclasses import dataclass


@classmethod
class Profil:
    username: str
    email: str
    parol: str

    def tek_parol(self):
        if len(self.parol) > 8:
            return True
