{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello! Let's explore some US bikeshare data!\n"
     ]
    }
   ],
   "source": [
    "\"version     aaaaaaaa   considererrrrrrrrrrrrrrrr\"\n",
    "\"Final Version\"\n",
    "\n",
    "import time\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "CITY_DATA = { 'chicago': 'chicago.csv',\n",
    "              'new york': 'new_york_city.csv',\n",
    "              'washington': 'washington.csv' }\n",
    "\n",
    "def get_filters():\n",
    "    \"\"\"\n",
    "    Asks user to specify a city, month, and day to analyze.\n",
    "\n",
    "    Returns:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "        \n",
    "    \"\"\"\n",
    "    \n",
    "    print('Hello! Let\\'s explore some US bikeshare data!')\n",
    "    \n",
    "    \n",
    "    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs\n",
    "    while True:\n",
    "        city = input(\"Would you like to see data for chicago, new york, or washington ? \").lower()\n",
    "        if city not in(CITY_DATA.keys()):\n",
    "            print('We are sorry, you provided an invalid city name. Please, provide a correct city name by choosing between chicago, new york or washington')\n",
    "        else :\n",
    "            break\n",
    "   \n",
    "\n",
    "    # TO DO: get user input for month (all, january, february, ... , june)\n",
    "    while True :\n",
    "        month = input (\" Please; enter a month between january, february, march, april, may or june. \").lower()\n",
    "        all_months = ['january','february','march','april','may','june']\n",
    "        if month != 'all' and month not in all_months :\n",
    "            print('We are very sorry, you provided an invalid month. You have to provide a valid month by choosing between january, february, march, april, may or june. ')\n",
    "        else:\n",
    "            break  \n",
    "  \n",
    "         \n",
    "    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)\n",
    "    while True :\n",
    "        day = input (\" Please, choose a day between monday, tuesday, wednesday, thursday, friday, saturday or sunday? \").lower()\n",
    "        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']\n",
    "        if day != 'all' and day not in days :\n",
    "            print('We are sorry, you provided an invalid day. Enter a valid day by choosing between monday, tuesday, wednesday, thursday, friday, saturday or sunday ')   \n",
    "        else:\n",
    "            break   \n",
    "        \n",
    "                 \n",
    "    print('-'*40)\n",
    "    return city, month, day\n",
    "\n",
    "\n",
    "\n",
    "def load_data(city, month, day):\n",
    "    \"\"\"\n",
    "    Loads data for the specified city and filters by month and day if applicable.\n",
    "\n",
    "    Args:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    Returns:\n",
    "        df - Pandas DataFrame containing city data filtered by month and day\n",
    "    \"\"\"\n",
    "# load data file into a dataframe\n",
    "    df = pd.read_csv(CITY_DATA[city])\n",
    "\n",
    "    # convert the Start Time column to datetime\n",
    "    df['Start Time'] = pd.to_datetime(df['Start Time'])\n",
    "\n",
    "    # extract month and day of week from Start Time to create new columns\n",
    "    df['month'] = df['Start Time'].dt.month\n",
    "    df['day_of_week'] = df['Start Time'].dt.day_name()\n",
    "\n",
    "    # filter by month if applicable\n",
    "    if month != 'all':\n",
    "        # use the index of the months list to get the corresponding int\n",
    "        months = ['january', 'february', 'march', 'april', 'may', 'june']\n",
    "        month = months.index(month) + 1\n",
    "\n",
    "        # filter by month to create the new dataframe\n",
    "        df = df[df['month'] == month]\n",
    "\n",
    "    # filter by day of week if applicable\n",
    "    if day != 'all':\n",
    "        # filter by day of week to create the new dataframe\n",
    "        df = df[df['day_of_week'] == day.title()]\n",
    "    # print (df.head())\n",
    "\n",
    "    return df\n",
    "\n",
    "\n",
    "\n",
    "def time_stats(df):\n",
    "    \"\"\"Displays statistics on the most frequent times of travel.\"\"\"\n",
    "\n",
    "    print('\\n Calculating The Most Frequent Times of Travel...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    \n",
    "    # display the most common month\n",
    "    months = ['january','february','march','april','may','june']\n",
    "    common_month = df[\"month\"].mode()[0]\n",
    "    print(f'The most common month is: {months[common_month-1]}')\n",
    "    \n",
    "\n",
    "    # display the most common day of week\n",
    "    common_weekday = df[\"day_of_week\"].mode()[0]\n",
    "    print(f'The most common day of week is: {common_weekday}')\n",
    "\n",
    "\n",
    "    # display the most common start hour\n",
    "    df[\"hour\"] = df[\"Start Time\"].dt.hour\n",
    "    common_hour = df[\"hour\"].mode()[0]\n",
    "    print(f'The most common start hour is: {common_hour}')\n",
    "    \n",
    "    \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "\n",
    "    \n",
    "    \n",
    "def station_stats(df):\n",
    "    \"\"\"Displays statistics on the most popular stations and trip.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Popular Stations and Trip...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # display most commonly used start station\n",
    "    common_start_station = df[\"Start Station\"].mode()[0] \n",
    "    print(f'The most commonly used start station is :{common_start_station}')\n",
    "\n",
    "    # display most commonly used end station\n",
    "    common_end_station = df[\"End Station\"].mode()[0] \n",
    "    print(f'The most commonly used end station is : {common_end_station}')\n",
    "\n",
    "    # display most frequent combination of start station and end station trip\n",
    "    common_start_end_station = df[\"Start Station\"] + \" to \" + df[\"End Station\"] \n",
    "    print(f'The most frequent combination of start station and end station trip is : from {common_start_end_station.mode()[0]}')\n",
    "    \n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)\n",
    "\n",
    "    \n",
    "\n",
    "    \n",
    "def trip_duration_stats(df):\n",
    "    from datetime import timedelta as td\n",
    "    \"\"\"Displays statistics on the total and average trip duration.\"\"\"\n",
    "    \n",
    "    \n",
    "    print('\\nCalculating Trip Duration...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # display total travel time\n",
    "    total_travel_time = (pd.to_datetime(df[\"End Time\"]) - pd.to_datetime(df[\"Start Time\"])).sum()\n",
    "    v_days = total_travel_time.days\n",
    "    v_hours = total_travel_time.seconds // (60*60)\n",
    "    v_minutes = total_travel_time.seconds % (60*60) // 60\n",
    "    v_seconds = total_travel_time.seconds % (60*60) % 60\n",
    "    print(f'The total travel time is: {v_days} days, {v_hours} hours, {v_minutes} minutes and {v_seconds} seconds')\n",
    "    \n",
    "    \n",
    "    # display mean travel time\n",
    "    avg_travel_time = (pd.to_datetime(df[\"End Time\"]) - pd.to_datetime(df[\"Start Time\"])).mean()\n",
    "    avg_days = avg_travel_time.days\n",
    "    avg_hours = avg_travel_time.seconds // (60*60)\n",
    "    avg_minutes = avg_travel_time.seconds % (60*60) // 60\n",
    "    avg_seconds = avg_travel_time.seconds % (60*60) % 60\n",
    "    print(f'The average travel time is: {avg_days} days, {avg_hours} hours, {avg_minutes} minutes and {avg_seconds} seconds')\n",
    "    \n",
    "    \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)  \n",
    "\n",
    "\n",
    "def user_stats(df):\n",
    "    \"\"\"Displays statistics on bikeshare users.\"\"\"\n",
    "\n",
    "    print('\\nCalculating User Stats...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    \n",
    "    # Display counts of user types\n",
    "    #print(df[\"User Type\"].value_counts())\n",
    "    print(\"The count of user types is : \\n\",df[\"User Type\"].value_counts())\n",
    "    print('\\n\\n')\n",
    "\n",
    "    \n",
    "    # Display counts of gender\n",
    "    if \"Gender\" in (df.columns) :\n",
    "        #print (df[\"Gender\"].value_counts())\n",
    "        print(\" \\n The count of gender is : \\n\",df[\"Gender\"].value_counts())\n",
    "        \n",
    "\n",
    "    # Display earliest, most recent, and most common year of birth  \n",
    "    if \"Birth Year\" in (df.columns):\n",
    "        year = (df[\"Birth Year\"].fillna(0).astype('int64')) \n",
    "        #earliest_birth_year = (year.min())\n",
    "        earliest_birth_year = int(df[\"Birth Year\"].min())\n",
    "        print(\" \\n The earliest birth of year is : \\n\", earliest_birth_year)\n",
    "        most_recent_birth_year = (year.max())\n",
    "        print(\" \\n The most recent birth of year is : \\n\", most_recent_birth_year)\n",
    "        #most_common_birth_year = (year.mode()[0]:.0f)\n",
    "        print(f'The most common birth of year is : {df[\"Birth Year\"].mode()[0]:.0f}')\n",
    "        \n",
    "        \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*40)       \n",
    "    \n",
    "    \n",
    "    \n",
    "\n",
    "def display_rows_of_data(df): \n",
    "    \"\"\"Ask the user if he wants to display the row data and print 5 rows at the same time.\"\"\"\n",
    "\n",
    "    print('\\n Display rows of data...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    answer_row = input(\" Would you like to display the first 5 rows of data? yes/no\")\n",
    "    if answer_row.lower() == \"yes\":\n",
    "        count = 0\n",
    "        while True :\n",
    "            print(df.iloc[count:count+5])\n",
    "            count+=5\n",
    "            question = input(\" Would you like to display the next 5 rows of data? yes/no\")\n",
    "            if question.lower() != \"yes\":\n",
    "                break\n",
    "         \n",
    "        \n",
    "        \n",
    "def main():\n",
    "    while True:\n",
    "        city, month, day = get_filters()\n",
    "        df = load_data(city, month, day)\n",
    "\n",
    "        time_stats(df)\n",
    "        station_stats(df)\n",
    "        trip_duration_stats(df)\n",
    "        user_stats(df)\n",
    "        display_rows_of_data(df)\n",
    "\n",
    "        restart = input('\\nWould you like to restart? Enter yes or no.\\n')\n",
    "        if restart.lower() != 'yes':\n",
    "            break\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "\tmain()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
