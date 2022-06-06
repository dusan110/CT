def merge_intervals(intervals):
    """
    Merges the intervals in a set if they intersect eachother and create a union from those intervals.

    Args:
        intervals : the intervals in the set

    Returns:
        all_merged_intervals: A list with unified intervals
    """
        
    # Sorting the collection of intervals such that the intervals with the lowest start value come first
    # Now I know that the leftmost intervals always have the lowest values
    intervals.sort(key = lambda elem: elem[0])
        
    # Merge part
    # Based on the examples I am assuming that we are only dealing with integers from the whole or natural number domain
    all_merged_intervals = []
    start_value = -1  #starting value of the interval
    end_value = -1    #end value of the interval

    # Traverse the intervals
    for interval in range(len(intervals)):
        current_interval = intervals[interval]
        
        # Check if there is no overlap
        # If the current_intervals start-point is past the end-point of the previous interval we know that they do not intersect.
        if current_interval[0] > end_value:
            
            # If this is not the first interval we have found a new merged interval so we append it to the list
            if interval != 0:
                all_merged_intervals.append([start_value,end_value])
            
            # Update values
            end_value = current_interval[1]
            start_value = current_interval[0]
        
        # Intervals intersect
        else:
            
            # Update the end point if the current interval has a bigger end point than the previous one. 
            if current_interval[1] >= end_value:
                end_value = current_interval[1]

    # Add the last merged interval after all the intervals have been traversed
    if end_value != -1 and [start_value, end_value] not in all_merged_intervals:
        all_merged_intervals.append([start_value, end_value])
    
    return all_merged_intervals




def find_intersection(inc_interval, ex_interval):
    """
    Finds the intersection between the inc_interval and the ex_interval, so
    that the different ranges may be determined. There are different kinds of formations based on the
    start and stop value of each interval. These values will create new intervals.

    Ther has to be a better way to do this.

    Args:
        inc_interval : Contains the inclusive interval, i.e the interval that we want to keep
        ex_interval : Contains the excludiong interval, i.e the interval that needs to be removed 

    Returns:
        All of the new intervals
    """

    new_intervals = []

    # X'start_value are inc_intervals, O'start_value are ex_intervals

    #  X O X O formation
    if inc_interval[0] <= ex_interval[0] and  inc_interval[1] >= ex_interval[0] and ex_interval[1] >= inc_interval[1]:
        new_intervals.append((inc_interval[0], ex_interval[0] - 1))

    # O X O X formation
    elif ex_interval[0] <= inc_interval[0] and  ex_interval[1] >= inc_interval[0] and inc_interval[1] >= ex_interval[1]:
        new_intervals.append((ex_interval[1] + 1, inc_interval[1]))

    # X O O X formation
    elif inc_interval[0] <= ex_interval[0] and  ex_interval[1] <= inc_interval[1]:
        new_intervals.append((inc_interval[0], ex_interval[0] - 1))
        new_intervals.append((ex_interval[1] + 1, inc_interval[1]))
    
    # O X X O formation
    elif ex_interval[0] <= inc_interval[0] <= ex_interval[1] and ex_interval[0] <= inc_interval[1] <= ex_interval[1]:
        return new_intervals #empty
    
    return new_intervals




def my_non_overlapping_sorting_interval_program(include, exclude):
    """
    This program outputa the result of taking all the includes (intervals in include) and “remove” the excludes (intervals in the exclude).
    Returns a list of non-overlapping intervals in a sorted order.

    Maybe I can use an Interval search tree to solve it next time.
    """

    #Merge the intervals. We can also return here if there are no excluding intervals
    m_include = merge_intervals(list(include))
    if len(exclude) == 0:
        return m_include
    m_exclude = merge_intervals(list(exclude))
    
    # Compute and find all intervals
    res = []

    for inclusive_interval in m_include:
        for excluding_interval in m_exclude:
            res.extend(find_intersection(inclusive_interval, excluding_interval))

    return res





if __name__ == "__main__":
    Include1 = {(10,100)}
    Exclude1 = {(20,30)}

    Include2 = {(50,5000), (10,100)}
    Exclude2 = {} #empty

    Include3 = {(10,100), (200,300)}
    Exclude3 = {(95,205)}

    Include4 = {(10,100), (200,300), (400,500)}
    Exclude4 = {(95,205), (410,420)}

    Include5 = {(5,13), (2,8)}
    Exclude5 = {(4,10), (5,11)}

    Include6 = {(5,100000000)}
    Exclude6 = {(4,5)}

    print(my_non_overlapping_sorting_interval_program(Include1, Exclude1))
    print(my_non_overlapping_sorting_interval_program(Include2, Exclude2))
    print(my_non_overlapping_sorting_interval_program(Include3, Exclude3))
    print(my_non_overlapping_sorting_interval_program(Include4, Exclude4))
    print(my_non_overlapping_sorting_interval_program(Include5, Exclude5))
    print(my_non_overlapping_sorting_interval_program(Include6, Exclude6)) 
