import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data
    df = pd.read_csv("adult.data.csv")

    # 1. How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelors
    percentage_bachelors = round((df['education'].value_counts()['Bachelors'] / df.shape[0]) * 100, 1)

    # 4. Advanced education filter
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # % >50K with advanced education
    higher_education_rich = round((df[higher_education]['salary'].eq('>50K').mean()) * 100, 1)

    # % >50K without advanced education
    lower_education_rich = round((df[lower_education]['salary'].eq('>50K').mean()) * 100, 1)

    # 5. Min hours per week
    min_work_hours = df['hours-per-week'].min()

    # % >50K among those who work min hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'].eq('>50K').mean()) * 100, 1)

    # 6. Country with highest % of >50K
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    country_percentage = (country_earnings / country_counts) * 100

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 7. Most popular occupation in India for >50K earners
    india_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_occupation['occupation'].mode()[0]

    # Store results in dictionary
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
