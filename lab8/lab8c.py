# Write your code for lab 8C (remove) here.
from cal_ui import *

def cd_remove_appointment(day: CalendarDay, start_time: Time):
    """ 
    Returns a list of all the appointments NOT starting
    at the given time 
    """
    ensure_type(day, CalendarDay)
    ensure_type(start_time, Time)
    
    appointments = []

    if cd_is_empty(day):
        print("There was no appointment at the given day")
        return []

    else:
        for appointment in cd_iter_appointments(day):
            if start_time != ts_start(app_span(appointment)):
                appointments.append(appointment)
           
    print("Appointment has been removed.")
    return appointments


def remove(cal_name: str, day: int, month: str, time: str):
    """ 
    Creats a copy of the calendar year with 
    the right appointments removed
    """
    day = new_day(day)
    month = new_month(month)
    time = new_time_from_string(time)

    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(month, cal_year)
    cal_day = cm_get_day(cal_month, day)

    new_date(day, month)

    new_cal_day = new_calendar_day(day, cd_remove_appointment(cal_day, time))
    new_cal_month = cm_plus_cd(cal_month, new_cal_day)
    new_cal_year = cy_plus_cm(cal_year, new_cal_month)

    insert_calendar(cal_name, new_cal_year)


if __name__ == "__main__":

    create("Bob")
    book("Bob", 22, "sep", "12:00", "13:00", "Lunch")
    book("Bob", 22, "sep", "10:00", "12:00", "Business Meeting")
    book("Bob", 10, "nov", "09:00", "15:00", "Business Conference")
    book("Bob", 10, "nov", "19:00", "22:00", "Dinner with wife")

    def test_remove_from_existing_day():
        remove("Bob", 22, 'sep', "12:00")
        remove("Bob", 10, 'nov', "09:00")

        show("Bob", 22, "sep")
        show("Bob", 10, "nov")
    
    def test_remove_from_nonexisting_app():
        remove("Bob", 22, 'sep', "13:00")
        remove("Bob", 10, 'nov', "23:00")
        remove("Bob", 10, 'nov', "12:00")

        remove("Bob", 15, "jan", "14:00")
        remove("Bob", 30, "apr", "22:00")

        show("Bob", 22, "sep")
        show("Bob", 10, "nov")
    
    def test_edge_cases():
        remove("David", 22, "sep", "10:00") # Should raise a ValueError
        remove("Bob", 10, "nov", "25:00")   # Should raise an AssertionError
        remove("Bob", 35, "dec", "10:00")   # Should raise an AssertionError

        show("Bob", 22, "sep")
        show("Bob", 10, "nov")
    

    #test_remove_from_existing_day()
    #test_remove_from_nonexisting_app()
    test_edge_cases()

    