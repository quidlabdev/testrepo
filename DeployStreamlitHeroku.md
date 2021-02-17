# Archivos necesarios
setup.sh
procfile
requirements.txt


# requirements.txt
pip install pipreqs
pipreqs <directory path>



# On setup.sh
mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"your@domain.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\


# setup2



# procfile - option 1
import os
with open(os.path.join('<Enter your directory path>','Procfile'), "w") as file1:
    toFile = 'web: sh setup.sh && streamlit run <app name>.py'
    
file1.write(toFile)

# procfile - option 2
web: sh setup.sh && streamlit run [name-of-app].py







# Proceso
1. Crear repo github
2. Crear archivos necesarios
3. Hacer push en github
4. Hacer push en heroku




# Pasos:

cd <directory path>
C:/Users/....> git init
Initialized empty Git repository in C:/Users/....

C:\Users...> heroku login

C:\Users...> heroku create
Creating app... done, ⬢ infinite-lowlands-22673
https://infinite-lowlands-22673.herokuapp.com/ | https://git.heroku.com/infinite-
lowlands-22673.git


git add .
git commit -m "Enter your message here"
git push heroku master

heroku ps:scale web=1



# xxxxxx
Create app with CLI
Commit
Push to deploy
