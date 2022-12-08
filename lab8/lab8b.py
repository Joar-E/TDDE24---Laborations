from cal_abstraction import *
from cal_output import *
# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
TimeSpanSeq = NamedTuple("TimeSpanSeq", [("timespans", List[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(timespans: List[TimeSpan] = None):
    if timespans is None:
        timespans = []
    else:
        ensure_type(timespans, List[TimeSpan])
    return TimeSpanSeq(timespans)


def tss_is_empty(tss: TimeSpanSeq):
    ensure_type(tss, TimeSpanSeq)
    return not tss.timespans


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan):

    ensure_type(tss, TimeSpanSeq)
    ensure_type(ts, TimeSpan)

    def add_ts(tss, ts):
        if not tss or isinstance(tss, TimeSpanSeq) and tss_is_empty(tss): #time_precedes(#ts_start(app_span(app)), ts_start(app_span(appointments[0])):
            return [ts]
        
        elif time_precedes(ts_start(ts), ts_start(tss[0][0])):
            print("jgfhdjhgdfhbjhfdbvhfdhvhdhbhvdfbh")        
            return [ts] + tss[0]
        else:
            print("hej")
            print(tss)
            print(tss[0][0])
            print(tss[1:])
            return tss[0] + add_ts(tss[1:], ts)

    return new_time_span_seq(add_ts(tss, ts))
    # if tss_is_empty(tss):
    #     return [ts]

    # elif time_precedes(ts_start(ts), ts_start(tss_iter_spans(tss))):
    #     return TimeSpanSeq

    # else:
    #     position += 1

def tss_iter_spans(tss: TimeSpanSeq):
    ensure_type(tss, TimeSpanSeq)
    for timespan in TimeSpanSeq.timespans:
        yield timespan


def show_time_spans(tss: TimeSpanSeq):
    for timespan in tss.timespans:
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