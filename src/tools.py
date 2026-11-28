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
        'Date':          filtered['Date'].to_numpy()
        'isHome':        home.astype(int).to_numpy()
        'TeamElo':       np.where(home, games['HomeElo'],   games['AwayElo']),
        'OpponentElo':   np.where(home, games['AwayElo'],   games['HomeElo']),
        'Form3Team':     np.where(home, games['Form3Home'], games['Form3Away']),
        'Form3Opponent': np.where(home, games['Form3Away'], games['Form3Home']),
        'Form5Team':     np.where(home, games['Form5Home'], games['Form5Away']),
        'Form5Opponent': np.where(home, games['Form5Away'], games['Form5Home']),
        'HTTeam':        np.where(home, games['HTHome'],    games['HTAway']),
        'HTOpponent':    np.where(home, games['HTAway'],    games['HTHome']),
        'OddTeam':       np.where(home, games['OddHome'],   games['OddAway']),
        'OddOpponent':   np.where(home, games['OddAway'],   games['OddHome']),
        'OddDraw':       games['OddDraw'].to_numpy(),
        'Result':        result,
    })

    return processed