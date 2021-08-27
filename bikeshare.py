import time
import pandas as pd
import numpy as np
import datetime
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities= ['chicago','new york city', 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' ]

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
        city = input('\nWould you like to see the data for chicago, new york city, or washington?: ').lower()
        if city in cities:
            break
        else:
            print('\nTry again: This is case sensitive; Check spelling and choose between chicago, new york city, or washington')
    #if the user types a city in cities then it will go on the next question if not it will ask the user to try again

             
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month would you want to filter by january, february, march, april, may, june or all?: ').lower()
        if month in months:
            break
        else:
            print('\nTry Again: This is case sensitive; Check spelling and choose between the options listed')
    #if the user types a month in months then it will go on the next question if not it will ask the user to try again



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('\nWhich day would you like to filter by monday, tuesday, wednesday, thursday, friday, saturday, or sunday?: ').lower()
        if day in days:
            break #This will cause it to go to the next question
        else:
            print('\nTry Again: This is case sensitive; Check spelling and choose between the options listed')
            
   #if the day the user types is in days then it will go on to the next function if not it will ask the user to try again    
            
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
        df        - Pandas DataFrame containing city data filtered by month an   """

    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    df['common_month'] = df['Start Time'].dt.month #This grabs the months from the start time column
    most_common_month = df['common_month'].mode()[0] #This grabs the mode out of month provided 
    print("The most common month is ",most_common_month)
    
    # display the most common day of week
    
    df['common_day'] = df['Start Time'].dt.weekday_name #this grabs the days of the week from the start time column
    most_common_day_of_week = df['common_day'].mode()[0] #This grabs the mode for days of the week
    print("The most common day is ",most_common_day_of_week)

    # display the most common start hour
    
    df['common_start_hour'] = df['Start Time'].dt.hour #This grabs the hours from the start time column
    most_common_start_hour = df['common_start_hour'].mode()[0] #This grabs the mode out of the hours provided
    print("The most common start hour is ", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station= df['Start Station'].mode()[0] #This grabs the mode out of the start station column
    print('\nThe most common Start Station is',common_start_station)
    

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]#This grabs the mode out of the end station column
    
    print('\nThe most common End Station is', common_end_station)

    # display most frequent combination of start station and end station trip
    df['freq_combination'] = df['Start Station']+'/ '+df['End Station']
    freq_combine_of_start_and_end =df['freq_combination'].value_counts().index[0]
    print('\nThe most frequent combination of start station and end station trip is\n', freq_combine_of_start_and_end)
    #This gets the only the top frequent combination of start and end station
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel= df['Trip Duration'].sum()
    print('The total travel time is:', datetime.timedelta(float(total_travel)))#prints and displays the total travel time in days,hours, minutes and seconds
    #This gets the sum of the travel time
    
    
    # display mean travel time

    mean_travel = df['Trip Duration'].mean()
    print('\nThe mean travel time is:', datetime.timedelta(mean_travel))#prints and displays the mean travel time in days,hours, minutes and seconds

    #This gets the mean for the travel time
    
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_type_count = df['User Type'].value_counts()
    print('The counts for user types are:\n', user_type_count)
    #This gets the count for the subcriber and customer
    
    # Display counts of gender
    #This will only run if chicago or new york city is picked by the user
    if city == 'chicago' or city =='new_york_city':
        
        gender_count = df['Gender'].value_counts()
        print('\nThe counts for gender are:\n',gender_count)
        #This gets the count for female and male

    # Display earliest, most recent, and most common year of birth
        earliest_bitrh = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('\nThe Earliest Year Of Birth is ',earliest_bitrh)
        print('\nThe Most Recent Year Of Birth is ',recent_birth)
        print('\nThe Most Common Year Of Birth is ',common_birth)
     
    else:
        print('\nThere is no data on birth year for washington')
  
    # This prints out the earliest, most recent and common year of birth by getting the minimum,maximum and mode of the birth years
   
    
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

def raw_data(df): #This will ask the user if they want to see raw data
    data = 0
    while True:
        ask_for_raw_data = input('\nWould you like to see 5 lines of raw data? yes or no?: ').lower()
        if ask_for_raw_data == 'yes':
            data += 5
            print(df.iloc[data : data + 5])
            while True:
           #This second loop will run as long as ask_again== 'yes' & if ask_again== 'no' it will break out of the function and continue
                ask_again = input('\nDo you want to see 5 more lines? yes or no: ').lower()
                if ask_again == 'yes':
                    data += 5
                    print(df.iloc[data : data + 5])
                elif ask_again == 'no':
                    break 
                else:
                    print('\nTry Again: This is case sensitive; Please type in yes or no: ')
            break  #This will break to loop and go to the next question    
        elif ask_for_raw_data == 'no':
            break
       
        else:
            print('\nTry Again: This is case sensitive; Please type in yes or no:')
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == '__main__':
	main()
