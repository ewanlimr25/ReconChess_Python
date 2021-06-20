# ReconChess_Python
This is a repo for building out the ReconChess Bots to participate in the Blind Chess tournaments : https://rbc.jhuapl.edu/


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

This will fetch all of the changes from remote branch
1. git fetch --all

Through the messages of the above command you will see either new branches or changes made to existing local branch.
So you want to either work in the new branch you fetched or merge the changes.

To work in new branch you will use:
2. git switch NewBranch

To merge changes from remote repo branch into your local branch:
3. git merge YourRemoteRepo YourRepo

------------------------------------------------------------------------------------------------------------------------------------------------------------

Steps to set up remote repo names

To make sure you have a remote name set up, you want to add it first in short form.

git remote add NameYouSet UrlToRepo


