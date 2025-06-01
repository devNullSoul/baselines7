# baselines7
Die Voraussetzung ist docker compose version 2.x

Das docker-compose.yml wird gestartet:
```
cd baselines7
docker compose up
```
dazu braucht man Docker Deskop (unter Windows) oder eine lokale Docker Installation unter Linux.

Nach dem Start sind die Applikationen unter folgenden URLs erreichbar

| Docker container-zu-container | host-zu-container (Browser) |
|------------------------------|-----------------------------|
| postgres:5432                |                             |
| ollama:11434                 |                             |
| openwebui:3000               | http://localhost:3000       |
| elasticsearch:9200           |                             |
| kibana:5601                  | http://localhost:5601       |
| n8n:5678                     | http://localhost:5678       |

# Ollama
Beim ersten Starten wird ollama die LLMs llama3 llava:7b herunterladen, 
was aufgrund der Datenmenge einige Zeit dauern kann.
- llama3 ist ein mächtiges, frei verfügbare LLM, welches in den Varianten 8b und 70b gibt. 
Der Wert 8b bedeutet 8 billon hyperparameter, wobei 1 billion in der 
deutschen Sprache 1 Milliarde bedeutet.  
- llava:7b ist ein multimodales Modell welches mit Vicuna, einem Vision Encoder, kombiniert wurde
um visuelle und schriftliche Sprache zu verstehen.

Hinweis: Ein Modell mit mehr hyperparameter benötigt mehr Speicherplatz, liefert bessere Ergebnisse
und hat eine höhere Latenzeit.

Quellen: https://ollama.com/library/llava, https://ollama.com/library/llama3

# n8n
Das n8n bietet eine hohe Anzahl an AI-Tools und Agents, die miteinander kombiniert werden können, 
um einen vollständigen AI-Workflow visuell zu prototypen. Es werden viele Protokolle und 
Datenquellen unterstützt

In dem Repository liegen n8n_workflow.json und n8n_workflow.json, welche in n8n importiert werden können.

# baselines/ReinforcementLearning
Das Bodebeispiel dient zur Darstellung der Konzepte des Reinforcement Learning 
des Action-Space des State-Space am Beispiel einer Wette auf Kopf oder Zahl 
als Zufallsexperiments mit einer Laplace-Münze.

Im Bereich des Reinforment Learning sind der Acion Space und der State Space zentral, denn sie
beschreiben die möglichen Aktionen beschreiben, die ein Agent durchführen kann und die zustände, 
die ein Agent in seiner Umgebung erfahren kann. 

Im Beispiel des Münzwurfes besteht der Action Space aus Kopf oder Zahl bzw. 0 oder 1. Der Agent
wettet auf ein bestimmtes Ereignis: kopf oder Zahl.

Der State Space beschreibt, welche Ereignisse eintreten können. Das sind die Ereignisse: 
Die Münze zeigt Kopf und die Münze zeigt Zahl bzw. 0 oder 1. 

