# Terminal Setup (Mac)

## Better terminal:

[iterm2](https://iterm2.com/)

	brew install --cask iterm2

## Themes:

- [Atom One Dark Theme](https://github.com/nathanbuchar/atom-one-dark-terminal)

## Plugins:

Great Setup by [Kevin Smets](https://gist.github.com/kevin-smets/8568070)

### Oh My Zsh

	sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

### Powerlevel10k

	git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k

edit your `~/.zshrc` and set `ZSH_THEME="powerlevel10k/powerlevel10k"`

### Auto Suggestions

[Install](https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#oh-my-zsh)

### Natural text selection

### Syntax highlighting

```git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

Activate the plugin in `~/.zshrc`

```plugins=( [plugins...] zsh-syntax-highlighting)
```

**Pygments**
[github](https://github.com/pygments/pygments)

```
brew install pygments
```

`.aliases`

```
alias ccat='pygmentize -g -P style=vim'
```
[*](https://coderwall.com/p/o6_ong/cat-syntax-highlighting)

`.bashprofile` or `.zshrc`

```
export LESSOPEN='| pygmentize -g -P style=vim %s`
```
[*](https://askubuntu.com/questions/406135/how-to-use-pygmentize-automatically-with-less)

## Primary Tools

### Vim

- [Neovim](https://github.com/neovim/neovim)
- [Using git in vim](https://www.vimfromscratch.com/articles/using-git-from-vim)
## Other Command Line Tools

### mdcat
Render markdown files in terminal.

	brew install mdcat
