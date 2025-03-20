import datetime

# Funksioni për të përshëndetur përdoruesin
def greet_user():
    try:
        name = input("Si quheni? ")  # Kërkoni emrin e përdoruesit
        if not name:
            raise ValueError("Emri nuk mund të jetë bosh.")
        print(f"Përshëndetje, {name}!")
    except ValueError as e:
        print(f"Gabim: {e}")
        greet_user()  # Përsëri kërkojmë emrin

# Programi kryesor
def main():
    print("Hello, World!")  # Shfaq "Hello, World"
    greet_user()  # Thirr funksionin për përshëndetje
    print(f"Data dhe ora aktuale: {datetime.datetime.now()}")  # Shfaq datën dhe orën aktuale

if __name__ == "__main__":
    main()
