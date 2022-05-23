import pandas as pd


class Calculator:
    def __init__(self, data):
        # Add the data to class attributes, make all NaN values 0
        self.data = data.fillna(0)
        self.new_data = self.create_df()
        self.total_list = []
        self.high_df = self.create_df()
        self.low_df = self.create_df()
        self.mid_df = self.create_df()

    # Simplifies a player's points chosen stat
    # section = stat wanting to simplify
    def get_points(self, section):

        # Get the 25 percentile
        q1 = self.data[section].quantile(0.25)

        # Get the 75 percentile
        q2 = self.data[section].quantile(0.75)

        # Compare all players on the column chosen
        self.data.loc[self.data[section] == 0, section] = 0
        self.data.loc[self.data[section] >= q2, section] = 3
        self.data.loc[(self.data[section] > q1) & (self.data[section] < q2), section] = 2
        self.data.loc[self.data[section] <= q1, section] = 1

        # Add the section into the new_data
        self.new_data[section] = self.data[section]

        # Add the section name to the total_list
        self.total_list.append(section)

    # Creates a df
    def create_df(self):
        # Create an empty dataframe
        new_df = pd.DataFrame()

        # Make columns and add the Player and Contract Worth information
        new_df["Player"] = self.data.loc[:, "Player"]
        new_df["Contract Worth"] = self.data.loc[:, "Contract Worth"]

        # Return the new dataframe
        return new_df

    # Gets the total points of each row
    def get_total(self):
        # Add columns together and create Total column
        self.new_data["Total"] = self.new_data[self.total_list].sum(axis=1)

    # Creates the high, mid, and low df
    def get_groups(self):
        # Get the total amount of points
        self.get_total()

        # Get the 25th and 75th percentile of the Total points
        total_q1 = self.new_data["Total"].quantile(0.25)
        total_q2 = self.new_data["Total"].quantile(0.75)

        # High dataframe where Players are above average
        self.high_df = self.new_data.loc[self.new_data["Total"] > total_q2].sort_values(
            by="Contract Worth",
            ascending=False
        )
        # Get only Players that have Contract Worth
        self.high_df["Contract Worth"] = self.high_df["Contract Worth"].loc[self.high_df["Contract Worth"] > 0]
        self.high_df = self.high_df.dropna()

        # Low dataframe where Players are below average
        self.low_df = self.new_data.loc[self.new_data["Total"] < total_q1].sort_values(
            by="Contract Worth",
            ascending=False
        )
        # Get only Players that have Contract Worth
        self.low_df["Contract Worth"] = self.low_df["Contract Worth"].loc[self.low_df["Contract Worth"] > 0]
        self.low_df = self.low_df.dropna()

        # Mid dataframe where Players are average
        self.mid_df = self.new_data.loc[(self.new_data["Total"] > total_q1) & (self.new_data["Total"] < total_q2)] \
            .sort_values(
            by="Contract Worth",
            ascending=False
        )
        # Get only Players that have Contract Worth
        self.mid_df["Contract Worth"] = self.mid_df["Contract Worth"].loc[self.mid_df["Contract Worth"] > 0]
        self.mid_df = self.mid_df.dropna()

    # Creates ROI column
    # inv = money invested in thousands
    def get_roi(self, inv):

        # Get the investment offer
        investment = inv

        # Create ROI Column
        self.data["ROI"] = ""

        # For each row in our original data
        for row in self.data.loc[:, ["Player", "Contract Worth"]].iterrows():

            # Get the current contract price
            current_value = (row[1]["Contract Worth"] * (10 ** (-6)))
            # Calculate ROI
            roi = ((current_value - investment) / investment)
            # Calculate return on investment
            self.data.loc[self.data["Player"] == row[1]["Player"], "ROI"] = (roi*inv)*(10**3)

        # Add new column to the new data frame
        self.new_data["ROI"] = self.data["ROI"]

        # Create groups
        self.get_groups()



