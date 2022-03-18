# discord-role-adder
Automates the process of mass assigning roles.

# Requirements
Python >=3.7.0

# Setup
It's always a good idea to have a separate environment for each project.
However, I'm feeling a bit lazy (again) so I'll show how to install packages globally

```bash
pip3 install -r requirements.txt
```

Add a `.env` file with the `DISCORD_TOKEN=<your_token>"` line. In this example I am using a `list.csv` obtained from [premint](https://premint.xyz).
In the `bot.py` file change the `ROLE_ID` to the role you will be assigning. You can use `\@rolename` in the chat to obtain it.

Finally, run it with:

```bash
python3 bot.py
```

# Troubleshooting
If you are getting an error about missing certificates while connecting to the Discord host, run `install_certificate.py` to fix it.
