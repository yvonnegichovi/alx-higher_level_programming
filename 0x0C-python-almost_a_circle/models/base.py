#!/usr/bin/python3

"""This module creates the 'bases' for all other classes in the project
it mwnages id attribute in all the future classes and avoid duplicating
the same code
"""

import json
import csv
from models.rectangle import Rectangle
from models.square import Square


class Base:
    """This class has a private attribute that counts the id"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is a class constructor that tracks id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def reset_nb_objects(cls):
        cls.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string rep of list_objs to a file
        """
        if list_objs is None:
            list_objs = []
        filename = "{}.json".format(cls.__name__)
        dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dictionaries)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method that writes the CSV string rep of list_objs to a file
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if list_objs is None:
            list_objs = []
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline='') as file:
            csv_writer = csv.writer(file)
            for obj in list_objs:
                if isinstance(obj, Rectangle):
                    csv_writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif isinstance(obj, Square):
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances"""
        from models.rectangle import Rectangle
        from models.square import Square

        filename = "{}.csv".format(cls.__name__)
        instances = []
        try:
            with open(filename, "r", newline='') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
                    instances.append(instance)
        except FileNotFoundError:
            pass
        return instances
