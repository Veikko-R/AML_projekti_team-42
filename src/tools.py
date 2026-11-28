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

    home = filtered['HomeTeam'] == team
    as_home = filtered['FTResult'].map({'H': 'W', 'D': 'D', 'A': 'L'})
    as_away = filtered['FTResult'].map({'H': 'L', 'D': 'D', 'A': 'D'})

    result = np.where(home, as_home, as_away)

    processed = pd.DataFrame({
        'Date':          filtered['Date'].to_numpy(),
        'isHome':        home.astype(int).to_numpy(),
        'TeamElo':       np.where(home, filtered['HomeElo'],   filtered['AwayElo']),
        'OpponentElo':   np.where(home, filtered['AwayElo'],   filtered['HomeElo']),
        'Form3Team':     np.where(home, filtered['Form3Home'], filtered['Form3Away']),
        'Form3Opponent': np.where(home, filtered['Form3Away'], filtered['Form3Home']),
        'Form5Team':     np.where(home, filtered['Form5Home'], filtered['Form5Away']),
        'Form5Opponent': np.where(home, filtered['Form5Away'], filtered['Form5Home']),
        'HTTeam':        np.where(home, filtered['HTHome'],    filtered['HTAway']),
        'HTOpponent':    np.where(home, filtered['HTAway'],    filtered['HTHome']),
        'OddTeam':       np.where(home, filtered['OddHome'],   filtered['OddAway']),
        'OddOpponent':   np.where(home, filtered['OddAway'],   filtered['OddHome']),
        'OddDraw':       filtered['OddDraw'].to_numpy(),
        'Result':        result,
    })

    return processed