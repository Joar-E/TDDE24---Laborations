from cal_abstraction import *
from cal_output import *
# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
TimeSpanSeq = NamedTuple("TimeSpanSeq", [("timespans", TimeSpan)])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(timespans: TimeSpan = None):
    """ Returns a new TimeSpanSeq but if no argument is givin 
        it returns an empty list
    """
    if timespans is None:
        timespans = []
    else:
        ensure_type(timespans, List[TimeSpan])
    return TimeSpanSeq(timespans)


def tss_is_empty(tss: TimeSpanSeq) -> bool:
    """ Returns True if tss is empty"""
    ensure_type(tss, TimeSpanSeq)
    return not tss.timespans


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan):
    """ Creates a copy of the given TimeSpanSeq and returns it 
        with the added timepan"""
    ensure_type(tss, TimeSpanSeq)
    ensure_type(ts, TimeSpan)

    def add_ts(tss: TimeSpanSeq, ts: TimeSpan):
        """ If the given timespan precedes the earliest timespan in the tss
            it is placed in the first position of the tss 
        """
        if not tss or tss_is_empty(tss) or time_precedes(
            ts_start(ts), ts_start(tss.timespans[0])):

            return [ts] + tss.timespans #tss.timespans == tss[0] 
 
        else:
            # tss.timespans[0] == tss[0][0]
            """ Otherwise it is pu through the same function again but with the rest of
                the tss
            """
            return [tss.timespans[0]] + add_ts(new_time_span_seq(tss.timespans[1:]), ts)

    return new_time_span_seq(add_ts(tss, ts))


def tss_iter_spans(tss: TimeSpanSeq):
    """ Iterates through the tss"""
    ensure_type(tss, TimeSpanSeq)
    for timespan in tss.timespans:
        yield timespan


def show_time_spans(tss: TimeSpanSeq):
    """ Iterates through the tss and shows all the TimeSpans """
    for timespan in tss.timespans: #tss_iter_spans(tss):
        show_ts(timespan)
        print()


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result

min1 = 90
min2 = 120

minmid = 120

min3 = 300
min4 = 400


time = new_time_span(Time(Hour(min1 // 60), Minute(min1 % 60)), Time(Hour(min2 // 60), Minute(min2 % 60)))

time2 = new_time_span(Time(Hour(min3 // 60), Minute(min3 % 60)), Time(Hour(min4 // 60), Minute(min4 % 60)))

time3= new_time_span(Time(Hour(minmid // 60), Minute(minmid % 60)), Time(Hour(min4 // 60), Minute(min4 % 60)))
timespanseq = new_time_span_seq()

hej = tss_plus_span(timespanseq, time2)

hej2 = tss_plus_span(hej, time)

hej3 = tss_plus_span(hej2, time3)
show_time_spans(hej3)