# Git commands to get started

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
