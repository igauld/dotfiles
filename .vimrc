set nocompatible
filetype off

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
" call vundle#begin('~/some/path/here')
" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-commentary'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on

autocmd FileType python setlocal commentstring=#\ %s

" show existing tab with 4 spaces each
set tabstop=4

" when indenting with '>' use 4 spaces width
set shiftwidth=4

" on pressing tab, insert 4 spaces
set expandtab

" show column information in status bar
set ruler

"  word wrap at 80 columns
set tw=80
