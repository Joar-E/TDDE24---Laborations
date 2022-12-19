# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from settings import CHECK_AGAINST_FACIT
from cal_ui import *

if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *


def show_free(cal_name: str, day: int, month: str, start: str, end: str):
    """
    Makes a copy of the given day and shows all available time
    """
    day = new_day(day)
    month = new_month(month)
    start_time = new_time_from_string(start)
    end_time = new_time_from_string(end)

    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(month, cal_year)
    cal_day = cm_get_day(cal_month, day)

    if cd_is_empty(cal_day):
        print("There are no appointments booked for this day")
    
    show_time_spans(free_spans(cal_day, start_time, end_time))



def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    """
    Returns a TimeSpanSeq with all non-booked timespans during the given
    interval
    """
    app_spans_seq = new_time_span_seq()

    for appointment in cd_iter_appointments(cal_day):
        app_spans_seq = tss_plus_span(app_spans_seq, app_span(appointment))
    
    free_time = new_time_span_seq()
    starting_point = start

    for ts in tss_iter_spans(app_spans_seq):
        time_span_start = ts_start(ts)
        time_span_end = ts_end(ts)

        if time_precedes_or_equals(time_span_start, starting_point):
            # The timespan is out of the time interval
            if time_precedes(time_span_end, starting_point):
                continue
            # The end of timespan is within the interval 
            if time_precedes_or_equals(time_span_end, end):
                starting_point = time_span_end
                pass
            # The timespan is longer than the interval
            if time_precedes_or_equals(end, time_span_end):
                starting_point = time_span_end
                break
            # if time_precedes_or_equals(starting_point, time_span_end):
            #     starting_point = time_span_end
            #     pass
        
        elif time_precedes(starting_point, time_span_start):
            if time_precedes_or_equals(end, time_span_start):
                free_time = tss_plus_span(free_time, new_time_span(starting_point, end))
                starting_point = time_span_end
                break
            if time_precedes_or_equals(end, time_span_end):
                free_time =tss_plus_span(free_time, new_time_span(starting_point, time_span_start))
                starting_point = time_span_end
                break
            if time_precedes(time_span_end, end):
                free_time =tss_plus_span(free_time, new_time_span(starting_point, time_span_start))
                starting_point = time_span_end
                pass
    

    if time_precedes(starting_point, end):
        free_time = tss_plus_span(free_time, new_time_span(starting_point, end))
    
    return free_time



    
    

