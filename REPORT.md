<h2>Anwendungsentwicklung - Verwendung von APIs</h2>

- Definieren Sie einen Test-Endpunkt auf localhost mit der Port Nummer 8080. Was müssen Sie dafür beim Flask-Server konfigurieren?
    - Beim Flask-Server wird bei app.run() als Parameter der Port 8080 eingegeben. Also auf app.run(debug=true, port=8080) gesetzt.

- Implementieren Sie eine TODO-Liste mit Flask mit folgenden Elementen: {id, todo, assignee, done}. Was haben Sie geändert oder welche Elemente haben Sie neu definiert?
    - Ich habe die BOOKS-Liste so angepasst, so dass es diese Elemente speichert und die Liste auf TODO benannt. Todo

- Bereiten Sie die grafische Oberfläche für eine einfache Erstellung, Anzeige, Löschung und Anpassung der TODOs vor. Welche Komponenten müssen dafür erstellt werden?
    - Es wurde die Todo.vue erstellt und darin die GUI-Elemente für die CRUD-Befehle erstellt, sowie Funktionen, die mit Axios die CRUD-Befehle ausführen.. 
    In Index.js wurde die route vom Todo.vue eingegeben, damit es im VueJS-Client ausgeführt wird. 
    Mit dem Befehl 'npm run dev' habe ich den VueJS-Client unter dem Port 8081
     gestartet. 
     
- Ermöglichen Sie die einfache Erweiterung der grafischen Oberfläche und beschreiben Sie notwendige Schritte um neue Komponenten zur Anmeldung oder persönlichen Definition von personenbezogenen TODOs zu ermöglichen
    - Komponenten erstellen und die routes auf Index.js hinzufügen. Login.vue Komponente erstellen für den Login und die Login-Funktionalität implemetieren. 
    Man muss nun überprüfen, ob man schon eingeloggt ist oder nicht und ob man die Website neu aufgemacht hat. 
    Falls nicht, wird die Login.vue aufgerufen und der User kann sich anmelden, bzw. registrieren.

- Wie würden Sie eine einfache Authentifizierung implementieren? Beschreiben Sie die notwendigen Schritte!
    - Da es eine Simple Authentifizierung sein soll, würde HTTP Basic Auth ausreichen.
      Zuerst würde ich eine Funktion schreiben, die prüft, ob eine Authentifizierung notwendig ist und eine die prüft, ob ein Nutzername und der Password gültig sind. Und noch eine Funktion zum authentifizieren. 




<h2>Anwendungsentwicklung - Anforderungsmanagement und SW-Design</h2>

- Implementieren Sie einen Client in Python, der sich mit der vorhandenen Server-Einheit verbindet und die Daten in eine eigene JSON Struktur lädt.

- Was würden Sie bei der Server-API anders definieren, damit verschiedene Clients auf die angebotenenen Funktionen zugreifen könnten?




<h2>Softwareentwicklungsprozess - Verifikation und kontinuierliche Entwicklung
</h2>

- Welche Tools würden Sie einsetzen, und wie würden die entsprechenden Konfigurationsdateien aussehen? Erstellen Sie ein Konzept!
    - Ich würde für die Tests des Backends, bzw. dem Server, Pytests, die mit Tox ausgeführt werden, verwenden. 
    Für den Frontend, bzw. dem VueJS-Client, würde ich Cypress verwenden. 
    Zudem würde ich Travis CI als Continuous Integrations Plattform verwenden.
    Mit Travis würde ich Cypress und Tox verwenden.
    
tox.ini:
    
```
[tox]
envlist = py37
#,docs

[testenv]
deps = -requirements.txt
commands =
    pytest --cov=server --html=testreport.html --self-contained-html -vv
setenv =
    PYTHONPATH = src/main/python

[testenv:docs]
description = invoke sphinx-build to build the HTML docs
basepython = python3.7
deps = sphinx -requirements.txt
commands =
    sphinx-apidoc -o docs/source --tocfile index -F -f -P -l --ext-autodoc --ext-coverage src/main/python
    sphinx-build -c docs/source "docs/source" "docs/build" --color -W -bhtml {posargs}
    python -c 'import pathlib; print("documentation available under file://\{0\}".format(pathlib.Path(r"{toxworkdir}") / "docs_out" / "index.html"))'

[pytest]
testpaths = src/unittest/python
python_files = test_*.py
python_classes = Test
```
    
und die requirements.txt für tox.ini:
```
pytest
pytest-cov
pytest-html
pytest-flask
flask
flask-restful
flask_cors
```
.travis.yml:
```
matrix:
  include:
  - stage: Tox
    language: 'python'
    python:
    - "3.7"
    install: pip install tox-travis
    script: tox
  - stage: Vue
    language: 'node_js'
    install:
    - cd src/main/vue/client
    - npm ci
    script: npm test
```

    
- Bereiten Sie einen einfachen Test für den Aufruf der Random Funktion vor. Wie würden Sie diesen starten?
    - Zuerst test_run.py erstellen. Hier werden die Tests durchgeführt. 
    pytest importieren. Eine client Funktion definieren, wo für jeden Test der Client neu gestartet wird. Darüber @pytest.fixture.
    Dann die Funktion test_get(client) definiert, wo der GET getestet wird.
    Man ruft die URL auf und bekommt die JSON-Daten, falls die Übertragung geklappt hat.
    Um dies zu testen, vergleich man den Statuscode mit 200. Falls es True ist, hat die übertragung geklappt.
    
    
- Implementieren Sie einen einfachen grafischen Test. Worauf achten Sie dabei?
    - Ich achte darauf, dass das Backend bzw. der Server läuft.
  
- Definieren Sie eine Konfiguration mit TravisCI für eine kontinuierliche Integration. Was müssen Sie dabei für die Python Tests und was für die grafischen Tests vorsehen?
  Im Konfig.-File einstellen, das es verwendet wird.
  
- Welche Tests würden Sie für die Grenzen der Random Funktion vorsehen?
    - Um zu prüfen, ob die Random Funktion einen Wert zwischen 1 bis 100 liefert,
  kann man mit assert prüfen, ob der Rückgabewert, zwischen 1 bis 100 ist.
  Man bekommt den Int-Wert mit: res.json("randomNumber").
  Man kann auch prüfen ob es ungleich einer Zahl unter 1, bzw. über 100 ist.