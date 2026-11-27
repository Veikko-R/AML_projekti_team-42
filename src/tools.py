def filterTeam(df, team):
  """Select all matches played by a given team.

    Returns every row where the team appears as either the home team
    or the away team.

    Args:
        df (pandas.DataFrame): Match data. Must contain the columns
            'HomeTeam' and 'AwayTeam'.
        team (str): Team name, spelled exactly as in the data

    Returns:
        pandas.DataFrame: A new dataframe containing only the matches
        where the team played.

    Example:
        >>> villa = filterTeam(df, "Aston Villa")
    """
  filtered = df.loc[(df['HomeTeam']==team) | (df['AwayTeam']==team)].copy()
  return filtered
