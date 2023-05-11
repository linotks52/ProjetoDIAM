from django.urls.converters import StringConverter


class IntArrayConverter(StringConverter):
    regex = r'\d+(,\d+)*'

    def to_python(self, value):
        return [int(val) for val in value.split(',')]

    def to_url(self, value):
        return ','.join(str(val) for val in value)
