from random import randint
from time import sleep

def main():
    for i in range(100):
        rand = randint(1, 100)
        print(f"Hola mundo {rand}...")
        sleep(1)

if __name__ == "__main__":
    main()