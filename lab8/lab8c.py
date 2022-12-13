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
        print("There was no appointment at the given time")
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

    create("Jayne")
    book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
    book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")

    remove("Jayne", 20, "sep", "15:00")
    book("Jayne", 20, "sep", "15:00", "16:00", "Return loot")
    show("Jayne", 20, "sep")

    remove("Jayne", 20, "sep", "09:00")
    show("Jayne", 20, "sep")
    remove("Jayne", 21, "aug", "13:00")