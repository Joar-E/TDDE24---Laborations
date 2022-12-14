# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from settings import CHECK_AGAINST_FACIT

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


def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    time_spans_seq = new_time_span_seq()

    for appointment in cd_iter_appointments(cal_day):
        tss_plus_span(time_spans_seq, app_span(appointment))
    
    

