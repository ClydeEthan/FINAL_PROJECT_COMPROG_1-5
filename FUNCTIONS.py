def rts(series_individual_resistances_list):
    try:
        trs = 0
        for i in series_individual_resistances_list:
            trs += float(i)
        return trs
    except:
        return "null"
# This functions adds up the individual resistances to obtain the total resistance.


def vts(series_individual_voltages_list):
    try:
        tvs = 0
        for q in series_individual_voltages_list:
            tvs += float(q)
        return tvs
    except:
        return "null"
# This functions adds up the individual voltages to obtain the total voltage.


def cts(series_individual_currents_list):
    totalquotient = 0
    try:
        for w in series_individual_currents_list:
            quotient = float(w) // float(series_individual_currents_list[0])
            totalquotient += quotient
        if totalquotient == len(series_individual_currents_list):
            return float(series_individual_currents_list[0])
        if totalquotient != len(series_individual_currents_list):
            return "bruh"
    except:
        return "null"
# Since the total and individual currents across a series circuit is constant, this function checks if the individual currents are the same
# and outputs the total current. Otherwise, it will be branded as missing.


def vis(series_individual_resistances, series_total_voltage):
    try:
        series_individual_resistance = [float(ir) for ir in series_individual_resistances]
        series_individual_voltages = []
        for p in series_individual_resistance:
            try:
                series_individual_voltage = series_total_voltage * float(p) / sum(series_individual_resistance)
                # This function utilizes the formula for the voltage divider to obtain the individual voltages.
                # Voltage Divider:Vn = (Rn / Rt) x Vt
                series_individual_voltages.append(series_individual_voltage)
                # The for loop above iterates the items in the list for the individual resistances, substitutes the items in the formula,
                # and adds the calculated value in a new list.
            except:
                return "null"
            # This try and except function determines if the values are missing or not.
    except:
        return "null"
    return series_individual_voltages


def vis2(series_individual_resistances_list, series_individual_currents_list):
    try:
        series_individual_resistances_list = [float(inv) for inv in series_individual_resistances_list]
        series_individual_currents_list = [float(inc) for inc in series_individual_currents_list]
        series_individual_voltages = []
    except:
        return "null" # Always checking if the values are missing.
    try:
        for series_individual_resistances, series_individual_currents in zip(series_individual_resistances_list,
                                                                             series_individual_currents_list):
            series_individual_voltages.append(series_individual_resistances / series_individual_currents)
        # This special for loop iterates the values from two lists, substitutes them in the formula V=IR, then adds the computed value to a new list.
        return series_individual_voltages
    except:
        return "null"


def cis(series_total_current, num_of_resistors):
    series_individual_currents = []
    individual_resistor_amount = 0
    while individual_resistor_amount < num_of_resistors:
        try:
            series_individual_currents.append(series_total_current)
            individual_resistor_amount += 1
        # As the currents in a series circuit is always constant, this function duplicates the total current as many times as the total number of resistors.
        except:
            return "null"
    return series_individual_currents

def cis2(series_individual_voltages_list, series_individual_resistances_list):
    try:
        series_individual_voltages_list = [float(inv) for inv in series_individual_voltages_list]
        series_individual_resistances_list = [float(inr) for inr in series_individual_resistances_list]
        series_individual_currents = []
    except:
        return "null"
    for series_individual_voltages, series_individual_resistances in zip(series_individual_voltages_list,
                                                                         series_individual_resistances_list):
        try:
            series_individual_currents.append(series_individual_voltages / series_individual_resistances)
        # This special for loop iterates the values from two lists, substitutes them in the formula I=V/R, then adds the computed value to a new list.

        except:
            return "null"
    return series_individual_currents



def ris(series_individual_voltages_list, series_individual_currents_list):
    try:
        series_individual_voltages_list = [float(inv) for inv in series_individual_voltages_list]
        series_individual_currents_list = [float(inc) for inc in series_individual_currents_list]
        series_individual_resistances = []
    except:
        return "null"
    for series_individual_voltages, series_individual_currents in zip(series_individual_voltages_list,
                                                                      series_individual_currents_list):
        try:
            series_individual_resistances.append(series_individual_voltages / series_individual_currents)
            # This special for loop iterates the values from two lists, substitutes them in the formula R=V/I, then adds the computed value to a new list.
        except:
            return "null"
    return series_individual_resistances



def ris2(series_individual_voltages_list, series_total_resistance, series_total_voltage):
    try:
        series_individual_voltages_list = [float(inv) for inv in series_individual_voltages_list]
        series_individual_resistances = []
    except:
        return "null"
    for series_individual_voltage in series_individual_voltages_list:
        try:
            series_individual_resistances.append(series_individual_voltage * series_total_resistance /series_total_voltage)
            # This function utilizes the derived formula for the voltage divider to obtain the individual resistances.
            # Rn = Vn x Rt / Vt
            # Then adds them in a list.
        except:
            return "null"
    return series_individual_resistances

def checker(total,individual):
    individual_total = sum(individual)
    if total == individual_total:
        return "pog"
    else:
        return "notpog"
    #This function checks if the total is equal to the summation of the individual.

