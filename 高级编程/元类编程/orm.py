# -*- coding:utf-8 -*-
import numbers


class Field:
    pass


class IntField(Field):
    # 数据描述符
    def __init__(self, db_column, min_value=None, max_value=None):
        self.db_column = db_column
        self._min_value = min_value
        self._max_value = max_value
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("need int value")
            elif min_value < 0:
                raise ValueError("need positive value")
        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError("need int value")
            elif max_value < 0:
                raise ValueError("need positive value")

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if value < self._min_value or value > self._max_value:
            raise ValueError
        self.value = value


class CharField(Field):
    # 数据描述符
    def __init__(self, db_column=None, max_length=None):
        self.value = None
        self.db_column = db_column
        if max_length is None:
            raise ValueError("max_length is none")

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("need str value")
        self.value = value


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
        attr_meta = attrs.get('Meta', None)
        _meta = {}
        db_table = getattr(attr_meta, 'db_table', None) or name.lower()
        _meta['db_table'] = db_table
        attrs['_meta'] = _meta
        attrs['fields'] = fields
        del attrs['Meta']
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return super().__init__()

    def save(self):
        fields = []
        values = []
        for k, v in self.fields.items():
            db_column = v.db_column or k.lower()
            fields.append(db_column)
            value = getattr(self, k)
            values.append(str(value))
        sql = "insert {db_table} ({fields}) value({values})".format(db_table=self._meta['db_table'],
                                                                    fields=','.join(fields), values=','.join(values))
        print(sql)


class User(object):
    name = CharField(db_column='', max_length=10)
    age = IntField(db_column='', min_value=0, max_value=100)

    class Meta:
        db_table = 'user'


if __name__ == '__main__':
    user = User()
    user.name = 'bobby'
    user.age = 28
    user.save()
