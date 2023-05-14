import pandas as pd
import matplotlib.pyplot as plt

## LOADING & PREPARING DATA
# Load in the datasets
pulls_one = pd.read_csv("datasets/pulls_2011-2013.csv")
pulls_two = pd.read_csv("datasets/pulls_2014-2018.csv")
pull_files = pd.read_csv("datasets/pull_files.csv")

# Prepare & Clean
pulls = pulls_two._append(pulls_one, ignore_index=True)
pulls["date"] = pd.to_datetime(pulls["date"], utc=True) # this converts the strings in this column to datetime
data = pulls.merge(pull_files, on="pid")

## INVESTIGATE THE ACTIVITY ON THE PROJECT
# Count the PRs to determine the project's engagement

data['month'] = data["date"].dt.month # this creates a column in the df to store the month
data['year'] = data["date"].dt.year # this creates a column in the df to store the year
counts = data.groupby(["month", "year"])["pid"].count() # count PRs by month, year
counts.plot(kind='bar', figsize = (12,4)) # plot the results

by_user = data.groupby('user').agg({'pid': 'count'}) # count PRs by user
by_user.hist() # plot the results

# Investigate the most recent activity on the project
last_10 = pulls.nlargest(10, "date") # the 10 newest PRs: by sorting by the largest dates, which would also be the most recent dates
joined_pr = last_10.merge(pull_files, on="pid") # produces a dataset with only the files affected by the PRs that happened in the 10 most recent dates

files = set(joined_pr["file"]) # gets the specific, unique files that have recently seen changes from the 'file' column of the joined_pr dataset

## INVESTIGATE THE ACTIVITY ON A SINGLE FILE
# File chosen: 'src/compiler/scala/reflect/reify/phases/Calculate.scala'

# Identify those with the most PRs on the target file
file_pr = data[data['file'] == 'src/compiler/scala/reflect/reify/phases/Calculate.scala']
author_counts = file_pr.groupby('user').count()
author_counts.nlargest(3, 'file') # select the 3 developers with the most activity from the file column

# Identify those with the most recent PRs on the target file
file_pr = pull_files[pull_files['file'] == 'src/compiler/scala/reflect/reify/phases/Calculate.scala']
joined_pr = pulls.merge(file_pr, on='pid')
users_last_10 = set(joined_pr.nlargest(10, 'date')['user']) # get the 10 most recent PRs' users

# Visualize their activity on the target file
authors = []

for o in users_last_10:
    authors.append(o)

# Select all PRs submitted by the authors, from the `data` DataFrame
by_author = data[data["user"].isin(authors)]
# Select the pull requests that affect the file
by_file = by_author[by_author["file"] == 'src/compiler/scala/reflect/reify/phases/Calculate.scala']
# Group and count the number of PRs done by each user each year
grouped = by_file.groupby(['user', by_file['date'].dt.year]).count()['pid'].reset_index()

by_file_wide = grouped.pivot_table("pid", index="date", columns="user", fill_value=0)
# Plot the results
by_file_wide.plot(kind='bar')


plt.show()