# Table: Scores

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | score       | decimal |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
 

# Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

# The scores should be ranked from the highest to the lowest.
# If there is a tie between two scores, both should have the same ranking.
# After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
# Return the result table ordered by score in descending order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Scores table:
# +----+-------+
# | id | score |
# +----+-------+
# | 1  | 3.50  |
# | 2  | 3.65  |
# | 3  | 4.00  |
# | 4  | 3.85  |
# | 5  | 4.00  |
# | 6  | 3.65  |
# +----+-------+
# Output: 
# +-------+------+
# | score | rank |
# +-------+------+
# | 4.00  | 1    |
# | 4.00  | 1    |
# | 3.85  | 2    |
# | 3.65  | 3    |
# | 3.65  | 3    |
# | 3.50  | 4    |
# +-------+------+



import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = (scores['score']).rank(method = 'dense', ascending= False)
    return (scores[['score','rank']]).sort_values('rank')



if __name__ == "__main__":
    df = pd.DataFrame({'id' :[1,2,3,4,5,6],'score':[2.30,3.65,4.00,3.85,4.00,3.65]},index =[0,1,2,3,4,5])
    ordered = order_scores(df)
    expected = pd.DataFrame({'score':[2.30,3.65,4.00,3.85,4.00,3.65],'rank':[1,1,2,3,3,4]},index =[0,1,2,3,4,5])
    print("Expected Output:")
    print(expected)
    print("Actual Output:")
    print(ordered)
