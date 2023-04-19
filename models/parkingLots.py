class Parking():
  def __init__(self, state):
    self.occupied = state

  def fill(self):
    if self.occupied == False:
      self.occupied = True

  def unfill(self):
    if self.occupied == True:
      self.occupied = False


parkingLots = []

for i in range(10):
  if i % 2 == 0:
    state = True
  else:
    state = False
  newParkingLot = Parking(state)
  parkingLots.append(newParkingLot)