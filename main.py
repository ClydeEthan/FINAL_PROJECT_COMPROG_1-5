from FUNCTIONS import *
from CLASS import *

print(f"From BSECE 1-5; Made by:"
      f"\n LOBERIANO, CLYDE ETHAN"
      f"\n REDOBLADO, NICOLE")
print(f"This is a series and parallel circuit calculator. "
      f"\nIt calculates the total and individual voltage, current, and resistance of the circuit.")

print("Please input the values being asked. Type ANY WORD if the value is unknown.")
completed = False

while completed == False:
        type = input("Type of circuit: SERIES or PARALLEL: ")

        if type == "SERIES":
            circuit1 = Series(
                input("Circuit Name: "),
                input("Total Resistance: "),
                input("Total Voltage: "),
                input("Total Current: ")
            )

            series_individual_resistances = input("Insert the individual resistances. Separate using space: ")

            series_individual_voltages = input("Insert the individual voltages. Separate using space: ")

            series_individual_currents = input("Insert the individual currents. Separate using space: ")

            try:
                circuit1.series_total_resistance = float(circuit1.series_total_resistance)
            except ValueError:
                circuit1.series_total_resistance = "null"

            try:
                circuit1.series_total_voltage = float(circuit1.series_total_voltage)
            except ValueError:
                circuit1.series_total_voltage = "null"

            try:
                circuit1.series_total_current = float(circuit1.series_total_current)
            except ValueError:
                circuit1.series_total_current = "null"

            try:
                series_individual_resistances = series_individual_resistances.split()
                series_individual_resistances = [float(inr) for inr in series_individual_resistances]
            except:
                series_individual_resistances = "null"

            try:
                series_individual_voltages = series_individual_voltages.split()
                series_individual_voltages = [float(inv) for inv in series_individual_voltages]
            except:
                series_individual_voltages = "null"

            try:
                series_individual_currents = series_individual_currents.split()
                series_individual_currents = [float(inc) for inc in series_individual_currents]
            except:
                series_individual_currents = "null"

        # These try and except functions are meant to check the data type of the inputted values by converting them into floats.
        # If the inputted values fail to be converted, they will be branded as missing and will be named "null".
            if (circuit1.series_total_resistance != "null" and circuit1.series_total_voltage != "null" and circuit1.series_total_current != "null"
                    and series_individual_resistances != "null" and series_individual_voltages != "null" and series_individual_currents != "null"):
                print("Hmmm, there seems to be no missing values from your circuit. Only use this program if at least one value is missing.")
                completed = True
        # If no inputted values are missing, prints the text above.

            else:
                loop_count = 0 # Counts the number of loops of the while loop below.
                while (circuit1.series_total_resistance == "null" or circuit1.series_total_voltage == "null" or circuit1.series_total_current == "null"
                       or series_individual_resistances == "null" or series_individual_voltages == "null" or series_individual_currents == "null"):
                    # This while loop checks if any of the inputted values are missing.
                    if circuit1.series_total_resistance == "null": # If the total resistance is missing,
                        series_total_resistance = circuit1.formula_series_total_resistance() # Tries R = V/I first,
                        if series_total_resistance == "null":
                            series_total_resistance = rts(series_individual_resistances) # Then, it tries Rt = summation of all resistances.
                        if series_total_resistance == "null":
                            series_total_resistance = "null"
                            # If both functions above failed to find the value, the missing value will remain missing and still named "null".
                        if series_total_resistance != "null":
                            circuit1.series_total_resistance = series_total_resistance
                        # Otherwise, the computed value will replace the missing value.

                    if circuit1.series_total_resistance != "null":
                        # If the total resistance is not missing, the total resistance in the class will used as the variable for the functions.
                        series_total_resistance = circuit1.series_total_resistance
                        # This process will repeat for the total voltage and the total current.

                    if circuit1.series_total_voltage == "null":
                        series_total_voltage = circuit1.formula_series_total_voltage()
                        if series_total_voltage == "null":
                            series_total_voltage = vts(series_individual_voltages)
                        if series_total_voltage == "null":
                            series_total_voltage = "null"
                        if series_total_voltage != "null":
                            circuit1.series_total_voltage = series_total_voltage

                    if circuit1.series_total_voltage != "null":
                        series_total_voltage = circuit1.series_total_voltage

                    if circuit1.series_total_current == "null":
                        series_total_current = circuit1.formula_series_total_current()
                        if series_total_current == "null":
                            series_total_current = cts(series_individual_currents)
                        if series_total_current == "null":
                            series_total_current = "null"
                        if series_total_current != "null":
                            circuit1.series_total_current = series_total_current

                    if circuit1.series_total_current != "null":
                        series_total_current = circuit1.series_total_current

                    if series_individual_resistances != "null":
                        num_of_resistors = len(series_individual_resistances)
                    if series_individual_voltages != "null":
                        num_of_resistors = len(series_individual_voltages)
                    if series_individual_currents != "null":
                        num_of_resistors = len(series_individual_currents)
                    if series_individual_resistances == "null" and series_individual_voltages == "null" and series_individual_currents == "null":
                        num_of_resistors = 1
                        # Determines the number of resistors, useful for the calculations of the individual R, V, and C.

                    if series_individual_resistances == "null": # If the individual resistances are missing,
                        series_individual_resistances = ris(series_individual_voltages, series_individual_currents) # Tries Rn = Vn/In,
                    if series_individual_resistances == "null":
                        series_individual_resistances = ris2(series_individual_voltages, series_total_resistance, series_total_voltage)
                        #Then, tries to use a derived formula of the voltage divider,
                    if series_individual_resistances == "null":
                        series_individual_resistances = "null" # If it remains unsolved, it will remain missing.
                    # The process above is also repeated for the calculations of the individual voltages and currents.
                    if series_individual_voltages == "null":
                        series_individual_voltages = vis(series_individual_resistances, series_total_voltage)
                    if series_individual_voltages == "null":
                        series_individual_voltages = vis2(series_individual_resistances, series_individual_currents)
                    if series_individual_voltages == "null":
                        series_individual_voltages = "null"
                    if series_individual_currents == "null":
                        series_individual_currents = cis(series_total_current, num_of_resistors)
                    if series_individual_currents == "null":
                        series_individual_currents = cis2(series_individual_voltages, series_individual_resistances)
                    if series_individual_currents == "null":
                        series_individual_currents = "null"

                    if loop_count == 5:
                        break
                    # This statement breaks the while loop if it has looped for too long, usually because of the lack of data for the computation.

                    if (circuit1.series_total_resistance == "null" or circuit1.series_total_voltage == "null" or circuit1.series_total_current == "null"
                            or series_individual_resistances == "null" or series_individual_voltages == "null" or series_individual_currents == "null"):
                        loop_count += 1
                        continue
                    # This statement determines if any of the missing values remains missing and uncalculated after 1 loop. If there are still any missing values,
                    # the code starts from the top to calculate again for the missing value using new calculated values obtained from the other functions.
                    if (circuit1.series_total_resistance != "null" and circuit1.series_total_voltage != "null" and circuit1.series_total_current != "null"
                            and series_individual_resistances != "null" and series_individual_voltages != "null" and series_individual_currents != "null"):
                        break
                    # This statement breaks the loop if all values are computed and accounted for.

                if loop_count == 5:
                    print("Insufficient data are given for computation.")
                    # This indicates that the inputted values are not enough to find the complete values.
                    completed = False
                else:
                    print("Circuit name: ", circuit1.circuitname)
                    print("Total Resistance: ", circuit1.series_total_resistance, " Ohms")
                    print("Total Voltage: ", circuit1.series_total_voltage, " Volts")
                    print("Total Current: ", circuit1.series_total_current, " Amperes")
                    # Prints the values.


                    try:
                        series_individual_resistances = [float(inr) for inr in series_individual_resistances]
                        #Checks if there are still any missing values after the while loop.
                        series_individual_resistances_print = []
                        for indrs in series_individual_resistances:
                            series_individual_resistances_print.append(str(indrs) + " Ohms")
                            # Adds the proper unit for the computed values.
                        if checker(series_total_resistance, series_individual_resistances) == "pog":
                            # Checks if the total and individual values match up.
                            print("Individual Resistances: ", series_individual_resistances_print)
                            completed = True
                        else:
                            print("Your given total and individual resistances doesn't seem to match up. "
                                  "\nPlease recheck your given so that the total "
                                  "number of resistors matches with the total of each individual values. ")
                            completed = False
                    except:
                        print("The data inputted is insufficient to conduct calculations for the individual resistances.")
                        completed = False
                    # The process above remains the same for the Voltages and Currents.


                    try:
                        if cts(series_individual_currents) == series_total_current:
                            series_individual_currents = [float(inc) for inc in series_individual_currents]
                            series_individual_currents_print = []
                            for indcs in series_individual_currents:
                                series_individual_currents_print.append(str(indcs) + " Amperes")
                            print("Individual Currents: ", series_individual_currents_print)
                            completed = True
                        elif cts(series_individual_currents) == "bruh":
                            # This is a special statement for the currents in a series circuit.
                            # Since the individual and total currents of a series circuit are constant, the block of code below
                            # checks if the inputted and calculated total and individual currents are the same.
                            series_individual_currents_real = cis(series_total_current, num_of_resistors)
                            series_individual_currents_real = [float(inc) for inc in series_individual_currents_real]
                            series_individual_currents_real_print = []
                            for indcs in series_individual_currents_real:
                                series_individual_currents_real_print.append(str(indcs) + " Amperes")
                            print("Please make sure that the individual resistances of a series circuit is constant.",
                                  f"\nSince the total current of the series circuit has already been solved, "
                                  f"the individual currents of {circuit1.circuitname} are: ",
                                  f'\n{series_individual_currents_real_print}')
                            completed = False
                            # This special print function prints the individual currents if they are not constant.
                    except:
                        print("The data inputted is insufficient to conduct calculations for the individual currents.")
                        completed = False

                    try:
                        series_individual_voltages = [float(inc) for inc in series_individual_voltages]
                        # This is similar to checking for the resistances.
                        series_individual_voltages_print = []
                        for indvs in series_individual_voltages:
                            series_individual_voltages_print.append(str(indvs) + " Volts")
                        if checker(series_total_voltage, series_individual_voltages) == "pog":
                            print("Individual Voltages: ", series_individual_voltages_print)
                            completed = True
                        else:
                            print("Your given total and individual voltages doesn't seem to match up.")
                            completed = False
                    except:
                        print("The data inputted is insufficient to conduct calculations for the individual currents.")
                        completed = False

    # The functions above are repeated for the parallel circuit only differing in the formulas used.

        elif type == "PARALLEL":
            circuit2 = Parallel(
                input("Circuit Name: "),
                input("Total Resistance: "),
                input("Total Voltage: "),
                input("Total Current: ")
            )

            parallel_individual_resistances = input("Insert the individual resistances. Separate using space: ")

            parallel_individual_voltages = input("Insert the individual voltages. Separate using space: ")

            parallel_individual_currents = input("Insert the individual currents. Separate using space: ")

            try:
                circuit2.parallel_total_resistance = float(circuit2.parallel_total_resistance)
            except ValueError:
                circuit2.parallel_total_resistance = "null"

            try:
                circuit2.parallel_total_voltage = float(circuit2.parallel_total_voltage)
            except ValueError:
                circuit2.parallel_total_voltage = "null"

            try:
                circuit2.parallel_total_current = float(circuit2.parallel_total_current)
            except ValueError:
                circuit2.parallel_total_current = "null"

            try:
                parallel_individual_resistances = parallel_individual_resistances.split()
                parallel_individual_resistances = [float(inr) for inr in parallel_individual_resistances]
            except:
                parallel_individual_resistances = "null"

            try:
                parallel_individual_voltages = parallel_individual_voltages.split()
                parallel_individual_voltages = [float(inv) for inv in parallel_individual_voltages]
            except:
                parallel_individual_voltages = "null"

            try:
                parallel_individual_currents = parallel_individual_currents.split()
                parallel_individual_currents = [float(inc) for inc in parallel_individual_currents]
            except:
                parallel_individual_currents = "null"

            if (circuit2.parallel_total_resistance != "null" and circuit2.parallel_total_voltage != "null" and
                    circuit2.parallel_total_current != "null" and parallel_individual_resistances != "null" and
                    parallel_individual_voltages != "null" and parallel_individual_currents != "null"):
                print("Hmmm, there seems to be no missing values from your circuit. "
                      "Only use this program if at least one value is missing.")
                completed == True

            else:
                loop_count = 0
                while (circuit2.parallel_total_resistance == "null" or circuit2.parallel_total_voltage == "null" or
                       circuit2.parallel_total_current == "null" or parallel_individual_resistances == "null" or
                       parallel_individual_voltages == "null" or parallel_individual_currents == "null"):
                    if circuit2.parallel_total_resistance == "null":
                        parallel_total_resistance = circuit2.formula_parallel_total_resistance()
                        if parallel_total_resistance == "null":
                            parallel_total_resistance = rtr(parallel_individual_resistances)
                        if parallel_total_resistance == "null":
                            parallel_total_resistance = "null"
                        if parallel_total_resistance != "null":
                            circuit2.parallel_total_resistance = parallel_total_resistance

                    if circuit2.parallel_total_resistance != "null":
                        parallel_total_resistance = circuit2.parallel_total_resistance

                    if circuit2.parallel_total_voltage == "null":
                        parallel_total_voltage = circuit2.formula_parallel_total_voltage()
                        if parallel_total_voltage == "null":
                            parallel_total_voltage = vtr(parallel_individual_voltages)
                        if parallel_total_voltage == "null":
                            parallel_total_voltage = "null"
                        if parallel_total_voltage != "null":
                            circuit2.parallel_total_voltage = parallel_total_voltage

                    if circuit2.parallel_total_voltage != "null":
                        parallel_total_voltage = circuit2.parallel_total_voltage

                    if circuit2.parallel_total_current == "null":
                        parallel_total_current = circuit2.formula_parallel_total_current()
                        if parallel_total_current == "null":
                            parallel_total_current = ctr(parallel_individual_currents)
                        if parallel_total_current == "null":
                            parallel_total_current = "null"
                        if parallel_total_current != "null":
                            circuit2.parallel_total_current = parallel_total_current

                    if circuit2.parallel_total_current != "null":
                        parallel_total_current = circuit2.parallel_total_current

                    if parallel_individual_resistances != "null":
                        num_of_resistors = len(parallel_individual_resistances)
                    if parallel_individual_voltages != "null":
                        num_of_resistors = len(parallel_individual_voltages)
                    if parallel_individual_currents != "null":
                        num_of_resistors = len(parallel_individual_currents)
                    if parallel_individual_resistances == "null" and parallel_individual_voltages == "null" and parallel_individual_currents == "null":
                        num_of_resistors = 1

                    if parallel_individual_resistances == "null":
                        parallel_individual_resistances = rir(parallel_individual_voltages, parallel_individual_currents)
                    if parallel_individual_resistances == "null":
                        parallel_individual_resistances = rir2(parallel_individual_voltages, parallel_total_resistance,
                                                               parallel_total_voltage)
                    if parallel_individual_resistances == "null":
                        parallel_individual_resistances = "null"
                    if parallel_individual_voltages == "null":
                        parallel_individual_voltages = vir(parallel_total_voltage, num_of_resistors)
                    if parallel_individual_voltages == "null":
                        parallel_individual_voltages = vir2(parallel_individual_currents, parallel_individual_resistances)
                    if parallel_individual_voltages == "null":
                        parallel_individual_voltages = "null"
                    if parallel_individual_currents == "null":
                        parallel_individual_currents = cir(parallel_individual_resistances, parallel_total_current)
                    if parallel_individual_currents == "null":
                        parallel_individual_currents = cir2(parallel_individual_resistances, parallel_individual_voltages)
                    if parallel_individual_currents == "null":
                        parallel_individual_currents = "null"

                    if loop_count == 5:
                        break

                    if (circuit2.parallel_total_resistance == "null" or circuit2.parallel_total_voltage == "null" or
                            circuit2.parallel_total_current == "null" or parallel_individual_resistances == "null" or
                            parallel_individual_voltages == "null" or parallel_individual_currents == "null"):
                        loop_count += 1
                        continue
                    if (circuit2.parallel_total_resistance != "null" and circuit2.parallel_total_voltage != "null" and
                            circuit2.parallel_total_current != "null" and parallel_individual_resistances != "null" and
                            parallel_individual_voltages != "null" and parallel_individual_currents != "null"):
                        break

                if loop_count == 5:
                    print("Insufficient data are given for computation.")
                    completed = False
                else:
                    print("Circuit name: ", circuit2.circuitname)
                    print("Total Resistance: ", circuit2.parallel_total_resistance, " Ohms")
                    print("Total Voltage: ", circuit2.parallel_total_voltage, " Volts")
                    print("Total Current: ", circuit2.parallel_total_current, " Amperes")
                    completed = True

                    try:
                        parallel_individual_resistances = [float(inr) for inr in parallel_individual_resistances]
                        parallel_individual_resistances_print = []
                        for indrs in parallel_individual_resistances:
                            parallel_individual_resistances_print.append(str(indrs) + " Ohms")
                        if checker_res(parallel_total_resistance, parallel_individual_resistances) == "pog":
                            print("Individual Resistances: ", parallel_individual_resistances_print)
                            completed = True
                        else:
                            print(
                                "Your given total and individual resistances doesn't seem to match up. \nPlease recheck "
                                "your given so that the total number of resistors matches with the total of each individual values. ")
                            completed = False
                    except:
                        print("The data inputted is insufficient to conduct calculations for the individual resistances.")
                        completed = False

                    try:
                        if vtr(parallel_individual_voltages) == parallel_total_voltage:
                            parallel_individual_voltages = [float(inc) for inc in parallel_individual_voltages]
                            parallel_individual_voltages_print = []
                            for indvs in parallel_individual_voltages:
                                parallel_individual_voltages_print.append(str(indvs) + " Volts")
                            print("Individual Voltages: ", parallel_individual_voltages_print)
                            completed = True
                        elif vtr(parallel_individual_voltages) == "bruh":
                            parallel_individual_voltages_real = vir(parallel_total_voltage, num_of_resistors)
                            parallel_individual_voltages_real = [float(inc) for inc in parallel_individual_voltages_real]
                            parallel_individual_voltages_real_print = []
                            for indvs in parallel_individual_voltages_real:
                                parallel_individual_voltages_real_print.append(str(indvs) + " Volts")
                            print("Please make sure that the individual voltages of a parallel circuit is constant.",
                                  f"\nSince the total current of the parallel circuit has already been solved, the individual voltages of {circuit2.circuitname} are: ",
                                  f'\n{parallel_individual_voltages_real_print}')
                            completed = False
                    except:
                        print("The data inputted is insufficient to conduct calculations for the individual voltages.")
                        completed = False

                    try:
                        parallel_individual_currents = [float(inc) for inc in parallel_individual_currents]
                        parallel_individual_currents_print = []
                        for indcs in parallel_individual_currents:
                            parallel_individual_currents_print.append(str(indcs) + " Amperes")
                        if checker(parallel_total_current, parallel_individual_currents) == "pog":
                            print("Individual Currents: ", parallel_individual_currents_print)
                            completed = True

                        else:
                            print("Your given total and individual currents doesn't seem to match up with the given total current.")
                            completed = False

                    except:
                        print("The data inputted is insufficient to conduct calculations for the individual currents.")
                        completed = False

        if type != "SERIES" and type != "PARALLEL":
            print("Please make sure that SERIES or PARALLEL are all capitalized and spelled correctly.")
            # Prints if user failed to type SERIES or PARALLEL correctly.
            completed = False

        tryagain = input("Do you want to calculate again? YES or NO: ")

        if completed == False:
            try:
                if tryagain == "YES" or tryagain.lower() == "yes":
                    continue
                elif tryagain == "NO" or tryagain.lower() == "no":
                    break
                else:
                    print("Try typing properly.")
                    break
            except ValueError:
                print("Try typing properly.")
                break
        elif completed == True:
            print("Process Complete...")
            try:
                if tryagain == "YES" or tryagain.lower() == "yes":
                    completed = False
                    continue
                elif tryagain == "NO" or tryagain.lower() == "no":
                    break
                else:
                    print("Try typing properly.")
                    break
            except ValueError:
                print("Try typing properly.")
                break