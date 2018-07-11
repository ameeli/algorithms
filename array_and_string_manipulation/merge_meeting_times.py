def merge_ranges(meetings):
    """Merge meeting ranges"""
    meetings.sort()
    all_meetings = [meetings[0]]
    
    for start, end in meetings:
        if start - all_meetings[-1][1] < 1: 
            if end > all_meetings[-1][1]:
                all_meetings[-1] = (all_meetings[-1][0], end)
        else:
            all_meetings.append((start, end))

    return all_meetings
