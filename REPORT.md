<h2>Anwendungsentwicklung - Verwendung von APIs</h2>

- Definieren Sie einen Test-Endpunkt auf localhost mit der Port Nummer 8080. Was müssen Sie dafür beim Flask-Server konfigurieren?
    - Beim Flask-Server wird bei app.run() als Parameter der Port 8080 eingegeben. Also auf app.run(debug=true, port=8080) gesetzt.

- Implementieren Sie eine TODO-Liste mit Flask mit folgenden Elementen: {id, todo, assignee, done}. Was haben Sie geändert oder welche Elemente haben Sie neu definiert?
    - Ich habe die BOOKS-Liste so angepasst, so dass es diese Elemente speichert und die Liste auf TODO benannt. Todo

- Bereiten Sie die grafische Oberfläche für eine einfache Erstellung, Anzeige, Löschung und Anpassung der TODOs vor. Welche Komponenten müssen dafür erstellt werden?
    - Es wurde die Todo.vue erstellt und darin die GUI-Elemente für die CRUD-Befehle erstellt. 
    In Index.js wurde die route vom Todo.vue eingegeben, damit es im VueJS-Client ausgeführt wird. 
    Mit dem Befehl 'npm run dev' habe ich den VueJS-Client unter dem Port 8081
     gestartet. 
     
- Ermöglichen Sie die einfache Erweiterung der grafischen Oberfläche und beschreiben Sie notwendige Schritte um neue Komponenten zur Anmeldung oder persönlichen Definition von personenbezogenen TODOs zu ermöglichen
    - Komponenten erstellen und die routes auf Index.js hinzufügen. Login.vue Komponente erstellen für den Login und die Login-Funktionalität implemetieren. 
    Man muss nun überprüfen, ob man schon eingeloggt ist oder nicht und ob man die Website neu aufgemacht hat. 
    Falls nicht, wird die Login.vue aufgerufen und der User kann sich anmelden, bzw. registrieren.

- Wie würden Sie eine einfache Authentifizierung implementieren? Beschreiben Sie die notwendigen Schritte!





<h2>Anwendungsentwicklung - Anforderungsmanagement und SW-Design</h2>
- Implementieren Sie einen Client in Python, der sich mit der vorhandenen Server-Einheit verbindet und die Daten in eine eigene JSON Struktur lädt.

- Was würden Sie bei der Server-API anders definieren, damit verschiedene Clients auf die angebotenenen Funktionen zugreifen könnten?




<h2>Softwareentwicklungsprozess - Verifikation und kontinuierliche Entwicklung
</h2>
- Welche Tools würden Sie einsetzen, und wie würden die entsprechenden Konfigurationsdateien aussehen? Erstellen Sie ein Konzept!

- Bereiten Sie einen einfachen Test für den Aufruf der Random Funktion vor. Wie würden Sie diesen starten?

- Implementieren Sie einen einfachen grafischen Test. Worauf achten Sie dabei?

- Definieren Sie eine Konfiguration mit TravisCI für eine kontinuierliche Integration. Was müssen Sie dabei für die Python Tests und was für die grafischen Tests vorsehen?

- Welche Tests würden Sie für die Grenzen der Random Funktion vorsehen?
