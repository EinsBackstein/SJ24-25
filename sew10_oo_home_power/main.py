from controller import Building, generate_random_device

def main():
    # Create a new building
    building = Building()
    # Generate some devices and add them to the building
    for i in range(5):
        random = generate_random_device()
        id = random[0]
        name = random[1]
        power = random[2]
        efficiency = random[3]
        new_device = building.create_new_device(id, name, power, efficiency)
        building.add_device(new_device)
    # let the devices run for a while
    building.run_all_devices(10)
    # Show the total energy balance
    print(building.total_energy_balance())
    # Export the devices to a CSV and JSON file
    building.export_to_csv()
    building.export_to_json()
    # Create a new building and import the devices from the JSON file
    building2 = Building()
    building2.import_from_json()
    # Show the total energy balance again
    print(building2.total_energy_balance())


if __name__ == "__main__":
    main()