import json
from datetime import date, datetime

# 继承json源代码，让jason可以接受日期格式

d = {'time1': date.today(), 'time2': datetime.today()}


class Myjson(json.JSONEncoder):

    def default(self, o): # o 就是你想要序列化的对象
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %X')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        else:
            return super().default(o)


res = json.dumps(d, cls=Myjson)
print(res)

