import time
import pandas as pd
import numpy as np

CITY_DATA = { 
    'chicago': './all-project-files/chicago.csv',
    'new york city': './all-project-files/new_york_city.csv',
    'washington': './all-project-files/washington.csv' 
}

def get_filters():
    """Asks the user to specify a city, month, and day to analyze

    Returns:
       (str) city: name of the city to be analyzed
       (str) month: choose which month in particular, or "all" to apply no filter
       (str) day: choose which day in particular, or "all" to apply no filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    while True: #Specifying the city
        city = input("Would you like to see data for Chicago, New York City, or Washington? ").strip().lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid input. Please enter 'Chicago', 'New York City', or 'Washington'.")
    while True: #Specifying the month
        month = input("Would you like to filter by month (January to June) or 'all'? ").strip().lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("Invalid input. Please enter a valid month or 'all'.")
    while True: #Specifying the day
        day = input("Would you like to filter by day or 'all'? ").strip().lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else: #If user's input is invalid
            print("Invalid input. Please enter a valid day or 'all'.")
    print('-'*40)
    return city, month, day

# Define the months list as a constant at the top
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']


def load_data(city, month, day):
    """Loads the specified data and reads the CSV file of whatever city the user chose and applies the needed filters

    Args:
        city (str): name of the city to analyze
        month (str): filtering by month, or "all" to apply no month filter
        day (str): filtering by day, or "all" to apply no day filter

    Returns:
        df: pandas DataFrame that contains the city data filtered by month and day
    """
    # Load and filter data based on user selections
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        # Use the MONTHS constant instead of a hardcoded list
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day.lower()]

    return df

def time_stats(df):
    
    """Provides statistics on the most frequent times of travel including the most common month,
    day, and hour"""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('Most Common Month:', df['month'].mode()[0])
    print('Most Common Day of Week:', df['day_of_week'].mode()[0])
    print('Most Common Start Hour:', df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    
    """Provides statistics on which station is the most popular with the most commonly used start station,
    most commonly used end station, and most common trip"""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('Most Commonly Used Start Station:', df['Start Station'].mode()[0])
    print('Most Commonly Used End Station:', df['End Station'].mode()[0])
    print('Most Common Trip:', df.groupby(['Start Station', 'End Station']).size().idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
   
    """Provides statistics on the total and average trip durations, calculating the total hours,
    minutes, and seconds, with the mean of minutes and seconds
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate total travel time in seconds
    total_trip_duration_seconds = df['Trip Duration'].sum()
    total_hours = int(total_trip_duration_seconds // 3600)
    total_minutes = int((total_trip_duration_seconds % 3600) // 60)
    total_seconds = int(total_trip_duration_seconds % 60)
    print(f'Total Travel Time: {total_hours} hours, {total_minutes} minutes, {total_seconds} seconds')

    # Calculate mean travel time in seconds
    mean_travel_time = df['Trip Duration'].mean()
    mean_minutes = int(mean_travel_time // 60)
    mean_seconds = int(mean_travel_time % 60)
    print(f'Mean Travel Time: {mean_minutes} minutes, {mean_seconds} seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    
    """Provides statistics on the users, with counts of user types, counts of gender if possible,
    and counts of birth year based on the most common year, most recent year, and earliest year"""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('Counts of User Types:', df['User Type'].value_counts())
    if 'Gender' in df.columns:
        print('Counts of Gender:', df['Gender'].value_counts())
    else:
        print("Gender data not available.")
    if 'Birth Year' in df.columns:
        print('Earliest Year:', int(df['Birth Year'].min()))
        print('Most Recent Year:', int(df['Birth Year'].max()))
        print('Most Common Year:', int(df['Birth Year'].mode()[0]))
    else:
        print("Birth year data not available.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    
    """Displays raw data in increments of 5 rows upon user request, 
    and continues to do so until the user choose to stop or until no data is available"""
    
    start = 0
    while True:
        show_data = input("Would you like to see 5 rows of raw data? Enter yes or no: ").strip().lower()
        if show_data == 'yes':
            print(df.iloc[start:start+5])
            start += 5
            if start >= len(df):
                print("No more data to display.")
                break
        elif show_data == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    
    """Runs the program including loading and filtering data. 
    Asks the user if they wish to restart or end the program"""
    
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)  # Prompt for viewing raw data after statistics
        restart = input('\nWould you like to restart? Enter yes or no.\n').strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
