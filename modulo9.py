def informes(tanque1, tanque2, tanque3):
    promedio = (int(tanque1) + int(tanque2) + int(tanque3)) / 2
    print(f""" reporte:
    promedio {str(promedio)}%
    tanque 1 {str(tanque1)}%
    tanque 2 {str(tanque2)}%
    tanque 3 {str(tanque3)}%
    """)

informes(14,15,16)

def reporteDeMision(pre_launch_time, flight_time, destination, external_tank, main_tank):
    return f"""
    Mission to {destination}
    Total travel time: {pre_launch_time + flight_time} minutes
    Total fuel left: {external_tank + main_tank} gallons
    """

def mission_report(destination, *minutes, **fuel_reservoirs):
    return f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """

print(mission_report("Moon", 10, 15, 51, main=300000, external=200000))

def mission_report2(destination, *minutes, **fuel_reservoirs):
    main_report = f"""
    Mission to {destination}
    Total travel time: {sum(minutes)} minutes
    Total fuel left: {sum(fuel_reservoirs.values())}
    """
    for tank_name, gallons in fuel_reservoirs.items():
        main_report += f"{tank_name} tank --> {gallons} gallons left\n"
    return main_report

print(mission_report("Moon", 8, 11, 55, main=300000, external=200000))

print(reporteDeMision(14, 51, "Moon", 200000, 300000))

