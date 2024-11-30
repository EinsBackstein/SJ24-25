from abc import ABC, abstractmethod
import json


class ElectricDevice(ABC):
    def __init__(self, device_id: int, name: str, power: int, total_runing_time: int = 0):
        self._device_id = device_id
        self._name = name
        self._power = power
        self._total_runing_time = total_runing_time

    def __eq__(self, other: object) -> bool:
        for obj in other:
            if obj.device_id == self.device_id:
                return True
        return False

    @property
    def device_id(self):
        return self._device_id

    @property
    def name(self):
        return self._name

    @property
    def power(self):
        return self._power

    @device_id.setter
    def device_id(self, device_id: int, deviceList: list):
        if device_id in deviceList:
            raise ValueError("Device ID already exists")
        else:
            self._device_id = device_id

    def run(self, period: int):
        self._total_runing_time += period

    def energy_consumed(self):
        return self._power * self._total_runing_time

    def to_dict(self):
        if (self.__class__.__name__ == "ConsumingDevice"):
            dict = {
                "device_id": self._device_id,
                "name": self._name,
                "power": self._power,
                "total_runing_time": self._total_runing_time,
                "type": self.__class__.__name__
            }
        else:
            dict = {
                "device_id": self._device_id,
                "name": self._name,
                "power": self._power,
                "total_runing_time": self._total_runing_time,
                "type": self.__class__.__name__,
                "efficiency": self.efficiency
            }
        return dict

    def from_dict(self, dict):
        def __init__():
            self._device_id = dict["device_id"]
            self._name = dict["name"]
            self._power = dict["power"]
            self._total_runing_time = dict["total_runing_time"]

    @abstractmethod
    def energy_balance(self):
        pass


class ConsumingDevice(ElectricDevice):
    def __init__(self, id: int, name: str, power: int, total_runing_time: int = 0):
        super().__init__(id, name, power, total_runing_time)

    def energy_balance(self):
        return self.energy_consumed()/1000


class ProducingDevice(ElectricDevice):
    def __init__(self, efficiency: int, device_id: int, name: str, power: int, total_runing_time: int = 0):
        self.efficiency = efficiency
        super().__init__(device_id, name, power, total_runing_time)

    def energy_balance(self):
        return self.energy_consumed()/1000 * self.efficiency
