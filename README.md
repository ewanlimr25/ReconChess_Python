# ReconChess_Python
This is a repo for building out the ReconChess Bots to participate in the Blind Chess tournaments : https://rbc.jhuapl.edu/

Bot strategy:
1. If you can take their king, you should take it
2. Set up simple system-openings to win - London as white and ?slav? as black (Prashanth)

- Set 1 (Ewan): Keep track of absolute piece positions as well as possible (based on sensing and exchanges - NOT PROBABILITIES)
- Set 2: Probabilities of positions based on [a) turn #] and [b) common openings] and [c) projections of pieces]




Bots folder:

To better learn how ReconChess APIs and Interfaces work, the LearningBot.py file contains the comments on how each method works.
They are all called in a sequenced order based on you opponent's moves and you own move sets. 
Each function/method contains a bit of an overview in how you should consider structuring your strategies. 
It is most likely you will need to write custom scripts to calculate and store your board pieces and your opponent board pieces.




Git Tutorial:

To commite your changes to a specific branch, make sure you save all of your changes first.

"git status" and "git branch" can help you understand what position you are at in your git branch.

Steps to commit all of your changes:

This will add all changes and "package" them together to be shipped to the remote repo branch you are working with

1. git add -A 

This will stamp your "package" with the contents of what will be changed to the remote repo branch you are working with

2. git commit -m "Details of your changes"

Then once everything is ready to go you will send it off to the remote repo branch

3. git push YourRemoteRepo YourBranch

Example for this repository: git push reconChess master

Now at this stage you will want to go online and create a pull request to merge into other branches. As of now, you can approve PRs yourself and merge them.

-----------------------------------------------------------------------------------------------------------------------------------------------------------

Steps to fetch changes from remote repo to see what changes others have made:

We can try with this command first

git pull YourRemoteRepo Branch

This will fetch all of the changes from remote branch

1. git fetch --all

Through the messages of the above command you will see either new branches or changes made to existing local branch.

So you want to either work in the new branch you fetched or merge the changes.

To work in new branch you will use:

2. git switch NewBranch

To merge changes from remote repo branch into your local branch:

3. git merge YourRemoteRepo Branch

------------------------------------------------------------------------------------------------------------------------------------------------------------

Steps to set up remote repo names

To make sure you have a remote name set up, you want to add it first in short form.

git remote add NameYouSet UrlToRepo


