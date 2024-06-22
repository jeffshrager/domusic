For the moment just copy-paste the code into test.py on your local
machine.  (Eventually you'll want to use a git interface, like
sourcetree, but it's such a pita to connect to github that for the
moment just d/l'ing the code will be fine.)

You should really use anaconda which manages python environments, but
you can probably get around with just using your default environment.

If you are using anaconda, you'll need to do:

   conda install pip

But if you're just using the default enviroment (not anaconda) skip
that.

Regardless, you'll need to install these packages:

  pip install pygame
  pip install numpy
  pip install scipy
  (Or maybe pip3 instead of pip)

After that you should be able to just do:

  python3 test.py

and you'll hear some sounds. If it complains that the packages can't
be found, try pip3 instead of pip.
