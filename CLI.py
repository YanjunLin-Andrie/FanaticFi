import sys
import fire
import questionary

print('\n Welcome to FanaticFi Calculator \n')
print('This calculator is designed to help athletes project their contract value based on their stats and to help investors project their future earnings\n')
    
"""Prompt dialog to let user choose if they are athelets or investors.
    """
role = questionary.select('Are you an athlete or an investor?', choices = ['Athlete', 'Investor']).ask()

def get_athlete_stats():

    """Prompt dialog to get the athlete's stats.
    Returns:
        Returns the athlete's projected contract value and suggested payback rate.
    """
    pos = questionary.select('What is your primary position?', choices=['SG','PG','PF','SF','C']).ask()
    mpg = questionary.text('How many munites do you play per game?').ask()
    ppg = questionary.text('How many points do you score per game?').ask()
    rpg = questionary.text('How many rebounds do you have per game?').ask()
    apg = questionary. text('How many assists do you have per game?').ask()
    fg_pct = questionary.text('What is your field goal percentage?').ask()
    three_p_pct = questionary.text('What is your 3 pointer percentage?').ask()
    ft_pct = questionary.text('What is your free throw percentage?').ask()

    # Convert the information provided by the athlete to data types that are required for later use in the app
    mpg = float(mpg)
    ppg = float(ppg)
    rpg = float(rpg)
    apg = float(apg)
    fg_pct = float(fg_pct)
    three_p_pct = float(three_p_pct)
    ft_pct = float(ft_pct)

    return pos, mpg, ppg, rpg, apg, fg_pct, three_p_pct, ft_pct

    contract_range = contract_calculator(pos,mpg,ppg,rpg,apg,fg_pct,three_p_pct,ft_pct)
    payback_rate_range = payback_rate_calculator(pos,mpg,ppg,rpg,apg,fg_pct,three_p_pct,ft_pct)
    print(f'\n Your projected contract value range is {contract_range}.')
    print(f'\n Your suggested payback rate range is {payback_rate_range}.')


def get_investor_info():
    """Prompt dialog to get the investor's info.
    Returns:
        Returns the investor's projected future earnings based on thier choices.
    """
    amount = questionary.text('How much would you like to invest monthly on an athlete?').ask()
    payback_rate = questionary.select('Please select your prefered payback rate:', choices = ['1.25','1.50','1.75','2.00']).ask()

    # Convert the information provided by the investor to data types that are required for later use in the app
    amount = float(amount)

    return amount, payback_rate

    investment_return = investment_return_calculator(amount,payback_rate)
    print(f'\n Your extimated investment return range at maturity is {investment_return:.02f}.')





def run():
    if role == 'Athlete':
        get_athlete_stats
    else:
        get_investor_info
