from normalize import normalize
from render import render


def make_receipt(name):
    return render(normalize(name, upper=True))
