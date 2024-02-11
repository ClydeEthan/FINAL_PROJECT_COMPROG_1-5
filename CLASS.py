class Series:

    def __init__(self, circuitname, series_total_resistance, series_total_voltage, series_total_current):
        self.circuitname = circuitname
        self.series_total_resistance = series_total_resistance
        self.series_total_voltage = series_total_voltage
        self.series_total_current = series_total_current
# This Series object is composed of a name, its total resistance, its total voltage, and its total current.

    def formula_series_total_resistance(self):
        try:
            self.series_total_resistance = float(self.series_total_resistance)
            self.series_total_resistance = self.series_total_voltage / self.series_total_current
            return self.series_total_resistance
        except:
            return self.series_total_resistance
        # This method determines the value for the total resistance using R = V/I

    def formula_series_total_voltage(self):
        try:
            self.series_total_voltage = float(self.series_total_voltage)
            self.series_total_voltage = self.series_total_resistance * self.series_total_current
            return self.series_total_voltage
        except:
            return self.series_total_voltage
        # This method determines the value for the total voltage using V=IR


    def formula_series_total_current(self):
        try:
            self.series_total_current = self.series_total_voltage / self.series_total_resistance
            return self.series_total_current
        except:
            return self.series_total_current
        # This method determines the value for the total resistance using I=V/R

# The class object below follows the same format from the class and methods of the object Series with the only
# difference being the variable names as VIR or Ohm's law is universal
class Parallel:

    def __init__(self, circuitname, parallel_total_resistance, parallel_total_voltage, parallel_total_current):
        self.circuitname = circuitname
        self.parallel_total_resistance = parallel_total_resistance
        self.parallel_total_voltage = parallel_total_voltage
        self.parallel_total_current = parallel_total_current

    def formula_parallel_total_resistance(self):
        try:
            self.parallel_total_resistance = float(self.parallel_total_resistance)
            self.parallel_total_resistance = self.parallel_total_voltage / self.parallel_total_current
            return self.parallel_total_resistance
        except:
            return self.parallel_total_resistance

    def formula_parallel_total_voltage(self):
        try:
            self.parallel_total_voltage = float(self.parallel_total_voltage)
            self.parallel_total_voltage = self.parallel_total_resistance * self.parallel_total_current
            return self.parallel_total_voltage
        except:
            return self.parallel_total_voltage

    def formula_parallel_total_current(self):
        try:
            self.parallel_total_current = self.parallel_total_voltage / self.parallel_total_resistance
            return self.parallel_total_current
        except:
            return self.parallel_total_current
