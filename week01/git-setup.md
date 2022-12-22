# Git commands to get started

```
brew install git
git config --global user.name "User Name"

echo "# Title" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:user/project.git
git push -u origin main

# Other Commands
git clone <repo name>
git add .
git commit -am 'Commit all changes'

# Useful Aliases
alias gitlog="git log --all --graph --decorate --pretty --oneline"

# Git Branches
git checkout -b new-branch-name
git add -A
git commit -m 'New Branch'
git push origin new-branch-name

# Merge
git checkout receiving-branch
git pull
git merge merging-branch

# Resolving conflict
git diff
#  Edit conflict file
git add file
git commit -m 'Merge'

# Deleting Old git Branches
# https://ardalis.com/why-delete-old-git-branches/
# Local
git branch -d branchname
# Remote
git push origin --delete branchname
# List git Branches
git branch -a
git branch --merged
# Keep record with tags
git tag tagname
git push --tags
# Git pruning: https://railsware.com/blog/git-housekeeping-tutorial-clean-up-outdated-branches-in-local-and-remote-repositories/

# Undo a commit & redo

$ git commit -m "Something terribly misguided" # (0: Your Accident)
$ git reset HEAD~                              # (1)
[ edit files as necessary ]                    # (2)
$ git add .                                    # (3)
$ git commit -c ORIG_HEAD                      # (4)

[StackOverflow](https://stackoverflow.com/questions/927358/how-do-i-undo-the-most-recent-local-commits-in-git)

```
## Submodules

```
git submodule add https://github.com/<user>/rock rock

git clone --recursive <project url>
```
[https://dev.to/jjokah/submodules-a-git-repo-inside-a-git-repo-36l9]

## Github CLI

### Create repo
```
# create a repository interactively
gh repo create

# create a new remote repository and clone it locally
gh repo create my-project --public --clone

# create a remote repository from the current directory
gh repo create my-project --private --source=. --remote=upstream
```
https://cli.github.com/manual/gh_repo_create
