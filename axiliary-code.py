import datetime


def today_date(with_time=True):
    """
    Today date in text format.

    The function returns a current calendar day as a string to print out or to attach.
    It requires to import datetime, preferably in global environment.
    Otherwise, the function does not need anything else.

    Parameters
    ----------
    No parameters.

    Returns
    -------
    TYPE: str
        DESCRIPTION: a current calendar day in format Year.month.day, all as
        numbers and separated by dots. A day time can be added, then the date numbers
        are separated by slashes and time follows after a space.
    """
    if with_time:
        return datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    else:
        return datetime.datetime.now().strftime("%Y.%m.%d")

def exe_time(start_time):
    """
    Compute CPU time in minutes and create a message to print out.

    The function returns elapsed execution time in minutes given time
    of the execution start in datetime.datetime format.
    In additon it outputs a message which can be printed out.
    
    Parameters
    ----------
    start_time : datetime.datetime module format
        DESCRIPTION: A beginning moment to compute time difference between
        initial time and now.

    Returns
    -------
    Elapsed time, message to print

    """
    spent = (datetime.datetime.now() - start_time).seconds
    loop_message = "Elapsed time in minutes from the start: " +\
        str(round(spent/60, 1))
    return spent, loop_message


def approx_finish_time(start_time, iteration_count, iteration_indx):
    """
    Approximate finish time.

    The function prints an estimated finish time based at the execution start
    time, number of repetitions (loops, iterations) and a current repetition
    index. Note that iterations are enumerated from 1. 

    Parameters
    ----------
    start_time : datetime.datetime module format
        DESCRIPTION: A start time before iterations, or a loop.

    loop_runs : integer
        DESCRIPTION: A total number of repetitions (iterations).

    current_loop_n : TYPE
        DESCRIPTION: A current executed number of repetitions/iterations) 
        to approximate an execution termination. Remember that Python counts 
        from 0, so if you go with a standard Python loop enumeration add 1 
        to the value when you apply the function.

    Returns
    -------
    None.

    """
    spent = (datetime.datetime.now() - start_time).seconds
    est_elapsed = iteration_count * spent / iteration_indx
    estimated_end = start_time + datetime.timedelta(seconds=est_elapsed)
    print("Estimated time to finish is around " +
          estimated_end.strftime("%m/%d/%Y, %H:%M"))


def write_dfs_to_excel(excel_file_name, df_dict):
    """
    Write data frames in provided dictionary into Excel Workbook.

    The function accepts an Excel file name (without an extension) and a 
    dictionary of Pandas data frames with keys as Excel Worksheet names and 
    values as data frames. It writes an Excel file to a current working
    directory with tables and their corresponding sheet names. 

    Parameters
    ----------
    excel_file_name : str
        DESCRIPTION: a name for a future Excel file without Excel extension.
        If a file under such name already exists, it will be overwritten.
    df_list : dictionary
        DESCRIPTION: The dictionary should have the following structure:
            its values are data frames, and corresponding keys must be proposed
            Excel sheet names.

    Returns
    -------
    None

    """

    excel_file_name = excel_file_name + '.xlsx'
    with pd.ExcelWriter(excel_file_name) as writer:
        for sheet_name, data_frame in df_dict.items():
            data_frame.to_excel(writer, sheet_name=sheet_name)

