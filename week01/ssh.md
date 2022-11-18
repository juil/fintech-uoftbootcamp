# SSH Keys

Check ssh keys
`ls -al ~/.ssh`

Create new ssh key
`ssh-keygen -t rsa -b 4096 -C "YOURGITHUB@EMAIL.NET"`


`eval "$(ssh-agent -s)"`

`ssh-add ~/.ssh/id_rsa`

`pbcopy < ~/.ssh/id_rsa.pub`


