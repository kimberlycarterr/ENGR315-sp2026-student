import sys


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)
            continue
        # place entries as tuple into list
        data.append(entry)

    return data
def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    for line in data:
        # My if statement checks the lines with Rockingham and Virginia in it's county/state lines. Since there are other Rockingham counties 
        # this keeps it to just Rockingham Virginia cases.

        if line[1] == 'Rockingham' and line[2] == 'Virginia' and line[4] > 0:
            print('First positive COVID case in Rockingham County was on ', line[0])
            break #I stop the loop after it records the first case since that is all we need for this question

# My code for Harrionsburg works the same way
    for line in data:
        if line[1] == 'Harrisonburg city' and line[2] == 'Virginia' and line[4] > 0:
            print('First positive COVID case in Harrisonburg City was on ', line[0])
            break
    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    # Making variables I can use in my loops that will be updated. H and R stand for Harrisonburg and Rockingham respectively.
    H_cases = 0
    R_cases = 0
    difference = 0
    H_max_diff = 0
    R_max_diff = 0
    H_date = None
    R_date = None

    for line in data:
        if line[1] == 'Harrisonburg city' and line[2] == 'Virginia':
            difference = (line[4]) - H_cases
            H_cases = (line[4])
#I call it 'difference' here, but what I am solving for is the number of cases in 1 day. Since the cases value accumulates over time, by using 
# the difference between two days I can find how many cases happened per day
            if difference > H_max_diff:
                H_max_diff = difference
                H_date = line[0]
                #H_max_diff is my variable I am using to store the highest number of cases in 1 day, H_date is the day this happens
    print('The greatest number of daily cases recorded in Harrisonburg City was on', H_date,'with', H_max_diff, 'cases.')    

#My code process is the same for Rockingham County
    for line in data:
        if line[1] == 'Rockingham' and line[2] == 'Virginia':
            difference = (line[4]) - R_cases
            R_cases = (line[4])
            if difference > R_max_diff:
                R_max_diff = difference
                R_date = line[0]
    print('The greatest number of daily cases recorded in Rockingham County was on', R_date,'with', R_max_diff, 'cases.')   
    return

def third_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    :return:
    """

    # blank variables and lists I use
    H_cases = 0
    H_daily_cases = []
    H_days = []

    # I'm making 2 lists: one with the harrisonburg recorded case dates and one with the number of recorded cases that day. I did this so I could
    # sift through the data easier with my loops
    for line in data:
        if line[1] == 'Harrisonburg city' and line[2] == 'Virginia':
            difference = max(0,(line[4]) - H_cases) # when I looked at list of recorded cases, there were some negative values. I filter those out
                                                    # here since I assumed those were because of retroactive data corrections
            H_cases = (line[4])
            H_daily_cases.append(difference)
            H_days.append(line[0])

    H_max_week = 0
    H_max_index = 0

    # For loop to look through the daily cases, 6 is subtracted so we can't start a 7 day period within the last 6 datapoints 
    for i in range(len(H_daily_cases) - 6):
        H_week_total = sum(H_daily_cases[i:i+7]) #Adding the cases through each 7 day window
        if H_week_total > H_max_week: #if the number is the largest amount of cases, it saves this value
            H_max_week = H_week_total
            H_max_index = i
    print('The worst week of reported cases for Harrisonburg city was from', H_days[H_max_index], 'to', H_days[H_max_index + 6], 'with', H_max_week, 'cases.')

# Same process is repeated for Rockingham County
    R_cases = 0
    R_daily_cases = []
    R_days = []
    for line in data:
        if line[1] == 'Rockingham' and line[2] == 'Virginia':
            difference = max(0,(line[4]) - R_cases)
            R_cases = (line[4])
            R_daily_cases.append(difference)
            R_days.append(line[0])
 
    R_max_week = 0
    R_max_index = 0
    for i in range(len(R_daily_cases) - 6):
        R_week_total = sum(R_daily_cases[i:i+7])
        if R_week_total > R_max_week:
            R_max_week = R_week_total
            R_max_index = i
    print('The worst week of reported cases for Rockingham County was from', R_days[R_max_index], 'to', R_days[R_max_index + 6], 'with', R_max_week, 'cases.')
    return

if __name__ == "__main__": 
    data = parse_nyt_data('us-counties.csv')

    for (date,county, state, fips, cases, deaths) in data:
        break
      #print("fix")  #print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)

    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question: Use print() to display your responses.
    # What was the worst seven day period in Harrisonburg for new COVID cases (in terms of absolute number of cases)?
    # What was the worst seven day period in Rockingham County for new COVID cases (in terms of absolute number of cases)?
    third_question(data) 