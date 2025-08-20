# Overview
This is a deployable, interactive, web browser app to create radar plots, popularized by Statsbomb. There are two options of plots - a single player, and a player comparison. Players can be selected from the top 5 European leagues with seasons spanning back to 2020/2021. 5 positions can be selected from: centerback, fullback, midfielder, attacking midfielder/winger, and striker. Player comparison plots also allow you to compare players to themselves from previous seasons, as well as different players across different seasons. The radar plot minimum and maximum values are the 5th and 95th percentiles respectively, across all 5 leagues since the 2020/2021 season, across specified position. Data is from Fbref and acquired using soccerdata package; radar plots are created using mplsoccer.

# Individual scripts
Below is a breakdown of the individual scripts and the part they play in the app:

get_data.py: Uses soccerdata to get relevant stats for each position. Replaces values for certain columns as well as renames columns. Saves data frame as a csv for later use.

radar_function.py: Uses mplsoccer to create functions that will create the single player and player comparison radar plots.

create_data_dict.py: Uses data csv file to create dictionary of seasons, leagues, teams, and players that can be used for dropdown bars in app.

app.py: Creates app.
