msg = ('Тип тренировки: {}; '
       'Длительность:{} ч.; '
       'Дистанция:{} км; '
       'Ср. скорость:{} км/ч; '
       'Потрачено ккал:{}.')

d = {'training_type': 'Swimming', 'duration': 1.5, 'distance': 0.9935999999999999, 'speed': 0.6666666666666666,
     'calories': 423.99999999999994}
print(msg.format(*d))
