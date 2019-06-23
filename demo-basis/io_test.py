# coding:utf-8

import json
import os
import pickle

print(os.name)
print(os.environ)
print(os.path.abspath("."))

# =====================================序列化==========================================

d = dict(name='bob', age=20, score=30)
print(pickle.loads(pickle.dumps(d)))

# ========================================JSON序列化===========================================

print(json.dumps(d))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return json.dumps(to_json_string(self))


def to_json_string(std: Student):
    """
    序列化
    """
    return {'name': std.name, 'age': std.age, 'score': std.score}


s = Student('bob', 20, 88)
j = json.dumps(s, default=to_json_string)


def dict_to_student(d):
    """
    反序列化
    """
    return Student(d['name'], d['age'], d['score'])


print(json.loads(j, object_hook=dict_to_student))
