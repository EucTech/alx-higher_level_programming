#!/usr/bin/python3
"""The base class"""
import json
import os.path
import csv
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """To return json string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            To write JSON string representaion of
            list_objs to file
        """
        filename = cls.__name__ + ".json"
        llist = []
        if list_objs is None:
            with open(filename, 'w') as f:
                f.write("[]")
        elif list_objs is not None:
            for obj in range(len(list_objs)):
                llist.append(list_objs[obj].to_dictionary())

            j_list = cls.to_json_string(llist)
            with open(filename, 'w', encoding="utf-8") as f:
                f.write(j_list)

    @staticmethod
    def from_json_string(json_string):
        """
           returns the list of the JSON string
            representation json_string
        """
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """that returns an instance with all attributes
            already set
        """
        if cls.__name__ == "Rectangle":
            get_instance = cls(10, 10)
        elif cls.__name__ == "Square":
            get_instance = cls(10)

        get_instance.update(**dictionary)
        return get_instance

    @classmethod
    def load_from_file(cls):
        """return list of instances"""
        filename = cls.__name__ + ".json"

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            string = f.read()

        cls_instance = cls.from_json_string(string)
        l_instance = []

        for i in range(len(cls_instance)):
            l_instance.append(cls.create(**cls_instance[i]))

        return l_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save file in csv"""
        filename = cls.__name__ + ".csv"

        if cls.__name__ == "Rectangle":
            ld = [0, 0, 0, 0, 0]
            lk = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            ld = ['0', '0', '0', '0']
            lk = ['id', 'size', 'x', 'y']

        llist = []

        if list_objs is None:
            with open(filename, 'w', newline="") as f:
                csv.writer("[]")
        elif list_objs is not None:
            for ob in list_objs:
                for x in range(len(lk)):
                    ld[x] = ob.to_dictionary()[lk[x]]
                llist.append(ld[:])

        with open(filename, "w") as f:
            c_file = csv.writer(f)
            c_file.writerows(llist)

    @classmethod
    def load_from_file_csv(cls):
        """To load file csv"""
        filename = cls.__name__ + ".csv"

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            r_file = csv.reader(f)
            c_list = list(r_file)

        if cls.__name__ == "Rectangle":
            lk = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            lk = ['id', 'size', 'x', 'y']

        llist = []

        for i in c_list:
            dc = {}
            for x in enumerate(i):
                dc[lk[x[0]]] = int(x[1])
            llist.append(dc)

        l_ins = []

        for k in range(len(llist)):
            l_ins.append(cls.create(**llist[k]))

        return l_ins

    def draw(list_rectangles, list_squares):
        """To draw the shape of the rectangles
            and squar
        """
        shape = turtle.Turtle()

        for i in range(4):
            list_rectangle.forward(self.width)
            list_rectanglt.forward(self.heght)


        turtle.done()
