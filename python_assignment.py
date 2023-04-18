import pandas as pd

user_ids = pd.read_excel('Python_Assignment.xlsx', sheet_name=0)
rigor_raw = pd.read_excel('Python_Assignment.xlsx', sheet_name=1)
 
df1 = pd.DataFrame(user_ids)
df2 = pd.DataFrame(rigor_raw)

def teamLeaderBoard():
    print('######### Leaderboard TeamWise #########')

    # merge dataframes on User ID and uid columns
    merged_df = pd.merge(df1, df2, left_on="User ID", right_on="uid")

    # calculate total statements and total reasons team-wise and sort in descending order
    team_stats = merged_df.groupby("Team Name").agg({
        "total_statements": "mean",
        "total_reasons": "mean"
    }).reset_index().sort_values(by=["total_statements", "total_reasons"], ascending=False)

    # create rank column
    team_stats["Rank"] = range(1, len(team_stats) + 1)

    # rearrange columns
    team_stats = team_stats[["Rank", "Team Name", "total_statements", "total_reasons"]]
    team_stats.columns = ['Team Rank', 'Thinking Teams Leaderboard', 'Average Statements', 'Average Reasons']

    # # save the dataframe to an Excel file
    # team_stats.to_excel('example.xlsx', index=False)

    print(team_stats)

def individualLeaderBoard():
    print('######### Leaderboard Individual #########')

    # calculate total score
    df = df2
    df['total_score'] = df['total_statements'] + df['total_reasons']

    # sort by total score and assign rank
    df['rank'] = df['total_score'].rank(method='first', ascending=False).astype(int)

    # rearrange columns
    df = df[['rank', 'name', 'uid', 'total_statements', 'total_reasons']]

    # sort by rank
    df = df.sort_values(by='rank')
    df.columns = ['Rank', 'Name', 'UID', 'No. of Statements', 'No. of Reasons']

    # display result
    print(df)

teamLeaderBoard()
individualLeaderBoard()