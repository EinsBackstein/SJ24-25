from device import ElectricDevice, ConsumingDevice, ProducingDevice
import json
import csv
from faker import Faker
import random


class Building:
    def __init__(self):
        self._devices = list()

    def add_device(self, device: ElectricDevice):
        self._devices.append(device)

    def remove_device(self, device_id: int):
        for device in self._devices:
            if device.device_id == device_id:
                self._devices.remove(device)

    def run_all_devices(self, period: int):
        for device in self._devices:
            device.run(period)

    def total_energy_balance(self):
        total = 0
        for device in self._devices:
            total += device.energy_balance()
        return total

    def export_to_csv(self):
        with open("devices.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["device_id", "name", "power",
                            "total_runing_time", "type", "efficiency"])
            for device in self._devices:
                if (device.__class__.__name__ == "ConsumingDevice"):
                    writer.writerow([device.device_id, device.name, device.power,
                                    device._total_runing_time, device.__class__.__name__, None])
                else:
                    writer.writerow([device.device_id, device.name, device.power,
                                    device._total_runing_time, device.__class__.__name__, device.efficiency])

    def export_to_json(self):
        with open("devices.json", "w") as file:
            json.dump([device.to_dict() for device in self._devices], file)

    def import_from_json(self):
        with open("devices.json", "r") as file:
            data = json.load(file)
            for device in data:
                if device["type"] == "ConsumingDevice":
                    new_device = ConsumingDevice(
                        device["device_id"], device["name"], device["power"], device["total_runing_time"])
                elif device["type"] == "ProducingDevice":
                    new_device = ProducingDevice(
                        device["efficiency"], device["device_id"], device["name"], device["power"], device["total_runing_time"])
                new_device.from_dict(device)
                self._devices.append(new_device)

    def create_new_device(self, id: int, name: str, power: int, efficiency: int):
        efficiency = efficiency
        if (power < 0):
            new_device = ConsumingDevice(id, name, power)
        else:
            new_device = ProducingDevice(efficiency, id, name, power)
        return new_device


def generate_random_device():
    faker = Faker()
    word = faker.word()
    power = random.randint(-1000, 1000)
    id = random.randint(0, 1000)
    efficiency = random.randint(0, 100)/100
    return id, word, power, efficiency
