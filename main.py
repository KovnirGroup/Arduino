# create realtime data monitor with Kalman filter
def get_sensor_data():
  return Ax, Ay, Az, Gx, Gy, Gz, T, B

varVolt = 0.25  # среднее отклонение (ищем в excel)
varProcess = 0.05  # скорость реакции на изменение (подбирается вручную)
Pc = 0.0
G = 0.0
P = 1.0
Xp = 0.0
Zp = 0.0
Xe = 0.0

def kalman(val):
  Pc = P + varProcess
  G = Pc/(Pc + varVolt)
  P = (1-G)*Pc
  Xp = Xe
  Zp = Xp
  Xe = G*(val-Zp)+Xp  # "фильтрованное" значение
  return Xe

def draw_live_graph():
  pass

def Calculate_raww_pinch_tang():
  pass

def Calculate_X_Y_Z():
  pass
