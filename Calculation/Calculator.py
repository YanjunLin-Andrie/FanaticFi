
class Calculator:
    def __init__(self, data):
        # Add the data to class attributes, make all NaN values 0
        self.data = data.fillna(0)

    def get_points(self, section):

        # Get the 25 percentile
        q1 = self.data[section].quantile(0.25)

        # Get the 75 percentile
        q2 = self.data[section].quantile(0.75)

        # Compare all players on the column chosen
        for row in self.data.loc[:, ["Player", section]].iterrows():

            # If the stat does not exist
            if row[1][section] == 0:
                # Replace value with point of 0
                self.data.loc[self.data["Player"] == row[1]["Player"], section] = 0

            # If in the higher percentile
            elif row[1][section] > q2:
                # Replace value with point of 3
                self.data.loc[self.data["Player"] == row[1]["Player"], section] = 3

            # If in the average percentile
            elif q1 <= row[1][section] <= q2:
                # Replace value with point of 2
                self.data.loc[self.data["Player"] == row[1]["Player"], section] = 2

            # If in the lower percentile
            elif row[1][section] < q1 and row[1][section] != 0:
                # Replace value with point of 2
                self.data.loc[self.data["Player"] == row[1]["Player"], section] = 1


