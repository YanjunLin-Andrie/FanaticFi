import sys
import csv
import fire
import questionary
from pathlib import Path
import pandas as pd
from calculator import Calculator
from filio import load_csv
from roi import roi_calculator


# Welcome message
print('\n Welcome to FanaticFi! \n')
print('This application will help athletes project their contract value and will also help investors project their earnings if they invest in a player.\n')
    
"""Prompt dialog to let user choose if they are athelets or investors.
    """
role = questionary.select('Are you an athlete or an investor?', choices = ['Athlete', 'Investor']).ask()

# Take user input and save into athlete.csv file
def get_athlete_stats():
    
    with open("2022_top_30.csv", "a", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        
        pos = input('What is your primary position? Choose from: SG, PG, PF, SF, C: ')
        mpg = float(input('What is your average minutes played per game: '))
        ppg = float(input('What is your average points scored per game: '))
        rpg = float(input('What is your average rebounds collected per game: '))
        apg = float(input('What is your average assist amount per game: '))
        fg_pct = float(input('What is your average field goal percentage? Please enter in number format (ex: 0.456): '))
        three_p_pct = float(input('What is your average 3 pointer percentage? Please enter in number format (ex: 0.456): '))
        ft_pct = float(input('What is your average free throw percentage? Please enter in number format (ex: 0.456): '))
        csvwriter.writerow([2022, "", "", pos, "", "", "", mpg, ppg, "", "", rpg, apg, fg_pct, "", "", three_p_pct, "", "", ft_pct, "", "", "", "", "", ""])
        print('Calculating your contract range...')

    # Our team ran into some issue getting contract range based on new input. We will update soon.




    # athlete_points()

# #  Get total points of the player's input 
# def athlete_points():
#     athlete_df = pd.read_csv(Path('2022_top_30.csv'))
#     new_data = Calculator(athlete_df)
#     new_data.get_points('MPG')
#     new_data.get_points('PPG')
#     new_data.get_points('RPG')
#     new_data.get_points('APG')
#     new_data.get_points('FG%')
#     new_data.get_points('3P%')
#     new_data.get_points('FT%')
#     new_data.get_total()
#     total_points = new_data.get_total()
#     return total_points

# def load_athlete_points():
#     csvpath = Path('_22_all_stats.csv')
#     return pd.read_csv(csvpath)

# # Use total points generate contract range    
# # def get_contract_range():
# #     points_to_contract_df = load_athlete_points()
# #     total_points
# #     low = points_to_contract_df.loc[points_to_contract_df['Pos'] == pos,].values
# #     high = 

    # print(f"Based on our analysis, your projected contract range is {low} - {high}")
    # signup = questionary.select('Would you like to sign up to recieve investments?', choices=['Yes','No']).ask()

    # if signup == 'Yes':
    #     email = questionary.text('Please enter your email:').ask()
    #     print('Great! Our team will contact you shortly to create your profile.')
    # if signup == 'No':
    #     print('Thanks for using FanaticFi. Good luck in the draft!')
    
    # return low, high
    



# This function is used to get 2022 players stats and contract worth prediction
def load_player_contract():
    csvpath = Path('_22_all_stats.csv')
    return pd.read_csv(csvpath)

# This function is used to let investor choose who to invest in
def get_investor_info():
    """Prompt dialog to get the investor's info.
    Returns:
        Returns the investor's projected future earnings based on thier choices.
    """
    player_name = questionary.select('What current NCAA player would you like to choose?', choices=['Jabari Smith',
'Chet Holmgren',
'Paolo Banchero',
'Jaden Ivey',
'Keegan Murray',
'Shaedon Sharpe',
'Johnny Davis',
'A.J. Griffin',
'Jalen Duren',
'Bennedict Mathurin',
'Dyson Daniels',
'Tari Eason',
'TyTy Washington',
'Ochai Agbaji',
'Jeremy Sochan',
'Mark Williams',
'Kennedy Chandler',
'Malaki Branham',
'Ousmane Dieng',
'Kendall Brown',
'Jaden Hardy',
'Blake Wesley',
'Nikola Jovic',
'E.J. Liddell',
'Marjon Beauchamp',
'Wendell Moore Jr',
'Walker Kessler',
'Jean Montero',
'Patrick Baldwin Jr',
'Christian Braun']).ask()

    # Get the 2022 players' dataframe
    player_contract_df = load_player_contract()
  
    # From the dataframe, get chosen player's contract range
    min = player_contract_df.loc[player_contract_df['Player'] == player_name,'min'].values
    max = player_contract_df.loc[player_contract_df['Player'] == player_name,'max'].values
    print(f"Our analysis predicts this player's contract worth to be in between $ {min} and $ {max}")
    
    # If investor wants to invest, generate profit estimation
    invest = questionary.select('Would you like to invest in this player?', choices=['Yes','No','Choose another player']).ask()
    if invest == 'Yes':
        amt = questionary.text('How much would you like to invest?').ask()
        amt = float(amt)
        profit = roi_calculator(amt)
        print(f"With a $ {amt} investment, your projected investment profit is $ {profit}")
        cont = questionary.select('Would you like to continue with the investment?', choices=['Yes','No']).ask()
        if cont == 'Yes':
            email = questionary.text('Please enter your email:').ask()
            print('Great! Our team will contact you shortly to help you set up your investor profile.')
            print("Thank you for using FanaticFi")
        if cont == 'No':
            print("Thank you for using FanaticFi")
    if invest == 'No':
        print("Thanks for using FanaticFi!")
    if invest == 'Choose another player':
        get_investor_info()

    return min, max



def run():
    
    if role == 'Athlete':
        get_athlete_stats()
    else:
        get_investor_info()

if __name__ == "__main__": run()