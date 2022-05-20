import sys
import fire
import questionary
from pathlib import Path

#Import calc functions here
#From -- import ---
from calculators import roi_calculator

print('\n Welcome to FanaticFi! \n')
print('This application will help athletes project their contract value and will also help investors project their earnings if they invest in a player.\n')
    
"""Prompt dialog to let user choose if they are athelets or investors.
    """
role = questionary.select('Are you an athlete or an investor?', choices = ['Athlete', 'Investor']).ask()

def get_athlete_stats():

    """Prompt dialog to get the athlete's stats.
    Returns:
        Returns the athlete's projected contract value and suggested payback rate.
    """
    pos = questionary.select('What is your primary position?', choices=['SG','PG','PF','SF','C']).ask()
    mpg = questionary.text('What is your average minutes played per game?').ask()
    ppg = questionary.text('What is your average points scored per game?').ask()
    rpg = questionary.text('What is your average rebounds collected per game?').ask()
    apg = questionary. text('What is your average assist amount per game?').ask()
    fg_pct = questionary.text('What is your average field goal percentage? Please enter in number format - ex: 0.456').ask()
    three_p_pct = questionary.text('What is your average 3 pointer percentage? Please enter in number format - ex: 0.456').ask()
    ft_pct = questionary.text('What is your average free throw percentage? Please enter in number format - ex: 0.456').ask()

    # Convert the information provided by the athlete to data types that are required for later use in the app
    # mpg = float(mpg)
    # ppg = float(ppg)
    # rpg = float(rpg)
    # apg = float(apg)
    # fg_pct = float(fg_pct)
    # three_p_pct = float(three_p_pct)
    # ft_pct = float(ft_pct)

    # return pos, mpg, ppg, rpg, apg, fg_pct, three_p_pct, ft_pct

    # contract_range = contract_calculator(pos,mpg,ppg,rpg,apg,fg_pct,three_p_pct,ft_pct)
    # print(f'\n Your projected contract value range is {contract_range}.')

    print("Based on our analysis, your projected contract range is $ 1000000 - $ 2250000")

    signup = questionary.select('Would you like to sign up to recieve investments?', choices=['Yes','No']).ask()
    
    if signup == 'Yes':
        email = questionary.text('Please enter your email:').ask()
        print('Great! Our team will contact you shortly to create your profile.')
    if signup == 'No':
        print('Thanks for using FanaticFi. Good luck in the draft!')




def get_investor_info():
    """Prompt dialog to get the investor's info.
    Returns:
        Returns the investor's projected future earnings based on thier choices.
    """
    player = questionary.select('What current NCAA player would you like to choose?', choices=['Jabari Smith',
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

    if player == 'Keegan Murray':
        print("Our analysis predicts this player's contract worth to be $ 2500000 - $3500000")
    else:
        print("Our analysis predicts this player's contract worth to be $ 4000000 - $4750000")

    invest = questionary.select('Would you like to invest in this player?', choices=['Yes','No','Choose another player']).ask()

    if invest == 'Yes':
        amt = questionary.text('How much would you like to invest?').ask()
        print(f"With a $ {amt} investment, your projected ROI is 87.24%")
        cont = questionary.select('Would you like to continue with the investment?', choices=['Yes','No']).ask()
        if cont == 'Yes':
            email = questionary.text('Please enter your email:').ask()
            print('Great! Our team will contact you shortly to help you set up your investor profile.')
            print("Thank you for using FanaticFi")
        if cont == 'No':
            get_investor_info

    if invest == 'No':
        print("Thanks for trying FanaticFi!")
    if invest == 'Choose another player':
        get_investor_info()




def run():
    if role == 'Athlete':
        get_athlete_stats()
    else:
        get_investor_info()

if __name__ == "__main__": run()
