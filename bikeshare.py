import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago','new york','washington']
MONTHS = ['january','february','march','april','may','june']
DAYS = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('\nWhich city would you like to explore? \nChicago, New York, or Washington?\n>').lower()
        if city in CITIES:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    month = get_user_input('\nThanks! Please provide a month from the following list: January, February, March, April, May, June\nOr \"all\" to apply no month filter.\n>', MONTHS)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = get_user_input('\nThanks! Please provide a day to analyze.\nOr \"all\" to apply no day filter.\n>', DAYS)
    
    print('\nGreat!\nYou selected: '+city+', '+month+', '+day)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    #Load date file
    df = pd.read_csv(CITY_DATA[city])

    #Start Time field to DateTime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Create additional date fields
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #Filter by Month
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    #Filter by day of the week
    if day != 'all':
        
        df = df[ df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('The most common month is: ', MONTHS[common_month-1])

    # TO DO: display the most common day of week
    common_day_of_the_week = df['day_of_week'].value_counts().idxmax()
    print('The most common day of the week is: ', common_day_of_the_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].value_counts().idxmax()
    print('The most common start hour is: ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station: ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_combo = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most commonly used start station and end station: \n{}'.format(common_start_end_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time in seconds: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time in seconds: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n')
    user_counts = df['User Type'].value_counts()
    for index, user_count in enumerate(user_counts):
        print("  {}: {}\n".format(user_counts.index[index], user_count))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of gender:\n')
        gender_counts = df['Gender'].value_counts()
        for index, gender_count in enumerate(gender_counts):
            print('  {}: {}\n'.format(gender_counts.index[index], gender_count))
              

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year_stats(df)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def birth_year_stats(df):
    '''Birth year stats of the user where applicable'''
    
    birth_year = df['Birth Year']
    
    #Earliest year of birth
    earliest_year = birth_year.min()
    print('The earliest year of birth: ', int(earliest_year))
    
    #Most recent year of birth
    recent_year = birth_year.max()
    print('The most recent year of birth: ', int(recent_year))
    
    #Most common year of birth
    common_year = birth_year.value_counts().idxmax()
    print('The most common year of birth: ', int(common_year))
    
#Loop for user input, including 'all'
def get_user_input(message, user_list):
    
    while True:
        user_input = input(message).lower()
        if user_input in user_list:
            break
        if user_input == 'all':
            break

    return user_input   

def display_table_data(df):
    '''Raw data is displayed upon request by the user in the following manner. 5 Rows.'''
    
    display_data = input('Would you like to view 5 rows of associated data? Enter yes if so.\n>').lower()
    
    #Checks for display data input
    if display_data in ('yes', 'y'):
        #Index set at 0 to start
        i = 0 
        #While loop for additional 5 rows. Until we run out of rows
        while True:
            #Prints the rows of data using the index. Plus 5 everytime the user enters yes under additional_data
            print(df.iloc[i:i+5])
            i += 5
            additional_data = input('Would you like to see more? Enter yes if so.\n>').lower()
            if additional_data not in ('yes', 'y'):
                break
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_table_data(df)

        restart = input('\nWould you like to restart? Enter yes if so.\n>')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
