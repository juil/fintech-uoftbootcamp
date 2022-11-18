# Git commands to get started
git config --global user.name "User Name"

echo "# Title" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:user/project.git
git push -u origin main
