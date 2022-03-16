# FastAPI presentation

## Development environment

- **Fedora 35**
- **python3.10.2 and venv**
- **VSCodium 1.65.2** (currently the latest version)
- **Chromium 99.0.4844.51**
- **gnome-terminal 3.42.2 with zsh and oh-my-zsh**
- **SQLiteBrowser 3.12.99**
- **git 2.35.1**
- **gh 2.5.2 (GitHub cli)**

---

## "Content"

### main
- @app.[get|post|put|delete]
- simple and basic
    - just to visualize how it works
- just have outputs, nothing special

### app.main
- @app.[get|post|put|delete] && @route.[get|post|put|delete]
- database
- relationship

---

### usage | test

#### remember: I'm using Linux! some of your commands may vary
- open a terminal
  - keep it in your mind: Linux users are not afraid to use terminal
- navigate into your working directory
- if you wish: create new directory and `cd` in, but the following command will make you a `FastAPI-presentation` directory
- `git clone https://github.com/dabzse/FastAPI-presentation.git`
    - or use the GitHub cli: `gh repo clone dabzse/FastAPI-presentation`
- `cd FastAPI-presentation`
- `python -m venv` + [virtual_environment_name]
- `source` + [virtual_environment_name] + `/bin/activate`
- first: upgrade pip
    - `pip install --upgrade pip`
- `pip install -r requirements.txt`
    - this will install the versions which I have used
- it depends which one would you like to run
    - for example try the better one, the "app" version
- `uvicorn app.main:app --reload`
- the given link: `http://localhost:8000` or `http://127.0.0.1:8000` open in a browser

now you have two choices: **Swagger UI** and **ReDoc**
 - if you prefer **Swagger UI**: extend the link with `/docs`
 - if you prefer **ReDoc**: extend the link with `/redoc`

---

## question &mdash; answer
- why **"app"**?
- why **"main"**?
  - because these are the most widely used names

---

### known issues
- hopefully there is nothing
    - I found 4 issues after the development, but those are fixed before the publishing.

---

### licence:
MIT
-
- all of the used things are free and open source, so this one should be the same

---

if you find something, feel free to send me an email

---

### footnote
- you can use the following code snippet, if you want to try it

      @app.api_route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
      def ....(....):
          ....
          return ....

---

#### I hope I didn't make a mistake....

---

<center>initial release was uploaded on: March 16<sup>th</sup>, 2022 [CET |=> GMT+1]</center>
<center>{{ MNY : @dabzse }}</center>
