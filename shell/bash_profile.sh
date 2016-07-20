# ALIASES
alias gpl="git pull"
alias gps="git push"
alias gps++="gps origin $(git rev-parse --abbrev-ref HEAD)"
alias gs="git status"
alias gc="git status && git add -u && git status && git commit -m"
alias test_user_id="32148"
alias vs="vagrant status"

# Custom Functions
function note () 
{ 
	cp $1 ~/notes/$2/$1;
	cwd=$(pwd);
	cd ~/notes;
	git add -A;
	git commit -m $2/$1;
	git push origin master;
	cd $cwd; 
}

# Add RVM to PATH for scripting
export PATH="$PATH:$HOME/.rvm/bin"

