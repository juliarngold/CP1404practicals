from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """display menu to chose from quit, chose a taxi or calculate the fare costs"""
    print("Let's drive!")
    taxis = [Taxi(100, "Prius"), SilverServiceTaxi(100, "Limo", 2), SilverServiceTaxi(200, "Hummer", 4)]
    current_taxi = None
    total_bill = 0.0

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break

        elif choice == 'c':
            current_taxi = choose_taxi(taxis, total_bill)

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                total_bill += trip_cost
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")

        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")


def display_taxis(taxis):
    """display taxis"""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis, total_bill):
    """get a taxi choice"""
    display_taxis(taxis)
    while True:
        choice = input("Choose taxi: ")
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(taxis):
                return taxis[choice]
        print("Invalid taxi choice")
        print(f"Bill to date: ${total_bill:.2f}")


main()
