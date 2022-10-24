# alias settings
alias build='docker-compose build'
alias up='docker-compose up'
alias stop='docker-compose stop'
alias down='docker-compose down'
alias upd='docker-compose up -d' # up with detached mode(background)

alias makemigrations='docker-compose run --rm fastapi poetry run python manage.py makemigrations'
alias migrate='docker-compose run --rm fastapi poetry run python manage.py migrate'
alias createsuperuser='docker-compose run --rm fastapi poetry run python manage.py createsuperuser'
alias lessfastapilog='docker-compose run --rm fastapi less /var/log/fastapi.log'
alias catfastapilog='docker-compose run --rm fastapi cat /var/log/fastapi.log'
alias collectstatic='docker-compose run --rm fastapi poetry run python manage.py collectstatic --noinput'
