![PP3-Tic-Tac-Toe](https://github.com/micsanhag/pp3/blob/main/tictactoe.jpg)


## Welcome to my Tic-Tac-Toe game written in Python!
This classic game is a perfect way to challenge your strategic thinking and have fun.
Play against the computer and see if you can outsmart it. 
Enjoy the timeless game of Tic-Tac-Toe right on your computer!


## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