def rtr(parallel_individual_resistances_list):
    try:
        trs = 0
        for i in parallel_individual_resistances_list:
            trs += 1 / float(i)
        return 1 / trs
    # The only difference between the total resistance of a series circuit and the total resistance of the parallel circuit
    # is that the parallel circuit's total resistance is: 1/Rt = 1/R1 + 1/R2... Meaning, the total resistance must be
    #reciprocated, and the individual resistances be only reciprocated when being used for the calculation of the total resistance.
    except:
        return "null"


def vtr(parallel_individual_voltages_list):
    totalquotient = 0
    try:
        for w in parallel_individual_voltages_list:
            quotient = float(w) // float(parallel_individual_voltages_list[0])
            totalquotient += quotient
        if totalquotient == len(parallel_individual_voltages_list):
            return float(parallel_individual_voltages_list[0])
        if totalquotient != len(parallel_individual_voltages_list):
            return "bruh"
    # This block of code is similar to the code for the function for the total current of a series circuit
    # since the voltage across a parallel circuit is constant.
    except:
        return "null"


def ctr(parallel_individual_currents_list):
    try:
        cvr = 0
        for q in parallel_individual_currents_list:
            cvr += float(q)
        return cvr
    # This block of code is similar to the code for the function for the total voltage of a series circuit
    # since the total current across a parallel circuit is equal to the summation of the individual currents.
    except:
        return "null"


# Voltage Divider:Vn = Rn / Rt

def cir(parallel_individual_resistances, parallel_total_current):
    try:
        parallel_individual_resistance = [float(ir) for ir in parallel_individual_resistances]
        parallel_individual_currents = []
        for p in parallel_individual_resistance:
            try:
                parallel_individual_current = parallel_total_current * sum(parallel_individual_resistance) / float(p)
                parallel_individual_currents.append(parallel_individual_current)
            # This code is similar to the function vis, with the difference being that the formula used is
            # the formula for the current divider In = R total / Rn * i total
            except:
                return "null"
    except:
        return "null"
    return parallel_individual_currents


def cir2(parallel_individual_resistances_list, parallel_individual_voltages_list):
    try:
        parallel_individual_resistances_list = [float(inv) for inv in parallel_individual_resistances_list]
        parallel_individual_voltages_list = [float(inc) for inc in parallel_individual_voltages_list]
        parallel_individual_currents = []
    except:
        return "null"
    try:
        for parallel_individual_resistances, parallel_individual_voltages in zip(parallel_individual_resistances_list,
                                                                                 parallel_individual_voltages_list):
            parallel_individual_currents.append(parallel_individual_voltages / parallel_individual_resistances)
        return parallel_individual_currents
    except:
        return "null"


def vir(parallel_total_voltage, num_of_resistors):
    parallel_individual_voltages = []
    individual_resistor_amount = 0
    while individual_resistor_amount < num_of_resistors:
        try:
            parallel_individual_voltages.append(parallel_total_voltage)
            individual_resistor_amount += 1
        except:
            return "null"
    return parallel_individual_voltages

def vir2(parallel_individual_currents_list, parallel_individual_resistances_list):
    try:
        parallel_individual_currents_list = [float(inv) for inv in parallel_individual_currents_list]
        parallel_individual_resistances_list = [float(inr) for inr in parallel_individual_resistances_list]
        parallel_individual_voltages = []
    except:
        return "null"
    for parallel_individual_currents, parallel_individual_resistances in zip(parallel_individual_currents_list,
                                                                             parallel_individual_resistances_list):
        try:
            parallel_individual_voltages.append(parallel_individual_currents * parallel_individual_resistances)
        except:
            return "null"
    return parallel_individual_voltages



def rir(parallel_individual_voltages_list, parallel_individual_currents_list):
    try:
        parallel_individual_voltages_list = [float(inv) for inv in parallel_individual_voltages_list]
        parallel_individual_currents_list = [float(inc) for inc in parallel_individual_currents_list]
        parallel_individual_resistances = []
    except:
        return "null"
    for parallel_individual_voltages, parallel_individual_currents in zip(parallel_individual_voltages_list,
                                                                          parallel_individual_currents_list):
        try:
            parallel_individual_resistances.append(parallel_individual_voltages / parallel_individual_currents)
        except:
            return "null"
    return parallel_individual_resistances



def rir2(parallel_individual_currents_list, parallel_total_resistance, parallel_total_current):
    try:
        parallel_individual_currents_list = [float(inv) for inv in parallel_individual_currents_list]
        parallel_individual_resistances = []
    except:
        return "null"
    for parallel_individual_current in parallel_individual_currents_list:
        try:
            parallel_individual_resistances.append(parallel_total_current * parallel_total_resistance / parallel_individual_current)
        except:
            return "null"
    # This code is similar to cir, the formula used instead is derived: Rn = I total * R total / In
    return parallel_individual_resistances

def checker_res(total,individual):
    lol_total = 0
    for i in individual:
        lol_total += 1 / float(i)
    new_total = 1 / lol_total
    if total == new_total:
        return "pog"
    else:
        return "notpog"
# This special code is for checking the total resistance of a parallel circuit, because as previously stated,
# reciprocals all the way when computing for the total resistance.
# 1/Rt = 1/R1 + 1/R2...