# Stuff you frequently want to do:

1. Find file path by name
```
find . "*name*" -print
find . -name '*.py'
```

2. Find file name by string inside that file 
```
grep '*pattern*' . -r
```

3. Write a function (and store vals in variables)
```
function funtime ()
{
  cwd=$(pwd) # <- capture the output of one func and store it in a var
  cd / ;
  fun=$(find . "*name*")[1];
  echo $fun;
  cd $cwd;
}
```
