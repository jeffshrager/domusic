For the moment just copy-paste the code into test.py on your local
machine. (Click on test.py then the [Raw] button at the top, and you
can copy the code from there and just paste it into a code editor of
your choice on your local machine and save it in your own local
domusic folder on your desktop, or whatever.)

(Eventually you'll want to use a git interface, like sourcetree, but
it's such a pita to connect to github that for the moment just
downloading the code will be fine.)

You'll eventually want to use anaconda which manages python
environments, but you can probably get going with just using your
default environment.

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
