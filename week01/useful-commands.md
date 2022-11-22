# Useful Commands

## Terminal

### Better Tools

- Editor: `vim` -> `nvim` [NeoVim](https://neovim.io/)
- Reader: `cat`
	- `less` Output without cluttering terminal buffer.
	- `mdcat`, `glow` Markdown output.

### Navigation

#### PATH

See path of program:

	type type
	which which

#### Alias

Edit `~/.aliases`, `~/.zshrc`, `~/.bash_profile`

	alias shortcut='cd ~/path'
	alias cmd='type command`

[More Info](https://wpbeaches.com/make-an-alias-in-bash-or-zsh-shell-in-macos-with-terminal/)

#### Search

	find /folder -type f -name file.txt

**File Types:**
- f – regular file
- d – directory
- l – symbolic link
- c – character devices
- b – block devices

[More Info](https://linuxhostsupport.com/blog/how-to-search-files-on-the-linux-terminal/)

	ls folder/ | grep regular expression

[`grep`](https://man7.org/linux/man-pages/man1/grep.1.html)

### Editing

#### vim

##### Copy & Paste:
- `d` delete/cut
- `y` yank/copy
- `p` paste

[More Info](https://vim.fandom.com/wiki/Copy,_cut_and_paste)

##### Undo and Redo
- `u` undo last change
- `ctrl-r` redo changes which were undone
