# BREAKDOWN
 

## Variables -
`Last_5_yrs_1_rnd_draft_df,`

`school `,
  
`school_rookie_count_df`,

`group_a_df `,
 
`group_b_df `,

`group_c_df`

## FILTER DATA
  * `Step 1`

The csv of nba draft stats from 1990 - 2017 is now a dataframe.Filtering the data a new dataframe now holds 2017 -2021 which is the last 5 year of draft and 1st round pick only which is stored in a variable ‘last_5_yrs_1_rnd_draft_df’

* `Step 2`

school variable contains a new dataframe of picks and colleges during 2017-2021
 * - school_rookie_count_df contains how many picks came from each school during 2017 -2021
 * - kentucky contains the highest number of picks
---
* `Step 3`

The  `last_5_yrs_1_rnd_draft_df` dataframe now get put into 3 groups ['A','B','C']'. 
* - Group A contains  top pick 1-5
* - B contains 13-17 
* - C  contains 26 - 30
 
 `Each  group ` created a new dataframe that inovoles there specific group
* - each group is all sorted by draft year  least to greatest 
* - we can now visual each stats from each group such ass  3pt% to MPG

# new edits
