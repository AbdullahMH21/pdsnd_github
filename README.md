>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
November 2, 2024

### Project Title
Bikeshare Data Analysis Tool

### Description
This project is a command-line Python tool that provides data analysis for bike-sharing systems in three major U.S. cities: Chicago, New York City, and Washington. Users can filter data by city, month, and day to explore various statistics, such as popular travel times, commonly used stations, trip durations, and user demographics. It uses data provided in CSV files and relies on the Pandas library to process and analyze the information based on user-specified filters. It also allows users to view raw data in increments of 5 rows upon request.

### Files used
- `chicago.csv`: Contains bikeshare data for Chicago.
- `new_york_city.csv`: Contains bikeshare data for New York City.
- `washington.csv`: Contains bikeshare data for Washington.
- `bikeshare.py`: Main Python script that performs data loading, filtering, and statistical analysis.

### Credits
This project is part of the Udacity Data Analyst Nanodegree program. Special thanks to Udacity for providing the initial dataset and project framework. Additional resources and inspiration were taken from the Pandas documentation and Stack Overflow.

### Usage Example
After running the script with `python bikeshare.py`, you’ll be prompted to select a city, month, and day. Here’s an example interaction:

Would you like to see data for Chicago, New York City, or Washington? chicago Would you like to filter by month (January to June) or 'all'? march Would you like to filter by day or 'all'? all

### Future Improvements
- Expand the data to include additional months and cities.
- Create a graphical interface to visualize the statistics.
- Implement more advanced data filtering options for enhanced analysis.
