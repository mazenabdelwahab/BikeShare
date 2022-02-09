import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    global cities
    global months
    global days
    # TO DO: get user input for city (chicago, new york city,  ). HINT: Use a while loop to handle invalid inputs
    cities = input("Please enter your city name from list: (chicago , new  york city , washington)").lower()
    while cities not in CITY_DATA.keys():
          print(" invaild input \n " + "please Enter a vaild city!")
          cities = input("Please enter your city name from list (chicago , newyork city , washington):").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months= ['jan' , 'feb' , 'mar' , 'apr' , 'may' , 'jun' , 'jul' , 'all']
    select_month = input("choose a months : ('jan' , 'feb' , 'mar' , 'apr' , 'may' , 'jun' , 'jul' , 'all')")
   
    while select_month not in months:
            print("Enter Vaild input!")
            month = input("choose a months : ('jan' , 'feb' , 'mar' , 'apr' , 'may' , 'jun' , 'jul' , 'all')")
          

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days= ["Sunday" , "Monday" , "Tuesday" , "Wendsday" , "Thursday" , "Friday" , "All"]
    select_day = input("Please Select Day : ('sunday' , 'monday' , 'tuesday' , 'wendsday' , 'thursday' , 'friday' , 'all')").title()
     
    while select_day not in days:
         print("Please Enter Vaild input")
         select_day = input("Please Select Day : ('sunday' , 'monday' , 'tuesday' , 'wendsday' , 'thursday' , 'friday' , 'all')").title()

                       
        
    print('-'*40)
    return cities, months, days


def load_data(cities, months, days):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[cities])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour
    
    
    month = ['jan' , 'feb' , 'mar' , 'apr' , 'may' , 'jun' , 'all']

    #Filter by month
    if months in month :
       #indexing months to get int as in data
        months= month.index(months) + 1
        # Filter month to create new dataframe
        df= df[df['month'] == months]
   
    
    if days != 'All':
        #Filter by day to get new dataframe , day.title to make frist word capitalized 
        df[df['day_of_week'] == str(days).title()]         
                 
    return  df

def time_stats(df):
    #"""Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: {}' .format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day is: {}' .format(df['day_of_week'].mode()[0]))


    # TO DO: display the most common start hour
    print('The most common hour is: {}' .format(df['start hour'].mode()[0]))

    print('The time takes {} seconds'.format(time.time()-start_time))
    print('-'*40)

def station_stats(df):
    #"""Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: {}' .format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print('The most common end station is: {}' .format(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    df['route_station'] =df['End Station']+ "___" + df['End Station']
    print('The most common route station: {}' .format(df['route_station'].mode()[0]))


    print('The time takes {} seconds'.format(time.time()-start_time))
    print('-'*40)


def trip_duration_stats(df):
    #"""Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum().round()
    print('The Total Time is :' , total_travel)
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean().round()
    print('The Mean time is:' , mean_travel)


    print('The time takes {} seconds'.format(time.time()-start_time))
    print('-'*40)


def user_stats(df,cities):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame())
    #function to_frame() is used to convert the given series object to a dataframe.
 
        # TO DO: Display counts of gender
    if cities != 'washington':
        print('Gender Satstics')
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_com_year =int( df['Birth Year'].mode()[0])
        print('Most Common Year is:',most_com_year)
        most_rec_year = int( df['Birth Year'].max())
        print('Most Recent Year is:',most_rec_year)
        earl_year = int(df['Birth Year'].min())
        print('Earliest Year is:',earl_year)

        print('The time takes {} seconds'.format(time.time()-start_time))
        print('-'*40)
#To Ask the user if he want to show frist 5 rows 
def display_dataset(df):
    print(' Dataset is ready to check \n')
    input_user = input('Would You Like to Display Frist 5 Rows? , y or n \n')
    if input_user == 'y':
        count = 1
        while True:
            print(df.iloc[ count : count+5])
            count += 5
            #To Ask the user if he want to show the next 5 rows
            ask_next_rows= input('Would You Like To Show Next 5 Rows? \n')
            if ask_next_rows.lower() != 'y':
                break

def main():
    while True:
        cities, months, days = get_filters()
        df= load_data(cities, months, days)
        


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,cities)
        display_dataset(df) 
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
     main()