from cProfile import run
from doctest import debug
from app import app

if __name__ == '__main__':
    run(debug = True)